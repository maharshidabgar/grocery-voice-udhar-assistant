import re


def validate_name(name: str):
    """
    Validate customer name.
    """

    name = name.strip()

    if len(name) < 2:
        raise ValueError("Customer name is too short.")

    if len(name) > 50:
        raise ValueError("Customer name is too long.")

    if not re.match(r"^[A-Za-z ]+$", name):
        raise ValueError(
            "Customer name should contain only letters and spaces."
        )

    return name.title()


def validate_mobile(mobile: str):

    mobile = mobile.strip()

    if mobile == "":
        return ""

    if not mobile.isdigit():
        raise ValueError("Mobile number must contain only digits.")

    if len(mobile) != 10:
        raise ValueError("Mobile number must be 10 digits.")

    return mobile