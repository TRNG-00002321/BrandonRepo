package com.revature.employees;

public class EmployeeManager {

    public static void main(String[] args) {

        SalariedEmployee e1 = new SalariedEmployee("Brandon", 177, 100, 5);
        ContractEmployee e2 = new ContractEmployee("Eric", 166, 12.50, 40);

        System.out.println(e1);
        System.out.println("Salary: " + e1.calculateSalary());

        System.out.println(e2);
        System.out.println("Salary: " + e2.calculateSalary());

        System.out.println("Salaried employee benefits: " + e1.benefits());



    }



}
