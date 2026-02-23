# Beautylish Product Category Scraper - Cheerio (Node.js)

Automate the extraction of organized product lists and navigational data from Beautylish category pages using Node.js and Cheerio. This high-performance scraper efficiently captures subcategories, filter metadata, and category hierarchies by leveraging axios for requests and ScrapeOps for proxy management to ensure reliable data collection.

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

- **appliedFilters (array)**: List of currently active filters including filter names and values.
- **bannerImage (null)**: The URL of the category header image if available.
- **breadcrumbs (null)**: Navigation path leading to the current category.
- **categoryId (string)**: Unique identifier for the category (e.g., "skincare").
- **categoryName (string)**: Human-readable name of the category.
- **categoryUrl (string)**: The direct canonical URL of the category page.
- **description (null)**: SEO or display description text for the category.
- **pagination (null)**: Information about total pages and current page position.
- **products (null)**: List of product items found within the category.
- **subcategories (array)**: Nested navigation links including sub-brand names and URLs.

## Quick Start

### Prerequisites

- Node.js 14 or higher
- pip package manager (for Python) or npm (for Node.js)

### Installation

1. Install required dependencies:

```bash
npm install cheerio axios
```

2. Get your ScrapeOps API key from [https://scrapeops.io/app/register/ai-scraper](https://scrapeops.io/app/register/ai-scraper)

3. Update the API key in the scraper:

```javascript
const API_KEY = "YOUR-API-KEY";
```

### Running the Scraper

1. Navigate to the scraper directory:

```bash
cd node/cheerio-axios/product_category
```

2. Edit the URLs in `scraper/beautylish_scraper_product_category_v1.js`:

```javascript
// In beautylish_scraper_product_category_v1.js
const url = "https://example.com/product";
```

3. Run the scraper:

```bash
node beautylish_scraper_product_category_v1.js
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

Example URL: `https://proxy.scrapeops.io/v1/?`

## Configuration

### Scraper Parameters

The scraper supports several configuration options. See the scraper code for available parameters.

### ScrapeOps Configuration

The scraper can use ScrapeOps for anti-bot protection and request optimization:

```javascript
// ScrapeOps proxy configuration
const proxyUrl = `https://proxy.scrapeops.io/v1/?api_key=${API_KEY}`;
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
| `appliedFilters` | array | Array of objects |
| `bannerImage` | null | null value |
| `breadcrumbs` | null | null value |
| `categoryId` | string | String value |
| `categoryName` | string | String value |
| `categoryUrl` | string | String value |
| `description` | null | null value |
| `pagination` | null | null value |
| `products` | null | null value |
| `subcategories` | array | Array of objects |

### Field Descriptions

- **appliedFilters** (array): Contains a list of object items
- **bannerImage** (null): The category banner image URL if present.
- **breadcrumbs** (null): Array of navigation links.
- **categoryId** (string): skincare
- **categoryName** (string): Skincare
- **categoryUrl** (string): https://www.beautylish.com/shop/browse?tag=skincare
- **description** (null): Textual description of the category.
- **pagination** (null): Object containing page count and current page.
- **products** (null): Array of product objects.
- **subcategories** (array): Contains a list of object items

### Field Details
- **subcategories**: An array of objects, each containing `name` (string) and `url` (string) of related brands or sub-sections.
- **appliedFilters**: An array of objects containing `filterName` and `filterValue` used to generate the current view.

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

This scraper uses **Axios** to fetch the HTML content of Beautylish category pages and **Cheerio** to parse the DOM. It follows a structured workflow:
1. **Requesting**: It sends a GET request via the ScrapeOps Proxy API to bypass basic IP restrictions.
2. **Parsing**: Cheerio loads the HTML, and the script uses CSS selectors to locate category metadata, subcategory lists, and filter information.
3. **Cleaning**: It includes helper functions like `stripHTML` to clean up text and `detectCurrency` to normalize pricing data if present.
4. **Data Pipeline**: Extracted items are passed through a `DataPipeline` class which checks for duplicates before appending the result as a new line in a `.jsonl` file.
5. **Concurrency**: It is configured for controlled concurrency to avoid overwhelming the target server.

## Error Handling & Troubleshooting

- **403 Forbidden**: This usually indicates that the anti-bot protection has flagged the request. Ensure your ScrapeOps API key is active and try increasing `maxRetries`.
- **Selector Mismatch**: If fields return `null`, Beautylish may have updated their layout. Inspect the page and update the selectors in the scraper code.
- **Network Timeouts**: If the connection drops, adjust the `timeout` setting in the `CONFIG` object.

### Debugging

Enable detailed logging:

```javascript
// Enable debug logging
console.log('Debug mode enabled');
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
- [Selenium - Product Category](./python/selenium/product_category/README.md)

### Node.js Implementations

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
- **Scraper Code**: See `scraper/beautylish_scraper_product_category_v1.js` for implementation details

## License

This scraper is provided as-is for educational and commercial use. Please ensure compliance with Beautylish's Terms of Service and robots.txt when using this scraper.