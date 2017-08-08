# -*- coding: utf-8 -*-

from model.contact import contact


    
def test_create_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_out_form(contact(firstname="Romn", middlename="M", lastname="Smith", nickname="Pet", company="Ford", address="Chicago"))
    app.session.logout()


