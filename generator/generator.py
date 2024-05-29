import os
import sys
import json
import argparse
from os import environ as env
from openai import OpenAI

from generator import __version__


class Words:
    def __init__(self, fd) -> None:
        self.fd = fd
        self.data = json.load(fd)

    def __str__(self) -> str:
        return json.dumps(self.data, indent=4)

    def add_item(self, word):
        item = {word: {"dict": None, "notes": None, "AI": None}}
        self.data.update(item)


def check_env():
    filepath = os.path.expanduser("~/.yaoyao.json")
    if not os.path.isfile(filepath):
        print("No such file: '~/.yaoyao.json'! Creating it...")
        with open(filepath, "w") as fd:
            fd.write("{}")
    return open(filepath, "r+")


def get_parser():
    parser = argparse.ArgumentParser(
        prog="apkg",
        description="Auto Generate apkg file for Anki created by Hu Yaoyao :)",
        epilog="Happly Learning!",
    )
    parser.add_argument(
        "word",
        metavar="WORD",
        nargs="+",
        help="add the word(s) you want to add",
    )
    parser.add_argument(
        "--openai_key", dest="openai_key", type=str, default="", help="OpenAI api key"
    )
    parser.add_argument("-v", "--version", help="display the version of APKG-Generator")

    return parser


def command_line_runner():
    fd = check_env()
    parser = get_parser()
    args = vars(parser.parse_args())

    if args["version"]:
        print(__version__)
        exit

    if not args["word"]:
        parser.print_help()
        return

    word = Words(fd)
    for w in args["word"]:
        word.add_item(w)

    fd.seek(0)  # Reset file pointer to the beginning of the file
    fd.truncate()  # Clear the file before writing
    json.dump(word.data, fd)
    print(word)

    fd.close()


if __name__ == "__main__":
    command_line_runner()
