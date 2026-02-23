# Beautylish Product Data Scraper - Playwright (Python)

This professional-grade scraper is designed to extract comprehensive product information from Beautylish using the Playwright framework in Python. It features asynchronous data extraction, stealth browser integration to mimic human behavior, and seamless ScrapeOps proxy support to handle high-volume data collection efficiently.

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

- **Product Identity**: Name (string), Brand (string), and Product ID.
- **Pricing & Availability**: Current Price (number), Pre-discount Price (number), Currency (string), and Availability status (string).
- **Media Assets**: Images (array of objects with URLs) and Videos (array of objects).
- **Product Details**: Full Description (HTML/string), Features (list of strings), and Specifications (array of key-value pairs).
- **Social Proof**: Aggregate Rating (object including rating value and review count) and detailed Reviews (array).
- **Metadata**: Product URL (string), Seller information (object), and Serial Numbers (array).

## Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager (for Python) or npm (for Node.js)

### Installation

1. Install required dependencies:

```bash
pip install playwright beautifulsoup4
```

2. Get your ScrapeOps API key from [https://scrapeops.io/app/register/ai-scraper](https://scrapeops.io/app/register/ai-scraper)

3. Update the API key in the scraper:

```python
API_KEY = "YOUR-API-KEY"
```

### Running the Scraper

1. Navigate to the scraper directory:

```bash
cd python/playwright/product_data
```

2. Edit the URLs in `scraper/beautylish_scraper_product_data_v1.py`:

```python
# In beautylish_scraper_product_data_v1.py
url = "https://www.beautylish.com/s/vital-proteins-vanilla-collagen-creamer-10-6-oz"
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

- `https://www.beautylish.com/s/[product-slug]`
- `https://www.beautylish.com/p/[brand-slug]/[product-name]`

Example URL: `https://www.beautylish.com/s/vital-proteins-vanilla-collagen-creamer-10-6-oz`

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
| `aggregateRating` | object | Object containing nested fields (ratingValue, reviewCount, etc.) |
| `availability` | string | Stock status (e.g., "in_stock") |
| `brand` | string | The manufacturer or brand name |
| `category` | null | Product category classification |
| `currency` | string | Three-letter currency code (e.g., "USD") |
| `description` | string | Detailed product description, often containing HTML |
| `features` | array | Array of key product highlight strings |
| `images` | array | Array of objects containing image URLs |
| `name` | string | Full title of the product |
| `preDiscountPrice` | null | Original price before any active discounts |
| `price` | integer | Current selling price |
| `productId` | null | Unique identifier for the product |
| `reviews` | array | List of individual customer reviews |
| `seller` | object | Information about the merchant (defaults to Beautylish) |
| `serialNumbers` | array | List of associated serial or identification numbers |
| `specifications` | array | Array of objects containing technical specs |
| `url` | string | The source URL of the product page |
| `videos` | array | List of associated product video assets |

### Field Descriptions

- **aggregateRating** (object): Contains nested data such as `ratingValue` (e.g., 4) and `reviewCount`.
- **availability** (string): Indicates if the product is currently purchasable (e.g., "in_stock").
- **brand** (string): The brand name, such as "Vital Proteins".
- **category** (null): Placeholder for hierarchical category data if available.
- **currency** (string): The currency used for pricing, typically "USD".
- **description** (string): Comprehensive product details, including "About", "How to Use", and "Other Details".
- **features** (array): Contains a list of string items highlighting specific product benefits.
- **images** (array): Contains a list of object items with image source links.
- **name** (string): The full product name including size (e.g., "Vital Proteins Vanilla Collagen Creamer 10.6 oz").
- **preDiscountPrice** (null): Used if the product is on sale to show the original price.
- **price** (integer): The numerical cost of the item.
- **productId** (null): Internal unique ID used by the site.
- **reviews** (array): Contains a list of customer feedback items.
- **seller** (object): Contains nested data about the shop, including name and URL.
- **serialNumbers** (array): Contains a list of identification codes.
- **specifications** (array): Contains a list of object items defining product attributes.
- **url** (string): The canonical URL of the scraped product page.
- **videos** (array): Contains a list of video links or metadata.

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

This scraper uses **Playwright** for high-fidelity browser automation. Here is the technical workflow:
- **Initialization**: It launches a headless Chromium instance and applies `stealth_async` to bypass common bot detection scripts.
- **Navigation**: The script navigates to the specified Beautylish product URL, utilizing residential proxies via the ScrapeOps gateway to mask the scraper's origin.
- **Extraction**: Once the page is loaded, it uses CSS selectors and Playwright's API to locate product elements. It extracts data points like price, brand, and description directly from the DOM.
- **Data Structuring**: Extracted data is mapped to a `ScrapedData` dataclass, ensuring a consistent schema.
- **Persistence**: The `DataPipeline` class checks for duplicate URLs and appends the results to a `.jsonl` file in real-time, preventing data loss during long runs.

## Error Handling & Troubleshooting

### Common Issues
- **Timeout Errors**: If a page takes too long to load, increase the `timeout` parameter in the `goto` function.
- **Selector Mismatch**: If Beautylish updates their UI, selectors may fail. Check the logs to identify which field is returning `None`.
- **Proxy Authentication**: Ensure your `API_KEY` is valid and has remaining credits in the ScrapeOps dashboard.

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
- [Selenium - Product Data](./python/selenium/product_data/README.md)

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