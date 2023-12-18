all: $(patsubst %.py, %, $(wildcard *.py))

%: %.in %.py
	@echo -n '$*: '
	@python3 $*.py < $*.in | xargs echo
