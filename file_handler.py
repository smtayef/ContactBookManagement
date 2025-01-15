import os

FILE_NAME = "contacts.csv"

def load_contacts():
    """Load contacts from a file."""
    if not os.path.exists(FILE_NAME):
        return []

    contacts = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, email, phone, address = line.strip().split(",")
            contacts.append({"name": name, "email": email, "phone": phone, "address": address})
    return contacts

def save_contacts(contacts):
    """Save contacts to a file."""
    with open(FILE_NAME, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['email']},{contact['phone']},{contact['address']}\n")
