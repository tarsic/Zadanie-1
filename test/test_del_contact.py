from model.contact import contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_out_form(contact(firstname="Romn", middlename="M", lastname="Smith", nickname="Pet", company="Ford", address="Chicago"))
    app.contact.delete_contact()
