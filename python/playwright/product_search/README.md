# Beautylish Product Search Scraper - Playwright (Python)

Beautylish Product Search Scraper is a robust data extraction tool developed in Python using the Playwright framework. It is specifically designed to navigate Beautylish search result pages, handle dynamic content through browser automation, and extract comprehensive product listings into structured JSONL format.

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

- **searchMetadata**: Information about the search execution including the query, total results found, and the search URL.
- **products**: A detailed list of products containing:
    - Product Name (string)
    - Price (number) and Currency (string)
    - Brand (string)
    - Product URL (string)
    - Availability status (string)
    - Image URLs (array)
    - Product ID and Category (string)
    - Ratings and Review counts
    - Features and Specifications (arrays)
- **breadcrumbs**: Navigation path data (if available).
- **pagination**: Details on current page and total pages (if available).
- **recommendations**: Suggested items related to the search.
- **relatedSearches**: Alternative search terms suggested by the site.
- **sponsoredProducts**: List of promoted items within the search results.

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
cd python/playwright/product_search
```

2. Edit the URLs in `scraper/beautylish_scraper_product_search_v1.py`:

```python
# In beautylish_scraper_product_search_v1.py
url = "https://www.beautylish.com/shop/browse?q=hair+shampoo"
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
- `https://www.beautylish.com/shop/browse?q=[QUERY]`
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
| `products` | array | Array of product objects |
| `recommendations` | null | null value |
| `relatedSearches` | null | null value |
| `searchMetadata` | object | Object containing nested fields like query and totalResults |
| `sponsoredProducts` | null | null value |

### Field Descriptions

- **breadcrumbs** (null): Navigation hierarchy for the current page.
- **pagination** (null): Information regarding the result pages.
- **products** (array): Contains a list of items found in the search results.
- **recommendations** (null): Items suggested by the Beautylish engine.
- **relatedSearches** (null): List of similar keywords.
- **searchMetadata** (object): Contains nested data regarding the search parameters used.
- **sponsoredProducts** (null): List of paid product placements.

### Field Details
The `products` array contains detailed objects including `name`, `price`, `brand`, and `productId`. The `searchMetadata` object includes `query` (the string searched) and `searchUrl`.

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

The scraper utilizes **Playwright** to launch a headless browser instance. It navigates to the Beautylish search URL and applies `stealth_async` to minimize detection by anti-bot systems. Once the page is loaded, it executes JavaScript or uses CSS selectors to locate product containers. The data is parsed into Python `dataclasses` (`Product` and `ScrapedData`), ensuring type safety and consistency. Finally, the `DataPipeline` class handles deduplication and streams the results into a JSONL file to conserve memory.

## Error Handling & Troubleshooting

- **Timeout Errors**: If the page fails to load, increase the `timeout` parameter in the Playwright `goto` function.
- **Empty Results**: This often happens if selectors have changed. Check if Beautylish has updated their HTML class names.
- **Proxy Issues**: Ensure your ScrapeOps API key is valid and you have remaining credits.

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
- [Selenium - Product Search](./python/selenium/product_search/README.md)

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