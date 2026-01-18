import pytest
from core.driver_factory import create_driver
from utils.screenshot import take_screenshot

@pytest.fixture
def driver(request):
    driver = create_driver()
    yield driver

    if request.node.rep_call.failed:
        screenshot_path = take_screenshot(driver, request.node.name)
        if hasattr(request.node, "extra"):
            request.node.extra.append(pytest_html.extras.image(screenshot_path))
        else:
            request.node.extra = [pytest_html.extras.image(screenshot_path)]

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    outcome = yield
    rep = outcome.get_result()
    extra = getattr(rep, "extra", [])
    item.extra = extra
    


def pytest_configure(config):
    if not hasattr(config, "_metadata"):
        config._metadata = {}

    config._metadata["Project"] = "QA Automation Portfolio"
    config._metadata["Tested By"] = "Wahyu"
    config._metadata["Base URL"] = "https://the-internet.herokuapp.com"
    config._metadata["Browser"] = "Chrome"

    
def pytest_html_report_title(report):
    report.title = "QA Automation Report – HerokuApp Login"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "<p><strong>Project:</strong> QA Automation Portfolio</p>",
        "<p><strong>Scope:</strong> Login & Logout Automation</p>",
        "<p><strong>Framework:</strong> Selenium + Pytest</p>",
        "<p><strong>Author:</strong> Wahyu Agustiar</p>"
    ])

