#
# Makefile
# steve, 2017-01-05 14:08
#

PY_SRC_ALL = $(shell find ./ -name '*.py')

LINTTOOL = python3 -m pylint
LINTFLAGS = -rn --rcfile=.pylint

all:
	@echo "Makefile needs your attention"

# Format all python files with autopep8
format_pep8: $(PY_SRC_ALL)
	@echo "Running autopep8 formatter"
	@autopep8 -i $(PY_SRC_ALL)

codecheck: $(PY_SRC_ALL)
	@echo "Running code check"
	$(LINTTOOL) $(LINTFLAGS) $(PY_SRC_ALL)

clean:
	find -name "*.pyc" | xargs rm

# vim:ft=make
#
