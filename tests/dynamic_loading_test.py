import pytest
import os
from selenium import webdriver
from pages import dynamic_loading_page

# The fixture is a type of function are run before a test, and provides input, or data to the test you choose to run
# https://docs.pytest.org/en/6.2.x/fixture.html
# https://docs.pytest.org/en/latest/how-to/fixtures.html
# https://simplythetest.tumblr.com/post/640676369255268352/fixtures-over-classes-why-using-pytest-fixtures
@pytest.fixture
def dynamic_loading(driver):
    return dynamic_loading_page.DynamicLoadingPage(driver)

def test_hidden_element(dynamic_loading):
    dynamic_loading.load_example("1")
    assert dynamic_loading.finish_text_present(), "Dynamic loading finish text should be present for hidden element"

def test_rendered_element(dynamic_loading):
    dynamic_loading.load_example("2")
    assert dynamic_loading.finish_text_present(), "Dynamic loading finish text should be present for rendered element"
