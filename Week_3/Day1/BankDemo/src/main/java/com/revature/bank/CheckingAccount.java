package com.revature.bank;

public class CheckingAccount extends BankAccount{


    public CheckingAccount() {
    }

    public CheckingAccount(String accountID, String accountName, double balance) {
        super(accountID, accountName, balance);
    }

    @Override
    public String toString() {
        return "CheckingAccount{} " + super.toString();
    }

    //call deposit
    @Override
    public double deposit(double amount) throws NegativeAmountException {
        return super.deposit(amount);
    }

    @Override
    public double withdraw(double amount) throws NegativeAmountException {

        if (amount < 0) {
            throw new NegativeAmountException("Amount cannot be negative");
        }

        double balance=super.getBalance();

        if(balance < 500){
            throw new IllegalArgumentException("Balance is below 500. Cannot withdraw.");
        }

        double surcharge = amount * 0.01;
            amount += surcharge;
            balance -= amount;
            super.setBalance(balance);
            return balance;
        }
}

