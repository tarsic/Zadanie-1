from model.contact import Contact
import random
import time

#def test_del_some_contact(app, db):
  #  if app.contact.count() == 0:
   #     app.contact.fill_out_form(Contact(firstname="Romn", middlename="M", lastname="Smith", nickname="Pet",
    #                                      company="Ford", address="Chicago"))
    #old_contacts = db.get_contact_list()
    #index = randrange(len(old_contacts))
    #app.contact.delete_contact_by_id(id)
    #new_contacts = db.get_contact_list()
    #assert len(old_contacts) - 1 == len(new_contacts)
    #old_contacts[index:index+1] = []
    #assert old_contacts == new_contacts


def test_del_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.fill_out_form(Contact(firstname="Romn", middlename="M", lastname="Smith", nickname="Pet",
                                          company="Ford", address="Chicago"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(1)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                           address=contact.address.strip())
        new_contacts = list(map(clean, db.get_contact_list()))
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


