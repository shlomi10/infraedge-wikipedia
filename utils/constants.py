import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://en.wikipedia.org/wiki/Test_automation")
API_BASE_URL = os.getenv("API_BASE_URL", "https://en.wikipedia.org")

PAGE_TITLE = "Test automation"
TDD_SECTION_TITLE = "Test-driven development"
TDD_HEADING_ID = "Test-driven_development"

USER_AGENT = os.getenv(
    "WIKIPEDIA_USER_AGENT",
    "InfraedgeAutomation/1.0 (Senior Automation QA assignment)",
)
