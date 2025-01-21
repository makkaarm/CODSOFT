
def add_contact(contacts):
    while True:
        name = input("Enter name: ").strip()
        if name in contacts:
            print("Contact already exists!")
        else:
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            print(f"Contact '{name}' added successfully.\n")
            break

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.\n")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['Phone']}")
    print()

def search_contacts(contacts):
    option = input("Do you want to search by name or phone? Press 1 for name and 2 for phone: ").strip()
    if option == "1":
        search_by_name = input("Enter name: ").strip()
        if search_by_name in contacts:
            details = contacts[search_by_name]
            print(f"Name: {search_by_name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}\n")
        else:
            print("Contact not found.\n")
    elif option == "2":
        search_by_phone = input("Enter phone number: ").strip()
        for name, details in contacts.items():
            if details['Phone'] == search_by_phone:
                print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}\n")
                return
        print("Contact not found.\n")
    else:
        print("Invalid option.\n")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        print("Leave fields blank to keep the current value.")
        phone = input(f"Enter new phone (current: {contacts[name]['Phone']}): ").strip() or contacts[name]['Phone']
        email = input(f"Enter new email (current: {contacts[name]['Email']}): ").strip() or contacts[name]['Email']
        address = input(f"Enter new address (current: {contacts[name]['Address']}): ").strip() or contacts[name]['Address']
        contacts[name].update({"Phone": phone, "Email": email, "Address": address})
        print(f"Contact '{name}' updated successfully.\n")
    else:
        print("Contact not found.\n")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.\n")
    else:
        print("Contact not found.\n")

def main():
    contacts = {}
    while True:
        print("Contact Book:")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.\n")

if __name__ == "__main__":
    print("Welcome to the Contact Book!")
    main()
