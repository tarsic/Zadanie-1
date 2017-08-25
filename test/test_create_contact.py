# -*- coding: utf-8 -*-

from model.contact import Contact

    
def test_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Romn", middlename="M", lastname="Smith", nickname="Pet", company="Ford", address="Chicago")
    app.contact.fill_out_form(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
