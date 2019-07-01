import re
from validate_email import validate_email


def valid_email(email):

    permitidos = r"\"?([-a-zA-Z0-9._-]+@(?:[a-zA-Z0-9]+\.)+[a-zA-Z]{1,3}$)\"?"

    padrao = re.compile(permitidos)

    if not re.match(padrao, email):
        return False
    elif not permitidos:
        return False
    elif validate_email(email):
        return True
    else:
        return False


def filter_email(emails):
    return list(filter(lambda email: True if valid_email(email)
                else False, emails))
