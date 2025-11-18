package com.revature.collect;

import java.sql.SQLOutput;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;
import java.util.TreeSet;

public class SetDemo {
    public static void main(String[] args) {
        //LinkedHashSet will maintain the insertion order
        //Hashset will not maintain the insertion order
        //Treeset will order the order alphabetically
        Set<String> names = new TreeSet<>();

        names.add("Brandon");
        names.add("David");
        names.add("Austin");
        names.add("Eric");

        for (String n:names){
            System.out.println(n);
        }

        if(names.isEmpty()){
            System.out.println("Empty");
        } else {
            System.out.println("Not empty");
        }

        names.remove("Eric");

        System.out.println("\nRemoved Eric from list");
        for (String n:names){
            System.out.println(n);
        }


    }
}
