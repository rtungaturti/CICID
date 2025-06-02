Here is the Playwright test code for invalid login to Rediffmail:
```
const playwright = require('playwright');

test('Invalid login to Rediffmail, async ({ browser }) => {
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('https://www.rediff.com');

  await page.click('a:has-text("Sign in")');
  await page.fill('input[name="login"]', 'invalidusername');
  await page.fill('input[name="passwd"]', 'invalidpassword');

  await Promise.all([
    page.click('input[name="proceed"]'),
    page.waitForNavigation({ waitUntil: 'networkidle0' }),
  ]);

  await page.screenshot({ path: 'invalid-login.png' });

  await expect(page).toHaveURL('https://www.rediff.com/?err=1');
});
```
Note: You need to have Playwright installed and configured in your project.