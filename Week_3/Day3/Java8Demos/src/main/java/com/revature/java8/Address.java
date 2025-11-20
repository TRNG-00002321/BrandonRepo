package com.revature.java8;

// Create a class named "Address" having the following fields: street, city, zip code.
// Create constructors, getters, setters, and toString() methods. Create another class,
// Person, having name, phone, and address as attributes. Create a main class wherein you create
// two Person objects, one with an address and another without an
// address. Check the nullability of address for each Person object.

public class Address {

    private String street;
    private String city;
    private int zip;

    public Address() {
    }

    public Address(String street, String city, int zip) {
        this.street = street;
        this.city = city;
        this.zip = zip;
    }

    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
    }

    @Override
    public String toString() {
        return "Address{" +
                "street='" + street + '\'' +
                ", city='" + city + '\'' +
                ", zip=" + zip +
                '}';
    }
}
