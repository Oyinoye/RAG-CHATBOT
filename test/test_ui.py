from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv

import os


load_dotenv()

BASE_URL =  os.getenv("APP_BASE_URL")


# Get browser for testing. Try Chrome, if not try firefox, etc...
def get_browser():
    try:
        # Try Chrome first
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run headless if needed
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        print("Running tests on Chrome")
    except Exception as e:
        print(f"Chrome not found: {e}")

        try:
            # Try Firefox next
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
            print("Running tests on Firefox")
        except Exception as e:
            print(f"Firefox not found: {e}")

            try:
                # Try Safari next
                driver = webdriver.Safari()
                print("Running tests on Safari")
            except Exception as e:
                print(f"Safari not found: {e}")

                try:
                    # Try Edge as the final fallback
                    options = webdriver.EdgeOptions()
                    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
                    print("Running tests on Edge")
                except Exception as e:
                    print(f"Edge not found: {e}")
                    print("No compatible browser found. Exiting.")
                    sys.exit(1)  # Exit if no browser is found

    return driver

# Example usage
driver = get_browser()

# Set up Chrome WebDriver
driver = webdriver.Chrome()

try:

    # Open the FastAPI app page
    driver.get(BASE_URL)

    # Wait for the chatbot button to load
    time.sleep(3)

    # Locate and click on the chat icon to open the chatbox
    chat_button = driver.find_element(By.CLASS_NAME, "chatbox__button")
    chat_button.click()

    # Wait for the chatbox to open
    time.sleep(1)

    # Locate the input box within the chat and send a test message
    input_box = driver.find_element(By.CSS_SELECTOR, ".chatbox__footer input")
    input_box.send_keys("Hello, What do you know about football?" + Keys.RETURN)

    # Wait for response to load
    time.sleep(10)

    # Verify the chatbot responds (check for message display or specific text)
    messages = driver.find_elements(By.CLASS_NAME, "messages__item--operator")
    assert len(messages) > 0, "Expected response not found."

    print("Chatbot responded as expected!")

finally:
    # Close the driver
    driver.quit()
