package com.revature.bank;

public class NegativeAmountException extends Exception {
    public NegativeAmountException(String message){
        super(message);
    }
}
