import json

def load_contacts(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contacts, filename):
    with open(filename, 'w') as f:
        json.dump(contacts, f, indent=4)

def contact_book():
    filename = "contacts.json"
    contacts = load_contacts(filename)

    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            contacts[name] = phone
            save_contacts(contacts, filename)
            print("Contact saved.")

        elif choice == '2':
            if contacts:
                print("\n--- Contact List ---")
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
            else:
                print("No contacts found.")

        elif choice == '3':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid option. Try again.")

contact_book()
