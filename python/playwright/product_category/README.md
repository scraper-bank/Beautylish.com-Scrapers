# Beautylish Product Category Scraper - Playwright (Python)

This specialized Python scraper allows you to extract comprehensive product listing data from Beautylish category and brand pages. Utilizing the Playwright framework for robust browser automation and ScrapeOps for proxy management, it efficiently captures product details, subcategory links, and pagination metadata to facilitate large-scale e-commerce data collection.

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

- **appliedFilters (array)**: List of active filters applied to the current view (e.g., tags, brands).
- **bannerImage (string/null)**: URL of the category header or banner image.
- **breadcrumbs (array/null)**: Navigation path leading to the current category.
- **categoryId (string)**: The internal identifier or slug for the category.
- **categoryName (string)**: The human-readable name of the category.
- **categoryUrl (string)**: The full canonical URL of the scraped category page.
- **description (string/null)**: The SEO or marketing description text for the category.
- **pagination (object)**: Includes current page, total pages, results per page, and next/previous page URLs.
- **products (array)**: List of product items found on the page, including names, prices, and links.
- **subcategories (array)**: List of related sub-categories or brands including their names and URLs.

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
cd python/playwright/product_category
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

- `https://www.beautylish.com/shop/browse?tag=[CATEGORY_NAME]`
- `https://www.beautylish.com/b/[BRAND_NAME]`
- `https://www.beautylish.com/shop/[CATEGORY_PATH]`

Example URL: `https://www.beautylish.com/shop/browse?tag=skincare`

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
| `appliedFilters` | array | List of objects containing `filterName` and `filterValue`. |
| `bannerImage` | null | URL of the category banner image if present. |
| `breadcrumbs` | null | Hierarchical navigation links for the category. |
| `categoryId` | string | Unique identifier for the category (e.g., "skincare"). |
| `categoryName` | string | Display name of the category. |
| `categoryUrl` | string | The absolute URL of the category page. |
| `description` | null | Textual description of the category or brand. |
| `pagination` | object | Nested object containing `currentPage`, `totalPages`, and navigation URLs. |
| `products` | array | Array of product objects extracted from the grid. |
| `subcategories` | array | Array of objects containing `name` and `url` for related links. |

### Field Descriptions

- **appliedFilters** (array): Contains a list of object items currently filtering the results.
- **bannerImage** (null): Placeholder for the top-level category hero image.
- **breadcrumbs** (null): List of parent categories.
- **categoryId** (string): The slug used in the URL or internal database (e.g., skincare).
- **categoryName** (string): The title shown at the top of the product grid.
- **categoryUrl** (string): The source URL for the data.
- **description** (null): The introductory text for the brand or category.
- **pagination** (object): Contains nested data regarding the result set size and page numbers.
- **products** (array): Contains a list of product items including titles, prices, and thumbnails.
- **subcategories** (array): Contains a list of object items representing sidebar or filter links.

### Field Details
The `pagination` object includes:
- `currentPage`: Integer
- `totalPages`: Integer or null if unknown
- `nextPageUrl`: String or null

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

This scraper uses **Playwright** for browser automation, which is essential for Beautylish as the site relies on JavaScript to render product grids and manage dynamic filtering. 

1. **Initialization**: The script launches a headless browser and applies `playwright_stealth` to mask the automation signature.
2. **Navigation**: It navigates to the provided category URL using ScrapeOps Residential Proxies to avoid IP-based blocking.
3. **Extraction**: Once the page is loaded, it uses CSS selectors and regex to parse the HTML. It specifically targets the category metadata, the list of subcategories, and the product data objects.
4. **Data Normalization**: Functions like `make_absolute_url` ensure all relative links are converted to full URLs, and `strip_html` cleans up any text content.
5. **Deduplication**: The `DataPipeline` class checks for duplicate entries before saving to ensure data integrity.
6. **Output**: Extracted items are saved line-by-line into a JSONL file, which is memory-efficient for large category crawls.

## Error Handling & Troubleshooting

If the scraper fails to find products or categories:
- **Selector Changes**: Beautylish may update their class names. Check the logs to see if extraction is returning empty values.
- **Proxy Issues**: Ensure your `API_KEY` is valid and you have remaining credits in your ScrapeOps account.
- **Timeouts**: Some category pages with many products may take longer to load; increase the Playwright `timeout` parameter if necessary.

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

- [BeautifulSoup - Product Category](./python/BeautifulSoup/product_category/README.md)
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
- **Example Output**: See `example-data/product_category.json` for sample data structure
- **Scraper Code**: See `scraper/beautylish_scraper_product_category_v1.py` for implementation details

## License

This scraper is provided as-is for educational and commercial use. Please ensure compliance with Beautylish's Terms of Service and robots.txt when using this scraper.