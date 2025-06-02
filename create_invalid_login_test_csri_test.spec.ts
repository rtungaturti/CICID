Here is the Playwright test code for creating an invalid login test script for Rediffmail:
```
const playwright = require('playwright');

(async () => {
  const browser = await playwright.chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('https://mail.rediff.com/cgi-bin/login.cgi');

  await page.fill('input[name="login"]', 'invalidusername');
  await page.fill('input[name="passwd"]', 'invalidpassword');

  await Promise.all([
    page.click('input[type="submit"]'),
    page.waitForNavigation({ waitUntil: 'networkidle2' }),
  ]);

  await page.screenshot({ path: 'invalid-login.png' });

  await browser.close();
})();
```
Note: This code assumes that the login form fields have names `login` and `passwd`, and the submit button is an `input` element with no specific ID or class. You may need to adjust the selectors based on the actual HTML structure of the Rediffmail login page.