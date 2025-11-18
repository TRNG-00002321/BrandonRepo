package com.revature.collect;

import java.util.ArrayList;

public class ArrayListDemo {

    public static void main(String[] args) {
        ArrayList<String> myList = new ArrayList<String>();

        myList.add("Test");
        myList.add("Test2");
        myList.add("Test3");

        if(myList.contains("Test")){
            System.out.println("Exists");
        } else {
            System.out.println("Does not exist");
        }

        for(String s : myList){
            System.out.println(s);
        }

        myList.removeAll(myList);


    }


}
