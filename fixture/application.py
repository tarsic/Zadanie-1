from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")


    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()


    def init_group_creation(self):
        wd = self.wd
        wd.find_element_by_name("new").click()


    def fill_group_form(self, group):
        wd = self.wd
        self.open_groups_page()
        self.init_group_creation()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.submit_group_creation()


    def submit_group_creation(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()



    def destroy(self):
        self.wd.quit()