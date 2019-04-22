import pickle
import os

# contact_list = [
#     {'name': 'Aimee Brunelle', 'email': 'ai-brunelle@arvinmeritor.info',
#         'phone': '862-467-5121'},
#     {'name': 'Stockley Meiners',
#         'email': 'stokley-meine@arvinmeritor.info', 'phone': '867-651-4298'},
#     {'name': 'Elmer Wilcox', 'email': 'elmerwillcox@autozone-inc.info',
#         'phone': '808-433-4285'},
#     {'name': 'Lainey Amezcua',
#      'email': 'lainey_am@arvinmeritor.info', 'phone': '867-319-2418'}
# ]

contactdata = 'contacts.txt'
# f = open(contactdata, 'wb')
# pickle.dump(contact_list, f)
# f.close()

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def print_contacts(self):
        # Checks if the contacts file exists, then prints the contacts
        if os.path.exists(contactdata):
            # Checks to see if contacts even exist within the text file
            if os.path.getsize(contactdata) <= 0:
                print("You have no contacts.")
            else:
                print('Name:\t\t\tEmail:\t\t\tPhone:')

                f = open(contactdata, 'rb')
                # Load the object from the file
                contactList = pickle.load(f)

                for contact in contactList:
                    print(contact['name'], '\t', contact['email'],
                        '\t', contact['phone'])
        else:
            print("Sorry, but you do not have any contacts. Please add some now:\n")
            f = open(contactdata, 'wb')
            f.close()

    def add_contacts(self):
        # Opens contact text file and asks for name, email, and phone number
        f = open(contactdata, 'rb')
        contactList = pickle.load(f)
        self.name = input("What is your full name: ")
        self.email = input("What is your email: ")
        self.phone = input("What is your phone number: ")

        # Adds the answers from the user into a list
        for i in range(1):
            d = {}
            d['name'] = self.name
            d['email'] = self.email
            d['phone'] = self.phone
            contactList.append(d)
        
        # Writes the next list to the contact file
        f.close()
        f = open(contactdata, 'wb')
        pickle.dump(contactList, f)
        f.close()


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
