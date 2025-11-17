//Write a program -declare two variables a and b and initialize
//them to true and false respectively. Get the output of the following computations:
//!a
//a | b
//(!a & b) | (a & !b)

public class Main {
    public static void main(String[] args) {

        boolean a = true;
        boolean b = false;

        System.out.println(!a);
        System.out.println(a | b);
        System.out.println((!a & b) | (a & !b));

    }
}