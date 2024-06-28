# Zomato Top Rated Restaurants Scraper

This project scrapes the top-rated restaurants in a city from Zomato using Python packages like Selenium, BeautifulSoup, and WebDriver Manager. It retrieves a list of top restaurants based on specific dishes and writes their URLs to a file.

## Features

- Scrapes top-rated restaurants from Swiggy for given dish URLs.
- Uses Selenium to handle dynamic loading and scrolling.
- Stores the URLs of the top 5 restaurants for each dish in a text file.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- `pip` (Python package installer)


## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/AdiOs46/zomato-resto-scraper.git
   cd zomato-resto-scraper

2. Install the required packages (as per imports in the code)

## Usage

    Create a dish_urls.txt file in the root directory with the dish names and URLs, formatted as follows:
    Dish Name 1,URL 1
    Dish Name 2,URL 2

## Run the scraper script:

    python scraper.py
    The top 5 restaurant URLs for each dish will be saved in all_restaurant_urls.txt.

## Contributing

  Feel free to submit issues and pull requests if you have suggestions or improvements!
