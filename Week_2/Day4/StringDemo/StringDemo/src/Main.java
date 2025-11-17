import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        String myString = " Hello World! ";

        System.out.println(myString);

        String newString = myString.trim();
        System.out.println(newString);

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name_String =  scanner.nextLine();

        String helloString = "Hello ";
        System.out.println(helloString.concat(name_String));

        // see if string = other string
        String myOtherString = "Hello World!";
        System.out.println(myOtherString.equals(newString));
        System.out.println(myOtherString + " = " + newString);

        // lower case hello world vs upper case hello world
        String lowerHelloWorld = "hello world";
        String upperHelloWorld = "HELLO WORLD";
        System.out.println(lowerHelloWorld.equalsIgnoreCase(upperHelloWorld));
        System.out.println(lowerHelloWorld + " = " +  upperHelloWorld + " with equalsIgnoreCase()");

        // swap the casing
        System.out.println(lowerHelloWorld.toUpperCase());
        System.out.println(upperHelloWorld.toLowerCase());

        // replace
        System.out.println(lowerHelloWorld.replace("hello", "goodbye"));
    }
}