PYTHON := @python3
run:
	${PYTHON} main.py
clean:
	@rm -rf result.csv `find . -name test.log`
	@rm -rf result.csv `find . -name test`
	@rm -rf result.csv `find . -name __pycache__`
