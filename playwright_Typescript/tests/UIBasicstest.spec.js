import {test, expect} from 'playwright/test';

test("Browser context playwright test", async ({browser})=>{
    const context = await browser.newContext()
    const page = await context.newPage()

    await page.goto("https://rahulshettyacademy.com/loginpagePractise/");
    console.log(await page.title());

    // css  - to identify the elements  
    await page.locator("#username").fill("rahulshettyacademy") 
    await page.locator("[type='password']").fill("Learning@") //Learning@830$3mK2
    await page.locator("#signInBtn").click()
    const errorMessage = await page.locator("[style*='block']").textContent()
    console.log(errorMessage);

})

test("Playwright page test", async({page})=>{

    await page.goto("https://www.communitymedicalgroup.com/en/", { waitUntil: 'domcontentloaded' });
    await page.waitForLoadState('domcontentloaded');
    await expect(page).toHaveTitle(/Community Medical Group/i);
    console.log(await page.title());

    const aboutUsMenu = page.locator('.menu-item.menu-item-sub').filter({ hasText: /^ABOUT US/ });
    await expect(aboutUsMenu).toBeVisible({ timeout: 15000 });
    await aboutUsMenu.hover();

    const introductionLink = page.getByRole('link', { name: /Introduction/i });
    await expect(introductionLink).toBeVisible({ timeout: 15000 });
    await introductionLink.click();
    await page.waitForLoadState('domcontentloaded');

    //await expect(page).toHaveTitle("Google")
})