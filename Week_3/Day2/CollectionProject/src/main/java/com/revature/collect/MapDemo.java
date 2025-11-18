package com.revature.collect;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MapDemo {

    public static void main(String[] args) {
        Map<String, Double> persons = new HashMap<String, Double>();

        //no add method because map is not a part of collections
        //can use put instead
        persons.put("Brandon", 10000.00); //made entry into the map
        persons.put("David", 20000.00);
        persons.put("Eric", 30000.00);
        persons.put("Robert", 40000.00);

        System.out.println(persons.get("Brandon"));

        //making a set //always get keys like this
        Set<String> names = persons.keySet(); //or use entrySet
        for (String n:names){
            System.out.println(n + " , " + persons.get(n));
        }
    }
}
