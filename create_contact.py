# -*- coding: utf-8 -*-

import pytest
from contact import contact
from applicashka import Applicashka


@pytest.fixture
def app(request):
    fixture = Applicashka()
    request.addfinalizer(fixture.destroy)
    return fixture


    
def test_create_contact(app):
    app.login()
    app.fill_out_form(contact(firstname="Romn", middlename="M", lastname="Smith", nickname="Pet", company="Ford", address="Chicago"))
    app.logout()


