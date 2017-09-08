from model.contact import Contact
from string import digits, hexdigits
from random import choice
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_decoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
