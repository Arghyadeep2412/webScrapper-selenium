from selenium import webdriver;
from selenium.webdriver.common.keys import Keys; 
import time;
import os.path;
import csv;
import asyncio;
from getInputs import GetInputsClass;
from allConfigs import scrapperConfig, pageConfig, attributeConfig;
from loadAndCheckThePages import LoadAndCheckPagesClass;
from extractData import ExtractDataClass;


class ScrapperClass:
	def __init__(self):
		self.getInputsObj = GetInputsClass(scrapperConfig['inputFilePath']);
		self.loadAndCheckPagesObj = None;
		self.inputKeywords = [];
		self.driver = None;
		self.extractDataObj = None;
		self.allInputsData = [];

	async def get_the_inputs(self, getInputsObj):
		gotInputsSuccessfully = await getInputsObj.execute();
		return gotInputsSuccessfully;

	async def check_if_path_has_file(self, pathToCheck):
		if(os.path.isfile(pathToCheck)):
			return True;
		return False;

	async def initiate_driver(self, driverPath):
		pathHasDriver = await self.check_if_path_has_file(driverPath);
		if(pathHasDriver):
			self.driver = webdriver.Chrome(driverPath);
			self.driver.maximize_window();
		else:
			print('we do not have file at the given path');
		return pathHasDriver;

	async def execute_and_return_success(self):
		allSuccess = True;

		print('first need to get the data from the given input xlsx file');
		gotInputsSuccessfully = await self.get_the_inputs(self.getInputsObj);
		print('gotInputsSuccessfully', gotInputsSuccessfully);
		if(gotInputsSuccessfully):
			self.inputKeywords = await self.getInputsObj.get_keywords();
		else:
			print('got some error while getting inputs from the file');
			allSuccess = False;

		if(not(allSuccess)):
			return allSuccess;

		print('now need to initiate the driver');
		driverLoaded = await self.initiate_driver(scrapperConfig['driverPaths']['Chrome']);
		print('driverLoaded', driverLoaded);
		if(not(driverLoaded)):
			allSuccess = False;

		if(not(allSuccess)):
			return allSuccess;
		
		self.loadAndCheckPagesObj = LoadAndCheckPagesClass(self.driver);
		homePageLoadedSuccess = False;
		if(self.loadAndCheckPagesObj):
			homePageLoadedSuccess = await self.loadAndCheckPagesObj.execute();
		if(not(homePageLoadedSuccess)):
			allSuccess = False;

		if(not(allSuccess)):
			return allSuccess;

		for keyword in self.inputKeywords:
			self.extractDataObj = ExtractDataClass(self.driver, keyword);
			if(self.extractDataObj):
				allSuccess = await self.extractDataObj.execute();
				if(allSuccess):
					self.allInputsData = self.allInputsData + await self.extractDataObj.get_data_for_input();

		if(len(self.allInputsData) > 0):
			print(self.allInputsData);
			keys = self.allInputsData[0].keys();
			with open('result.csv', 'w', newline='')  as output_file:
			    dict_writer = csv.DictWriter(output_file, keys);
			    dict_writer.writeheader();
			    dict_writer.writerows(self.allInputsData);

		print('everything went fine, closing the browser');
		self.driver.close();

		return allSuccess;



async def main():
	scrapeObj = ScrapperClass();
	allPerformedSuccess = await asyncio.gather(scrapeObj.execute_and_return_success());
	print('allPerformedSuccess', allPerformedSuccess);

if(__name__ == "__main__"):
    print('running the main function');
    s = time.perf_counter();
    asyncio.run(main());
    elapsed = time.perf_counter() - s;
    print('elapsed time is {0}'.format(elapsed));
