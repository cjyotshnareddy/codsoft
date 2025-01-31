contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    print("Contact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    query = input("Enter name or phone number to search: ")
    found = [c for c in contacts if c['name'] == query or c['phone'] == query]
    if found:
        for contact in found:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("Contact not found.")

def update_contact():
    query = input("Enter name or phone number of contact to update: ")
    for contact in contacts:
        if contact['name'] == query or contact['phone'] == query:
            contact['name'] = input("Enter new name: ") or contact['name']
            contact['phone'] = input("Enter new phone number: ") or contact['phone']
            contact['email'] = input("Enter new email: ") or contact['email']
            contact['address'] = input("Enter new address: ") or contact['address']
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    query = input("Enter name or phone number of contact to delete: ")
    global contacts
    contacts = [c for c in contacts if c['name'] != query and c['phone'] != query]
    print("Contact deleted successfully!")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
