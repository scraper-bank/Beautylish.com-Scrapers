# Beautylish Product Category Scraper - Selenium (Python)

This Python-based scraper utilizes Selenium and Selenium-wire to extract comprehensive category and product listing data from Beautylish. It is designed to navigate product category pages, handle dynamic content, and integrate with ScrapeOps residential proxies to bypass anti-bot protections effectively.

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

- **appliedFilters (array)**: List of currently active filters including filter name and value.
- **bannerImage**: URL of the category header banner image (if available).
- **breadcrumbs**: Navigation path tracking the user's location on the site.
- **categoryId (string)**: The unique identifier for the category.
- **categoryName (string)**: The display name of the category (e.g., "Skincare").
- **categoryUrl (string)**: The direct URL of the scraped category page.
- **description**: The textual description of the category.
- **pagination**: Data regarding total pages and current page position.
- **products (array)**: List of product items found within the category.
- **subcategories (array)**: List of related sub-brands or sub-categories with their names and URLs.

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
cd python/selenium/product_category
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

- `https://www.beautylish.com/shop/browse?tag=[category-name]`
- `https://www.beautylish.com/brands`
- `https://www.beautylish.com/b/[brand-name]`

Examples:
- `https://www.beautylish.com/shop/browse?tag=skincare`
- `https://www.beautylish.com/shop/browse?tag=makeup`

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
| `appliedFilters` | array | Array of objects containing active filter metadata |
| `bannerImage` | null | URL string or null if no banner exists |
| `breadcrumbs` | null | Navigation hierarchy data |
| `categoryId` | string | Slug or ID of the category |
| `categoryName` | string | Human-readable category name |
| `categoryUrl` | string | The source URL |
| `description` | null | Category text description |
| `pagination` | null | Page navigation details |
| `products` | array | List of product objects |
| `subcategories` | array | List of objects with subcategory names and links |

### Field Descriptions

- **appliedFilters** (array): Contains a list of object items (filterName, filterValue)
- **bannerImage** (null): Usually a string URL, null if not present on page
- **breadcrumbs** (null): Structural path to the current page
- **categoryId** (string): e.g., "skincare"
- **categoryName** (string): e.g., "Skincare"
- **categoryUrl** (string): https://www.beautylish.com/shop/browse?tag=skincare
- **description** (null): Optional text describing the category collection
- **pagination** (null): Details about current page and total results
- **products** (array): Contains a list of items found in the grid
- **subcategories** (array): Contains a list of object items (name, productCount, url)

### Field Details
- **subcategories**: These objects typically include `name` (the brand or sub-type), `url` (the link to that specific section), and `productCount` (if displayed).
- **appliedFilters**: Useful for tracking which facets are currently modifying the product list results.

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

This scraper uses **Selenium** with `undetected_chromedriver` to simulate a real user session. 
1. **Initialization**: It sets up a WebDriver instance using `selenium-wire` to allow proxy injection via ScrapeOps.
2. **Navigation**: The scraper visits the category URL and waits for the DOM to be fully rendered using `WebDriverWait`.
3. **Extraction**: It uses CSS selectors and BeautifulSoup to parse the page source. It specifically targets the category metadata, subcategory links (like "Chantecaille", "Good Molecules"), and the product grid.
4. **Data Processing**: Extracted data is structured into a `ScrapedData` dataclass.
5. **Persistence**: A `DataPipeline` ensures that duplicate categories aren't processed twice and saves the results into a `.jsonl` file.

## Error Handling & Troubleshooting

- **TimeoutErrors**: Occur if the page takes too long to load. Increase the `WebDriverWait` timeout in the code.
- **StaleElementReferenceException**: If the page refreshes during extraction, the script is designed to catch this and retry.
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

This repository provides multiple implementations for scraping Beautylish Product Category pages:

### Python Implementations

- [BeautifulSoup - Product Category](./python/BeautifulSoup/product_category/README.md)
- [Playwright - Product Category](./python/playwright/product_category/README.md)

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