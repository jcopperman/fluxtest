class IncomeTaxCalculator:
    def __init__(self, income, age):
        self.income = income
        self.age = age

    def calculate_tax(self):
        if self.age < 65:
            if self.income <= 50000:
                return 0.0
            elif self.income > 50000:
                return (self.income - 50000) * 0.1
        elif self.age >= 65:
            if self.income <= 60000:
                return 0.0
            elif self.income > 60000:
                return (self.income - 60000) * 0.1
