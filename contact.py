class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name not in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email}
            print(f"Contact '{name}' added successfully.")
        else:
            print(f"Contact '{name}' already exists. Use 'edit_contact' to modify information.")

    def edit_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone is not None:
                self.contacts[name]['phone'] = phone
            if email is not None:
                self.contacts[name]['email'] = email
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' does not exist. Use 'add_contact' to add a new contact.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' does not exist.")

    def display_contacts(self):
        print("Contacts:")
        for name, info in self.contacts.items():
            print(f"{name}: Phone - {info['phone']}, Email - {info['email']}")

contact_manager = ContactManager()

contact_manager.add_contact('John Doe', '123-456-7890', 'john.doe@example.com')
contact_manager.add_contact('Jane Smith', '987-654-3210', 'jane.smith@example.com')

contact_manager.display_contacts()

contact_manager.edit_contact('John Doe', phone='555-555-5555')

contact_manager.display_contacts()

contact_manager.delete_contact('Jane Smith')

contact_manager.display_contacts()
