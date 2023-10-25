# Product Image Scraper README

This Python script uses Selenium to scrape product images from a website. It's designed to work with the Chrome browser. Before using this bot, please follow the instructions below.

## Prerequisites

1. **Python**: Make sure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

2. **Chrome Browser**: Ensure you have Google Chrome installed on your system. You can download it from the official website: https://www.google.com/chrome/

3. **ChromeDriver**: Download and install ChromeDriver, which is a WebDriver for Chrome. ChromeDriver allows Selenium to interact with the Chrome browser. You can download it from here: https://sites.google.com/chromium.org/driver/

   - **Note**: Download the appropriate version of ChromeDriver that matches your Chrome browser version.

## Usage

1. Clone this repository or download the script to your local machine.

2. Open the script in a text editor, and locate the section where `product_links` is defined. Replace the sample links with the actual product links you want to scrape. You can create your list of product links.

```python
product_links = [ "https://www.example.com/product/1", "https://www.example.com/product/2", ...]
