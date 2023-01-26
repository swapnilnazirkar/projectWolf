from selenium import webdriver
import pytest
@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
################ HTML report ######################
def pytest_configure(config):
    config._metadata["project name"]="project wolf"
    config._metadata["Module name"] = "costomers"
    config._metadata["Tester"] = "swapnil"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("plugin",None)