.PHONY: clean
clean:
	rm -v */*.cfg || true
all:
	python extract.py
