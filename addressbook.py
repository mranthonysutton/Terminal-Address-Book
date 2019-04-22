import pickle

contact_list = [
    {'name': 'Aimee Brunelle', 'email': 'ai-brunelle@arvinmeritor.info',
        'phone': '862-467-5121'},
    {'name': 'Stockley Meiners',
        'email': 'stokley-meine@arvinmeritor.info', 'phone': '867-651-4298'},
    {'name': 'Elmer Wilcox', 'email': 'elmerwillcox@autozone-inc.info',
        'phone': '808-433-4285'},
    {'name': 'Lainey Amezcua',
     'email': 'lainey_am@arvinmeritor.info', 'phone': '867-319-2418'}
]


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def print_contacts(self):
        print('Name:\t\t\tEmail:\t\t\tPhone:')
        for contact in contact_list:
            print(contact['name'], '\t', contact['email'],
                  '\t', contact['phone'])

    def add_contacts(self):
        self.name = input("What is your full name: ")
        self.email = input("What is your email: ")
        self.phone = input("What is your phone number: ")
        
        for i in range(1):
            d = {}
            d['name'] = self.name
            d['email'] = self.email
            d['phone'] = self.phone
            contact_list.append(d)


print("What would you like to do: \n")
prompt = input("(V)iew contacts\n(A)dd new contact\n").lower()

c = Contact('Aimee Brunelle', 'ai-brunelle@arvinmeritor.info', '862-467-5121')

if prompt == 'v':
    c = Contact('Anthony Sutton', 'anthonysutton.io', '702-886-7493')
    print()
    c.print_contacts()
elif prompt == 'a':
    c = Contact('Anthony Sutton', 'anthonysutton.io', '702-886-7493')
    print()
    c.add_contacts()
    print()
    c.print_contacts()
else:
    print("Sorry, but the program has ended due to wrong input.")
