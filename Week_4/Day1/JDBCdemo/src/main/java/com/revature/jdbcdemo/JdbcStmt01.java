package com.revature.jdbcdemo;

import java.sql.*;

public class JdbcStmt01 {

    public static void main(String[] args) {
        Connection connection = null;
        Statement statement = null;
        ResultSet resultSet = null;

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            connection = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/mydb",
                    "root",
                    "mypassword" //find password
            );

            //step 3 create the statement
            statement = connection.createStatement();
            String selectQuery = "select * from contact";

            //step 4 execute the query and collect the result in result set
            resultSet = selectQuery.executeUpdate(selectQuery);

            //step 5 process the resultset
            while(resultSet.next()){ //i dont have any tables
                System.out.println(resultSet.getInt("id") + " , " + resultSet.getString("name"));
            }


        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }

        System.out.println("Connection completed");
    }
}
