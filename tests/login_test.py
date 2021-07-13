import pytest
from pages import login_page


# The fixture is a type of function are run before a test, and provides input, or data to the test you choose to run
# https://docs.pytest.org/en/6.2.x/fixture.html
# https://docs.pytest.org/en/latest/how-to/fixtures.html
# https://simplythetest.tumblr.com/post/640676369255268352/fixtures-over-classes-why-using-pytest-fixtures
@pytest.fixture
def login(driver):
    return login_page.LoginPage(driver)

    def quit():
        driver.quit()

    request.addfinalizer(quit)  # Actions in addfinalizer get executed after a test method completes
    return login_page


def test_valid_credentials(login):  # By naming the method test_*, Pytest will know it's a test method
    login.with_("tomsmith", "SuperSecretPassword!")
    assert login.success_message_present()


def test_invalid_credentials(login):
    login.with_("tomsmith", "bad password")
    assert login.failure_message_present()
