# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_edit_some_contact(app, db):
    if app.contact.count() == 0:
        app.contact.fill_out_form(Contact(firstname="Romn", middlename="M", lastname="Smith", nickname="Pet",
                                          company="Ford", address="Chicago"))
    old_contacts = db.get_contact_list()
    contact_was = random.choice(old_contacts)
    index = old_contacts.index(contact_was)
    contact_now = Contact(firstname="Roma", middlename="Mone", lastname="Johnson", nickname="Petya",
                          company="Ford", address="Chicago", id=contact_was.id)
    app.contact.fill_edit_form_by_id(contact_was.id, contact_now)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact_now
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)