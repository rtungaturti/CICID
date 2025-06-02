Here is the Playwright test code for creating an invalid login test using https://practicetestautomation.com/practice-test-login/:
```
const playwright = require('playwright');

(async () => {
  const browser = await playwright.chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('https://practicetestautomation.com/practice-test-login/');

  await page.fill('input#username', 'invalidusername');
  await page.fill('input#password', 'invalidpassword');

  await Promise.all([
    page.click('input#submit'),
  ]);

  await page.waitForSelector('text=Your username is invalid!');

  await browser.close();
})();
```
Note: This code assumes that the invalid username and password will result in an error message "Your username is invalid!" on the page. You may need to adjust the `waitForSelector` line to match the actual error message displayed on the page.