import sys
from faker import Faker
from contactModels import BaseContact, BusinessContact


fake = Faker()

def create_base_contacts(quantity):
    contacts = []
    for i in range(quantity):
        contact = BaseContact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone_number = fake.phone_number(),
            email = fake.email()
        )
        contacts.append(contact)
    return contacts

def create_business_contacts(quantity):
    contacts = []
    for i in range(quantity):
        contact = BusinessContact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone_number = fake.phone_number(),
            email = fake.email(),
            occupation= fake.job(),
            company_name= fake.company(),
            business_phone=fake.phone_number(),
        )
        contacts.append(contact)
    return contacts

def display_contact_info(contacts):
    for c in contacts:
        c.contact()
        print(f"Długość nazwy {c.label_length} znaki.")


def create_contacts(contact_type, qty):
    match contact_type:
        case 'base':
            base_contacts = create_base_contacts(qty)
            display_contact_info(base_contacts)
        case 'business':
            business_contacts = create_business_contacts(qty)
            display_contact_info(business_contacts)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(1)
    contact_type = sys.argv[1]
    quantity = int(sys.argv[2])
    create_contacts(contact_type, quantity)