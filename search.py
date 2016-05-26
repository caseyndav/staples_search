#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver

# Staples product data scraper using SKU
#
# Toy example that uses Selenium to provide a (very slow) way of collected
# product data using the SKU from the Staples website. Accepts user input from
# command line.

base_url = "http://www.staples.com/{sku}/directory_{sku}?"
browser = None


def search(sku):
    """
    Takes a product SKU and inserts it into the Staples product URL, then
    returns specific product data as a dictionary.
    """
    prod_url = base_url.replace("{sku}", sku)
    browser.get(prod_url)
    data = browser.execute_script("return STAPLES.angularData")
    if data is None:
        return None
    return data["selectedSKU"]


def main():
    """
    Contains main program loop.
    """
    global browser
    browser = webdriver.Chrome()  # New Selenium browser instance
    while True:
        sku = raw_input("Enter SKU: ")
        result = search(sku)
        print "\n"
        if result is not None:
            print result
        else:
            print "No results found"
        print "\n"


if __name__ == "__main__":
    try:
        # display = Display(visible=0, size=(800, 600))  # Used to hide browser
        # display.start()
        main()
    except KeyboardInterrupt:
        print "\nQuitting..."
    # display.stop()
