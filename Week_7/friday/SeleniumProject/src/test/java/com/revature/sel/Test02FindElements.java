package com.revature.sel;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertTrue;

@DisplayName("Finding Elements")
public class Test02FindElements {

    private final String BASE_URL="https://the-internet.herokuapp.com/";

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
        //driver.close(); //closes current window
    }

    private WebDriver driver;

    @DisplayName("Test By Id")
    @Test
    public void testById() throws InterruptedException {
        driver.get(BASE_URL+"/login");
        WebElement userName=driver.findElement(By.id("username"));
        WebElement pass=driver.findElement(By.id("password"));

        Thread.sleep(5000);

        assertTrue(userName.isDisplayed());
        assertTrue(pass.isDisplayed());
    }

    @DisplayName("Test By Name")
    @Test
    public void testByName() throws InterruptedException {

        driver.get(BASE_URL+"/login");
        WebElement userName=driver.findElement(By.name("username"));
        WebElement pass=driver.findElement(By.name("password"));

        Thread.sleep(5000);

        assertTrue(userName.isDisplayed());
        assertTrue(pass.isDisplayed());
    }


    @DisplayName("Test By Tag Name")
    @Test
    public void testByTagName() throws InterruptedException {

        driver.get(BASE_URL+"/login");
        List<WebElement> userName=driver.findElements(By.tagName("i"));
        //WebElement pass=driver.findElements(By.tagName("password"));

        Thread.sleep(5000);

        //assert
        //assertTrue(userName.isDisplayed());
        //assertTrue(pass.isDisplayed());
    }


    @DisplayName("Test Find the Login Button")
    @Test
    public void testLoginButton() throws InterruptedException {

        driver.get(BASE_URL+"/login");

        //get the element
        WebElement loginButton=driver.findElement(By.className("radius"));

        //load the elements text
        String loginButtonText = loginButton.getText();
        Thread.sleep(1000);

        //assert
        assertTrue(loginButtonText.contains("Login"));
    }










    @DisplayName("Test Find the Absolute Path")
    @Test
    public void testAbsolutePath() throws InterruptedException {

        driver.get(BASE_URL);

        //get the element
        WebElement absolute = driver.findElement(By.xpath("/html[1]/body[1]/div[2]/div[1]/h2[1]"));


        //assert
        //assertTrue(loginButtonText.contains("Login"));
    }










    @Test
    @DisplayName("Complete login form interaction")
    void completeForm_loginFlow() throws InterruptedException {

        driver.get(BASE_URL + "/login");
        // Find elements

        WebElement username = driver.findElement(By.id("username"));
        WebElement password = driver.findElement(By.id("password"));
        WebElement button = driver.findElement(By.className("radius"));

        // Verify elements are displayed and enabled
        assertTrue(username.isDisplayed());
        assertTrue(password.isDisplayed());
        assertTrue(button.isDisplayed());

        // Clear and enter credentials
        //username=tomsmith
        //password=SuperSecretPassword!

                // Verify input values
                username.clear();
                username.sendKeys("tomsmith");

                password.clear();
                password.sendKeys("SuperSecretPassword!");

                // Click login
                button.click();

                // Verify success (check for success message or URL)
                WebElement flash = driver.findElement(By.id("flash"));
                String flashText = flash.getText();


        assertTrue(flashText.contains("You logged into a secure area!") ||
                        driver.getCurrentUrl().contains("secure"));
    }
}
