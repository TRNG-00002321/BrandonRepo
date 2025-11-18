package com.revature.collect;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class ListDemo {
    public static void main(String[] args) {
        //have to use ArrayList() because it is an interface
        //<String> to specify which data type you are working with
        List<String> myList = new ArrayList<String>();
        //Can add anything you want to the list
        //myList.add(1);
        myList.add("Brandon");
        myList.add("David");
        myList.add("Eric");
        //myList.add(10.3);

        //System.out.println(myList.get(1)); //specify index of item - use get

        //instantiate an iterator to do a loop
        //hasNext will check for the existence of the next item
    //        Iterator iterator = myList.iterator();
    //        while(iterator.hasNext()){
    //            System.out.println(iterator.next());
    //        }

        //can use a for loop
//        for(int i=0;i<myList.size();i++){
//            System.out.println(myList.get(i));
//        }

        //need 1 type of data, cannot use this type of loop if multiple different type of
        //data are in the list
        //enhanced for loop
//        for(int i : myList){
//
//        }

        //1) Iterate over a list from the end to the beginning.
        for(String str: myList){
            System.out.println(str);
        }

        //2) Use the other methods in the list interface (except the equals() method; will use later).
        System.out.println("\nEric in list: " + myList.contains("Eric"));
        myList.remove("Eric");
        System.out.println("Eric in list: " + myList.contains("Eric"));
        myList.removeAll(myList);
        System.out.println("Printing my list again: ");
        for(String str: myList){
            System.out.println(str);
        }

        System.out.println("Is list empty? " + myList.isEmpty());











    }

}
