from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, homephone=None, mobilephone=None,
                 workphone=None, email=None, email2=None, email3=None, secondaryphone=None, nickname=None, company=None, address=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.secondaryphone = secondaryphone
        self.nickname = nickname
        self.company = company
        self.address = address
        self.id = id

    def __repr__(self):
        return "%s:%s %s %s" % (self.id, self.firstname, self.lastname, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname and self.address == other.address

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize