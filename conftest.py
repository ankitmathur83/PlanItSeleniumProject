import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import os


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to use: chrome, firefox or chrome,firefox")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.param
    if browser == "chrome":
        driver_path = os.path.join(os.getcwd(), "drivers", "chromedriver")
        service = ChromeService(executable_path=driver_path)
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        driver_path = os.path.join(os.getcwd(), "drivers", "geckodriver")
        service = FirefoxService(executable_path=driver_path)
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)

    yield driver
    driver.quit()


# Adding this function allows us to parametrize the tests based on the browsers specified
def pytest_generate_tests(metafunc):
    if "driver" in metafunc.fixturenames:
        browsers = metafunc.config.getoption("--browser").split(",")
        metafunc.parametrize("driver", browsers, indirect=True)

