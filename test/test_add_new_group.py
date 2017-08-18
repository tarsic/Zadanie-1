# -*- coding: utf-8 -*-

from model.group import group





def test_add_new_group(app):
    old_groups = app.group.get_group_list()
    app.group.fill_group_form(group(name="adept", header="more", footer="learning"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)



def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.fill_group_form(group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)





