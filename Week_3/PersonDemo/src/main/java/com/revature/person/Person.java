package com.revature.person;

import java.util.Objects;

public class Person {
    String Name = "";
    int Age = 0;


    public Person() {

    }

    public Person(String name, int age) {
        Name = name;
        Age = age;

    }

    @Override
    public String toString() {
        return "Person{" +
                "Name='" + Name + '\'' +
                ", Age=" + Age +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return Age == person.Age && Objects.equals(Name, person.Name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(Name, Age);
    }
}
