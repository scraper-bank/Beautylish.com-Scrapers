# Beautylish Product Category Scraper - Puppeteer (Node.js)

This specialized Beautylish scraper is designed to efficiently extract structured data from product category and browse pages. Built with Node.js and Puppeteer, it features stealth integration to navigate category hierarchies, capturing subcategory links and product metadata while bypassing common bot detection.

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

- **Category Metadata**: Name (string), ID (string), and Source URL (string)
- **Subcategories**: A detailed list of nested categories including names and URLs (array of objects)
- **Product List**: Array of products found on the category page (array)
- **Navigation Data**: Applied filters (array), breadcrumbs, and pagination info
- **Media**: Category banner images (string/null)
- **Descriptions**: Category-specific SEO text or descriptions (string/null)

## Quick Start

### Prerequisites

- Node.js 14 or higher
- pip package manager (for Python) or npm (for Node.js)

### Installation

1. Install required dependencies:

```bash
npm install puppeteer cheerio
```

2. Get your ScrapeOps API key from [https://scrapeops.io/app/register/ai-scraper](https://scrapeops.io/app/register/ai-scraper)

3. Update the API key in the scraper:

```javascript
const API_KEY = "YOUR-API-KEY";
```

### Running the Scraper

1. Navigate to the scraper directory:

```bash
cd node/puppeteer/product_category
```

2. Edit the URLs in `scraper/beautylish_scraper_product_category_v1.js`:

```javascript
// In beautylish_scraper_product_category_v1.js
const url = "https://www.beautylish.com/shop/browse?tag=skincare";
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
- `https://www.beautylish.com/shop/browse?tag=skincare`
- General Beautylish brand and tag-based browse pages.

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
| `appliedFilters` | array | Array of currently active filters |
| `bannerImage` | null | URL of the category header image |
| `breadcrumbs` | null | Navigation path to the current category |
| `categoryId` | string | Unique identifier for the category |
| `categoryName` | string | The display name of the category (e.g., Skincare) |
| `categoryUrl` | string | The full URL of the category page |
| `description` | null | Text description of the category |
| `pagination` | null | Information about total pages and current page |
| `products` | array | List of product objects found on the page |
| `subcategories` | array | Array of objects containing subcategory names and URLs |

### Field Descriptions

- **appliedFilters** (array): Contains a list of items currently filtering the view.
- **bannerImage** (null): The hero image associated with the category (if available).
- **breadcrumbs** (null): Hierarchy list showing the path from Home to the current page.
- **categoryId** (string): Internal ID used by the site for this specific tag or category.
- **categoryName** (string): Human-readable name (e.g., "Skincare").
- **categoryUrl** (string): The canonical URL being scraped.
- **description** (null): Marketing or SEO text found at the top or bottom of the page.
- **products** (array): A collection of product items, including titles and prices.
- **subcategories** (array): A list of related sub-sections (e.g., "Chantecaille", "Good Molecules").

### Field Details
- **subcategories**: Each item in this array is an object containing `name` (string), `url` (string), and `productCount` (number/null).

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

This scraper uses **Puppeteer** combined with the **Stealth Plugin** to launch a headless browser instance that mimics real user behavior. 
1. **Navigation**: It opens the target Beautylish category URL and waits for the DOM to load.
2. **Content Extraction**: Once loaded, the HTML content is passed to **Cheerio** for fast, synchronous parsing of the DOM tree.
3. **Data Mapping**: It targets specific CSS selectors to extract category names, subcategory links, and product lists.
4. **Absolute URLs**: A helper function ensures all relative links (like `/b/brand-name`) are converted to absolute URLs.
5. **Persistence**: Extracted data passes through a `DataPipeline` class which checks for duplicates and saves the result as a JSONL line to the local file system.

## Error Handling & Troubleshooting

- **Timeout Errors**: If the page fails to load within 180 seconds, the scraper will retry based on `CONFIG.maxRetries`.
- **Selector Changes**: If `categoryName` or `subcategories` return empty, Beautylish may have updated their class names. Check the `extractData` function.
- **Proxy Issues**: Ensure your ScrapeOps API key is valid if you encounter 403 Forbidden errors.

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

- [Cheerio - Product Category](./node/cheerio-axios/product_category/README.md)
- [Playwright - Product Category](./node/playwright/product_category/README.md)

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