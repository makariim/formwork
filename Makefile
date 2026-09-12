# For working ON Formwork, in this repository.
#
# This file deliberately does NOT travel with the kit. Your own project may
# already have a Makefile, and overwriting it would break your build to save
# you five characters of typing.
#
# In your own project, run the programs directly:
#
#     formwork install --runtime claude-code
#     formwork check
#
# Every target below is one line you could type yourself. Nothing is hidden.

RUNTIME ?= claude-code

.PHONY: help install check demo test roles clean-check

help:                ## show this list
	@grep -E '^[a-z-]+:.*##' $(MAKEFILE_LIST) \
		| sed 's/:.*## /|/' | awk -F'|' '{printf "  make %-12s %s\n", $$1, $$2}'

install:             ## set this project up. RUNTIME=codex to pick another tool
	formwork/install --runtime $(RUNTIME)

check:               ## run every check on this project
	formwork/check/run

demo:                ## watch every check refuse a broken input
	formwork/check/run --demo-fail

roles:               ## regenerate the role files after editing one
	formwork/build

test:                ## run every test
	@python3 formwork/guard/test_boundary.py
	@python3 formwork/guard/test_protection.py
	@python3 formwork/guard/test_quality_gate.py
	@python3 formwork/check/test_gate.py
	@python3 formwork/test_install.py
