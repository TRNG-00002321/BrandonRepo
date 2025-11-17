package com.revature.employees;

public class SalariedEmployee extends Employee {
    double dailyRate;
    private int daysWorked;

    SalariedEmployee(){
    }

    SalariedEmployee(String name, int id, double dailyRate, int daysWorked) {
        super(name, id);
        this.dailyRate = dailyRate;
        this.daysWorked = daysWorked;
    }

    @Override
    public String toString() {
        return "SalariedEmployee{} " + super.toString();
    }

    @Override
    public double calculateSalary() {
        return dailyRate * daysWorked;
    }

    public String benefits(){
        String[] benefits = {"Dental", "Vision"};
        return String.join(", ", benefits);
    }

}
