package com.revature.sel;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import static org.junit.jupiter.api.Assertions.assertTrue;

@DisplayName("Basic Selenium Test")
public class Test01SelBasics {

    @BeforeEach
    public void setUp(){
        // set up your WebDriverManager
        WebDriverManager.chromedriver().setup();
        //initialize youre webdriver
        driver=new ChromeDriver();
        //known as chaining
        driver.manage().window().maximize();
    }

    @AfterEach
    void tearDown(){
        //forgetting to close will leave it running
        driver.quit(); //closes all windows
        driver.close(); //closes current window
    }

    //first declare a web driver
    private WebDriver driver;

    //write first test case - setting up chrome driver
    @Test
    public void testBasic() throws InterruptedException {

        // navigate to the website
        driver.get("https://www.selenium.dev/");
        Thread.sleep(5000);

        //get the page title
        String title=driver.getTitle();
        System.out.println("Title :: "+title);

        assertTrue(title.contains("Selenium"));

    }

    @Test
    public void testDocumentationEndPoint() throws InterruptedException {

        driver.get("https://www.selenium.dev/documentation/");
        Thread.sleep(5000);

        //get the page title
        String title=driver.getTitle();
        System.out.println("Title :: "+title);

        assertTrue(title.contains("documentation"));

    }

}
