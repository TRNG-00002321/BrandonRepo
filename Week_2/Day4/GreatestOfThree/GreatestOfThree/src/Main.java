//Write a program to search for the greatest of three numbers
// using Short-circuit Operators and print the result

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // have user input three numbers
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the first number: ");
        int input1 = scanner.nextInt();
        System.out.print("Enter the second number: ");
        int input2 = scanner.nextInt();
        System.out.print("Enter the third number: ");
        int input3 = scanner.nextInt();

        // return the greatest of the three

        int greatestNumber = 0;

        if (input1 > input2 && input1 > input3) {
            greatestNumber = input1;
        }
        else if (input2 > input1 && input2 > input3) {
            greatestNumber = input2;
        }
        else if  (input3 > input1 && input3 > input2) {
            greatestNumber = input3;
        }
        else {
            System.out.println("Invalid input");
        }

        System.out.println("The greatest number is: " + greatestNumber);


    }
}