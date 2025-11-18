package com.revature.collect;

import java.util.ArrayList;
import java.util.List;

public class PersonCollection {

    public static void main(String[] args) {
        Person p1 = new Person("Brandon", 28, 177);
        Person p2 = new Person("Peter", 21, 101);
        Person p3 = new Person("Sunni", 25, 333);
        Person p4 = new Person("Brian", 21, 101);
        Person p5 = new Person("Steve", 26, 457);

        List<Person> personList=new ArrayList<Person>();

        personList.add(p1);
        personList.add(p2);
        personList.add(p3);
        personList.add(p4);
        personList.add(p5);

        for (Person p:personList){
            System.out.println(p); //use getter and setting to print specific item in list
        }


    }
}
