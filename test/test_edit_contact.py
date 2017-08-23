# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_out_form(Contact(firstname="Romn", middlename="M", lastname="Smith", nickname="Pet", company="Ford", address="Chicago"))
    app.contact.fill_edit_form(Contact(firstname="Roma", middlename="Mone", lastname="Johnson", nickname="Petya", company="Ford", address="Chicago"))
