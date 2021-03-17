scrapperConfig = {
	'driverPaths': {
		'Chrome': 'C:\Program Files (x86)\chromedriver.exe'
	},
	'inputFilePath': 'D:/personal-work/selenium-python/amazon_com/search_pagination/input.xlsx'
}

pageConfig = {
	'navigationTimeout': 30,
	'elementTimeout': 30,
	'homePageUrl': 'https://www.amazon.com/',
	'searchBarXpath': '//*[contains(@id,"nav-search-bar-form")]//input[contains(@id,"searchtextbox")]',
	'clearSearchBarBtnXpath': '',
	'xpathOrDelimiter': ' | ',
	'homePageLoadedXpath': ['//div[contains(@id,"card-layout")]//div[contains(@id,"desktop-grid")]'],
	'loadedXpath': ['//div[contains(@class,"result-list")]//div[contains(@data-component-type,"s-search-result")][@data-asin]'],
	'allCloseBtnXpath': [],
	'noResultsXpath': [],
	'hasPagination': True,
	'pagination': {
		'clickToNextPageXpath': '//ul[contains(@class,"pagination")]//a[contains(.,"Next")]',
	},
	'hasLazyLoading': False,
	'lazyLoadingSpecs': {
		'scrollPauseTime': 5
	},
	'hasLoadMoreBtn': False,
	'loadMoreSpecs': {
		'btnXpath': '//*[contains(@class,"pagination__button")]//button[contains(.,"Produits suivants")]',
		'loadTimeOut': 10
	}
};

dataConfig = {
	'maxResults': 100
}

attributeConfig = {
	'xpathOrDelimiter': ' | ',
	'rowXpath': ['//div[contains(@class,"result-list")]//div[contains(@data-component-type,"s-search-result")][@data-asin]'],
	'attributes': {
		'prodLink': {
			'xpath': ['//*[contains(@data-component-type,"product-image")]//a'],
			'param': 'href',
			'prefix': 'https://www.amazon.com'
		},
		'name': {
			'xpath': ['//*[contains(@data-component-type,"product-image")]//following-sibling::div//h2//a//*'],
			'param': '',
		},
		'asin': {
			'xpath': [''],
			'param': 'data-asin',
		},
		'salesprice': {
			'xpath': ['//*[contains(@class,"a-price") and not(contains(@class,"text-price"))]//*[contains(@class,"a-offscreen")]'],
			'param': '',
		}
	},
};