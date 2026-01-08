VENV_PY=/workspaces/blank-app-260108/.venv/bin/python
STREAMLIT=$(VENV_PY) -m streamlit

.PHONY: run install

# Run the app using the venv Python so installed packages are available
run:
	$(STREAMLIT) run streamlit_app.py --server.enableCORS false --server.enableXsrfProtection false

# Install requirements into the venv
install:
	$(VENV_PY) -m pip install -r requirements.txt
