# -*- coding: utf-8 -*-
import pytest
from group import group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.login(username="admin", password="secret")
    app.fill_group_form(group(name="adept", header="more", footer="learning"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.fill_group_form(group(name="", header="", footer=""))
    app.logout()



