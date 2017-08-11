from model.group import group

def test_edit_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(group(name="New name"))
    app.session.logout()

def test_edit_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(group(header="New header"))
    app.session.logout()