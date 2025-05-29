from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IssuesPage(BasePage):
    ISSUES_TAB = (By.ID, "issues-tab")
    NEW_ISSUE_BUTTON = (By.LINK_TEXT, "New issue")
    ISSUE_TITLE_INPUT = (By.ID, "issue_title")
    SUBMIT_ISSUE_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")

    def open_issues(self, repo_url):
        self.driver.get(f"{repo_url}/issues")

    def create_issue(self, title):
        self.click(self.NEW_ISSUE_BUTTON)
        self.enter_text(self.ISSUE_TITLE_INPUT, title)
        self.click(self.SUBMIT_ISSUE_BUTTON)
