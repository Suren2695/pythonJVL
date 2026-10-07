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

    await page.goto("https://google.com");
    console.log(await page.title());
    await expect(page).toHaveTitle("Google")
})