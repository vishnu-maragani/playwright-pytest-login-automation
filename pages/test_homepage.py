from playwright.sync_api import Page, expect


class Homepage:
    def __init__(self,page:Page):
        self.page = page
        self.textbox_input = page.get_by_role("textbox", name="search")
        self.cartButton_input =  page.get_by_role("button", name="Add To Cart")
        self.navigation_text_input = page.get_by_role("navigation")
    
    def textBox(self):
        expect(self.textbox_input).to_be_visible()
    def addtoCart(self):
        self.cartButton_input.first.click()
        self.cartButton_input.nth(1).click()
    def text_validation(self,count):
        expect(self.navigation_text_input).to_contain_text(count)
        
    def actions_homepage(self,cart_count):
        self.textBox()
        self.addtoCart()
        self.text_validation(cart_count)