from model.group import Group
import random


def test_edit_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.fill_group_form(Group(name="test"))
    old_groups = db.get_group_list()
    group_was = random.choice(old_groups)
    index = old_groups.index(group_was)
    group_now = Group(name="New name", header="New header", footer="New footer", id=group_was.id)
    app.group.edit_group_by_id(group_was.id, group_now)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group_now
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        new_groups = list(map(clean, db.get_group_list()))
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



