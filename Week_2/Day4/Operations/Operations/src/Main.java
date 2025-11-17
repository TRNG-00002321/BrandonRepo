//Write a program to add, subtract, multiply, and divide two non-zero hard-coded numbers

public class Main {
    public static void main(String[] args) {

        int num1 = 5;
        int num2 = 3;

        System.out.println("Addition: " + addNum(num1, num2));
        System.out.println("Subtraction: " + subNum(num1, num2));
        System.out.println("Multiplication: " + mulNum(num1, num2));
        System.out.println("Division: " + divNum(num1, num2));

    }

    public static int addNum(int num1, int num2) {
        return num1 + num2;
    }

    public static int subNum(int num1, int num2) {
        return num1 - num2;
    }

    public static int mulNum(int num1, int num2) {
        return num1 * num2;
    }

    public static int divNum(int num1, int num2) {
        return num1 / num2;
    }
}