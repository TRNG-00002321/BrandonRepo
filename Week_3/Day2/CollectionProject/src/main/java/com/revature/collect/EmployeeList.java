package com.revature.collect;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class EmployeeList{
    public static void main(String[] args) {
        Employee e5 = new Employee(835, "Tsuchiya", 90000.00);
        Employee e1 = new Employee(931, "Andrew", 40000.00 );
        Employee e3 = new Employee(333, "Jinx", 70000.00);
        Employee e4 = new Employee(734, "Holland", 80000.00);
        Employee e2 = new Employee(832, "Bob", 50000.00);

        List<Employee> employees = new ArrayList<Employee>();
        employees.add(e5);
        employees.add(e1);
        employees.add(e3);
        employees.add(e4);
        employees.add(e2);

        //display list
        System.out.println(employees);

        //sorted by name
        employees.sort(Comparator.comparing(Employee::getName));
        System.out.println(employees);

        //sorted by id
        employees.sort(Comparator.comparing(Employee::getId));
        System.out.println(employees);

        //sorted by salary
        employees.sort(Comparator.comparing(Employee::getSalary));
        System.out.println(employees);
    }
}