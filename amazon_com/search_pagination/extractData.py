from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
import time;
import os.path;
from allConfigs import scrapperConfig, pageConfig, attributeConfig, dataConfig;
from helperFunctions import HelperFunctionsClass;

class ExtractDataClass():
	def __init__(self, driver, keyword):
		self.driver = driver;
		self.keyword = keyword;
		self.dataCountAlreadyPresent = 0;
		self.helperFunctionsObj = HelperFunctionsClass(self.driver);
		self.thisInputData = [];

	async def check_and_enter_keywords_in_search_bar(self):
		if(pageConfig['searchBarXpath']):
			searchBarXpath = pageConfig['searchBarXpath'];
			print('need to check if the search bar is present', searchBarXpath);
			searchBarLoaded = await self.helperFunctionsObj.wait_for_xpath(searchBarXpath, pageConfig['elementTimeout']);
			print('searchBarLoaded', searchBarLoaded);
			if(searchBarLoaded):
				print('clear the search bar first');
				clearSearchBarBtnXpath = pageConfig['clearSearchBarBtnXpath'];
				print('need to click on clearSearchBarBtnXpath', clearSearchBarBtnXpath);
				if(clearSearchBarBtnXpath):
					clearBtnPresent = await self.helperFunctionsObj.check_if_xpath_is_present(clearSearchBarBtnXpath);
					if(clearBtnPresent):
						await self.helperFunctionsObj.click_on_element(clearSearchBarBtnXpath);
						# time.sleep(15);
						print('cleared the search bar');
					else:
						print('clear btn is not detected, please check the clearSearchBarBtnXpath');
				else:
					print('we do not have a search bar clear btn xpath');

				print('now need to enter the keyword in the search bar field');
				keywordsEntered = await self.helperFunctionsObj.enter_text_in_input_field(searchBarXpath, self.keyword);
				print('keywordsEntered',keywordsEntered);
				if(not(keywordsEntered)):
					print('keywords are still not entered - returning from here!');
					return False;
			else:
				print('search bar is not loaded yet or check with the xpath for search bar');
				print('returning as of now');
				return False;

		else:
			print('searchBarXpath is not present - please provide one');
			return False;
		return True;

	async def get_data_from_this_page(self, attributeConfig):
		thisPageData = [];
		rank = len(self.thisInputData);
		rowXpath = attributeConfig['xpathOrDelimiter'].join(attributeConfig['rowXpath']);
		allProdElments = await self.helperFunctionsObj.get_all_the_elements(rowXpath);
		if(not(allProdElments is None)):
			print('we have got the results');
			elmInd = -1;
			for elm in allProdElments:
				elmInd = elmInd + 1;
				rank = rank + 1;
				thisProdData = {
									'rank': rank,
									'_input': self.keyword
								};
				
				for attr in attributeConfig['attributes']:
					attrXpath = attributeConfig['xpathOrDelimiter'].join(attributeConfig['attributes'][attr]['xpath']);
					thisElm = None;
					param = attributeConfig['attributes'][attr]['param'];
					prefix = '';
					if('prefix' in attributeConfig['attributes'][attr]):
						prefix = attributeConfig['attributes'][attr]['prefix'];
					attrValue = self.helperFunctionsObj.get_value_from_elm_for_xpath(attrXpath, elm, param, prefix);
					thisProdData[attr] = attrValue;
				thisPageData.append(thisProdData);

		return thisPageData;

	async def get_data_for_input(self):
		return self.thisInputData[:(dataConfig['maxResults']+1)];

	async def execute(self):

		dataExtractedSuccessfully = True;

		keywordsEnteredSuccess = await self.check_and_enter_keywords_in_search_bar();

		print('keywordsEnteredSuccess', keywordsEnteredSuccess);

		if(not(keywordsEnteredSuccess)):
			dataExtractedSuccessfully = False;
			return dataExtractedSuccessfully;

		print('need to wait for the page to load');

		loadedXpath = pageConfig['xpathOrDelimiter'].join(pageConfig['loadedXpath']);
		pageHasResults = False;
		if(loadedXpath):
			pageHasResults = await self.helperFunctionsObj.wait_for_xpath(loadedXpath, pageConfig['navigationTimeout']);
		print('pageHasResults', pageHasResults);

		if(not(pageHasResults)):
			dataExtractedSuccessfully = False;
			return dataExtractedSuccessfully;

		print('we need to scroll now');

		autoScrollSuccess = await self.helperFunctionsObj.auto_scroll(pageConfig['lazyLoadingSpecs']['scrollPauseTime']);

		print('autoScrollSuccess', autoScrollSuccess);

		print('need to get the data from this page');

		if(('hasPagination' in pageConfig) and pageConfig['hasPagination']):
			print('we might have pagination here!!');
			dataCountCollected = len(self.thisInputData);
			nextPageClickXpath = pageConfig['pagination']['clickToNextPageXpath'];
			clickForNextPageSuccess = True;
			while((dataCountCollected < dataConfig['maxResults']) and clickForNextPageSuccess and pageHasResults):
				self.thisInputData = self.thisInputData + await self.get_data_from_this_page(attributeConfig);
				dataCountCollected = len(self.thisInputData);
				if(nextPageClickXpath):
					print('need to click on the next page', nextPageClickXpath);
					clickForNextPageSuccess = await self.helperFunctionsObj.click_on_element(nextPageClickXpath);
					print('clickForNextPageSuccess',clickForNextPageSuccess);
					if(clickForNextPageSuccess):
						print('need to wait for loaded xpath to wait for the page to load')
						if(loadedXpath):
							pageHasResults = await self.helperFunctionsObj.wait_for_xpath(loadedXpath, pageConfig['navigationTimeout']);
						else:
							print('we do not have any loaded xpath to wait for');
					else:
						print('assuming that we have reached the last page!!');
				else:
					print('we do not have next page xpath to click on');
					clickForNextPageSuccess = False;
		else:
			print('it does not have pagination');

		return dataExtractedSuccessfully;


		
