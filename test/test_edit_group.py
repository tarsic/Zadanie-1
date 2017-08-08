from model.group import group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(group(name="adeptissimo", header="moreover", footer="learningpy"))
    app.session.logout()