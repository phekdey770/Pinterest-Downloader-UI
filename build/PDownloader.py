import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
import tkinter as tk
from tkinter import scrolledtext, messagebox, StringVar, filedialog
from threading import Thread

# Function to download an image
def download_image(url, save_path, image_name, index, log_text_widget, status_var, processed_var, total_links):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        if not os.path.exists(save_path):
            raise FileNotFoundError(f"Save path '{save_path}' does not exist.")
        indexed_image_name = f"{index}_{image_name}"
        with open(os.path.join(save_path, indexed_image_name), 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        status_var.set(f"Downloaded {index}_{image_name}")
        log_text_widget.insert(tk.END, f"Downloaded {index}_{image_name}\n")
    except Exception as e:
        status_var.set(f"Failed to download {index}_{image_name}")
        log_text_widget.insert(tk.END, f"Failed to download {index}_{image_name}. Error: {e}\n")
    finally:
        # Update the processed count
        current_processed = int(processed_var.get().split('/')[0]) + 1
        processed_var.set(f"{current_processed}/{total_links}")

# Function to get the highest resolution image URL
def get_high_res_image_url(image_url):
    parts = image_url.split('/')
    if 'originals' in parts:
        return image_url  # Already the highest resolution
    if '564x' in parts:
        parts[parts.index('564x')] = 'originals'
    return '/'.join(parts)

# Function to scrape image from a Pinterest pin URL
def scrape_pinterest_image(pin_url, save_path, index, log_text_widget, status_var, processed_var, total_links):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(pin_url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tag = soup.find('img', {'src': True})
        
        if (img_tag):
            img_url = img_tag['src']
            high_res_img_url = get_high_res_image_url(img_url)
            image_name = os.path.basename(urllib.parse.urlparse(high_res_img_url).path)
            download_image(high_res_img_url, save_path, image_name, index, log_text_widget, status_var, processed_var, total_links)
        else:
            status_var.set(f"No image found at {pin_url}")
            log_text_widget.insert(tk.END, f"No image found at {pin_url}\n")
    
    except Exception as e:
        status_var.set(f"Failed to scrape Pinterest pin: {e}")
        log_text_widget.insert(tk.END, f"Failed to scrape Pinterest pin. Error: {e}\n")

# Function to handle the scraping and downloading for a given pin URL and index
def handle_pin(pin_url, save_path, index, log_text_widget, status_var, processed_var, total_links):
    scrape_pinterest_image(pin_url, save_path, index, log_text_widget, status_var, processed_var, total_links)

# Function to start the download process
def start_download(urls, save_path, log_text_widget, status_var, processed_var):
    global stop_download
    stop_download = False  # Initialize the stop flag

    def download_task():
        global stop_download  # Use global to access the global variable
        
        pin_urls = urls.strip().split()
        total_links = len(pin_urls)
        if not pin_urls:
            messagebox.showerror("Error", "Please enter at least one URL.")
            return
        
        if not os.path.exists(save_path):
            messagebox.showerror("Error", f"Save path '{save_path}' does not exist.")
            return

        log_text_widget.delete(1.0, tk.END)
        processed_var.set(f"0/{total_links}")
        for index, pin_url in enumerate(pin_urls, start=1):
            if stop_download:  # Check if the stop flag is set
                status_var.set("Download process stopped.")
                break  # Exit the loop if stop flag is True
            
            handle_pin(pin_url, save_path, index, log_text_widget, status_var, processed_var, total_links)
            window.update_idletasks()  # Update the GUI during the loop

        if not stop_download:
            messagebox.showinfo("Download Complete", "All downloads have been completed.")

    download_thread = Thread(target=download_task)
    download_thread.start()

# Function to browse and select the directory
def browse_directory(entry_widget):
    directory = filedialog.askdirectory()
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, directory)

# Function to clear all input fields and log text
def clear_all(url_text, save_path_entry, log_text_widget):
    url_text.delete(1.0, tk.END)
    save_path_entry.delete(0, tk.END)
    log_text_widget.delete(1.0, tk.END)

# Function to stop the download process
def stop_download_process():
    global stop_download
    stop_download = True  # Set the stop flag to True

# Tkinter GUI setup
def create_gui():
    global window
    window = tk.Tk()
    window.title("Pinterest Image Downloader")

    # Center the window on the screen
    window_width = 600
    window_height = 670
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Header title
    header_title = tk.Label(window, text="DOWNLOAD PINTEREST IMAGES", font=("Arial", 18, "bold"))
    header_title.pack(pady=10)

    # Small text
    small_text = tk.Label(window, text="Created by Phekdey PHORN")
    small_text.pack()

    # Version
    version_text = tk.Label(window, text="Version 1.0.0")
    version_text.pack()

    tk.Label(window, text="Enter Pinterest Pin URLs (one per line):").pack(pady=5)

    url_text = scrolledtext.ScrolledText(window, width=60, height=10)
    url_text.pack(pady=5)

    save_path_frame = tk.Frame(window)
    save_path_frame.pack(pady=5)
    tk.Label(save_path_frame, text="Save Path:").pack(side=tk.LEFT)
    save_path_entry = tk.Entry(save_path_frame, width=50)
    save_path_entry.insert(0, os.path.join('D:', 'TEST 2', 'Data', 'Pinterest', 'Pinterest_Images'))  # Modify as needed
    save_path_entry.pack(side=tk.LEFT, padx=5)
    browse_button = tk.Button(save_path_frame, text="Browse", command=lambda: browse_directory(save_path_entry))
    browse_button.pack(side=tk.LEFT)

    log_text = scrolledtext.ScrolledText(window, width=60, height=10)
    log_text.pack(pady=0)

    status_var = StringVar()
    status_label = tk.Label(window, textvariable=status_var)
    status_label.pack(pady=0)

    processed_var = StringVar()
    processed_label = tk.Label(window, textvariable=processed_var)
    processed_label.pack(pady=0)

    download_button = tk.Button(window, text="Start Download",
                                command=lambda: start_download(url_text.get("1.0", tk.END), save_path_entry.get(), log_text, status_var, processed_var))
    download_button.pack(pady=0)

    stop_button = tk.Button(window, text="Stop Download", command=stop_download_process)
    stop_button.pack(pady=5)

    clear_button = tk.Button(window, text="Clear All", command=lambda: clear_all(url_text, save_path_entry, log_text))
    clear_button.pack(pady=5)

    window.mainloop()

# Run the GUI application
if __name__ == "__main__":
    create_gui()

