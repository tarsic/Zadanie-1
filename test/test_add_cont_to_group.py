from fixture.contact import Contact

def test_add_cont_to_group(app):
    if app.contact.count() == 0:
        app.contact.fill_out_form(Contact(firstname="Romn", middlename="M", lastname="Smith", nickname="Pet",
                                          company="Ford", address="Chicago"))
    app.contact.add_cont_to_group()
