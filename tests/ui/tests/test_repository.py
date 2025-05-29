import pytest
from selenium import webdriver
from pages.repository_page import RepositoryPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_create_new_repository(driver):
    repo_page = RepositoryPage(driver)
    repo_page.open()
    repo_page.create_repository("test-repo-automation")
    assert "test-repo-automation" in driver.current_url  # Confirm repo created
