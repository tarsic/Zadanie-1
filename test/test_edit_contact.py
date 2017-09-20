# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_some_contact(app, db):
    if app.contact.count() == 0:
        app.contact.fill_out_form(Contact(firstname="Romn", middlename="M", lastname="Smith", nickname="Pet", company="Ford", address="Chicago"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    cont = Contact(firstname="Roma", middlename="Mone", lastname="Johnson", nickname="Petya", company="Ford", address="Chicago")
    cont.id = old_contacts[index].id
    app.contact.fill_edit_form(cont, index)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = cont
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
