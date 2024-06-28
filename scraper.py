import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def scrape_restaurant_urls(driver, url):
    driver.get(url)
    time.sleep(5)  # Wait for page to load

    # Scroll down to load more results if needed
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    restaurant_cards = soup.find_all('div', class_='jumbo-tracker')  # Adjust class name as needed
    
    restaurant_urls = []
    for card in restaurant_cards[:5]:  # Get top 5 restaurants
        link = card.find('a')
        if link and 'href' in link.attrs:
            restaurant_urls.append('https://www.zomato.com' + link['href'])
    
    return restaurant_urls

def main():
    # Read dish names and URLs from file
    with open('dish_urls.txt', 'r') as file:
        dish_info = file.readlines()
    dish_info = [line.strip().split(',') for line in dish_info]

    # Set up Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open the output file in write mode
    with open('all_restaurant_urls.txt', 'w') as output_file:
        try:
            for dish_name, dish_url in dish_info:
                print(f"Processing {dish_name}...")

                restaurant_urls = scrape_restaurant_urls(driver, dish_url)
                
                # Write results to the file
                output_file.write(f"\n\n--- Top 5 Restaurants for {dish_name} ---\n\n")
                for url in restaurant_urls:
                    output_file.write(url + '\n\n')  # Add an extra newline for spacing
                
                print(f"Saved top 5 restaurant URLs for {dish_name}")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            driver.quit()

if __name__ == "__main__":
    main()