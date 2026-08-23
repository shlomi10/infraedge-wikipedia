<p align="center">
  <img src="assets/wikipedia-logo.png" width="180" alt="Wikipedia">
</p>

# Wikipedia Unique Words Automation

![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge&logo=github&logoColor=white)![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)![Playwright](https://img.shields.io/badge/Playwright-UI%20Automation-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)![Pytest](https://img.shields.io/badge/Pytest-Test%20Runner-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)![Allure](https://img.shields.io/badge/Allure-Test%20Reports-FF6A00?style=for-the-badge&logo=allure&logoColor=white)![REST API](https://img.shields.io/badge/REST%20API-Wikipedia%20Query-7B2CBF?style=for-the-badge&logo=swagger&logoColor=white)![POM](https://img.shields.io/badge/Pattern-Page%20Object%20Model-6C63FF?style=for-the-badge)

![GitHub Actions](https://img.shields.io/github/actions/workflow/status/shlomi10/infraedge-wikipedia/allure.yml?style=for-the-badge&logo=githubactions&logoColor=white&label=GitHub%20Actions)![HTML Report](https://img.shields.io/badge/HTML-Report-E34F26?style=for-the-badge&logo=html5&logoColor=white)![Logging](https://img.shields.io/badge/Logging-Enabled-06B6D4?style=for-the-badge&logo=datadog&logoColor=white)![Word Count](https://img.shields.io/badge/Validation-Unique%20Words-EC4899?style=for-the-badge)![Wikipedia](https://img.shields.io/badge/Target-Wikipedia-000000?style=for-the-badge&logo=wikipedia&logoColor=white)![Flask](https://img.shields.io/badge/Flask-UI-000000?style=for-the-badge&logo=flask&logoColor=white)![Streamlit](https://img.shields.io/badge/Streamlit-Local%20UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)![Live Allure](https://img.shields.io/badge/Allure-Live%20Report-F59E0B?style=for-the-badge&logo=allure&logoColor=white)

[![Docker](https://img.shields.io/badge/Docker-Image-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/shlomi10/infraedge-wikipedia)[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-shlomi10%2Finfraedge--wikipedia-086DD7?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/shlomi10/infraedge-wikipedia)[![Docker Tag](https://img.shields.io/badge/Tag-1-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/shlomi10/infraedge-wikipedia/tags)[![Live App](https://img.shields.io/badge/Live%20App-runmydocker--app-000000?style=for-the-badge&logo=flask&logoColor=white)](https://infraedge-wikipedia.runmydocker-app.com)[![Container Port](https://img.shields.io/badge/Port-8501-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://infraedge-wikipedia.runmydocker-app.com)[![Playwright Headless](https://img.shields.io/badge/Playwright-Headless-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/python/)

Automation framework that validates unique-word counts from the Wikipedia **Test automation** page — comparing the **Test-driven development** section between **UI** and **API** using **Python**, **Playwright**, **Pytest**, and **Allure**.

Repository:

```bash
https://github.com/shlomi10/infraedge-wikipedia
```

Live Allure report:

```bash
https://shlomi10.github.io/infraedge-wikipedia/
```

Docker Hub:

```bash
https://hub.docker.com/r/shlomi10/infraedge-wikipedia
```

Live app:

```bash
https://infraedge-wikipedia.runmydocker-app.com
```

---



## 📌 Overview

The assignment validates that the number of unique words extracted from the Test-driven development section stays consistent between UI automation and Wikipedia's query API.

Core flow:

```text
Open Wikipedia page → Extract TDD section (UI)
Query Wikipedia API → Extract TDD section (API)
Normalize words → Count occurrences → Assert unique counts match
```

This project includes:

- UI automation with Playwright and Page Object Model
- REST API automation through Wikipedia `action=query`
- Shared word-normalization logic for UI and API
- Allure reporting
- GitHub Actions CI with a published Allure report
- Flask runner UI in Docker / Run My Docker
- Streamlit runner UI for local use
- Failure screenshots
- Playwright traces
- Runtime logs

---



## 🧩 Target Application Context

The tested application is the public Wikipedia article:

```text
https://en.wikipedia.org/wiki/Test_automation
```

The framework extracts the page title plus the **Test-driven development** section.

Main endpoints:

```text
UI:  https://en.wikipedia.org/wiki/Test_automation
API: https://en.wikipedia.org/w/api.php
```

Wikipedia query used by the framework:

```text
GET /w/api.php
  action=query
  format=json
  prop=extracts
  titles=Test automation
  explaintext=1
  redirects=1
```

UI locators follow Page Object Model and stay scoped to the TDD section:

```text
#firstHeading
#mw-content-text .mw-parser-output
section[aria-labelledby='Test-driven_development']
get_by_role("heading", name="Test-driven development")
section paragraphs
```

---



## ✅ Automated Scenario



### UI + API Test — Unique Word Count

One test covers both layers.

Flow:

```text
Launch browser
Open Wikipedia Test automation page
Extract title + Test-driven development section from UI
Print occurrence of each word
Query Wikipedia API with action=query
Extract title + Test-driven development section from API
Print occurrence of each word
Assert unique word count in UI == unique word count in API
```

Word rules:

```text
Case-insensitive
Exclude brackets and their contents, e.g. [4]
Treat hyphens, periods, commas, and other delimiters as separators
Example: "Test-first, manual. Code," → "test first manual code"
```

Test file:

```text
tests/test_unique_word_count.py
```

---



## 🧱 Project Structure

```text
infraedge-wikipedia/
├── .github/
│   └── workflows/
│       └── allure.yml
├── .streamlit/
│   ├── config.toml
│   └── credentials.toml
├── Dockerfile
├── .dockerignore
├── assets/
│   └── wikipedia-logo.png
├── ui/
│   ├── app.py
│   ├── server.py
│   ├── runner.py
│   └── styles.py
├── api/
│   ├── api_client.py
│   └── wikipedia_api.py
├── pages/
│   ├── base_page.py
│   └── wikipedia_page.py
├── tests/
│   ├── conftest.py
│   └── test_unique_word_count.py
├── utils/
│   ├── constants.py
│   ├── logger.py
│   └── word_counter.py
├── reports/
│   ├── logs/
│   ├── screenshots/
│   └── traces/
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

---



## 🛠 Tech Stack

- Python
- Playwright
- Pytest
- Pytest-Playwright
- Allure Pytest
- Python Dotenv
- REST API testing through Playwright request context
- GitHub Actions
- GitHub Pages
- Flask
- Streamlit
- Docker

---



## ✅ Prerequisites

Install before running:

- Python 3.14+
- Git
- Node.js / npm only if you want to use Allure CLI through npm

---



## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/shlomi10/infraedge-wikipedia.git
cd infraedge-wikipedia
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install chromium
```

---



## ▶️ Running Tests

Run all tests:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Run with logs printed:

```bash
pytest -s
```

---



## 🖥️ Runner UI

Local Streamlit runner:

```bash
python -m streamlit run ui/app.py
```

Local Flask runner (same UI the Docker image uses):

```bash
python ui/server.py
```

Then open:

```text
http://localhost:8501
```

Hosted Docker app:

```text
https://infraedge-wikipedia.runmydocker-app.com
```

The UI lets you:

```text
Set the Wikipedia URL
Click Run test
Watch the Playwright browser open
See UI vs API unique counts
Inspect word-occurrence tables
Read the pytest output
```

---



## 🐳 Docker

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg" width="64" alt="Docker">
</p>

### Run the UI in a container

The published image is `shlomi10/infraedge-wikipedia:1`. It starts Flask on ports `8501` and `80`, includes Playwright Chromium, and runs pytest headless when you click **Run test**.

Use tag `1` on Run My Docker, not `latest`.

Hosted app:

```bash
https://infraedge-wikipedia.runmydocker-app.com
```

Map HTTPS to container port `8501`. Port `80` also works. The hosted UI is Flask over plain HTTP because that host does not upgrade Streamlit WebSockets.

Image page:

```bash
https://hub.docker.com/r/shlomi10/infraedge-wikipedia
```

Tags page:

```bash
https://hub.docker.com/r/shlomi10/infraedge-wikipedia/tags
```

### 1. Build

```bash
docker build -t infraedge-wikipedia .
```



### 2. Run the UI

```bash
docker run --rm -p 8501:8501 infraedge-wikipedia
```



### 3. Open

```text
http://localhost:8501
```

Inside Docker the pytest run is headless. Set a Wikipedia URL in the UI and click **Run test**.

### 4. Publish to Docker Hub

```bash
docker login
docker tag infraedge-wikipedia shlomi10/infraedge-wikipedia:1
docker push shlomi10/infraedge-wikipedia:1
```

Pull and run from Docker Hub:

```bash
docker pull shlomi10/infraedge-wikipedia:1
docker run --rm -p 8501:8501 shlomi10/infraedge-wikipedia:1
```

---



## 📊 Allure Report

<p align="center">
  <img src="https://cdn.simpleicons.org/githubactions/2088FF" width="64" alt="GitHub Actions">
</p>

### Local

Generate Allure results:

```bash
pytest --alluredir=allure-results
```

Generate an Allure HTML report:

```bash
allure generate allure-results -o allure-report
```

Open Allure report:

```bash
allure open allure-report
```



### GitHub Actions

Every push to `main` runs:

```text
pytest --alluredir=allure-results
allure generate allure-results -o allure-report
```

The report is available in two places:

1. The workflow run artifacts — download `allure-report`
2. The live GitHub Pages site:

```bash
https://shlomi10.github.io/infraedge-wikipedia/
```

After the first successful workflow, enable GitHub Pages:

```text
Settings → Pages → Build and deployment
Source: Deploy from a branch
Branch: gh-pages / root
```

Workflow permissions should allow writing:

```text
Settings → Actions → General → Workflow permissions
Read and write permissions
```

---



## 📄 HTML Report

Generate a standalone HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

The report will be created at:

```bash
reports/report.html
```

Open it directly in the browser after the test run.

Required package:

```bash
pytest-html
```

---



## 📁 Runtime Artifacts

Artifacts are generated under:

```text
reports/
├── logs/
│   └── automation.log
├── screenshots/
│   └── <test-name>.png
└── traces/
    └── <test-name>.zip
```

Open Playwright trace:

```bash
playwright show-trace reports/traces/<test-name>.zip
```

---



## 🧾 Logging

The framework writes runtime logs to:

```text
reports/logs/automation.log
```

Logging is implemented in:

```text
utils/logger.py
```

Used by:

```text
api/api_client.py
pages/base_page.py
tests/test_unique_word_count.py
```

The API client logs every request:

```text
GET /w/api.php params={action=query, prop=extracts, titles=Test automation}
```

---



## 🧪 Test Design



### UI Layer

Uses Page Object Model.

```text
pages/
├── base_page.py
└── wikipedia_page.py
```

Responsibilities:

- selectors are stored in page classes
- reusable actions are stored in `BasePage`
- UI test only describes the business flow
- `page_setup` fixture groups all page objects for UI tests

---



### API Layer

Uses API wrapper classes.

```text
api/
├── api_client.py
└── wikipedia_api.py
```

Responsibilities:

- `ApiClient` handles HTTP methods and response validation
- `SUCCESS_STATUSES` holds accepted HTTP statuses
- `WikipediaApi.query()` uses Wikipedia `action=query`
- Tests use the `api_setup` fixture

---



### Shared Word Counting

`utils/word_counter.py` is used by both UI and API so both sides apply the same rules.

---



### Shared Configuration

`utils/constants.py` holds environment-specific values only:

```text
BASE_URL
API_BASE_URL
PAGE_TITLE
TDD_SECTION_TITLE
TDD_HEADING_ID
USER_AGENT
```

API route paths are not stored in `constants.py`; they live on the API wrapper classes.

---



## 🧷 Pytest Configuration

`pytest.ini`:

```ini
[pytest]
testpaths = tests
pythonpath = .
markers =
    ui: UI tests
    api: API tests
addopts = -ra -s
```

---



## 📌 Notes

- The same word-normalization function is used for UI and API.
- Locators are scoped to the TDD section so parent headings are not collected.
- Local runs open a headed maximized browser. GitHub Actions runs headless.
- Runtime artifacts are generated automatically.
- API endpoint paths are defined on API wrapper classes, not in `constants.py`.
- The combined test uses both `page_setup` and `api_setup`.

---



## ✅ Useful Commands

```bash
pytest
pytest -v
pytest --alluredir=allure-results
pytest --html=reports/report.html --self-contained-html
allure generate allure-results -o allure-report
allure open allure-report
python -m streamlit run ui/app.py
python ui/server.py
docker build -t infraedge-wikipedia .
docker run --rm -p 8501:8501 infraedge-wikipedia
docker pull shlomi10/infraedge-wikipedia:1
docker run --rm -p 8501:8501 shlomi10/infraedge-wikipedia:1
```

---



## ❤️ Made By

Built by **Shlomi** — from code to the world, with love.