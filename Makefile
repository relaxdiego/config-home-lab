.DEFAULT_GOAL := help

##
## Available Goals:
##


## clean          : Uninstalls all dependencies and removes build and
##                  test artifacts.
##
.PHONY: clean
clean:
	@pip uninstall -y -r requirements.txt 2>/dev/null || true
	@pip uninstall -y pip-tools 2>/dev/null || true
	@rm -fv .last* .coverage ${requirements}
	@rm -rfv build/ *.egg-info **/__pycache__ .pytest_cache .tox htmlcov


## dependencies   : Ensures pip-tools is installed and then ensures
##                  the right dependency versions are installed.
##
.PHONY: dependencies
dependencies: .last-pip-tools-install .last-pip-sync

.last-pip-sync: requirements.txt
	@(pip-sync requirements.txt || echo "pip-sync error") | tee .last-pip-sync
	@(grep "pip-sync error" .last-pip-sync 1>/dev/null 2>&1 && rm -f .last-pip-sync && exit 1) || true
	@pyenv rehash

.last-pip-tools-install:
	@(pip-compile --version 1>/dev/null 2>&1 || pip --disable-pip-version-check install "pip-tools>=5.5.0,<6.0.0" || echo "pip-tools install error") | tee .last-pip-tools-install
	@(grep "pip-tools install error" .last-pip-tools-install 1>/dev/null 2>&1 && rm -f .last-pip-tools-install && exit 1) || true

requirements.txt: setup.py
	@CUSTOM_COMPILE_COMMAND="make dependencies" pip-compile

# From: https://swcarpentry.github.io/make-novice/08-self-doc/index.html
## help           : Print this help message
##
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
