import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

# Function to download an image
def download_image(url, save_path, image_name, index):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        indexed_image_name = f"{index}_{image_name}"
        with open(os.path.join(save_path, indexed_image_name), 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded {index}_{image_name}")
    except Exception as e:
        print(f"Failed to download {index}_{image_name}. Error: {e}")

# Function to get the highest resolution image URL
def get_high_res_image_url(image_url):
    # Pinterest stores images in various resolutions, we need to find the highest
    parts = image_url.split('/')
    if 'originals' in parts:
        return image_url  # Already the highest resolution
    if '564x' in parts:
        parts[parts.index('564x')] = 'originals'
    return '/'.join(parts)

# Function to scrape image from a Pinterest pin URL
def scrape_pinterest_image(pin_url, save_path, index):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(pin_url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tag = soup.find('img', {'src': True})
        
        if img_tag:
            img_url = img_tag['src']
            # Get the highest resolution image URL
            high_res_img_url = get_high_res_image_url(img_url)
            image_name = os.path.basename(urllib.parse.urlparse(high_res_img_url).path)
            download_image(high_res_img_url, save_path, image_name, index)
        else:
            print(f"No image found at {pin_url}")
    
    except Exception as e:
        print(f"Failed to scrape Pinterest pin. Error: {e}")

# List of Pinterest pin URLs
pin_urls = [
    'https://www.pinterest.com/pin/881790802059728963/',
    'https://www.pinterest.com/pin/881790802059728962/',
    'https://www.pinterest.com/pin/881790802059728961/',
    'https://www.pinterest.com/pin/881790802059728960/',
    'https://www.pinterest.com/pin/881790802059728959/',
    'https://www.pinterest.com/pin/881790802059728958/',
    'https://www.pinterest.com/pin/881790802059728957/',
    'https://www.pinterest.com/pin/881790802058808375/',
    'https://www.pinterest.com/pin/881790802058808374/',
    'https://www.pinterest.com/pin/881790802058808373/'
]

# Save path
save_path = os.path.join('D:', 'TEST 2', 'Data', 'Pinterest', 'Pinterest_Images')  # Modify this path as needed

# Function to handle the scraping and downloading for a given pin URL and index
def handle_pin(pin_url, save_path, index):
    scrape_pinterest_image(pin_url, save_path, index)

# Use ThreadPoolExecutor to download images concurrently
with ThreadPoolExecutor(max_workers=10) as executor:
    for index, pin_url in enumerate(pin_urls, start=1):
        executor.submit(handle_pin, pin_url, save_path, index)
