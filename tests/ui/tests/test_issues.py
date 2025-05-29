import pytest
from selenium import webdriver
from pages.issues_page import IssuesPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_create_issue(driver):
    issues_page = IssuesPage(driver)
    repo_url = "https://github.com/your_username/your_repo"
    issues_page.open_issues(repo_url)
    issues_page.create_issue("Test issue via automation")
    assert "Test issue via automation" in driver.page_source
