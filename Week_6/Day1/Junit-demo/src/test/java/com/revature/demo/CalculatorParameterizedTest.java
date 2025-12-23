//package com.revature.demo;
//
//import org.junit.jupiter.api.BeforeAll;
//import org.junit.jupiter.api.BeforeEach;
//import org.junit.jupiter.params.ParameterizedTest;
//import org.junit.jupiter.params.provider.Arguments;
//import org.junit.jupiter.params.provider.CsvSource;
//import org.junit.jupiter.params.provider.MethodSource;
//
//import java.util.stream.Stream;
//
//import static org.junit.jupiter.api.Assertions.assertEquals;
//
//public class CalculatorParameterizedTest {
//    Calculator calculator = null;
//
//    @BeforeEach //every time a test method is called
//    public void setUp(){
//        calculator = new Calculator();
//    }
//
//    //we will supply this with data
//    @ParameterizedTest(name="{0} + {1} = {2}") //the arrange is up here
//    @CsvSource({
//            "1, 2, 3",
//            "2, 2, 4",
//            "4, 4, 8",
//            "3, 1, 5",
//            "5, 5, 10"
//    }) //the source of the parameters
//    public void testAdd(int a, int b, int expectedResult){
//        assertEquals(expectedResult,calculator.add(a,b));
//
//    }
//
////    //we will supply this with data
////    @ParameterizedTest(name="{0} + {1} = {2}") //the arrange is up here
////    @CsvSource({
////            "1, 2, 3",
////            "2, 2, 4",
////            "4, 4, 8",
////            "3, 1, 5",
////            "5, 5, 10"
////    }) //the source of the parameters
////    public void testAddAgain(int a, int b, int expectedResult){
////        assertEquals(expectedResult,calculator.add(a,b));
////
////    }
//
//
//
//
//
////    @CsvSource
////    @MethodSource //learn these
//
//    static Stream<Arguments> testDataMethod(){
//        return Stream.of(
//                Arguments.of(1,2,3),
//                Arguments.of(-2, 4, 2),
//                Arguments.of(3,3,6),
//                Arguments.of(1,2,10),
//                Arguments.of(4,4,8)
//        );
//    }
//
//
//
//}
