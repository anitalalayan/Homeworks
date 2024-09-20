from accounts.account import CheckingAccount, SavingsAccount, JointAccount
from customer.customers import Customer

def main():
    checking_account = CheckingAccount(account_number=1123, balance=1000.0, overdraft_limit=2000)
    savings_account = SavingsAccount(account_number=2123, balance=500.0, interest_rate=0.02)
    joint_account = JointAccount(account_number=3123, balance=1700.0, joint_owners=["Emily", "Noah"])

    customer = Customer(name="Hanchar", contact_info= 'hanchar.hancharyan@gmail.com')

    customer.add_account(checking_account)
    customer.add_account(savings_account)
    customer.add_account(joint_account)

    print("Performing transactions...")
    checking_account.deposit(200.0)
    savings_account.withdraw(150.0)
    checking_account.transfer(savings_account, 100.0)
    joint_account.add_owner("Poghos")
    joint_account.deposit(500.0)
    joint_account.withdraw(200.0)

    print("\nAccount Balances")
    customer.view_accounts()

    print("\nTransaction History")
    customer.view_transaction_history()


if __name__ == "__main__":
    main()
