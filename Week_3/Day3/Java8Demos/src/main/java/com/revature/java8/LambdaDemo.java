package com.revature.java8;

public class LambdaDemo {
    public static void main(String[] args) {

//        Calculator calculator = (a,b) -> {return a + b; };
//        System.out.println(calculator.operation(3,4));

        //1. Write a lambda function that does not take a parameter and does not return a value but simply prints "Hello".
//        LambdaFuncs printHello = () -> {
//            System.out.println("Hello");
//        };
//
//        printHello.print();

        //2. Write another lambda function that takes one String parameter and returns "Hello" and the argument in uppercase.
//        LambdaFuncs printHelloName = (name) -> {
//            return "Hello " + name.toUpperCase();
//        };
//
//        System.out.println(printHelloName.helloName("Brandon"));

        //3. Write the lambda function with two String parameters: firstName, lastName. Return "Hello" with firstName and lastName concatenated with each other.
        LambdaFuncs twoString = (firstName, lastName) -> {
            return "Hello " + lastName + firstName;
        };

        System.out.println(twoString.nameFunc("Brandon", "Tsuchiya"));




















    }
}
