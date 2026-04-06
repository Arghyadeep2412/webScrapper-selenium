# Carrefour France Load More Button Scraper

This module is designed to scrape the 'Load More' button from the Carrefour France website using Selenium. It allows users to automate the process of loading additional products dynamically as they scroll down or click the button.

## Features
- **Dynamic Loading**: Handles the loading of more products without refreshing the page.
- **Selenium Integration**: Utilizes Selenium WebDriver to interact with the web page elements.
- **Efficient Scraping**: Collects data efficiently by waiting for elements to become available.

## Installation
To use this module, ensure you have the following prerequisites installed:
- Python 3.x
- Selenium library

You can install Selenium via pip:
```
pip install selenium
```

## Usage
To use the Load More Button Scraper, follow these steps:
1. Import the scraper module.
2. Initialize the WebDriver.
3. Call the scraper function and provide the necessary parameters.

### Example:
```python
from scrape_carrefour import LoadMoreButtonScraper

scraper = LoadMoreButtonScraper(driver)
scraper.scrape_load_more_button(url)
```

## Contributions
Feel free to fork the repository and submit pull requests for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.