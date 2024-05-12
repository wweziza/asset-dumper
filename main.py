import os
import requests
from dotenv import load_dotenv

load_dotenv()

# ANSI escape codes for colors
WARNING_COLOR = '\033[93m'  # Yellow color for warning
RESET_COLOR = '\033[0m'      # Reset color

def convert_bytes_to_mb(bytes_size):
    return bytes_size / (1024 * 1024)  # Convert bytes to megabytes

def download_images(base_url, start_index, end_index, custom_iterator, file_extension, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    if not file_extension:
        # Print warning message if file extension is empty
        print(f"{WARNING_COLOR}WARNING: File extension is empty. Pausing at first trying / first download.{RESET_COLOR}")
        input("Press Enter to continue...")

    for i in range(start_index, end_index + 1):
        if custom_iterator:
            url = f"{base_url}/{custom_iterator}_{i}.{file_extension}"
        else:
            url = f"{base_url}/{i}.{file_extension}"
        
        filename = os.path.join(output_folder, f"{custom_iterator}_{i}.{file_extension}" if custom_iterator else f"{i}.{file_extension}")


        # Download the image
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            total_size = int(response.headers.get('content-length', 0))
            total_size_mb = convert_bytes_to_mb(total_size)
            downloaded_size = 0
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        downloaded_size += len(chunk)
                        downloaded_size_mb = convert_bytes_to_mb(downloaded_size)
                        print(f"Downloading {filename} {downloaded_size_mb:.2f}/{total_size_mb:.2f} MB", end='\r')
            print(f"\nDownloaded {filename}")  # Add a newline before printing the filename
        else:
            print(f"Failed to download: {url}")

if __name__ == "__main__":
    base_url = os.getenv("BASE_URL")
    iterator = os.getenv("ITERATOR")
    custom_iterator = os.getenv("CUSTOM_ITERATOR")
    file_extension = os.getenv("FILE_EXTENSION")
    start_index = 0
    end_index = int(iterator)
    output_folder = os.getenv("FOLDER_NAME") or "output"  # Set default value to "output" if FOLDER_NAME is empty

    download_images(base_url, start_index, end_index, custom_iterator, file_extension, output_folder)
