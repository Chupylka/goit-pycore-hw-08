import pickle

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"Contact(name={self.name}, phone={self.phone}, email={self.email})"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def __repr__(self):
        return f"AddressBook(contacts={self.contacts})"


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    book = load_data()
    print("Downloaded address book:", book)
    while True:
        action = input("Type 'add' to add a contact or 'exit' to finish: ").strip().lower()
        if action == "add":
            name = input("Name: ")
            phone = input("Phone number: ")
            email = input("Email: ")
            new_contact = Contact(name, phone, email)
            book.add_contact(new_contact)
            print(f"Contact {new_contact} add.")
        elif action == "exit":
            break
        else:
            print("Wrong command. Try again.")
    save_data(book)
    print("Address book data saved.")


if __name__ == "__main__":
    main()