from fixture.contact import Contact
import random


def test_add_cont_to_group(app, db):
    if app.contact.count() == 0:
        app.contact.fill_out_form(Contact(firstname="Romn", middlename="M", lastname="Smith", nickname="Pet",
                                          company="Ford", address="Chicago"))
    old_contacts = db.get_contact_list()
    group_list = db.get_group_list()
    contact = random.choice(old_contacts)
    group = random.choice(group_list)
    group_id = int(group.id)
    contact_id = contact.id
    app.contact.add_cont_to_group_by_id(contact_id, group_id)

