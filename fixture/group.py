
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def init_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.init_group_creation()
        self.fill_out_group_form(group)
        self.submit_group_creation()

    def fill_out_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("home").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_out_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_out_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()



    def submit_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()