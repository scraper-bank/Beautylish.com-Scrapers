# Beautylish Product Search Scraper - Cheerio (Node.js)

This expert-level Node.js scraper is designed to efficiently extract search result data from Beautylish using the Cheerio and Axios libraries. It leverages the ScrapeOps Proxy API to bypass anti-bot detections, allowing for seamless collection of product listings, search metadata, and category information from Beautylish search result pages.

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

- **Products (array)**: A comprehensive list of product items found in the search results.
- **Search Metadata (object)**: Details about the search execution, including the query string, result count, and search type.
- **Breadcrumbs**: Navigation path data for the current search context.
- **Pagination**: Information regarding multiple pages of results.
- **Recommendations**: Suggested products related to the search terms.
- **Related Searches**: Alternative search queries suggested by the site.
- **Sponsored Products**: Promoted items appearing within the search results.

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
cd node/cheerio-axios/product_search
```

2. Edit the URLs in `scraper/beautylish_scraper_product_search_v1.js`:

```javascript
// In beautylish_scraper_product_search_v1.js
const url = "https://example.com/product";
```

3. Run the scraper:

```bash
node beautylish_scraper_product_search_v1.js
```

The scraper will generate a timestamped JSONL file (e.g., `Beautylish_com_product_search_page_scraper_data_20260114_120000.jsonl`) containing all extracted data.

### Example Output

See `example-data/product_search.json` for a sample of the extracted data structure.

## Supported URLs

The scraper supports the following URL patterns:

- `https://www.beautylish.com`
- `https://www.beautylish.com/shop/browse?q=`
- `https://www.beautylish.com/shop/browse?q=[QUERY]`

Example URL: `https://www.beautylish.com/shop/browse?q=hair+shampoo`

## Configuration

### Scraper Parameters

The scraper supports several configuration options, including `maxRetries` for failed requests, `maxConcurrency` to control load, and `timeout` settings for network requests. See the scraper code for available parameters.

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
| `breadcrumbs` | null | Navigation path information (if available) |
| `pagination` | null | Pagination details for multi-page results |
| `products` | array | Array of product objects found on the page |
| `recommendations` | null | Suggested items based on search |
| `relatedSearches` | null | List of related search terms |
| `searchMetadata` | object | Object containing nested fields like query and total results |
| `sponsoredProducts` | null | List of advertisement products |

### Field Descriptions

- **breadcrumbs** (null): Currently returns null if no breadcrumb structure is detected on the search page.
- **pagination** (null): Contains page numbering and "next" link data when multiple result pages exist.
- **products** (array): Contains a list of items extracted from the search grid.
- **recommendations** (null): Extracted "you might also like" product data.
- **relatedSearches** (null): Strings or objects representing similar search terms.
- **searchMetadata** (object): Contains nested data regarding the search execution.
- **sponsoredProducts** (null): Data for products marked as "Sponsored" or "Ad".

**Field Details:**
The `searchMetadata` object specifically includes `query` (string), `resultsDisplayed` (integer), `searchType` (string), `searchUrl` (string), and `totalResults` (integer).

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

This scraper uses **Axios** to fetch the raw HTML content of Beautylish search pages and **Cheerio** to parse the HTML and extract data using CSS selectors. 

1. **Navigation**: The script constructs a target URL (usually a search query URL) and sends a request via the ScrapeOps Proxy gateway.
2. **Extraction**: Once the HTML is received, Cheerio loads the DOM. The scraper targets specific containers (like product grids) to pull product details.
3. **Data Processing**: The script cleans extracted strings (stripping HTML tags and trimming whitespace) and structures the data into a clean JSON format.
4. **Saving**: Data is streamed to a `.jsonl` file line-by-line to ensure memory efficiency.

## Error Handling & Troubleshooting

- **Empty Results**: If the `products` array is empty, check if the CSS selectors in the script still match the current Beautylish layout.
- **403 Forbidden**: This usually indicates anti-bot blocking. Ensure your ScrapeOps API key is valid and that the proxy configuration is active.
- **Timeout Errors**: Increase the `timeout` value in the `CONFIG` object if the site is responding slowly.

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

This repository provides multiple implementations for scraping Beautylish Product Search pages:

### Python Implementations

- [BeautifulSoup - Product Search](./python/BeautifulSoup/product_search/README.md)
- [Playwright - Product Search](./python/playwright/product_search/README.md)
- [Selenium - Product Search](./python/selenium/product_search/README.md)

### Node.js Implementations

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
- **Scraper Code**: See `scraper/beautylish_scraper_product_search_v1.js` for implementation details

## License

This scraper is provided as-is for educational and commercial use. Please ensure compliance with Beautylish's Terms of Service and robots.txt when using this scraper.