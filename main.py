from dataclasses import dataclass

@dataclass
class User:
    name : str
    age : int
    gender : str

    def show_details(self):
        print('Pernal Details')
        print('')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')


# us = User(name='kanja',age=40,gender='Male')
# print(us.show_details())


@dataclass
class Bank:
    user : User
    balance : int = 0
    

    def deposit(self, amount):
        self.balance += amount
        print(f'Account bala]nce has been updated to:   Ksh {self.balance}')

    
    def withdrawal(self, amount):
        if self.balance < amount:
            print(f'Inssuficient funds balance availble is Ksh {self.balance}')
        else:
            self.balance -= amount
            print(f'Account bala]nce has been updated to:   Ksh {self.balance}' )

    def view_balance(self):
        self.user.show_details() 
        print(f'Account balance is Ksh: {self.balance}')




us = User(name='kanja',age=40,gender='Male')
acc = Bank(us)
acc.deposit(200)
acc.deposit(300)
acc.withdrawal(30)
acc.withdrawal(1000)
acc.view_balance()