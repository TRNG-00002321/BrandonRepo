package com.revature.employees;

public class ContractEmployee extends Employee {
    public double hourlyRate;
    private int hoursWorked;


    ContractEmployee() {
    }

    ContractEmployee(String name, int id, double hourlyRate, int hoursWorked) {
        super(name, id);
        this.hourlyRate = hourlyRate;
        this.hoursWorked = hoursWorked;
    }

    @Override
    public String toString() {
        return "ContractEmployee{} " + super.toString();
    }

    @Override
    public double calculateSalary() {
        //in here, I need to receive input and calculate
        //ask how many days worked. calc based on this
        return hourlyRate * hoursWorked;
    }
}
