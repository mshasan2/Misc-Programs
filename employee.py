import requests

class Employee:

    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    # In Python, @property is a built-in decorator 
    # that allows you to define methods that can be accessed like attributes. 
    # It is often used to create read-only properties or to define custom behavior 
    # for getting, setting, and deleting attributes.
    # In this case, the email method is used as a property.
    # obj.email
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
