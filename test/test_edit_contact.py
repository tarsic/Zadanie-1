# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_out_form(Contact(firstname="Romn", middlename="M", lastname="Smith", nickname="Pet", company="Ford", address="Chicago"))
    old_contacts = app.contact.get_contact_list()
    cont = Contact(firstname="Roma", middlename="Mone", lastname="Johnson", nickname="Petya", company="Ford", address="Chicago")
    cont.id = old_contacts[0].id
    app.contact.fill_edit_form(cont)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = cont
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
