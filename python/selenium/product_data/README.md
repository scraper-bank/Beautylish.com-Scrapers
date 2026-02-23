# Beautylish Product Data Scraper - Selenium (Python)

This powerful Python scraper is designed to extract comprehensive product information from Beautylish using the Selenium framework. It leverages advanced browser automation to navigate product pages, handle dynamic content, and bypass anti-bot protections via ScrapeOps integration, providing structured data for e-commerce analysis and monitoring.

## Table of Contents

- [What This Scraper Extracts](#what-this-scraper-extracts)
- [Quick Start](#quick-start)
- [Supported URLs](#supported-urls)
- [Configuration](#configuration)
- [Output Schema](#output-schema)
- [Anti-Bot Protection](#anti-bot-protection)
- [How It Works](#how-it-works)
- [Error Handling & Troubleshooting](#error-handling--troubleshooting)
- [Alternative Implementations](#alternative-implementations)

## What This Scraper Extracts

- **Product Identity**: Name (string), Brand (string), and Product ID (string)
- **Pricing**: Current Price (number), Pre-discount Price (number/null), and Currency (string)
- **Ratings & Reviews**: Aggregate Rating (object containing bestRating, ratingValue, reviewCount, worstRating) and detailed Reviews (array)
- **Availability**: Stock status (string)
- **Content**: Full Description (HTML string), Features (array of strings), and Specifications (array of objects)
- **Media**: Product Images (array of objects) and Videos (array of objects)
- **Seller Info**: Seller name, rating, and URL (object)
- **Metadata**: Product URL and Serial Numbers (array)

## Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager (for Python) or npm (for Node.js)

### Installation

1. Install required dependencies:

```bash
pip install selenium beautifulsoup4
```

2. Get your ScrapeOps API key from [https://scrapeops.io/app/register/ai-scraper](https://scrapeops.io/app/register/ai-scraper)

3. Update the API key in the scraper:

```python
API_KEY = "YOUR-API-KEY"
```

### Running the Scraper

1. Navigate to the scraper directory:

```bash
cd python/selenium/product_data
```

2. Edit the URLs in `scraper/beautylish_scraper_product_data_v1.py`:

```python
# In beautylish_scraper_product_data_v1.py
url = "https://example.com/product"
```

3. Run the scraper:

```bash
python beautylish_scraper_product_data_v1.py
```

The scraper will generate a timestamped JSONL file (e.g., `Beautylish_com_product_data_page_scraper_data_20260114_120000.jsonl`) containing all extracted data.

### Example Output

See `example-data/product_data.json` for a sample of the extracted data structure.

## Supported URLs

The scraper supports the following URL patterns:

- `https://www.beautylish.com/s/[product-slug]` (Standard product pages)
- `https://www.beautylish.com` (Base domain for relative path resolution)
- Example: `https://www.beautylish.com/s/vital-proteins-vanilla-collagen-creamer-10-6-oz`

## Configuration

### Scraper Parameters

The scraper supports several configuration options. See the scraper code for available parameters.

### ScrapeOps Configuration

The scraper can use ScrapeOps for anti-bot protection and request optimization:

```python
# ScrapeOps proxy configuration
proxy_url = f"https://proxy.scrapeops.io/v1/?api_key={API_KEY}"
```

**ScrapeOps Features:**
- Proxy rotation (may help reduce IP blocking)
- Request header optimization (can help reduce detection)
- Rate limiting management
- Note: CAPTCHA challenges may occur depending on site behavior and cannot be guaranteed to be resolved automatically

## Output Schema

The scraper outputs data in JSONL format (one JSON object per line). Each object contains:

| Field | Type | Description |
| :--- | :--- | :--- |
| `aggregateRating` | object | Object containing nested fields (bestRating, ratingValue, reviewCount, worstRating) |
| `availability` | string | Current stock status (e.g., "in_stock") |
| `brand` | string | The manufacturer or brand name |
| `category` | null | Product category classification (if available) |
| `currency` | string | Currency code (e.g., "USD") |
| `description` | string | Full product description, often containing HTML tags |
| `features` | array | Array of strings highlighting key product benefits |
| `images` | array | Array of objects containing image URLs and metadata |
| `name` | string | Full title of the product |
| `preDiscountPrice` | null | Original price before any applied discounts |
| `price` | integer | Current selling price (numeric) |
| `productId` | string | Unique identifier for the product |
| `reviews` | array | List of individual user reviews |
| `seller` | object | Object containing nested fields (name, rating, url) |
| `serialNumbers` | array | List of serial or identification numbers |
| `specifications` | array | Array of objects detailing technical specs |
| `url` | string | Source URL of the scraped product |
| `videos` | array | List of video resources associated with the product |

### Field Descriptions

- **aggregateRating** (object): Contains nested data including the average rating and total review count.
- **availability** (string): Indicates if the product is currently purchasable (e.g., in_stock).
- **brand** (string): The brand associated with the product (e.g., Vital Proteins).
- **category** (null): See field details for nested category hierarchies if present.
- **currency** (string): The currency used for the price (e.g., USD).
- **description** (string): Detailed product description, including HTML formatting for structure.
- **features** (array): Contains a list of string items highlighting specific selling points.
- **images** (array): Contains a list of object items with source URLs for product photos.
- **name** (string): The full name of the product as displayed on the page.
- **preDiscountPrice** (null): The list price before sales; null if no discount is active.
- **price** (integer): The current price of the item.
- **productId** (string): The slug or internal ID used by Beautylish (e.g., vital-proteins-vanilla-collagen-creamer-10-6-oz).
- **reviews** (array): Contains a list of items representing individual customer feedback.
- **seller** (object): Contains data about the merchant, including name and rating.
- **serialNumbers** (array): Contains a list of SKU or UPC items if available.
- **specifications** (array): Contains a list of object items defining size, weight, or technical details.
- **url** (string): The canonical URL of the product page.
- **videos** (array): Contains a list of video objects (e.g., YouTube or hosted clips).

## Anti-Bot Protection

This scraper can integrate with ScrapeOps to help handle Beautylish's anti-bot measures:

### Why ScrapeOps?

Beautylish may employ various anti-scraping measures including:
- Rate limiting and IP blocking
- Browser fingerprinting
- CAPTCHA challenges (may occur depending on site behavior)
- JavaScript rendering requirements
- Request pattern analysis

### ScrapeOps Integration

The scraper can use ScrapeOps proxy service which may provide:

1. **Proxy Rotation**: May help distribute requests across multiple IP addresses
2. **Request Optimization**: May optimize headers and request patterns to reduce detection
3. **Retry Logic**: Built-in retry mechanism with exponential backoff

**Note**: Anti-bot measures vary by site and may change over time. CAPTCHA challenges may occur and cannot be guaranteed to be resolved automatically. Using proxies and browser automation can help reduce blocking, but effectiveness depends on the target site's specific anti-bot measures.

### Getting Started with ScrapeOps

1. Sign up for a free account at [https://scrapeops.io/app/register/ai-scraper](https://scrapeops.io/app/register/ai-scraper)
2. Get your API key from the dashboard
3. Replace `YOUR-API-KEY` in the scraper code
4. The scraper can use ScrapeOps for requests (if configured)

**Free Tier**: ScrapeOps offers a generous free tier perfect for testing and small-scale scraping.

## How It Works

This scraper uses **Selenium** with `undetected_chromedriver` to simulate a real human user. It initiates a headless browser instance and navigates to the specified Beautylish product URLs. Once the page is loaded, it utilizes **WebDriverWait** to ensure all dynamic JavaScript elements (like price and reviews) are fully rendered before extraction. The data is parsed using a combination of Selenium's `By.CSS_SELECTOR` and **BeautifulSoup** for high-speed HTML processing of the page source. Extracted data is then mapped into a structured `ScrapedData` dataclass and passed through a `DataPipeline` which handles deduplication based on the `productId` before saving to a JSONL file.

## Error Handling & Troubleshooting

- **Timeout Errors**: If the page fails to load within the specified wait time, the scraper will log a `TimeoutException`. Try increasing the wait time or checking your proxy connection.
- **Missing Selectors**: If Beautylish updates their UI, selectors may break. The scraper uses `NoSuchElementException` handling to prevent crashes and logs the missing field.
- **Rate Limiting**: If you receive 403 or 429 errors, ensure your ScrapeOps API key is active and that you are using the residential proxy configuration.
- **Duplicate Prevention**: The `DataPipeline` tracks `productId`s; if you run the scraper multiple times on the same URL, it will skip existing items to prevent data inflation.

### Debugging

Enable detailed logging:

```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

This will show:
- Request URLs and responses
- Extraction steps
- Parsing errors
- Retry attempts

### Retry Logic

The scraper includes retry logic with configurable retry attempts and exponential backoff.

## Alternative Implementations

This repository provides multiple implementations for scraping Beautylish Product Data pages:

### Python Implementations

- [BeautifulSoup - Product Data](./python/BeautifulSoup/product_data/README.md)
- [Playwright - Product Data](./python/playwright/product_data/README.md)

### Node.js Implementations

- [Cheerio - Product Data](./node/cheerio-axios/product_data/README.md)
- [Playwright - Product Data](./node/playwright/product_data/README.md)
- [Puppeteer - Product Data](./node/puppeteer/product_data/README.md)

### Choosing the Right Implementation

**Use BeautifulSoup/Cheerio** when:
- You need fast, lightweight scraping
- JavaScript rendering is not required
- You want minimal dependencies
- You're scraping simple HTML pages

**Use Playwright** when:
- You need modern browser automation with excellent API
- You want built-in waiting and auto-waiting features
- You need cross-browser support (Chromium, Firefox, WebKit)
- You want reliable network interception

**Use Puppeteer** when:
- You only need Chromium/Chrome support
- You want a mature, stable API
- You need Chrome DevTools Protocol features
- You prefer a smaller dependency footprint

**Use Selenium** when:
- You need maximum browser compatibility
- You're working with legacy systems
- You need WebDriver standard compliance
- You want the most widely-used framework


## Performance Considerations

### Concurrency

The scraper supports concurrent requests. See the scraper code for configuration options.

**Recommendations:**
- Start with minimal concurrency for testing
- Gradually increase based on your ScrapeOps plan limits
- Monitor for rate limiting or blocking

### Output Format

Data is saved in JSONL format (one JSON object per line):
- Efficient for large datasets
- Easy to process line-by-line
- Can be imported into databases or data processing tools
- Each line is a complete, valid JSON object

### Memory Usage

The scraper processes data incrementally:
- Products are written to file immediately after extraction
- No need to load entire dataset into memory
- Suitable for scraping large pages

## Best Practices

1. **Respect Rate Limits**: Use appropriate delays and concurrency settings
2. **Monitor ScrapeOps Usage**: Track your API usage in the ScrapeOps dashboard
3. **Handle Errors Gracefully**: Implement proper error handling and logging
4. **Validate URLs**: Ensure URLs are valid Beautylish pages before scraping
5. **Update Selectors**: Beautylish may change HTML structure; update selectors as needed
6. **Test Regularly**: Test scrapers regularly to catch breaking changes early

## Support & Resources

- **ScrapeOps Documentation**: [https://scrapeops.io/docs/intro/](https://scrapeops.io/docs/intro/)
- **Framework Documentation**: See framework-specific documentation
- **Example Output**: See `example-data/product_data.json` for sample data structure
- **Scraper Code**: See `scraper/beautylish_scraper_product_data_v1.py` for implementation details

## License

This scraper is provided as-is for educational and commercial use. Please ensure compliance with Beautylish's Terms of Service and robots.txt when using this scraper.