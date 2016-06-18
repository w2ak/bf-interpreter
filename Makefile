.PHONY: all test py

SIZE	:=	512
BF2PY	:=	src/bf2py.py
PY	:=	python3
FILE	:=	samples/helloworld.bf
BIN	:=	bin/
EXEC	:=	exe

py:
	mkdir -p $(BIN)
	$(BF2PY) $(FILE) $(SIZE) > $(BIN)test.$(EXEC)
	chmod +x $(BIN)test.$(EXEC)

