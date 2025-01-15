from validator import validate_name, validate_phone

def add_contact(contacts):
    """Add a new contact."""
    print("\n--- Add Contact ---")
    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone Number: ").strip()
    address = input("Enter Address: ").strip()

    # Validate inputs
    if not validate_name(name):
        print("Error: Name must be a string.")
        return contacts
    if not validate_phone(phone):
        print("Error: Phone number must be numeric.")
        return contacts
    if any(contact['phone'] == phone for contact in contacts):
        print("Error: Phone number already exists.")
        return contacts

    # Add the new contact
    new_contact = {"name": name, "email": email, "phone": phone, "address": address}
    contacts.append(new_contact)
    print(f"Contact {name} added successfully!")
    return contacts

def view_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("\nNo contacts available.")
        return

    print("\n--- Contact List ---")
    print(f"{'Name':<20} {'Email':<30} {'Phone':<15} {'Address':<20}")
    print("-" * 85)
    for contact in contacts:
        print(f"{contact['name']:<20} {contact['email']:<30} {contact['phone']:<15} {contact['address']:<20}")
    print("-" * 85)

def remove_contact(contacts):
    """Remove a contact by name or phone number."""
    print("\n--- Remove Contact ---")
    identifier = input("Enter the Name or Phone Number of the contact to remove: ").strip()
    for contact in contacts:
        if contact['name'] == identifier or contact['phone'] == identifier:
            contacts.remove(contact)
            print(f"Contact {identifier} removed successfully!")
            return contacts

    print("Error: Contact not found.")
    return contacts

def search_contact(contacts):
    """Search for a contact."""
    print("\n--- Search Contact ---")
    query = input("Enter search term (Name, Email, Phone, or Address): ").strip().lower()
    results = [contact for contact in contacts if query in contact['name'].lower() or
               query in contact['email'].lower() or query in contact['phone'] or
               query in contact['address'].lower()]

    if results:
        print("\n--- Search Results ---")
        print(f"{'Name':<20} {'Email':<30} {'Phone':<15} {'Address':<20}")
        print("-" * 85)
        for contact in results:
            print(f"{contact['name']:<20} {contact['email']:<30} {contact['phone']:<15} {contact['address']:<20}")
        print("-" * 85)
    else:
        print("No contacts found matching the search term.")
