import uuid


def generate_unique_sesid():
    return str(uuid.uuid4())


def generate_navigation(lst: list) -> list:
    lst[-1] = lst[-1]['class'] + ' active'
    return lst

