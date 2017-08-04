from selenium.webdriver.firefox.webdriver import WebDriver

class Applicashka():

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)


    def open_home_page(self):
        # open home page
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")
        return wd

    def login(self, username="admin", password="secret"):
        wd = self.open_home_page()
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def create_new_contact(self):
        wd = self.wd
        # create new contact
        wd.find_element_by_link_text("add new").click()

    def fill_out_form(self, contact):
        wd = self.wd
        self.create_new_contact()
        # fill out the form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        self.submit_creating()


    def submit_creating(self):
            wd = self.wd
            # submit creating
            wd.find_element_by_name("submit").click()

    def logout(self):
        wd=self.wd
        # logout
        wd.find_element_by_link_text("Logout").click()


    def destroy(self):
        self.wd.quit()




