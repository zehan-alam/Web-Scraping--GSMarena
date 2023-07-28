# Smartphone Specifications Scraping from GSM Arena

This project utilizes Python's BeautifulSoup library to extract smartphone specifications from [GSM Arena](https://www.gsmarena.com). The step-by-step process is as follows:

1. **scrap_brand_links.py:** Extracts all brand links from the website and saves them in `brand_links.txt`.

2. **scrap_phone_links.py:** Iterates through brand links and finds phone links, including paginations, saving them in `phone_links.txt`.

3. **ip_generator.py:** Collects IP addresses from [https://sslproxies.org/](https://sslproxies.org/) and stores them in `ip_addresses.txt` for potential proxy usage in the scraping process to avoid blocks.

4. **csv_generator.py:** Creates `specs.csv` file for storing the scraped data. Run this if you need to reset the CSV file and start fresh.

5. **scrap_specs.py:** Goes through phone links, collects specifications data, and ratings. Utilizes proxies to avoid potential IP blocks. Resumes from where it left off if a proxy is blocked.

**Note:** You can customize the brands to scrape in `scrap_specs.py` to select specific brands rather than scraping all.

For the detailed project code and implementation, refer to the relevant scripts in the repository. Please ensure proper usage of proxies and adhere to the website's terms of use while scraping data.
