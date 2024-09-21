import json
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

    @staticmethod
    def from_dict(data):
        return Contact(data['name'], data['phone'], data['email'])

CONTACTS_FILE = 'contacts.json'

def read_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return [Contact.from_dict(contact) for contact in json.load(file)]
    return []

def write_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump([contact.to_dict() for contact in contacts], file, indent=4)

def add_contact(name, phone, email):
    contacts = read_contacts()
    contacts.append(Contact(name, phone, email))
    write_contacts(contacts)
    print(f"Contact {name} added successfully.")

def view_contacts():
    contacts = read_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

def edit_contact(index, name=None, phone=None, email=None):
    contacts = read_contacts()
    if 0 <= index < len(contacts):
        if name:
            contacts[index].name = name
        if phone:
            contacts[index].phone = phone
        if email:
            contacts[index].email = email
        write_contacts(contacts)
        print(f"Contact {index + 1} updated successfully.")
    else:
        print("Invalid contact index.")

def delete_contact(index):
    contacts = read_contacts()
    if 0 <= index < len(contacts):
        deleted_contact = contacts.pop(index)
        write_contacts(contacts)
        print(f"Contact {deleted_contact.name} deleted successfully.")
    else:
        print("Invalid contact index.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            view_contacts()
            index = int(input("Enter the index of the contact to edit: ")) - 1
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            edit_contact(index, name or None, phone or None, email or None)
        elif choice == '4':
            view_contacts()
            index = int(input("Enter the index of the contact to delete: ")) - 1
            delete_contact(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
