Here is the Selenium test code in Java:
```
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class RediffMailTest {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");
        WebDriver driver = new ChromeDriver();

        driver.get("https://www.rediff.com");
        driver.findElement(By.linkText("Sign in")).click();
        driver.findElement(By.id("login")).sendKeys("your_username");
        driver.findElement(By.id("password")).sendKeys("your_password");
        driver.findElement(By.name("proceed")).click();

        WebElement mailCountElement = driver.findElement(By.xpath("//span[@class='nw']"));
        String mailCountText = mailCountElement.getText();
        System.out.println("New Mails Count: " + mailCountText);

        driver.quit();
    }
}
```
Note: Replace `/path/to/chromedriver` with the actual path to the ChromeDriver executable on your system. Also, replace `your_username` and `your_password` with your actual Rediffmail login credentials.