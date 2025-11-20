package com.revature.employee;
//1. display employee using enhanced for loop
//2. display all employees using for all each loop - it is a method that iterates over a list
//3. return all the employee names in uppercase (use map method)
//4. from existing list, create a list of employees having salary more than 20,000 (use filter method)

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class streamAPI {
    public static void main(String[] args) {

        System.out.println("1.");
        //1. display employee using enhanced for loop
        List<Employee> employees = new ArrayList<>();

        employees.add(new Employee("Bob", 123, 17000));
        employees.add(new Employee("John", 929, 55000));
        employees.add(new Employee("Beth", 237, 72000));
        employees.add(new Employee("Eve", 735, 17000));
        employees.add(new Employee("Adam", 173, 21000));


        for (Employee employee : employees){
            System.out.println(employee);
        }

        System.out.println("2.");
        //2. display all employees using for all each loop - it is a method that iterates over a list
        employees.forEach(System.out::println);

        System.out.println("3.");
        //3. return all the employee names in uppercase (use map method)
        List<String> upperCaseNames = employees.stream().map(e->e.getName().toUpperCase()).toList();
        upperCaseNames.forEach(System.out::println);

        System.out.println("4. ");
        //4. from existing list, create a list of employees having salary more than 20,000 (use filter method)
        List<Employee> highSalary = employees.stream().filter(e -> e.getSalary() > 20000).toList();
        highSalary.forEach(System.out::println);

    }

}
