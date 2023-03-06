# PDF Downloader

This Python script allows you to download PDF files from a website using the `requests` and `BeautifulSoup` libraries.

## Installation

1. Clone this repository: `git clone https://github.com/votre-nom/pdf-downloader.git`
2. Navigate to the project directory: `cd pdf-downloader`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Open the `main.py` file in a code editor.
2. Replace the URL variable with the URL of the webpage containing the PDF files you want to download.
3. Run the script: `python main.py`
4. The script will download all the PDF files it finds to the current directory.

## Customization

You can modify the script to suit your specific needs by changing the following variables:

- `url`: The URL of the webpage containing the PDF files to download.
- `file_extension`: The file extension of the files to download (default is ".pdf").
- `download_directory`: The directory where the downloaded files will be saved (default is the current directory).

## Limitations

Note that this script may not work for all websites, as the HTML structure and link format can vary. You may need to modify the script to suit the specific website you are scraping.
