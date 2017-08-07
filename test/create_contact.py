# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application
from model.contact import contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


    
def test_create_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_out_form(contact(firstname="Romn", middlename="M", lastname="Smith", nickname="Pet", company="Ford", address="Chicago"))
    app.session.logout()


