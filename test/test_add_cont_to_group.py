from model.group import group

def test_add_cont_to_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_cont_to_group()
    app.session.logout()