package com.revature.myio;

import java.io.*;

public class LineStreamDemo {

    public static void main(String[] args) throws IOException {
        BufferedReader inputStream = null;
        BufferedWriter outputStream = null;

        try {
            inputStream = new BufferedReader(new FileReader("text.txt"));
            outputStream = new BufferedWriter(new FileWriter("charoutput.txt"));

            String l;
            while ((l = inputStream.readLine()) != null) {
                outputStream.write(l);
                //outputStream.newLine();
            }

        } finally {
            if (inputStream != null) {
                inputStream.close();
            }
            if (outputStream != null) {
                outputStream.close();
            }
        }
    }
}
