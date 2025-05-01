from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Brave browser
options = Options()
options.headless = False  # Set to True to run in background
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# Set up the ChromeDriver service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Open CourseJoiner "Free Udemy" page
    url = "https://www.coursejoiner.com/category/free-udemy/"
    driver.get(url)
    time.sleep(3)

    # Find all course blocks
    blocks = driver.find_elements(By.CLASS_NAME, "td-block-span6")

    # Store course titles and post links
    course_titles = []
    course_links = []

    for block in blocks:
        try:
            title = block.find_element(By.TAG_NAME, "h3").text
            link = block.find_element(By.TAG_NAME, "a").get_attribute("href")
            course_titles.append(title)
            course_links.append(link)
        except:
            continue

    # Loop through each course post
    for title, course_url in zip(course_titles, course_links):
        try:
            driver.get(course_url)
            time.sleep(3)

            # Find "APPLY HERE" button and extract the Udemy link
            apply_button = driver.find_element(By.XPATH, '//a[contains(text(), "APPLY HERE")]')
            udemy_link = apply_button.get_attribute("href")

            print("------------------------------------------------------------")
            print(f"Course Title: {title}")
            print(f"Course Page: {course_url}")
            print(f"✅ Udemy Link: {udemy_link}")

        except Exception as e:
            print("------------------------------------------------------------")
            print(f"⚠️ Skipped due to error: {e}")

finally:
    driver.quit()
