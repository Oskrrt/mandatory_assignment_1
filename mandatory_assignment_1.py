#### A: #####
import time

### Original algorithm: ###
def find_prime_factors_original(n, prime_factors=[]):
    print("Printing results of the original algorithm:")
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors

### Optimized algorithm: ###
def is_edge_case(number):
    return number <= 1

def find_prime_factors(n, prime_factors=None):
    print("Printing results of the optimized algorithm:")
    if prime_factors is None:
        prime_factors = []

    if is_edge_case(n):
        return prime_factors
    i = 2
    addend = 1
    while i * i <= n:
        if i == 3:
            addend = 2
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += addend
    if n > 1:
        prime_factors.append(n)
    return prime_factors

t0 = time.perf_counter()
print(find_prime_factors(315245180938241856225939))
t1 = time.perf_counter()
print("Execution time:")
print(t1 - t0)



#### B: ####
class BankAccount:
    INSUFFICIENT_FUNDS = "insufficient funds"

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(BankAccount.INSUFFICIENT_FUNDS)

    def account_info(self):
        return f"Account holder: {self.account_holder}, Balance: ${self.balance:.2f}"

class SavingsAccount(BankAccount):
    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.interest_rate = 0.02

    def apply_interest(self):
        self.balance *= (1 + self.interest_rate)

class CheckingAccount(BankAccount):
    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.transaction_fee = 1

    def withdraw(self, amount):
        amount_with_fee = amount + self.transaction_fee
        if amount_with_fee <= self.balance:
            self.balance -= amount_with_fee
        else:
            print(BankAccount.INSUFFICIENT_FUNDS)

#Test cases:
def test_bank_system():
    test_bank_account()
    test_savings_account()
    test_checking_account()

def test_bank_account():
    print("\nTesting BankAccount class: ")
    bank_account = BankAccount("Oskar")
    bank_account.deposit(100)
    print(bank_account.account_info())
    bank_account.withdraw(90)
    print("After withdrawing 90$: " + bank_account.account_info())
    print("Attempt to withdraw more than the amount in the balance: ")
    bank_account.withdraw(11)

def test_savings_account():
    print("\nTesting SavingsAccount class: ")
    savings_account = SavingsAccount("Oskar")
    savings_account.deposit(1000)
    print("After depositing 1000$: " + savings_account.account_info())
    savings_account.apply_interest()
    print("After 1 year of saving: " + savings_account.account_info())
    for i in range(1, 10):
        savings_account.apply_interest()
    print("After 10 years of saving: " + savings_account.account_info())
    savings_account.withdraw(500)
    print("After withdrawing 500$: " + savings_account.account_info())

def test_checking_account():
    print("\nTesting CheckingAccount class: ")
    checking_account = CheckingAccount("Oskar")
    checking_account.deposit(1000)
    print("After depositing 1000$: " + checking_account.account_info())
    checking_account.withdraw(900)
    print("After withdrawing 900$: " + checking_account.account_info())

    print("After attempting to withdraw 99$: (will fail because of the transaction fee) ")
    checking_account.withdraw(99)
    print(checking_account.account_info())

#Run tests
#test_bank_system()