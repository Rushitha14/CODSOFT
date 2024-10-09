class ContactInfo:
    def __init__(self, full_name, phone_number, email_address, house_address):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.house_address = house_address

    def __str__(self):
        return f"{self.full_name}, Phone: {self.phone_number}, Email: {self.email_address}, Address: {self.house_address}"

class ContactBookManager:
    def __init__(self):
        self.contacts = []

    def add_new_contact(self, full_name, phone_number, email_address, house_address):
        new_contact = ContactInfo(full_name, phone_number, email_address, house_address)
        self.contacts.append(new_contact)
        print(f"Contact '{full_name}' added successfully!")

    def display_all_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(contact)

    def search_for_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term in contact.full_name or search_term in contact.phone_number:
                found_contacts.append(contact)
        if found_contacts:
            print("\nSearch Results:")
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact_info(self, full_name, new_phone_number=None, new_email_address=None, new_house_address=None):
        for contact in self.contacts:
            if contact.full_name == full_name:
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_email_address:
                    contact.email_address = new_email_address
                if new_house_address:
                    contact.house_address = new_house_address
                print(f"Contact '{full_name}' updated successfully!")
                return
        print(f"Contact '{full_name}' not found.")

    def delete_contact(self, full_name):
        for contact in self.contacts:
            if contact.full_name == full_name:
                confirm = input(f"Are you sure you want to delete '{full_name}'? (yes/no): ")
                if confirm.lower() == 'yes':
                    self.contacts.remove(contact)
                    print(f"Contact '{full_name}' deleted successfully!")
                else:
                    print("Deletion canceled.")
                return
        print(f"Contact '{full_name}' not found.")


def is_valid_email(email):
    return "@" in email and "." in email

def is_valid_name(name):
    return name.isalpha() or " " in name  

def run_contact_book():
    contact_book = ContactBookManager()
    while True:
        print("\nContact Book Menu:")
        print("1. Add New Contact")
        print("2. Display All Contacts")
        print("3. Search for Contact")
        print("4. Update Contact Information")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            while True:
                full_name = input("Enter full name: ")
                if is_valid_name(full_name) and full_name.strip() != "":
                    break
                else:
                    print("Invalid name. Please enter a valid string without numbers.")
            while True:
                phone_number = input("Enter 10-digit phone number: ")
                if len(phone_number) == 10 and phone_number.isdigit():
                    break
                else:
                    print("Invalid phone number. Please enter a 10-digit number.")
            email_address = input("Enter email address: ")
            while not is_valid_email(email_address):
                print("Invalid email format. Please try again.")
                email_address = input("Enter email address: ")
            house_address = input("Enter house address: ")
            contact_book.add_new_contact(full_name, phone_number, email_address, house_address)
        elif choice == '2':
            contact_book.display_all_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_for_contact(search_term)
        elif choice == '4':
            full_name = input("Enter the name of the contact to update: ")
            while True:
                new_phone_number = input("Enter new 10-digit phone number (or leave blank to keep current): ")
                if new_phone_number == "":
                    new_phone_number = None
                    break
                elif len(new_phone_number) == 10 and new_phone_number.isdigit():
                    break
                else:
                    print("Invalid phone number. Please enter a 10-digit number or leave blank to keep current.")
            new_email_address = input("Enter new email address (or leave blank to keep current): ")
            if new_email_address != "" and not is_valid_email(new_email_address):
                print("Invalid email format. Update canceled.")
                continue
            new_house_address = input("Enter new house address (or leave blank to keep current): ")
            contact_book.update_contact_info(full_name, new_phone_number, new_email_address or None, new_house_address or None)
        elif choice == '5':
            full_name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(full_name)
        elif choice == '6':
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    run_contact_book()
