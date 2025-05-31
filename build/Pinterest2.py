import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import urllib.parse

# Function to download an image
def download_image(url, save_path, image_name):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        with open(os.path.join(save_path, image_name), 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded {image_name}")
    except Exception as e:
        print(f"Failed to download {image_name}. Error: {e}")

# Function to scrape high-resolution image from a Pinterest pin URL using Selenium
def scrape_pinterest_image(pin_url, save_path):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(pin_url)
        
        # Wait for the image element to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'img'))
        )

        # Get the page source and parse it with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

        # Find the full resolution image URL
        img_tag = soup.find('img', {'src': True})
        img_url = None
        if img_tag:
            if 'srcset' in img_tag.attrs:
                # Get the highest resolution image from srcset
                srcset = img_tag['srcset'].split(',')
                img_url = srcset[-1].split()[0]  # The last item is usually the highest resolution
            elif 'src' in img_tag.attrs:
                img_url = img_tag['src']

            if img_url:
                img_url = urllib.parse.urljoin(pin_url, img_url)
                image_name = os.path.basename(img_url).split('?')[0]  # Clean the image name
                download_image(img_url, save_path, image_name)
            else:
                print(f"No image URL found at {pin_url}")
        else:
            print(f"No image tag found at {pin_url}")
    
    except Exception as e:
        print(f"Failed to scrape Pinterest pin. Error: {e}")

# List of Pinterest pin URLs
pin_urls = [
    'https://www.pinterest.com/pin/630504016614541301/',
    'https://www.pinterest.com/pin/630504016614540615/',
    'https://www.pinterest.com/pin/630504016614036390/',
    'https://www.pinterest.com/pin/630504016614036329/',
    'https://www.pinterest.com/pin/630504016614035430/',
    'https://www.pinterest.com/pin/630504016614031031/',
    'https://www.pinterest.com/pin/630504016614030981/',
    'https://www.pinterest.com/pin/630504016614030903/'
]

# Save path
save_path = os.path.join('E:', 'BG', 'Pinterest', 'downloaded_images')  # Modify this path as needed

# Scrape images from all provided Pinterest pin URLs
for pin_url in pin_urls:
    scrape_pinterest_image(pin_url, save_path)
