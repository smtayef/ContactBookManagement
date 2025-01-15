def validate_name(name):
    """Validate that the name is a string."""
    return name.isalpha()

def validate_phone(phone):
    """Validate that the phone number is numeric."""
    return phone.isdigit()
