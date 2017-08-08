# -*- coding: utf-8 -*-

from model.group import group





def test_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.fill_group_form(group(name="adept", header="more", footer="learning"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.fill_group_form(group(name="", header="", footer=""))
    app.session.logout()



