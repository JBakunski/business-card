
from faker import Faker

class BusinessCard:
    def __init__(self, first_name, last_name, occupation, email):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.email = email

        self._fullname_length = ''


    def display_info(self):
        print(f"Imię: {self.first_name}, Nazwisko: {self.last_name}, Stanowisko: {self.occupation}, Adres email: {self.email}")
    
    def contact(self):
        print(f"Kontaktuje się z {self.first_name}, {self.last_name}, {self.occupation}, {self.email}")
    
    @property
    def fullname_length(self):
        return f"{len(self.first_name)}_{len(self.last_name)}"

    

fake = Faker()

business_cards = []

for x in range(5):
    card = BusinessCard(first_name=fake.first_name(),
    last_name=fake.last_name(),
    occupation=fake.job(),
    email=fake.email())
    business_cards.append(card)

for card in business_cards:
    card.contact()
    print(f"{card.fullname_length}")