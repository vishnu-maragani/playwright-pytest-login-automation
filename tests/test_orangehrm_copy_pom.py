import re
from playwright.sync_api import Page, expect
import pytest

from pages.test_homepage import Homepage
from pages.test_loginPage import LoginPage
from utils.app_url import URL , get_credentials



@pytest.mark.parametrize("credentials",get_credentials())
def test_example(page: Page,credentials):
    pageurl = URL(page)
    loginpage = LoginPage(page)
    homepage = Homepage(page)
    pageurl.page_url()
    #Login
    loginpage.login(credentials["username"],credentials["password"])
    #Homepage
    homepage.actions_homepage("2")