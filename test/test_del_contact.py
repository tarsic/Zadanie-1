from model.contact import Contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_out_form(Contact(firstname="Romn", middlename="M", lastname="Smith", nickname="Pet",
                                          company="Ford", address="Chicago"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)




