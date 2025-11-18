package com.revature.collect;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class SortDemo {

    public static void main(String[] args) {
        List<String> names = new ArrayList<String>();

        names.add("John");
        names.add("Xayne");
        names.add("Brandon");
        names.add("David");
        names.add("Eric");

        System.out.println(names);

        Collections.sort(names);
        System.out.println(names);

        Collections.sort(names, Collections.reverseOrder());
        System.out.println(names);
    }
}
