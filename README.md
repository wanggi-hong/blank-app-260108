# 🎈 Blank app template

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   If you are using the workspace virtual environment (recommended), run Streamlit with the venv Python so installed packages (like matplotlib) are available:

   ```bash
   $ /workspaces/blank-app-260108/.venv/bin/python -m streamlit run streamlit_app.py --server.enableCORS false --server.enableXsrfProtection false
   ```

   Or use the included helper script:

   ```bash
   $ ./scripts/run_streamlit.sh
   ```

   If you run `streamlit` directly, make sure it points to the same Python environment where you installed the dependencies. You can check with `which streamlit`.

---

### VS Code - 빠른 실행 (초보자용)

- **F5**: 좌측 Run & Debug에서 `Run Streamlit`을 선택하면 앱이 통합 터미널에서 실행됩니다.
- **터미널에서 한 번의 명령**: `make run` (Makefile에 정의되어 있으며 venv Python으로 실행됩니다)

> 팁: `.vscode/settings.json`에 작업공간의 Python 인터프리터 경로(`/workspaces/blank-app-260108/.venv/bin/python`)를 설정해 두었습니다. VS Code가 가상환경을 자동으로 인식하지 못하면 이 설정으로 바로잡을 수 있습니다.
