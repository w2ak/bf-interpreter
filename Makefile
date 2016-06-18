.PHONY: all test

SIZE	:=	512
BF2PY	:=	src/bf2py.py
PY	:=	python3
FILE	:=	samples/helloworld.bf

test:
	$(BF2PY) $(FILE) $(SIZE) | $(PY)
