# asset-dumper

Since i'm looking for skins, asset that has sequential file names and it's tiring to download one-by-one, I decided to make this simple script. Using `requests` to scrapping the website.

## Usage

`pip install -r requirements.txt` 

Then, make a file called .env 
```bash
BASE_URL= https://example.com/assets/image/
ITERATOR=4
CUSTOM_ITERATOR= EMPTY IF THERE JUST ITERATION/NUMBER
FILE_EXTENSION= JPG
FOLDER_NAME= OUTPUT
###EXAMPLE https://example.com/assets/image/0.jpg till 4.jpg will be downloaded
```

Last, `py main.py`

If you want to use this as library, feel free to see this [sequentialdw](htps://github.com/wweziza/sequentialdw)