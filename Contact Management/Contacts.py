import os
import re

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self): #For proper printing
        return (f'Contact -> name: {self.name} | phone: {self.phone} | email: {self.email}')
        
    def write_contact(self): #Format to write in file
        return (f'{self.name}, {self.phone}, {self.email}')
    
class ManageContacts:
    file_name = 'contacts.txt'
    def __init__(self):
        #List of contacts
        self.contacts = []
        #Check that file exists
        if os.path.isfile(self.file_name):
            #Add file contacts (formated) to the list
            self.contacts = self.read_contacts_file()
        else:
            #if no file, create file and add initial contacts
            self.add_initial_contacts()

    def add_initial_contacts(self):
        initial_contacts = [Contact('John Smith', '123456', 'john@gmail.com'), Contact('Peter Sousa', '654321', 'peter@hotmail.com')]
        self.contacts.extend(initial_contacts)
        self.save_contacts_in_file(initial_contacts)
    
    def save_contacts_in_file(self, contacts):
        try:
            with open(self.file_name, 'w') as file:
                for contact in contacts:
                    file.write(f'{contact.write_contact()}\n')
        except Exception as e:
            print(f'Error saving contacts in file: {e}')
    
    def read_contacts_file(self):
        contacts = []
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    line = line.strip()
                    #Skip empty lines
                    if not line:
                        continue
                    name, phone, email = line.strip().split(',')
                    contact = Contact(name.strip(), phone.strip(), email.strip())
                    contacts.append(contact)
        except Exception as e:
            print(f'Error readin file: {e}')
            return [] #return an empty list
        return contacts
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts_in_file([contact])
    
    def show_contacts(self):
        print('---CONTACT LIST---')
        for contact in self.contacts:
            print(contact)
    
    def getContacts(self):
        return self.contacts
    
    def delete_contact(self, name):
        count = len(self.contacts)
        #list comprehension to keep only contacts not matching the given name
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]
        if len(self.contacts) < count:
            self.save_contacts_in_file(self.contacts)
            return True
        return False
   
        
class AppContacts:
    def __init__(self):
        self.manage_contacts = ManageContacts()
    
    def app_contacts(self):
        print('\n*** CONTACT MANAGEMENT APP ***\n')
        print('''Options:
              1. Add Contact
              2. Show Contacts
              3. Search Contact
              4. Delete Contact
              5. Exit''')
        try:
            return int(input('Chose an option: '))
        except ValueError:
            print('Enter a number between 1-5')
            return 0

    def execute_option(self, option):
        if option == 1:
            self.add_contact()
        elif option == 2:
            self.manage_contacts.show_contacts()
        elif option == 3:
            self.search_contact()
        elif option == 4:
            self.delete_contact()
        elif option == 5:
            print('Leaving the system...')
            return True
        else:
            print('Not a valid option')
        return False
    
    @staticmethod
    def is_valid_phone(phone):
        #check that only contain digits
        return phone.isdigit()

    @staticmethod
    def is_valid_email(email):
        #basic email validation using regex
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def add_contact(self):
        name = input('Name: ')
        #With validation
        while True:
            phone = input('Phone: ')
            if self.is_valid_phone(phone):
                break
            print('Invalid Phone. Only digits allowed.')
        #with validation
        while True:
            email = input('Email: ')
            if self.is_valid_email(email):
                break
            print('Invalid email format.')
        contact = Contact(name, phone, email)
        self.manage_contacts.add_contact(contact)
        print('Contact added')

    def search_contact(self):
        name_search = input('What name do you want to search? ')
        contacts = self.manage_contacts.getContacts()
        contact = next((contact for contact in contacts if contact.name.lower() == name_search.lower()), None)
        if contact:
            print(contact)
        else:
            print(f'{name_search} not found')

    def delete_contact(self):
        name_to_delete = input('What name do you want to delete? ')
        if self.manage_contacts.delete_contact(name_to_delete):
            print(f'{name_to_delete} is no longer a contact')
        else:
            print(f'{name_to_delete} not found')

#PROGRAM
if __name__ == '__main__':
    app = AppContacts()
    while True:
        try:
            option = app.app_contacts()
            should_exit = app.execute_option(option)
            if should_exit:
                break
        except KeyboardInterrupt:
            print("\nOperation cancelled by user")
            break
        except Exception as e:
            print(f"An error occurred: {e}")