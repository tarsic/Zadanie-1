# -*- coding: utf-8 -*-

from model.group import Group


def test_add_new_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.fill_group_form(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        new_groups = list(map(clean, db.get_group_list()))
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)





