package com.revature.bank;

public class SavingAccount extends BankAccount implements SimpleInterest {

    public SavingAccount() {
    }

    public SavingAccount(String accountID, String accountName, double balance) {
        super(accountID, accountName, balance);
    }

    @Override
    public String toString() {
        return "SavingAccount{} " + super.toString();
    }

    @Override
    public double deposit(double amount) throws NegativeAmountException {
        return super.deposit(amount);
    }

    @Override
    public double withdraw(double amount) throws NegativeAmountException {
        double balance=super.getBalance();

        if (amount < 0) {
            throw new NegativeAmountException("Amount cannot be negative");
        }

        if(balance < 500){
            throw new IllegalArgumentException("Balance is below 500. Cannot withdraw.");
        }

            balance -= amount;
            super.setBalance(balance);
            return balance;
        }

}


