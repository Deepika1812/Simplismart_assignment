# Simplismart QA Assignment

This repository contains QA deliverables for testing GitHub’s web interface and REST API.

✅ Automated UI tests using Selenium + Python  
✅ Automated API tests for GitHub REST API  
✅ Detailed manual test cases  
✅ GitHub Actions CI setup  
✅ Test reports and documentation

---

## 📁 Folder Structure

```
/tests
  /ui
    /pages      → Page Object files for Selenium tests
    /tests      → Actual Selenium test scripts
    /utils      → Utility functions, setup/teardown
  /api          → API test scripts using requests + pytest
/manual-tests   → Manual test cases and testing docs
/reports        → HTML or log reports from automated tests
requirements.txt → Python dependencies list
```

---

## 🚀 Setup & Run

### Prerequisites

✅ Python 3.x  
✅ pip (Python package manager)  
✅ Chrome or Firefox browser + matching WebDriver

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Run Automated UI Tests

```bash
pytest tests/ui/tests --html=reports/ui_report.html
```

---

### Run Automated API Tests

```bash
pytest tests/api --html=reports/api_report.html
```

---

### View Test Reports

Open the generated HTML files in the `/reports` folder:
- `ui_report.html` → Selenium UI test results
- `api_report.html` → API test results

---

## 📝 Manual Test Cases

Manual test cases and detailed testing documentation can be found in:
```
/manual-tests/manual_test_cases.md
```

---

## 🔑 Authentication for API Tests

For API tests:
- Use a GitHub **personal access token (PAT)** stored as an environment variable or in a config file .
- The token should have appropriate scopes for repository, issues, and pull request access.
