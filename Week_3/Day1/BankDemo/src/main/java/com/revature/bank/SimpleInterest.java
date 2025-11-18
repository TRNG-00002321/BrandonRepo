package com.revature.bank;

public interface SimpleInterest {
    public default double calculateInterst(double balance){
        //5% interest
        double interest = balance * 0.05;
        balance = balance + interest;
        return balance;
    }
}
