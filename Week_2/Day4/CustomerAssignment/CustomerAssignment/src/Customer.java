public class Customer{
    String firstName;
    String lastName;
    int age;

    static int customerCount = 0;

    // final string
    final String company = "Cognizant";

    // constructor 1
    public Customer(String firstName, String lastName, int age) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        customerCount++;
    }

    // constructor 2
    public Customer(){
        this.firstName = "Brandon";
        this.lastName = "Tsuchiya";
        this.age = 28;
        customerCount++;
    }

    // overload method 1
    public void updateInfo(String firstName) {
        this.firstName = firstName;
    }

    // overload method 2
    public void updateInfo(String firstName, int age) {
        this.firstName = firstName;
        this.age = age;
    }

    // static variable
    public static void sayHello(){
        System.out.println("hello");
    }

    public void sayCompany(){
        System.out.println(company);
    }

}
