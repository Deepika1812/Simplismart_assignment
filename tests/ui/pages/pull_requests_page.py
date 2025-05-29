from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PullRequestsPage(BasePage):
    PR_TAB = (By.ID, "pull-requests-tab")
    NEW_PR_BUTTON = (By.LINK_TEXT, "New pull request")
    CREATE_PR_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    PR_TITLE_INPUT = (By.ID, "pull_request_title")

    def open_prs(self, repo_url):
        self.driver.get(f"{repo_url}/pulls")

    def create_pull_request(self, title):
        self.click(self.NEW_PR_BUTTON)
        self.enter_text(self.PR_TITLE_INPUT, title)
        self.click(self.CREATE_PR_BUTTON)
