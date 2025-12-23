package com.revature.myio;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

public class FileStreamsDemo01 {
    static FileInputStream fileInputStream;
    static FileOutputStream fileOutputStream;

    public static void main(String[] args) {
        try {
            fileInputStream = new FileInputStream("example.txt");
            fileOutputStream = new FileOutputStream("output1.txt"); //auto create file if exists. overwrite if exists
            int c;

            c = fileInputStream.read();
            while((c=fileInputStream.read())!=-1){
                //System.out.write(c);//-1 indicates end
                fileOutputStream.write(c);
            }

            fileInputStream.close(); // good practice
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
