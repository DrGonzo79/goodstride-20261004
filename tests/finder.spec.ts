import {test,expect} from "@playwright/test";
test("runner filters, saves, and builds a fundraising plan",async({page})=>{
 await page.goto("/");
 await expect(page.getByRole("heading",{name:/Missed the lottery/i})).toBeVisible();
 await page.getByLabel("Race").selectOption("Chicago Marathon");
 await expect(page.getByText("1 matching charity places")).toBeVisible();
 await page.getByRole("button",{name:"Save Clear Water Relay"}).click();
 await expect(page.getByRole("button",{name:"Remove Clear Water Relay"})).toHaveAttribute("aria-pressed","true");
 await page.getByRole("button",{name:"Build my plan"}).click();
 await expect(page.getByText("$73",{exact:true})).toBeVisible();
 await page.getByLabel("Already raised").fill("200");
 await page.getByLabel("Weeks remaining").fill("10");
 await page.getByLabel("Weeks remaining").blur();
 await expect(page.getByText("$200",{exact:true})).toBeVisible();
});
test("invalid planner input is visible",async({page})=>{
 await page.goto("/");
 await page.getByRole("button",{name:"Build my plan"}).first().click();
 await page.getByLabel("Weeks remaining").fill("0");
 await page.getByLabel("Weeks remaining").blur();
 await expect(page.locator(".error")).toContainText("between 1 and 52 weeks");
});
test("empty filters and mobile overflow are handled",async({page},testInfo)=>{
 await page.goto("/");
 await page.getByLabel("Search charities").fill("zzzz-no-match");
 await expect(page.getByText("No matches at this commitment")).toBeVisible();
 const overflow=await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
 expect(overflow).toBeLessThanOrEqual(1);
 await page.screenshot({path:testInfo.outputPath("goodstride.png"),fullPage:true});
});
