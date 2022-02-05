import re

PATTERN = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z-0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def email_parse(email_address):
    if re.fullmatch(PATTERN, email_address):
        print(re.split(r'@', email_address))
    else:
        raise ValueError(f'wrong email: {email_address}')


email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')
