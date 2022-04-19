import pytest
from src.base.browser_conf import BrowserConfiguration

@pytest.fixture()
def setUp():
    print("Running method level setUp")

    yield
    print("Running method level tearDown")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    bc = BrowserConfiguration(browser)
    driver = bc.WebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.test_report.com/"))
        report.extra = extra