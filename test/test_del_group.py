from model.group import group

def test_delete_first_group(app):
    if app.group.count () == 0:
        app.group.fill_group_form(group(name="test"))
    app.group.delete_first_group()

