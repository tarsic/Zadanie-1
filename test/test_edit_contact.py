# -*- coding: utf-8 -*-
from model.contact import contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_edit_form(contact(firstname="Roma", middlename="Mone", lastname="Johnson", nickname="Petya", company="Ford", address="Chicago"))
    app.session.logout()
