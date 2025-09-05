"""
TASK: Create a ContactBook class.

Requirements:
1. Store contacts in a dictionary (name → phone number).
2. Provide a method to add new contacts.
3. Provide a method to delete contacts.
4. Provide a method to search for a contact by name.
5. Provide a method to show all contacts.

Example Usage:
    book = ContactBook()
    book.add_contact("Alice", "08012345678")
    print(book.search_contact("Alice"))  # "08012345678"
"""
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
    def delete_contact(self, name, number):
        del self.contacts[name]

    def get_contact(self, name):
        return self.contacts.get(name)
    def search_contact(self, name):
        if name in self.contacts:
            return f"Contact found: {name} - {self.contacts[name]}"
        else:
            return f"Contact not found: {name}"

    def show_all_contacts(self):
        if not self.contacts:
            return "No contacts in the phonebook."
        else:
            return "\n".join(f"{name}: {number}" for name, number in self.contacts.items())

book = ContactBook()
book.add_contact("Alice", "08034560078")
book.add_contact("Paul", "09034561178")
#book.delete_contact("Paul", "09034561178")
print(book.get_contact("Alice"))
#print(book.get_contact("Paul"))
#print(book.get_contact("Paul"))
print(book.search_contact("Alice"))
print(book.show_all_contacts())


