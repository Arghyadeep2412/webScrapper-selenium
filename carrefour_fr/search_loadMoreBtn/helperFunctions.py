from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.common.action_chains import ActionChains;
import time;

class HelperFunctionsClass():
	def __init__(self, driver):
		self.driver = driver;

	async def scroll_to_bottom_and_wait(self, waitForPageLoad):
		thisScrollSuccess = False;
		try:
			driver = self.driver;
			driver.execute_script("window.scrollTo(0, document.body.clientHeight);");
			print('scrolling!!');
			# Wait to load page
			print('waiting for {0} secs'.format(waitForPageLoad));
			time.sleep(waitForPageLoad);
		except Exception as e:
			print('got some error while scrolling to the bottom', e.Message);
		else:
			thisScrollSuccess = True;

		return thisScrollSuccess;

	async def auto_scroll(self, waitForPageLoad):

		driver = self.driver;
		lastHeight = 0;
		newHeight = 0;
		autoScrollSuccess = True;

		try:
			lastHeight = driver.execute_script("return document.documentElement.scrollTop");
		except Exception as e:
			print('got some error while fetching the scroll top height of the page', str(e));
			autoScrollSuccess = False;

		try:
			newHeight = driver.execute_script("return document.documentElement.clientHeight");
		except Exception as e:
			print('got some error while fetching the client height of the page', str(e));
			autoScrollSuccess = False;

		while((newHeight > lastHeight) and autoScrollSuccess):
			print('lastHeight', lastHeight);
			print('newHeight',newHeight);
			autoScrollSuccess = await self.scroll_to_bottom_and_wait(waitForPageLoad);
			lastHeight = newHeight;
			try:
				newHeight = driver.execute_script("return document.documentElement.clientHeight");
			except:
				print('got some error while fetching the client height of the page');

		return autoScrollSuccess;

	async def click_on_element(self, xpathsToClickon):
		clickedOnXpath = False;
		print('need to click on the given xpaths -> {0}'.format(xpathsToClickon));
		driver = self.driver
		wait = WebDriverWait(driver, 10);
		
		try:
			allElements = driver.find_elements_by_xpath(xpathsToClickon);
			
			for element in allElements:
				wait.until(EC.element_to_be_clickable((By.XPATH, xpathsToClickon)));
				if(element):
					print('got the element to click');
					driver.execute_script("arguments[0].scrollIntoView();", element);
					actionchains = ActionChains(driver);
					actionchains.move_to_element(element);
					# actionchains.click(element);
					actionchains.perform();
					driver.execute_script("arguments[0].click();", element);
					print('clicked on the button');
					time.sleep(5);

			clickedOnXpath = True;
		except Exception as e:
			print('got some error while clicking on the xpaths, {0}'.format(str(e)));

		return clickedOnXpath;

	async def enter_text_in_input_field(self, inputFieldXpath, text):
		print('need to enter the text - "{0}" in the inputField for xpath -> {1}'.format(text, inputFieldXpath));
		driver = self.driver;
		textEntered = False;
		try:
			inputFieldElm = driver.find_element_by_xpath(inputFieldXpath);
			actionchains = ActionChains(driver);
			actionchains.move_to_element(inputFieldElm).click();
			actionchains.perform();
			while(inputFieldElm.text):
				inputFieldElm.send_keys(Keys.BACK_SPACE);
			inputFieldElm.clear();
			inputFieldElm.send_keys(text);
			inputFieldElm.send_keys(Keys.RETURN);
			textEntered = True;
		except Exception as e:
			print('got some error while entering keywords in the search bar', str(e));

		return textEntered;


	async def wait_for_xpath(self, xpathToCheck, timeout = 0):
		driver = self.driver;
		wait = WebDriverWait(driver, timeout);
		element = None;
		elementFound = False;
		try:
			print('waiting for this xpath -> {0}'.format(xpathToCheck));
			element = wait.until(EC.presence_of_element_located((By.XPATH, xpathToCheck)));
		except Exception as e:
			print('got some error while waiting for the xpath -> {0}'.format(str(e)));
		else:
			print('got the element for this xpath!!');
			elementFound = True;

		return elementFound;

	async def check_if_xpath_is_present(self, xpathToCheck):
		elementPresent = False;
		driver = self.driver;
		elements = driver.find_elements_by_xpath(xpathToCheck);
		elementsCount = len(elements);
		print('got a total of {0} elements for this xpath - {1}'.format(elementsCount, xpathToCheck));
		if(elementsCount > 0):
			elementPresent = True;

		return elementPresent;

	async def get_the_number_of_elements(self, xpathToCheck):
		driver = self.driver;
		elementsCount = 0;
		elements = None;
		try:
			elements = driver.find_elements_by_xpath(xpathToCheck);
			elementsCount = len(elements);
		except Exception as e:
			print('got some error while getting the count of elements for this xpath {0}'.format(xpathToCheck), e.Message);
		else:
			print('we got some count of elements --> {0}'.format(elementsCount));
		return elementsCount;

	async def get_all_the_elements(self, xpath):
		driver = self.driver;
		elements = None;
		try:
			elements = driver.find_elements_by_xpath(xpath);
		except Exception as e:
			print('we got some Exception while fetching elements', e.Message);

		return elements;

