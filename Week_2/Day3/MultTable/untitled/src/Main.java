import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // Using while loops, display the multiplication table up to 10 of an input numeric

        Scanner scanner = new Scanner(System.in);
        System.out.print("Please enter your number: ");
        int num =  scanner.nextInt();

        int i = 1;
        while(i <= 10){
            System.out.println(num + " * " + i + " = " + (num * i));
            i++;
        }


        }
    }
