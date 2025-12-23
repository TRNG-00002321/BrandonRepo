package com.revature.myio.serialize;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class WriteEmpObj {
    public static void main(String[] args) {
        Employee employee1 = new Employee(101, "Andrea", "Plano", "QEA");
        FileOutputStream fileOutputSteam;
        ObjectOutputStream objectOutputStream;

        try{
            fileOutputSteam = new FileOutputStream("employee.dat");
            objectOutputStream = new ObjectOutputStream(fileOutputSteam);
            objectOutputStream.writeObject(employee1);
        } catch(FileNotFoundException e){
            throw new RuntimeException(e);
        } catch (IOException e){
            throw new RuntimeException();
        }
    }
}
