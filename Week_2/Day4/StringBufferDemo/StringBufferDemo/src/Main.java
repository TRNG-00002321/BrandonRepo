public class Main {
    public static void main(String[] args) {

        StringBuffer str1 = new StringBuffer("This is my first string.");
        System.out.println(str1);

        str1.append(" Adding Text Here.");
        System.out.println(str1);

        // removed the period
        str1.deleteCharAt(23);
        System.out.println(str1);
    }
}