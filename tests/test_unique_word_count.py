import allure
import pytest

from utils.constants import BASE_URL
from utils.logger import get_logger
from utils.word_counter import count_words, format_word_counts, unique_word_count


@allure.epic("Wikipedia")
@allure.feature("Unique Words")
@allure.story("UI and API TDD section comparison")
@pytest.mark.ui
@pytest.mark.api
class TestUniqueWordCount:
    logger = get_logger(__name__)

    @allure.title("Unique word count matches between UI and API TDD section")
    def test_unique_word_count_matches_between_ui_and_api(self, page_setup, api_setup):
        with allure.step("Extract unique words from UI"):
            self.logger.info("Opening Wikipedia Test automation page")
            page_setup.wikipedia_page.open_test_automation_page(BASE_URL)

            ui_text = page_setup.wikipedia_page.get_tdd_section_text()
            ui_word_counts = count_words(ui_text)
            ui_unique_count = unique_word_count(ui_word_counts)

            print("\nUI word occurrences:")
            print(format_word_counts(ui_word_counts))
            print(f"UI unique words: {ui_unique_count}")
            self.logger.info(f"UI unique words: {ui_unique_count}")
            allure.attach(ui_text, name="UI section text", attachment_type=allure.attachment_type.TEXT)
            allure.attach(
                format_word_counts(ui_word_counts),
                name="UI word occurrences",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("Extract unique words from API"):
            self.logger.info("Querying Wikipedia API for Test automation extract")
            api_text = api_setup.wikipedia_api.get_tdd_section_text()
            api_word_counts = count_words(api_text)
            api_unique_count = unique_word_count(api_word_counts)

            print("\nAPI word occurrences:")
            print(format_word_counts(api_word_counts))
            print(f"API unique words: {api_unique_count}")
            self.logger.info(f"API unique words: {api_unique_count}")
            allure.attach(api_text, name="API section text", attachment_type=allure.attachment_type.TEXT)
            allure.attach(
                format_word_counts(api_word_counts),
                name="API word occurrences",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("Assert unique word counts match"):
            assert ui_unique_count == api_unique_count, (
                f"Unique word count mismatch: UI={ui_unique_count}, API={api_unique_count}"
            )
