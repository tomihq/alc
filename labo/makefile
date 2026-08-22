VENV := .venv
VENV_BIN := $(VENV)/bin
VENV_PIP := $(VENV_BIN)/pip
VENV_PYTHON := $(VENV_BIN)/python

.PHONY: all venv run clean

all: run

$(VENV)/.infrastructure_built: requirements.txt
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV)
	@echo "Installing dependencies..."
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install -r requirements.txt
	touch $(VENV)/.infrastructure_built

venv: $(VENV)/.infrastructure_built

clean:
	rm -rf $(VENV)