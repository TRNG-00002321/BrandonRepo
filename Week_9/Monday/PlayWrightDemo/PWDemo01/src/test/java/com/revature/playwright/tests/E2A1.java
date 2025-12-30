package com.revature.playwright.tests;

import com.microsoft.playwright.*;
import org.junit.jupiter.api.*;

import java.util.regex.Pattern;

import static com.microsoft.playwright.assertions.PlaywrightAssertions.assertThat;

public class E2A1 {

    //Shared across tests
    static Playwright playwright;
    static Browser browser;

    //Unique per test for isolation
    BrowserContext context;
    Page page;

    @BeforeAll
    static void launchBrowser() {
        playwright = Playwright.create();
        browser = playwright.chromium().launch(new BrowserType.LaunchOptions()
                .setHeadless(false)  // Set to true for CI
                .setSlowMo(100));    // Slow down for visibility (remove in production)
    }

    @AfterAll
    static void closeBrowser() {
        browser.close();
        playwright.close();
    }

    @BeforeEach
    void createContextAndPage() {
        context = browser.newContext();
        page = context.newPage();
    }

    @AfterEach
    void closeContext() {
        context.close();
    }

    @Test
    void loginTest(){

//    Navigate to login page
//    Enter valid credentials
//    Click login button
//    Wait for navigation to secure area
//    Verify welcome message displayed
//    Click logout button
//    Verify returned to login page
//    Verify logout message displayed

        //navigate to login page
        page.navigate("https://the-internet.herokuapp.com/login");

        //enter valid credentials
        page.fill("#username", "tomsmith");
        page.fill("#password", "SuperSecretPassword!");

        //click login
        page.click("//button[@type='submit']");

        //wait for navigation to secure area
        //verify welcome message displayed
        Locator heading = page.locator("//h4[@class='subheader']");
        assertThat(heading).hasText("Welcome to the Secure Area. When you are done click logout below.");

        //click logout button
        page.click("//a[@class='button secondary radius']");

        //verify returned to login page
        Locator flash = page.locator("#flash");
        assertThat(flash).hasText(Pattern.compile("You logged out of the secure area!"));
        //pattern.compile is like contains specific text

    }



}
