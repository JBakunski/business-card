class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        
        self._label_length = len(f"{self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return self._label_length
    
    def contact(self):
        print(f"Wybieram number {self.phone_number} i dzwonię do {self.first_name} {self.last_name}.")


class BusinessContact(BaseContact):
    def __init__(self, occupation, company_name, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.occupation = occupation
        self.company_name = company_name
        self.business_phone = business_phone
    
    def contact(self):
        print(f"Wybieram number {self.business_phone} i dzwonię do {self.first_name} {self.last_name}.")