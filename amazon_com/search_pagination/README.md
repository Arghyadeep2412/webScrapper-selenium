# Amazon Search Pagination Scraper

## Purpose
The Amazon Search Pagination Scraper module is designed to automate the extraction of product listings from Amazon search results across multiple pages. This is particularly useful for users who require data scraping for analysis, pricing strategies, or inventory management.

## Features
- **Multi-Page Scraping**: Automatically navigates through search result pages to gather product details.
- **Data Extraction**: Collects essential product information such as title, price, rating, and availability.
- **Flexible Configuration**: Easily adapt the scraper's settings to adjust the depth of pagination and specific product categories.
- **Error Handling**: Includes mechanisms to manage unexpected website changes or rate limits.

## Requirements
- Python 3.6+
- Selenium WebDriver
- Chromedriver or appropriate WebDriver for the browser of choice
- Beautiful Soup (for HTML parsing)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Arghyadeep2412/webScrapper-selenium.git
   cd webScrapper-selenium
   ```  
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Ensure that the required WebDriver is installed and available in your PATH.
2. Run the scraper script by executing:
   ```bash
   python amazon_search_pagination_scraper.py
   ```
3. Follow the on-screen prompts to enter search parameters.

## Configuration
Users can configure the following settings in the script:
- `search_query`: The keywords to search for on Amazon.
- `max_pages`: The maximum number of pages to scrape.
- `output_file`: The name of the file where the scraped data will be saved.

By adjusting these configurations, the module can be tailored to meet specific scraping needs.