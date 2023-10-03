"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, contract, commission=None):
        self.name = name
        self.contract = contract
        if commission is None:
            return
        self.commission = commission

    def get_pay(self):
        if hasattr(self, 'commission'):
            return self.contract.get_pay() + self.commission.get_amount()
        else:
            return self.contract.get_pay()

    def __str__(self):
        if hasattr(self, 'commission'):
            employeeString = self.name + " " + str(self.contract) + str(self.commission)
        else:
            employeeString = self.name + " " + str(self.contract)
        return employeeString + ". Their total pay is " + str(self.get_pay()) + "."


class Contract:

    def __init__(self, isHourly, amountPer, hours=0):
        self.isHourly = isHourly
        self.amountPer = amountPer
        if not hours == 0:
            self.hours = hours

    def get_pay(self):
        if self.isHourly:
            return (self.amountPer * self.hours)
        else:
            return self.amountPer

    def __str__(self):
        if self.isHourly:
            return f"works on a contract of {self.hours} hours at {self.amountPer}/hour"
        else:
            return f"works on a monthly salary of {self.amountPer}"


class Commission:

    def __init__(self, amountPer, isBonusCommission=False, numberOfContracts=0):
        self.amountPer = amountPer
        self.isBonusCommission = isBonusCommission
        if not numberOfContracts == 0:
            self.numberOfContracts = numberOfContracts

    def get_amount(self):
        if self.isBonusCommission:
            return self.amountPer
        else:
            return self.amountPer * self.numberOfContracts

    def __str__(self):
        commission_string = " and receives a "
        if self.isBonusCommission:
            return commission_string + f"bonus commission of {self.amountPer}"
        else:
            return commission_string + f"commission for {self.numberOfContracts} contract(s) at {self.amountPer}/contract"


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Contract(isHourly=False, amountPer=4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Contract(isHourly=True, amountPer=25, hours=100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Contract(isHourly=False, amountPer=3000), Commission(amountPer=200, numberOfContracts=4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', Contract(isHourly=True, amountPer=25, hours=150), Commission(amountPer=220, numberOfContracts=3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Contract(isHourly=False, amountPer=2000), Commission(amountPer=1500, isBonusCommission=True))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', Contract(isHourly=True, amountPer=30, hours=120), Commission(amountPer=600, isBonusCommission=True))
