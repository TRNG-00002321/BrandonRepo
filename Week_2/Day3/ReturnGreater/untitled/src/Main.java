import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        //receive 3 inputs from user
        System.out.println("Enter your first value: ");
        int value1 = scanner.nextInt();
        System.out.println("Enter your second value: ");
        int value2 = scanner.nextInt();
        System.out.println("Enter your third value: ");
        int value3 = scanner.nextInt();


        int greatest = 0;

        if (value1 > value2 && value1 > value3) {
            greatest = value1;
        }
        else if(value2 > value1 && value2 > value3)
        {
            greatest = value2;
        } else if (value3 > value1 && value3 > value2)
        {
            greatest = value3;
        }


        System.out.println("The greatest number is " + greatest);



        }
    }
