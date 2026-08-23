import os

import allure
import pytest
from pathlib import Path
from playwright.sync_api import Page

from api.api_client import ApiClient
from api.wikipedia_api import WikipediaApi
from pages.wikipedia_page import WikipediaPage
from utils.constants import API_BASE_URL, USER_AGENT


PROJECT_ROOT = Path.cwd()
ARTIFACTS_DIR = PROJECT_ROOT / "reports"
SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"
TRACES_DIR = ARTIFACTS_DIR / "traces"


class Pages:
    def __init__(self, page: Page):
        self.wikipedia_page = WikipediaPage(page)
        self.page = page


class ApiServices:
    def __init__(self, api_client: ApiClient):
        self.wikipedia_api = WikipediaApi(api_client)
        self.client = api_client


@pytest.fixture(scope="function")
def initialize(request, playwright):
    ci = os.getenv("CI", "").lower() in {"1", "true", "yes"}
    in_docker = Path("/.dockerenv").exists()
    headless = ci or in_docker
    browser = playwright.chromium.launch(
        headless=headless,
        args=["--no-sandbox", "--disable-dev-shm-usage"] if headless else ["--start-maximized"],
    )

    if headless:
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
    else:
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.evaluate("window.moveTo(0, 0); window.resizeTo(screen.availWidth, screen.availHeight);")
        window_size = page.evaluate("""() => {
                return {width: window.innerWidth, height: window.innerHeight};
            }""")
        page.set_viewport_size(window_size)

    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield page

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        screenshot_path = SCREENSHOTS_DIR / f"{request.node.name}.png"
        page.screenshot(path=str(screenshot_path), full_page=True)
        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name="screenshot", attachment_type=allure.attachment_type.PNG)

    TRACES_DIR.mkdir(parents=True, exist_ok=True)
    context.tracing.stop(path=str(TRACES_DIR / f"{request.node.name}.zip"))
    page.close()
    context.close()
    browser.close()


@pytest.fixture()
def page_setup(initialize: Page) -> Pages:
    return Pages(initialize)


@pytest.fixture(scope="session")
def api_context(playwright):
    context = playwright.request.new_context(
        base_url=API_BASE_URL,
        extra_http_headers={
            "User-Agent": USER_AGENT,
        },
    )
    yield context
    context.dispose()


@pytest.fixture()
def api_client(api_context):
    return ApiClient(api_context)


@pytest.fixture()
def api_setup(api_client) -> ApiServices:
    return ApiServices(api_client)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

    if rep.when != "call" or rep.passed:
        return

    page_setup = item.funcargs.get("page_setup")
    if page_setup is None:
        return

    png = page_setup.page.screenshot(full_page=True)
    allure.attach(
        png,
        name=f"{item.name}-failure",
        attachment_type=allure.attachment_type.PNG
    )
