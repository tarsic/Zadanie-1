from model.group import group

def test_delete_first_group(app):
    if app.group.count () == 0:
        app.group.fill_group_form(group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)

