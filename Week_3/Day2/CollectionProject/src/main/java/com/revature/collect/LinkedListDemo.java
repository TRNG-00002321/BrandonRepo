package com.revature.collect;

import java.util.LinkedList;

public class LinkedListDemo {

    public static void main(String[] args) {
        LinkedList<String> myList = new LinkedList<String>();


        myList.add("First");
        myList.add("Second");

        for(String s : myList){
            System.out.println(s);
        }

        if(myList.isEmpty()){
            System.out.println("List is empty");
        } else{
            System.out.println("List is NOT empty");
        }

        myList.remove("Second");
        myList.add("Third");

        for(String s : myList){
            System.out.println(s);
        }

    }



}
