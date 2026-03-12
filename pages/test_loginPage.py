

from playwright.sync_api import Page
class LoginPage:
    def __init__(self,page:Page):
        self.page=page
        self.username_input =  page.get_by_role("textbox", name="email@example.com")
        self.password_input =  page.get_by_role("textbox", name="enter your passsword")
        self.click_login =  page.get_by_role("button", name="Login")
    
    def enter_username(self,username):
        self.username_input.fill(username)
    def enter_password(self,password):
        self.password_input.fill(password)
    def login_click(self):
        self.click_login.click()
    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.login_click()
        