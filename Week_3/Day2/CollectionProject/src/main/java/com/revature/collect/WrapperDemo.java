package com.revature.collect;

import java.util.ArrayList;
import java.util.List;

public class WrapperDemo {
    public static void main(String[] args) {

        int num = 2;
        Integer wrappedNum = num;

        System.out.println(wrappedNum);

        List<Integer> myList = new ArrayList<>();
        myList.add(12);
        myList.add(wrappedNum);



        for (Integer i: myList){
            System.out.println(i);
        }


    }



}
