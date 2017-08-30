# -*- coding: utf-8 -*-

from model.contact import Contact
from string import digits, hexdigits
from random import choice

    
def test_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    some_phone = ''.join([choice(digits) for i in range(10)])
    some_email = ''.join([choice(hexdigits) for i in range(7)]) + "@.com"
    contact = Contact(firstname="Romn", middlename="M", lastname="Smith", homephone=some_phone, mobilephone=some_phone,
                     workphone=some_phone, email=some_email, email2=some_email, email3=some_email, secondaryphone=some_phone, nickname="Pet", company="Ford", address="Chicago")
    app.contact.fill_out_form(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
