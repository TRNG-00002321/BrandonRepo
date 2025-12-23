package com.revature.jdbcdemo;

import java.sql.*;

public class JdbcPSDemo {
    //prepared statement
    Connection connection = null;
    Statement statement = null;
    ResultSet resultSet = null;
    PreparedStatement preparedStatement = null;

    public static void main(String[] args) {
        try {
            connection = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/mydb",
                    "root",
                    "mypassword" //find password
            );
            Stirng insertQuery = "insert into contact(name,email,phone) values(?,?,?)";
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

    }
}
