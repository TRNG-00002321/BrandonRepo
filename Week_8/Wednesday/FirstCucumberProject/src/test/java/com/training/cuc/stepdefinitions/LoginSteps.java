package com.training.cuc.stepdefinitions;

import io.cucumber.java.After;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.And;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import io.github.bonigarcia.wdm.WebDriverManager;

import static org.junit.jupiter.api.Assertions.*;

public class LoginSteps {

    private WebDriver driver;
    private static final String BASE_URL = "https://the-internet.herokuapp.com";

    @After
    public void tearDown() {
        if (driver != null) {
            driver.quit();  // closes all browser windows and safely ends the session
        }
    }

    @Given("the user is on the login page")
    public void theUserIsOnTheLoginPage() {
        // TODO: Implement this step
        // 1. Set up WebDriverManager for Chrome
        // 2. Initialize ChromeDriver
        // 3. Navigate to login page

        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        driver.get(BASE_URL + "/login");
    }

    @When("the user enters username {string}")
    public void theUserEntersUsername(String username) {
        // TODO: Implement this step
        // Find username field and enter the provided username

        WebElement usernameField = driver.findElement(By.id("username"));
        usernameField.sendKeys(username);
    }

    @When("the user enters password {string}")
    public void theUserEntersPassword(String password) {

        WebElement passwordField = driver.findElement(By.id("password"));
        passwordField.sendKeys(password);
    }

    @When("the user clicks the login button")
    public void theUserClicksTheLoginButton() {

        WebElement loginButton = driver.findElement(By.className("radius"));
        loginButton.click();

    }

    @Then("the user should be redirected to the secure area")
    public void theUserShouldBeRedirectedToTheSecureArea() {

        assertTrue(driver.getCurrentUrl().contains("/secure"),
                "User was not redirected to secure area");
    }

    @Then("the user should see a success message containing {string}")
    public void theUserShouldSeeSuccessMessageContaining(String expectedMessage) {

        WebElement flashMessage = driver.findElement(By.xpath("//div[@id='flash']"));
        assertEquals(expectedMessage, flashMessage.getText());

    }

    @Then("the user should remain on the login page")
    public void theUserShouldRemainOnTheLoginPage() {

        assertTrue(driver.getCurrentUrl().contains("/login"),
                "User was redirected to secure area");
    }

    @Then("the user should see an error message containing {string}")
    public void theUserShouldSeeErrorMessageContaining(String expectedMessage) {

        WebElement flashErrorMessage = driver.findElement(By.xpath("//div[@id='flash']"));
        assertTrue(flashErrorMessage.getText().contains(expectedMessage));

    }
}