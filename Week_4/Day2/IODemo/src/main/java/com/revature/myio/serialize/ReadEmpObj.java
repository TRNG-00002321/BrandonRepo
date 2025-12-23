package com.revature.myio.serialize;

import java.io.*;

public class ReadEmpObj {
    public static void main(String[] args) {

        try (
                FileInputStream fileInputStream = new FileInputStream("employee.dat");
                ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream)
        ) {

            Employee emp = (Employee) objectInputStream.readObject();
            System.out.println(emp);

        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
}
