package com.revature.employees;

public abstract class Employee {
    private String name;
    private int id;


    public Employee() {
    }

    public Employee(String name, int id) {
        this.name = name;
        this.id = id;
    }

    @Override
    public String toString() {
        return "Employee{" +
                "name='" + name + '\'' +
                ", id=" + id +
                '}';
    }

    public abstract double calculateSalary();
}
