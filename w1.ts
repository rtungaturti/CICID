Here is the Playwright test code for creating a script for invalid login to Rediffmail:
```
const playwright = require('playwright');

(async () => {
  const browser = await playwright.chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('https://mail.rediff.com/cgi-bin/login.cgi');

  await page.fill('input[name="login");', 'invalidusername');
  await page.fill('input[name="passwd");', 'invalidpassword');

  await Promise.all([
    page.click('input[type="submit"]'),
    page.waitForNavigation({ waitUntil: 'networkidle0' }),
  ]);

  await page.screenshot({ path: 'invalid-login.png' });

  await browser.close();
})();
```
This code launches a new Chromium browser instance, navigates to the Rediffmail login page, fills in invalid credentials, submits the form, and takes a screenshot of the resulting error page.