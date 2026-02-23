# Beautylish Product Category Scraper - BeautifulSoup (Python)

This powerful Python scraper is designed to extract comprehensive category and product listing data from Beautylish using the BeautifulSoup framework. It efficiently captures category hierarchies, applied filters, and product metadata while leveraging ScrapeOps for robust proxy management and anti-bot circumvention.

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

- **appliedFilters (array)**: List of active filters including filter names and values.
- **bannerImage**: URL of the category header or banner image (if present).
- **breadcrumbs**: Navigation path leading to the current category.
- **categoryId**: Unique identifier for the specific category.
- **categoryName (string)**: The display name of the category (e.g., "Skincare").
- **categoryUrl (string)**: The full URL of the scraped category page.
- **description**: Textual description or SEO content for the category.
- **pagination**: Data regarding total pages and current page position.
- **products (array)**: List of product objects found within the category listing.
- **subcategories (array)**: List of related sub-sections, brands, or niche categories with their names and URLs.

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
cd python/beautifulsoup/product_category
```

2. Edit the URLs in `scraper/beautylish_scraper_product_category_v1.py`:

```python
# In beautylish_scraper_product_category_v1.py
url = "https://www.beautylish.com/shop/browse?tag=skincare"
```

3. Run the scraper:

```bash
python beautylish_scraper_product_category_v1.py
```

The scraper will generate a timestamped JSONL file (e.g., `Beautylish_com_product_category_page_scraper_data_20260114_120000.jsonl`) containing all extracted data.

### Example Output

See `example-data/product_category.json` for a sample of the extracted data structure.

## Supported URLs

The scraper supports the following URL patterns:

- `https://www.beautylish.com`
- `http://schema.org/Product`
- `https://proxy.scrapeops.io/v1/?`
- `https://www.beautylish.com/shop/browse?tag=skincare`

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
| `appliedFilters` | array | Array of objects containing filter metadata |
| `bannerImage` | null | URL of the category banner image |
| `breadcrumbs` | null | List of parent categories |
| `categoryId` | null | Unique internal ID for the category |
| `categoryName` | string | Name of the current category |
| `categoryUrl` | string | Full URL of the category page |
| `description` | null | Textual description of the category |
| `pagination` | null | Pagination metadata |
| `products` | array | List of products extracted from the grid |
| `subcategories` | array | List of nested category links |

### Field Descriptions

- **appliedFilters** (array): Contains a list of object items representing active search/browse tags.
- **bannerImage** (null): The hero image associated with the category page.
- **breadcrumbs** (null): Navigation links showing the site hierarchy.
- **categoryId** (null): The unique identifier used by the site's backend for this category.
- **categoryName** (string): Example: "Skincare"
- **categoryUrl** (string): Example: "https://www.beautylish.com/shop/browse?tag=skincare"
- **description** (null): The marketing text or summary for the category.
- **pagination** (null): Details about page numbers and total results.
- **products** (array): Contains a list of product items including names, prices, and ratings.
- **subcategories** (array): Contains a list of object items representing related links or brands.

### Field Details
Nested objects within `subcategories` typically include `name`, `url`, and `productCount` (where available). The `appliedFilters` list contains objects with `filterName` and `filterValue` keys.

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

The scraper follows a structured pipeline to extract data from Beautylish:
1. **Requesting**: It uses the `requests` library to fetch the HTML content of the category page. Requests are routed through the ScrapeOps Proxy API to ensure high delivery rates.
2. **Parsing**: It utilizes **BeautifulSoup** with the `lxml` or `html.parser` to navigate the DOM.
3. **Extraction**:
   - It identifies category metadata (name, URL) from the page header.
   - It iterates through the product grid to collect individual product details.
   - It extracts sidebar or header navigation to find `subcategories` and `appliedFilters`.
4. **Data Processing**: Using Python `dataclasses`, the scraper structures the raw HTML into clean, typed objects.
5. **Persistence**: A `DataPipeline` class handles deduplication and writes the data into a `.jsonl` file incrementally to prevent data loss.

## Error Handling & Troubleshooting

- **Missing Selectors**: If Beautylish updates its UI, extraction for specific fields may return `null`. Check the logs for warnings.
- **Connection Errors**: The scraper uses a retry mechanism. If errors persist, verify your ScrapeOps API key and remaining credits.
- **Duplicates**: The `DataPipeline` tracks `categoryUrl` to ensure the same page isn't processed twice in a single run.

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

This repository provides multiple implementations for scraping Beautylish Product Category pages:

### Python Implementations

- [Playwright - Product Category](./python/playwright/product_category/README.md)
- [Selenium - Product Category](./python/selenium/product_category/README.md)

### Node.js Implementations

- [Cheerio - Product Category](./node/cheerio-axios/product_category/README.md)
- [Playwright - Product Category](./node/playwright/product_category/README.md)
- [Puppeteer - Product Category](./node/puppeteer/product_category/README.md)

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

The scraper supports concurrent requests using `ThreadPoolExecutor`. See the scraper code for configuration options.

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
- **Example Output**: See `example-data/product_category.json` for sample data structure
- **Scraper Code**: See `scraper/beautylish_scraper_product_category_v1.py` for implementation details

## License

This scraper is provided as-is for educational and commercial use. Please ensure compliance with Beautylish's Terms of Service and robots.txt when using this scraper.