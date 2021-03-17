scrapperConfig = {
	'driverPaths': {
		'Chrome': 'C:\Program Files (x86)\chromedriver.exe'
	},
	'inputFilePath': 'D:/personal-work/selenium-python/carrefour_fr/search_loadMoreBtn/input.xlsx'
}

pageConfig = {
	'navigationTimeout': 30,
	'elementTimeout': 30,
	'homePageUrl': 'https://www.carrefour.fr/',
	'searchBarXpath': '//*[contains(@id,"search-bar-input")]',
	'clearSearchBarBtnXpath': '//*[contains(@id,"search-bar-input")]//following-sibling::*[contains(@id,"button-clean")]',
	'xpathOrDelimiter': ' | ',
	'homePageLoadedXpath': ['//*[contains(@id,"data-quick-access-bar")]'],
	'loadedXpath': ['//div[contains(@class,"product-list")]//ul[contains(@class,"product-grid")]'],
	'allCloseBtnXpath': ['//*[contains(@id,"privacy_button")][contains(.,"Accepter")]', '//*[contains(@class,"modal__close")][contains(@type,"button")]'],
	'noResultsXpath': [],
	'hasPagination': False,
	'pagination': {
		'clickToNextPageXpath': '',
	},
	'hasLazyLoading': False,
	'lazyLoadingSpecs': {
		'scrollPauseTime': 5
	},
	'hasLoadMoreBtn': True,
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
	'rowXpath': ['(//div[contains(@class,"product-list")]//ul[contains(@class,"product-grid")])[last()]//li//a[contains(@class,"product-card-title")]//ancestor::*[contains(@class,"product-grid-item")]'],
	'attributes': {
		'prodLink': {
			'xpath': ['//a[contains(@class,"product-card-title")]'],
			'param': 'href',
		},
		'name': {
			'xpath': ['//a[contains(@class,"product-card-title")]//*[contains(@class,"title")]'],
			'param': ''
		},
		'id': {
			'xpath': ['//article[contains(@class,"ds-product-card--")]'],
			'param': 'id'
		},
		'price': {
			'xpath': ['//div[@class="product-card-price"]//*[contains(@class,"product-card-price__price--final")]'],
			'param': ''
		}
	},
};