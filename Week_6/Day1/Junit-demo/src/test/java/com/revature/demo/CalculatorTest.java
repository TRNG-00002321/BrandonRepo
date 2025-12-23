package com.revature.demo;

import org.junit.jupiter.api.*;

public class CalculatorTest {

    @Test //used to execute the test
    void testAdd(){
        //Arrange
        Calculator calculator = new Calculator();
        int n1 = 10;
        int n2 = 12;
        int expectedResult = 22;
        int actualResult;

        //Act
        actualResult = calculator.add(n1, n2);
        System.out.println("Test Add Positive");

        //Assert
        Assertions.assertEquals(expectedResult, actualResult);
    }

    @Test
    void testSub(){
        Calculator calculator = new Calculator();
        int n1 = 12;
        int n2 = 10;
        int expectedResult = 2;
        int actualResult;

        actualResult = calculator.sub(n1, n2);
        //System.out.println("Test Sub Positive");

        Assertions.assertEquals(expectedResult, actualResult);
    }

    @Test
    void testDiv(){
        Calculator calculator = new Calculator();

        int n1 = 8;
        int n2 = 2;
        int expectedResult = 4;
        int actualResult;

        actualResult = calculator.div(n1, n2);

        Assertions.assertEquals(expectedResult, actualResult);
    }

    @Test
    void testDivByZero() {
        Calculator calculator = new Calculator();

        Assertions.assertThrows(ArithmeticException.class, () -> {
            calculator.div(10, 0);
        });
    }


    @Test
    void testMult(){
        Calculator calculator = new Calculator();

        int n1 = 2;
        int n2 = 2;
        int expectedResult = 4;
        int actualResult;

        actualResult = calculator.mult(n1, n2);

        Assertions.assertEquals(expectedResult, actualResult);
    }


    @Test //used to execute the test
    //@Disabled
    void testAddNegative(){
        //Arrange
        Calculator calculator = new Calculator();
        int n1 = -10;
        int n2 = 12;
        int expectedResult = 22;
        int actualResult;

        //Act
        actualResult = calculator.add(n1, n2);
        //System.out.println("Test Add Negative");

        //Assert
        Assertions.assertEquals(expectedResult, actualResult);


    }

    @BeforeEach // executed before each of the test method
    public void setUp(){
        //System.out.println("This is the Setup method ... BeforeEach");
    }

    @AfterEach
    public void tearDown(){
        //System.out.println("This is the Tear Down Method ... AfterEach");
    }

    @BeforeAll //has to be static method
    public static void setUpClass(){
        //System.out.println("Before All methods is called");
    }

    @AfterAll
    public static void tearDownClass(){
        //System.out.println("After all methods are called");
    }
}
