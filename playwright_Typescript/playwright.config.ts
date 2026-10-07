import {devices, defineConfig} from "playwright/test"

export default defineConfig({

  testDir: "./tests", //this will triggers the files inside the tests folder to run
  //maximum time one test cases run for. 
  timeout: 30 * 1000,
  expect: {
    timeout: 5000
  } ,

  reporter: 'html',

  use: {
    baseURL : "https://example.com", //base url - the url u need to mention
    headless: true // headless mode 
  },

  projects:[

    // this will trigger the chromium browser, if you want to add for firefox and explorer and even mobile devices.
    {
      name : "chromium",
      use: {...devices["Desktop Chrome"]}
    }
  ]
});
