PYTHON := @python3
run:
	${PYTHON} main.py
clean:
	@rm -f result.csv `find . -name command.log` `find . -name test`