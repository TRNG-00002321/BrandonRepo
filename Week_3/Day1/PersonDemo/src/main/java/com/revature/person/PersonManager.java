package com.revature.person;

import org.w3c.dom.ls.LSOutput;

public class PersonManager {

    static Person person1 = new Person("Brandon", 28);
    static Person person2 = new Person("Brandon", 28);

    public static void main(String[] args) {
        //print
        System.out.println("Name : " + person1.Name + ", age : " + person1.Age);

        //make another person and see if equal
        if(person1.equals(person2)){
            System.out.println("Person 1 and Person 2 are the same");
        } else {
            System.out.println("Person 1 and Person 2 are NOT the same");
        }

    }


}
