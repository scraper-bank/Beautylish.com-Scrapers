import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode, urljoin
import json
import re
from concurrent.futures import ThreadPoolExecutor
# Using standard logging as requested
import logging
from dataclasses import dataclass, asdict, field
from typing import Dict, Any, Optional, List

API_KEY = "YOUR-API_KEY"

def generate_output_filename() -> str:
    """Generate output filename with current timestamp."""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"beautylish_com_product_category_page_scraper_data_{timestamp}.jsonl"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class ScrapedData:
    appliedFilters: List[Dict[str, str]] = field(default_factory=list)
    bannerImage: Optional[str] = None
    breadcrumbs: Optional[List[Any]] = None
    categoryId: Optional[str] = None
    categoryName: str = ""
    categoryUrl: str = ""
    description: Optional[str] = None
    pagination: Optional[Any] = None
    products: List[Dict[str, Any]] = field(default_factory=list)
    subcategories: List[Dict[str, Any]] = field(default_factory=list)

class DataPipeline:
    def __init__(self, jsonl_filename="output.jsonl"):
        self.items_seen = set()
        self.jsonl_filename = jsonl_filename

    def is_duplicate(self, input_data: ScrapedData) -> bool:
        # Use categoryUrl as a unique identifier for the page
        item_key = input_data.categoryUrl
        if item_key in self.items_seen:
            logger.warning(f"Duplicate item found: {item_key}. Skipping.")
            return True
        self.items_seen.add(item_key)
        return False

    def add_data(self, scraped_data: ScrapedData):
        if not self.is_duplicate(scraped_data):
            with open(self.jsonl_filename, mode="a", encoding="UTF-8") as output_file:
                json_line = json.dumps(asdict(scraped_data), ensure_ascii=False)
                output_file.write(json_line + "\n")
            logger.info(f"Saved item to {self.jsonl_filename}")

def strip_html(html_str: str) -> str:
    """Port of Go's stripHTML function."""
    if not html_str:
        return ""
    clean = re.compile('<[^>]*>')
    return re.sub(clean, ' ', html_str).strip()

def make_absolute_url(url_str: str) -> str:
    """Port of Go's makeAbsoluteURL function logic."""
    domain = "https://www.beautylish.com"
    if not url_str:
        return ""
    if url_str.startswith(("http://", "https://")):
        return url_str
    if url_str.startswith("//"):
        return "https:" + url_str
    if url_str.startswith("/"):
        return domain + url_str
    return f"{domain}/{url_str}"

def detect_currency(price_text: str) -> str:
    """Port of Go's detectCurrency function."""
    price_text = price_text.upper()
    currency_map = {
        "USD": "USD", "US$": "USD", "US $": "USD", "$": "USD",
        "EUR": "EUR", "€": "EUR",
        "GBP": "GBP", "£": "GBP", "GB£": "GBP",
        "JPY": "JPY", "¥": "JPY", "JP¥": "JPY",
        "CAD": "CAD", "CA$": "CAD", "C$": "CAD",
        "AUD": "AUD", "AU$": "AUD", "A$": "AUD",
        "CNY": "CNY", "CN¥": "CNY", "RMB": "CNY",
        "CHF": "CHF", "FR.": "CHF",
        "SEK": "SEK", "KR": "SEK",
        "NZD": "NZD", "NZ$": "NZD",
    }
    for code, currency in currency_map.items():
        if code in price_text:
            return currency
    return "USD"

def extract_numeric(text: str) -> float:
    """Port of Go's extractNumeric function."""
    if not text:
        return 0.0
    text = text.replace(",", "")
    match = re.search(r'([\d,]+\.?\d*)', text)
    if match:
        try:
            return float(match.group(1))
        except ValueError:
            return 0.0
    return 0.0

def extract_data(soup: BeautifulSoup) -> Optional[ScrapedData]:
    """Port of Go's ExtractData function to Python BeautifulSoup."""
    try:
        data = ScrapedData()

        # Applied Filters
        title_tag = soup.find("title")
        title_text = title_tag.get_text() if title_tag else ""
        if "skincare" in title_text.lower():
            data.appliedFilters.append({
                "filterName": "tag",
                "filterValue": "skincare"
            })

        # Category Name
        h1_tag = soup.find("h1")
        if h1_tag and h1_tag.get_text(strip=True):
            data.categoryName = h1_tag.get_text(strip=True)
        elif title_text:
            data.categoryName = title_text.split("|")[0].strip()

        # Category URL
        canonical = soup.find("link", rel="canonical")
        cat_url = canonical.get("href", "") if canonical else ""
        data.categoryUrl = make_absolute_url(cat_url)

        # Products
        # Targeting specific classes as defined in the Go code
        product_selectors = [
            ".product-card", 
            ".category-products .item", 
            "[itemtype='http://schema.org/Product']", 
            ".product-list-item", 
            ".item-grid .item"
        ]
        product_elements = soup.select(", ".join(product_selectors))
        
        for s in product_elements:
            # Extract Name
            name_el = s.select_one(".product-name, .name, [itemprop='name'], .title")
            name = name_el.get_text(strip=True) if name_el else ""
            
            if not name:
                continue

            # Extract URL
            url = ""
            a_tag = s.find("a")
            if a_tag:
                url = a_tag.get("href", "")
            elif s.name == "a":
                url = s.get("href", "")
            
            # Extract Image
            img_el = s.find("img")
            img = ""
            if img_el:
                img = img_el.get("data-src") or img_el.get("src") or ""

            # Extract Price
            price_el = s.select_one(".price, .product-price, [itemprop='price'], .amount")
            price_text = price_el.get_text() if price_el else ""
            
            data.products.append({
                "name": name,
                "url": make_absolute_url(url),
                "image": make_absolute_url(img),
                "price": extract_numeric(price_text)
            })

        # Subcategories
        subcategory_elements = soup.select(".squeezeBox_sublist .squeezeBox_item a, .ocnNav .squeezeBox_link")
        for s in subcategory_elements:
            name = s.get_text(strip=True)
            url = s.get("href", "")
            if name and url:
                data.subcategories.append({
                    "name": name,
                    "productCount": None,
                    "url": make_absolute_url(url)
                })

        return data
    except Exception as e:
        logger.error(f"Error extracting data: {e}")
        return None

def scrape_page(url: str, pipeline: DataPipeline, retries: int = 3) -> None:
    """Scrape a single page with retry logic and ScrapeOps integration."""
    payload = {
        "api_key": API_KEY,
        "url": url,
        "optimize_request": True,
    }

    tries = 0
    success = False

    while tries <= retries and not success:
        try:
            proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
            response = requests.get(proxy_url, timeout=30)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "lxml") # Using lxml as requested in packages
                
                scraped_data = extract_data(soup)
                
                if scraped_data:
                    pipeline.add_data(scraped_data)
                    success = True
                else:
                    logger.warning(f"No data extracted from {url}")
            else:
                logger.warning(f"Request failed for {url} with status {response.status_code}")
        except Exception as e:
            logger.error(f"Exception scraping {url}: {e}")
        finally:
            tries += 1

    if not success:
        logger.error(f"Failed to scrape {url} after {retries} retries.")

def concurrent_scraping(urls: List[str], max_threads: int = 1, max_retries: int = 3, output_file: str = None) -> None:
    """Scrape multiple URLs concurrently."""
    if output_file is None:
        output_file = generate_output_filename()
    pipeline = DataPipeline(jsonl_filename=output_file)
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scrape_page, url, pipeline, max_retries) for url in urls]
        for future in futures:
            try:
                future.result()
            except Exception as e:
                logger.error(f"Thread generated an exception: {e}")

if __name__ == "__main__":
    urls = [
        "https://www.beautylish.com/shop/browse?tag=skincare",
    ]

    logger.info("Starting concurrent scraping...")
    # Keeping exact concurrency values from template (max_threads=1)
    concurrent_scraping(urls, max_threads=1, max_retries=3)
    logger.info("Scraping complete.")