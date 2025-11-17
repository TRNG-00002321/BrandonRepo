package com.revature.bank;

public class BankManager {
    public static void main(String[] args) throws NegativeAmountException {
        CheckingAccount checkingAccount = new CheckingAccount("S001", "Checking Account", 600);
        SavingAccount savingAccount = new SavingAccount("S002", "Saving Account", 600);

        // these will throw an error if your account balance is below 500
        // or if you try to enter a negative number

        System.out.println("Checking Account " + checkingAccount);

        checkingAccount.withdraw(100);
        System.out.println("Checking Account " + checkingAccount);

        System.out.println("Saving Account " + savingAccount);
        savingAccount.withdraw(100);
        System.out.println("Saving Account " + savingAccount);

        savingAccount.deposit(-100);
        System.out.println("Saving Account " + savingAccount);
    }
}
