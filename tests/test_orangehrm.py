import re
from playwright.sync_api import Page, expect


def test_example(page: Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    #Login
    page.get_by_role("textbox", name="email@example.com").fill("vis1@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").fill("VisTech@0126")
    page.get_by_role("button", name="Login").click()
    
    #Home page
    expect(page.get_by_role("textbox", name="search")).to_be_visible()
    page.get_by_role("button", name="Add To Cart").first.click()
    page.get_by_role("button", name="Add To Cart").nth(1).click()
    expect(page.get_by_role("navigation")).to_contain_text("2")
