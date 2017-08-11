from model.group import group

def test_edit_group_name(app):
    app.group.edit_first_group(group(name="New name"))

def test_edit_group_header(app):
    app.group.edit_first_group(group(header="New header"))
