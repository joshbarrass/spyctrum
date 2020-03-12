.PHONY: test
test:
	python3.6 -m nose -v test/

.PHONY: publish
publish:
	python3.6 setup.py publish
