from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Setup Brave WebDriver
options = Options()
options.headless = False  # Set to True if you want to run in headless mode

# Set the Brave browser executable path (adjust path as needed)
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"  # Update with correct path

# Set up the Chrome driver (Brave uses the Chrome driver)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Set a longer timeout to handle slow page loads
driver.set_page_load_timeout(180)  # Timeout after 180 seconds (3 minutes)

# URL to scrape
url = "https://www.coursejoiner.com/category/free-udemy/"

try:
    # Open the URL in the browser
    driver.get(url)
    print("Page opened successfully!")

    # Wait for the page to load completely
    time.sleep(5)  # You can adjust this wait time if needed

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Loop through each course block and extract the APPLY HERE link
    course_blocks = soup.find_all("div", class_="td-block-span6")
    for block in course_blocks:
        title = block.find("h3", class_="entry-title td-module-title")
        link = title.find("a")["href"] if title else None
        title_text = title.get_text(strip=True) if title else "No Title"

        print(f"Course Title: {title_text}")
        print(f"Course Link: {link}")

        # Now, find the "APPLY HERE" button and extract the href
        apply_button = block.find("a", class_="wp-block-button__link")
        if apply_button and apply_button.get("href"):
            apply_href = apply_button["href"]
            print(f"APPLY HERE Link: {apply_href}")
        else:
            print("APPLY HERE Link: Not found")

        print("-" * 50)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Ensure the driver quits after execution to avoid leaving processes open
    driver.quit()  