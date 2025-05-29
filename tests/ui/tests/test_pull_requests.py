import pytest
from selenium import webdriver
from pages.pull_requests_page import PullRequestsPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_create_pull_request(driver):
    pr_page = PullRequestsPage(driver)
    repo_url = "https://github.com/your_username/your_repo"
    pr_page.open_prs(repo_url)
    pr_page.create_pull_request("Automated PR Title")
    assert "Automated PR Title" in driver.page_source
