package com.revature.java8;

public class Main {
    public static void main(String[] args) {

        Address address = new Address("123 Street", "Frisco", 75035);
        Person p1 = new Person("Brandon", "123-456-7890", address);
        Person p2 = new Person("Bob", "123-456-7890");


        //check nullability for both persons
        if (p1.getAddress().isPresent()){
            System.out.println("P1 has an address");
            System.out.println(address);
        } else {
            System.out.println("P1 does NOT have an address");
        }

        if (p2.getAddress().isPresent()){
            System.out.println("P2 has an address");
            System.out.println(address);
        } else {
            System.out.println("P2 does NOT have an address");
        }

    }
}
