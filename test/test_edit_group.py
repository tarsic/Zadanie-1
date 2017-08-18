from model.group import group

def test_edit_group_name(app):
    if app.group.count () == 0:
        app.group.fill_group_form(group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(group(name="New name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_group_header(app):
    if app.group.count () == 0:
        app.group.fill_group_form(group(name="gut", header="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

