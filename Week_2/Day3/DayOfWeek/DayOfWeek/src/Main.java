//import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        //Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number in regards to the corresponding day: ");
        int day = Integer.parseInt(args[0]);//scanner.nextInt();
        //receive input (1-7)
        //receive command line argument

        String dayName = switch(day){
            case 1 -> "Sunday";
            case 2 -> "Monday";
            case 3 -> "Tuesday";
            case 4 -> "Wednesday";
            case 5 -> "Thursday";
            case 6 -> "Friday";
            case 7 -> "Saturday";
            default -> "Invalid day";
        };

        System.out.println(dayName);
        System.out.print(String.format("The day is: %s", dayName));




        }
    }
