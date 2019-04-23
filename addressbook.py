import csv
import os

# Prints out all of the contacts contained in the csv file to the terminal
def view_contacts():
    # Checks if the file exists, if not, directs the user to add contacts
    if os.path.isfile('contacts.csv'):
        with open('contacts.csv', 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            print('\nName:\t\tPhone:\t\tEmail:')

            for line in csv_reader:
                print(line['name'], '\t', line['phone'], '\t', line['email'])
    else:
        print("Sorry you do not have any contacts. Let's add some now!\n")
        add_contacts()

# Asks the user a series of questions to add the contact to their address book
def add_contacts():
    print('\n')
    row = []

    # Checks if the file exists then asks the user the questions
    # needed to import the contact information
    # If the file does not exist, creates a new file with the required headers
    if os.path.isfile('contacts.csv'):

        row.append(input("What is the name: "))
        row.append(input("What is the phone number: "))
        row.append(input("What is the email address: "))

        with open('contacts.csv', 'a', newline='') as csv_file:
            headers = ['name', 'phone', 'email']
            writer = csv.writer(csv_file)
            writer.writerow(row)

        csv_file.close()
    else:
        row.append(input("What is the name: "))
        row.append(input("What is the phone number: "))
        row.append(input("What is the email address: "))

        with open('contacts.csv', 'a', newline='') as csv_file:
            headers = ['name', 'phone', 'email']
            writer = csv.writer(csv_file)
            writer.writerow(headers)
            writer.writerow(row)

        csv_file.close()

    view_contacts()

# Program Interface
print("What would you like to do: \n")
prompt = input("(V)iew contacts\n(A)dd new contact\n").lower()

if prompt == 'v':
    view_contacts()
elif prompt == 'a':
    add_contacts()
else:
    print("Sorry, but the program has ended due to wrong input.")
