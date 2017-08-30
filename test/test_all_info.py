import re
from random import randrange


def test_contact_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
    assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
    assert contact_from_home_page.email == contact_from_edit_page.email
    assert contact_from_home_page.email2 == contact_from_edit_page.email2
    assert contact_from_home_page.email3 == contact_from_edit_page.email3
    assert contact_from_home_page.secondaryphone == clear(contact_from_edit_page.secondaryphone)


def clear(s):
    return re.sub("[() -]", "", s)

