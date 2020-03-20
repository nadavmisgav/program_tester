PYTHON := @python3
run:
	${PYTHON} main.py
clean:
	@rm -rf result.csv `find . -name command.log` `find . -name test` `find . -name __pycache__`