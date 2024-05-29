ARG = 
PYTHON = '/Users/yaoyhu/opt/miniconda3/envs/anki/bin/python'

init:
	pip install -r requirements.txt
test:
	$(PYTHON) test/test/py
run:
    # Demo: `make run ARG='-h'`, `make run ARG='word1 word2'`
	$(PYTHON) -m generator $(ARG)
