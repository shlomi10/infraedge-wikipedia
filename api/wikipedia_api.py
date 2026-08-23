import re

from utils.constants import PAGE_TITLE, TDD_SECTION_TITLE


class WikipediaApi:
    QUERY = "/w/api.php"
    SECTION_HEADING = re.compile(
        rf"^=== {re.escape(TDD_SECTION_TITLE)} ===\s*(.*?)(?=^={{2,}}|\Z)",
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )

    def __init__(self, api_client):
        self.api_client = api_client

    def query(self, params: dict):
        query_params = {
            "action": "query",
            "format": "json",
            **params,
        }
        return self.api_client.get(self.QUERY, params=query_params)

    def get_page(self, response: dict) -> dict:
        pages = response.get("query", {}).get("pages", {})
        if not pages:
            raise AssertionError(f"Wikipedia query returned no pages: {response}")
        return next(iter(pages.values()))

    def get_page_extract(self, title: str = PAGE_TITLE) -> dict:
        response = self.query({
            "prop": "extracts",
            "titles": title,
            "explaintext": "1",
            "redirects": "1",
        })
        return self.get_page(response)

    def extract_tdd_section(self, extract: str) -> str:
        match = self.SECTION_HEADING.search(extract)
        if not match:
            raise AssertionError("Test-driven development section was not found in API extract")
        return " ".join(match.group(1).split())

    def get_tdd_section_text(self) -> str:
        page = self.get_page_extract()
        title = page.get("title") or PAGE_TITLE
        extract = page.get("extract") or ""
        section_body = self.extract_tdd_section(extract)
        return " ".join([title, TDD_SECTION_TITLE, section_body])
