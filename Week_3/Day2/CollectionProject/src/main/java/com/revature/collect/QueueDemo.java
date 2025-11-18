package com.revature.collect;

import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class QueueDemo {
    public static void main(String[] args) {

        Queue<Integer> q=new PriorityQueue<Integer>();

        q.add(1);
        q.add(2);
        q.add(3);

        System.out.println(q);

        for (Integer i:q){
            System.out.println(i);
        }

        if(q.contains(2)){
            System.out.println("true");
        } else {
            System.out.println("false");
        }

        System.out.println(q.poll());

        System.out.println("After poll: ");
        for(Integer i:q){
            System.out.println(i);
        }

    }
}
