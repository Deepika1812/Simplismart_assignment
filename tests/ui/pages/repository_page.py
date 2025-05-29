from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RepositoryPage(BasePage):
    NEW_REPO_BUTTON = (By.LINK_TEXT, "New")
    REPO_NAME_INPUT = (By.ID, "repository_name")
    CREATE_REPO_BUTTON = (By.CSS_SELECTOR, "button.first-in-line")

    def open(self):
        self.driver.get("https://github.com/new")

    def create_repository(self, repo_name):
        self.enter_text(self.REPO_NAME_INPUT, repo_name)
        self.click(self.CREATE_REPO_BUTTON)
