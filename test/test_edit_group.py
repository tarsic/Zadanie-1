from model.group import group

def test_edit_group_name(app):
    if app.group.count () == 0:
        app.group.fill_group_form(group(name="test"))
    app.group.edit_first_group(group(name="New name"))

def test_edit_group_header(app):
    if app.group.count () == 0:
        app.group.fill_group_form(group(name="gut", header="test"))
    app.group.edit_first_group(group(header="New header"))
