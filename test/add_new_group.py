# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.fill_group_form(group(name="adept", header="more", footer="learning"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.fill_group_form(group(name="", header="", footer=""))
    app.session.logout()



