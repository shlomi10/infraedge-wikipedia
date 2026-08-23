import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from utils.constants import TDD_HEADING_ID, TDD_SECTION_TITLE


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("wikipedia page")
class WikipediaPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page_title = page.locator("h1.firstHeading.mw-first-heading")
        self.article_body = page.locator("#mw-content-text").locator(".mw-parser-output")
        self.tdd_section = self.article_body.locator(f"section[aria-labelledby='{TDD_HEADING_ID}']")
        self.tdd_heading = self.tdd_section.get_by_role(
            "heading",
            name=TDD_SECTION_TITLE,
            exact=True,
        )
        self.tdd_paragraphs = self.tdd_section.locator("p")

    @allure.step("Open Test automation Wikipedia page")
    def open_test_automation_page(self, url: str):
        self.goto(url)
        self.wait_visible(self.page_title)
        self.wait_visible(self.tdd_heading)

    @allure.step("Extract TDD section text including title")
    def get_tdd_section_text(self) -> str:
        self.wait_visible(self.tdd_heading)
        self.wait_visible(self.tdd_paragraphs.first)

        title = self.get_clean_text(self.page_title)
        heading = self.get_clean_text(self.tdd_heading)

        paragraphs = []
        for index in range(self.tdd_paragraphs.count()):
            paragraphs.append(self.get_clean_text(self.tdd_paragraphs.nth(index)))

        return " ".join([title, heading, *paragraphs])
