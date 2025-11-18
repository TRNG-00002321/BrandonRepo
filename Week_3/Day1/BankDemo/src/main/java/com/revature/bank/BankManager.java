package com.revature.bank;
import java.util.Scanner;

public class BankManager {
    public static void main(String[] args) throws NegativeAmountException {

        // if you want to throw error, make either account 500 dollars, and try to withdraw
        // if you enter a negative number anywhere, it will throw an error as well.

        CheckingAccount checkingAccount = new CheckingAccount("S001", "Checking Account", 600);
        SavingAccount savingAccount = new SavingAccount("S002", "Saving Account", 600);

        System.out.println("Options:");
        System.out.println("1. Checking Account");
        System.out.println("2. Saving Account");
        System.out.println("Please enter your selection");

        Scanner sc = new Scanner(System.in);
        int selection = sc.nextInt();  // read user input once

        if (selection == 1) {
            System.out.println("Checking Account");
            System.out.println("Current Balance: " + checkingAccount.getBalance());
            System.out.println("Options:");
            System.out.println("1. Deposit");
            System.out.println("2. Withdraw");

            int action = sc.nextInt();  // read the next user input

            if (action == 1) {
                System.out.println("Enter your deposit amount");
                double amount = sc.nextDouble();
                checkingAccount.deposit(amount);
                System.out.println("New Balance: " + checkingAccount.getBalance());
            } else if (action == 2) {
                System.out.println("Enter your withdraw amount");
                double amount = sc.nextDouble();
                checkingAccount.withdraw(amount);
                System.out.println("New Balance: " + checkingAccount.getBalance());
            } else {
                System.out.println("Invalid selection");
            }
        }
        else if (selection == 2) {
            System.out.println("Saving Account");
            System.out.println("Current Balance: " + savingAccount.getBalance());
            System.out.println("Options:");
            System.out.println("1. Deposit");
            System.out.println("2. Withdraw");

            int action = sc.nextInt();

            if (action == 1) {
                System.out.println("Enter your deposit amount");
                double amount = sc.nextDouble();
                savingAccount.deposit(amount);
                System.out.println("New Balance: " + savingAccount.getBalance());
            } else if (action == 2) {
                System.out.println("Enter your withdraw amount");
                double amount = sc.nextDouble();
                savingAccount.withdraw(amount);
                System.out.println("New Balance: " + savingAccount.getBalance());
            } else {
                System.out.println("Invalid selection");
            }
        }
        else {
            System.out.println("Invalid selection");
        }



//              tests
//        System.out.println("Checking Account " + checkingAccount);
//
//        checkingAccount.withdraw(100);
//        System.out.println("Checking Account " + checkingAccount);
//
//        System.out.println("Saving Account " + savingAccount);
//        savingAccount.withdraw(100);
//        System.out.println("Saving Account " + savingAccount);
//
//        savingAccount.deposit(-100);
//        System.out.println("Saving Account " + savingAccount);


    }
}
