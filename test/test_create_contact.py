# -*- coding: utf-8 -*-

from model.contact import Contact
from string import digits, hexdigits
from random import choice
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


some_phone = ''.join([choice(digits) for a in range(10)])
some_phone2 = ''.join([choice(digits) for b in range(10)])
some_phone3 = ''.join([choice(digits) for c in range(10)])
some_phone4 = ''.join([choice(digits) for g in range(10)])
some_email = ''.join([choice(hexdigits) for d in range(7)]) + "@.com"
some_email2 = ''.join([choice(hexdigits) for e in range(7)]) + "@.com"
some_email3 = ''.join([choice(hexdigits) for f in range(7)]) + "@.com"

testdata = [
    Contact(firstname=random_string("fname", 10), middlename=random_string("mname", 20), lastname=random_string("lname", 20),
            homephone=some_phone, mobilephone=some_phone2,
            workphone=some_phone3, email=some_email, email2=some_email2, email3=some_email3,
            secondaryphone=some_phone4, nickname=random_string("nick", 20),
            company=random_string("comp", 20), address=random_string("addr", 20))
    for i in range(2)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_create_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.fill_out_form(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
