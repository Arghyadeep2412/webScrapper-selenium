import time;
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
from allConfigs import scrapperConfig, pageConfig, attributeConfig;
from helperFunctions import HelperFunctionsClass;

class LoadAndCheckPagesClass:
    def __init__(self, driver):
        self.driver = driver;
        self.atLeastWaitInSecs = pageConfig['navigationTimeout'];
        self.helperFunctionsObj = HelperFunctionsClass(self.driver);


    async def load_the_home_page(self, driver, homePageUrl):
        driver.get(homePageUrl);

    async def execute(self):
        # first need to load the home page
        homePageUrl = pageConfig['homePageUrl'];
        if(homePageUrl):
            homePageUrl = homePageUrl.strip();

        print('homePageUrl', homePageUrl);
        homePageLoadedSuccess = False;

        if(homePageUrl):
            await self.load_the_home_page(self.driver, homePageUrl);
            homePageXpath = pageConfig['xpathOrDelimiter'].join(pageConfig['homePageLoadedXpath']);
            homePageLoadedSuccess = await self.helperFunctionsObj.wait_for_xpath(homePageXpath, pageConfig['navigationTimeout']);

        print('homePageLoadedSuccess', homePageLoadedSuccess);

        btnCloseXpaths = pageConfig['xpathOrDelimiter'].join(pageConfig['allCloseBtnXpath']);
        print('need to check and close all these btns -> {0}'.format(btnCloseXpaths));

        for xpath in pageConfig['allCloseBtnXpath']:
            btnsPresent = await self.helperFunctionsObj.wait_for_xpath(xpath, pageConfig['elementTimeout']);
            print('btnsPresent', btnsPresent);
            if(btnsPresent):
                await self.helperFunctionsObj.click_on_element(xpath);

        return homePageLoadedSuccess;