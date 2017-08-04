# -*- coding: utf-8 -*-

import pytest

from fixture.applicashka import Applicashka
from model.contact import contact


@pytest.fixture
def app(request):
    fixture = Applicashka()
    request.addfinalizer(fixture.destroy)
    return fixture


    
def test_create_contact(app):
    app.login()
    app.fill_out_form(contact(firstname="Romn", middlename="M", lastname="Smith", nickname="Pet", company="Ford", address="Chicago"))
    app.logout()


