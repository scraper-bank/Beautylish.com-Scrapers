# Beautylish Product Data Scraper - BeautifulSoup (Python)

This powerful Python scraper is designed to extract comprehensive product information from Beautylish using the BeautifulSoup framework. It efficiently captures detailed product specifications, pricing, availability, and media assets, utilizing ScrapeOps for optimized request handling and anti-bot bypass.

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

- **Product Identity**: Name (string), Brand (string), and Product ID (string/null)
- **Pricing & Availability**: Current Price (number), Pre-discount Price (number/null), Currency (string), and Availability status (string)
- **Content**: Product Description (HTML/string) and Category (string/null)
- **Media**: Images (array of objects with URLs) and Videos (array)
- **Ratings & Reviews**: Aggregate Rating (object containing rating value and review count) and detailed Reviews list (array)
- **Product Details**: Features (array of strings), Specifications (array of objects), and Serial Numbers (array)
- **Metadata**: Product URL and Seller information (object)

## Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager (for Python) or npm (for Node.js)

### Installation

1. Install required dependencies:

```bash
pip install -r requirements.txt
```

2. Get your ScrapeOps API key from [https://scrapeops.io/app/register/ai-scraper](https://scrapeops.io/app/register/ai-scraper)

3. Update the API key in the scraper:

```python
API_KEY = "YOUR-API-KEY"
```

### Running the Scraper

1. Navigate to the scraper directory:

```bash
cd python/beautifulsoup/product_data
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

- `https://www.beautylish.com/s/[product-slug]`
- `https://www.beautylish.com`

**Example Valid URL:**
`https://www.beautylish.com/s/vital-proteins-vanilla-collagen-creamer-10-6-oz`

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
| `currency` | string | Three-letter ISO currency code |
| `description` | string | Detailed product description, often containing HTML |
| `features` | array | Array of key product feature strings |
| `images` | array | Array of objects containing image URLs |
| `name` | string | Full product title |
| `preDiscountPrice` | null | Original price before any discounts |
| `price` | integer | Current selling price |
| `productId` | null | Unique identifier for the product |
| `reviews` | array | List of individual customer reviews |
| `seller` | object | Details about the product merchant |
| `serialNumbers` | array | List of relevant serial or identification numbers |
| `specifications` | array | Array of key-value objects for product specs |
| `url` | string | The source URL of the product page |
| `videos` | array | List of associated video content |

### Field Descriptions

- **aggregateRating** (object): Contains nested data including `ratingValue` and `reviewCount`.
- **availability** (string): Current stock status, typically "in_stock".
- **brand** (string): Brand name, e.g., "Vital Proteins".
- **category** (null): Currently returns null; can be mapped if category breadcrumbs are present.
- **currency** (string): Currency used for the price, e.g., "USD".
- **description** (string): Full HTML or text description of the product.
- **features** (array): Contains a list of string items highlighting product benefits.
- **images** (array): List of image objects including source URLs.
- **name** (string): The display name of the product.
- **preDiscountPrice** (null): The price before discount (if available).
- **price** (integer): The current numerical price.
- **productId** (null): Internal unique ID (if available in metadata).
- **reviews** (array): A collection of user-submitted reviews.
- **seller** (object): Information about the entity selling the product.
- **serialNumbers** (array): Identifiers like GTIN or MPN.
- **specifications** (array): Technical details like size, weight, or ingredients.
- **url** (string): The canonical URL of the scraped product.
- **videos** (array): Links to product demonstrations or promotional videos.

### Field Details
- **aggregateRating**: Includes `bestRating` and `worstRating` fields which are often null unless specified by the site's schema.
- **description**: This field preserves HTML tags like `<h5>` and `<ul>` to maintain formatting during data processing.

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

This scraper uses **Python** and **BeautifulSoup** to perform static HTML parsing. 
1. **Navigation**: It initializes a request to the provided Beautylish URL through the ScrapeOps Proxy API.
2. **Extraction**: Once the HTML is retrieved, it uses BeautifulSoup (BS4) to locate specific CSS selectors and regex patterns to find product data. It specifically looks for structured data (like JSON-LD) and standard HTML tags.
3. **Processing**: Extracted data is cleaned using helper functions like `strip_html` and `make_absolute_url`.
4. **Storage**: The `DataPipeline` class handles de-duplication and saves the results incrementally to a JSONL file.
5. **Concurrency**: It utilizes `ThreadPoolExecutor` to handle multiple product URLs simultaneously, significantly increasing throughput.

## Error Handling & Troubleshooting

### Troubleshooting
- **Empty Fields**: If fields like `price` are missing, Beautylish may have changed their HTML structure or the product may be out of stock/discontinued.
- **Rate Limiting**: If you receive 403 or 429 errors, ensure your ScrapeOps API key is valid and consider reducing concurrency.
- **Connection Errors**: Check your internet connection and ensure the ScrapeOps proxy URL is correctly formatted.

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

- [Playwright - Product Data](./python/playwright/product_data/README.md)
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