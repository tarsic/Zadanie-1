import re
from model.contact import Contact


def test_contact_on_home_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_full_contact_list()
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)
    #assert contacts_from_home_page.firstname == contacts_from_db.firstname
    #assert contacts_from_home_page.lastname == contacts_from_db.lastname
    #assert contacts_from_home_page.address == contacts_from_db.address
    assert contacts_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db)
    assert contacts_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),filter(lambda x: x is not None,
                                                   [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.email, contact.email2, contact.email3]))))
