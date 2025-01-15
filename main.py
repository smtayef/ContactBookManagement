from contact_manager import add_contact, view_contacts, remove_contact, search_contact
from file_handler import load_contacts, save_contacts

# Load existing contacts when the program starts
contacts = load_contacts()

def display_menu():
    """Display the main menu."""
    print("\n===== Contact Book Management System =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contacts")
    print("5. Exit")
    print("==========================================")

def main():
    """Main program loop."""
    global contacts
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            contacts = add_contact(contacts)
            save_contacts(contacts)  # Save after addition
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            contacts = remove_contact(contacts)
            save_contacts(contacts)  # Save after removal
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            print("Exiting the Contact Book Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
