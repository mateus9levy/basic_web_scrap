# Basic Web Scraping

This is a simple Python script that demonstrates web scraping using the BeautifulSoup library. The script retrieves game information from the OpenCritic website, including the game name, rating, supported platforms, release date, and image URL.

## How it Works

The script prompts the user to enter the number of pages they want to scrape from the OpenCritic website. It then sends HTTP requests to the corresponding page URLs, retrieves the HTML content, and uses BeautifulSoup to parse the HTML and extract the desired game information.

For each game found on the scraped pages, the script collects the relevant details and stores them in a JSON file named `data.json`. The JSON file serves as a structured data representation of the scraped game information.

## Usage

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/basic-web-scraping.git
   
2. Install dependencies:

   ```shell pip install -r requirements.txt
   pip install -r requirements.txt
   
3. Run the Script:

   ```shell
   python3 scraping.py
   
4. Enter the number of pages to be scraped when prompted.

5. The script will scrape the specified number of pages from the OpenCritic website and save the game information in a JSON file named data.json


