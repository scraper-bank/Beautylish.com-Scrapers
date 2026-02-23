# Beautylish Product Search Scraper - Selenium (Python)

This automated scraper is designed to extract comprehensive product listings and search results from Beautylish using Python and Selenium. It features high-performance data extraction, integrated proxy support via ScrapeOps, and handles dynamic content loading to capture product details, search metadata, and category structures efficiently.

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

- **searchMetadata (object)**: Contains the search query, total results found, results displayed, and the source URL.
- **products (array)**: A collection of product items found on the search page including names, prices, and IDs.
- **breadcrumbs (null)**: Navigation path leading to the current search or category.
- **pagination (null)**: Information regarding total pages and current page state.
- **recommendations (null)**: Suggested products based on the search intent.
- **relatedSearches (null)**: Alternative search terms related to the current query.
- **sponsoredProducts (null)**: List of promoted or advertisement-based product entries.

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
cd python/selenium/product_search
```

2. Edit the URLs in `scraper/beautylish_scraper_product_search_v1.py`:

```python
# In beautylish_scraper_product_search_v1.py
url = "https://example.com/product"
```

3. Run the scraper:

```bash
python beautylish_scraper_product_search_v1.py
```

The scraper will generate a timestamped JSONL file (e.g., `Beautylish_com_product_search_page_scraper_data_20260114_120000.jsonl`) containing all extracted data.

### Example Output

See `example-data/product_search.json` for a sample of the extracted data structure.

## Supported URLs

The scraper supports the following URL patterns:

- `https://www.beautylish.com`
- `https://www.beautylish.com/shop/browse?q={query}`
- `https://www.beautylish.com/shop/browse?utm_source=internal_search&utm_campaign=Search+Beautylish+Products&q=hair+shampoo`

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
| `breadcrumbs` | null | null value |
| `pagination` | null | null value |
| `products` | array | Array |
| `recommendations` | null | null value |
| `relatedSearches` | null | null value |
| `searchMetadata` | object | Object containing nested fields |
| `sponsoredProducts` | null | null value |

### Field Descriptions

- **breadcrumbs** (null): Navigation links showing the category hierarchy.
- **pagination** (null): Details about the current page, total pages, and next/previous links.
- **products** (array): Contains a list of items found in the search results.
- **recommendations** (null): Products suggested by the site algorithm.
- **relatedSearches** (null): List of terms users also searched for.
- **searchMetadata** (object): Contains nested data regarding the search execution (query, count, etc).
- **sponsoredProducts** (null): Paid placements appearing in the search results.

**Field Details:**
The `searchMetadata` object includes `query` (string), `totalResults` (integer), and `searchUrl` (string). The `products` array contains individual objects representing each product card found on the page.

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

The scraper utilizes **Selenium** with `undetected_chromedriver` to simulate a real user browsing Beautylish. It initializes a headless browser instance and navigates to the specified search URL. To bypass common detection, it uses `selenium-wire` to route traffic through **ScrapeOps Residential Proxies**. 

Once the page loads, the script uses **WebDriverWait** to ensure dynamic content is rendered before extraction. It then parses the DOM using a combination of Selenium selectors and **BeautifulSoup** for efficient HTML processing. Finally, the data is validated via Python `dataclasses` and appended to a JSONL file through a thread-safe `DataPipeline`.

## Error Handling & Troubleshooting

- **Timeout Errors**: If the page fails to load, check your internet connection or increase the `WebDriverWait` timeout in the code.
- **Selector Failures**: Beautylish may update their site structure. If fields return null, inspect the page and update the CSS selectors in the script.
- **Rate Limiting**: If you receive 403 or 429 errors, ensure your ScrapeOps API key is valid and that you are using the residential proxy configuration.

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

This repository provides multiple implementations for scraping Beautylish Product Search pages:

### Python Implementations

- [BeautifulSoup - Product Search](./python/BeautifulSoup/product_search/README.md)
- [Playwright - Product Search](./python/playwright/product_search/README.md)

### Node.js Implementations

- [Cheerio - Product Search](./node/cheerio-axios/product_search/README.md)
- [Playwright - Product Search](./node/playwright/product_search/README.md)
- [Puppeteer - Product Search](./node/puppeteer/product_search/README.md)

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
- **Example Output**: See `example-data/product_search.json` for sample data structure
- **Scraper Code**: See `scraper/beautylish_scraper_product_search_v1.py` for implementation details

## License

This scraper is provided as-is for educational and commercial use. Please ensure compliance with Beautylish's Terms of Service and robots.txt when using this scraper.