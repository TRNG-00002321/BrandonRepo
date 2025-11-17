//Create a customer class
//at least 2 constructors
//at least 2 overloaded methods
//at least 1 static variable
//at least 1 final variable

public class Main {
    public static void main(String[] args) {

        Customer c1 = new Customer("Some", "Body", 25);
        Customer c2 = new Customer();

        System.out.println(c1.firstName + " " + c1.lastName + " " + c1.age);
        System.out.println(c2.firstName + " " + c2.lastName + " " + c2.age);

        c1.updateInfo("No");
        c2.updateInfo("Alex", 30);

        System.out.println(c1.firstName + " " + c1.lastName + " " + c1.age);
        System.out.println(c2.firstName + " " + c2.lastName + " " + c2.age);

        c1.sayHello();
        c2.sayCompany();

        System.out.println("Total customers created: " + Customer.customerCount);

    }
}