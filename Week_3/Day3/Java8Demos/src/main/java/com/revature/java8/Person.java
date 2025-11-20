package com.revature.java8;

// Create a class named "Address" having the following fields: street, city, zip code.
// Create constructors, getters, setters, and toString() methods. Create another class,
// Person, having name, phone, and address as attributes. Create a main class wherein you create
// two Person objects, one with an address and another without an
// address. Check the nullability of address for each Person object.

import java.util.Optional;

public class Person {
    private String name;
    private String phone;
    private Address address;

    public Person(String name, String phone) {
        this.name = name;
        this.phone = phone;
    }

    public Person(String name, String phone, Address address) {
        this.name = name;
        this.phone = phone;
        this.address = address;
    }

    public Optional<Address> getAddress() {
        return Optional.ofNullable(address);
    }


}
