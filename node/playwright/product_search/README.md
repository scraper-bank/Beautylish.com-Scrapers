# Beautylish Product Search Scraper - Playwright (Node.js)

This high-performance Node.js scraper leverages Playwright and ScrapeOps to efficiently extract search result data from Beautylish. It is designed to handle dynamic content, providing comprehensive access to product listings, metadata, and search specifics with built-in anti-bot integration.

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

- **Breadcrumbs**: Navigation hierarchy for the current search context.
- **Pagination**: Details regarding result pages and navigation.
- **Products (array)**: A comprehensive list of products including names, prices, and links.
- **Recommendations**: Alternative product suggestions based on the search.
- **Related Searches**: Linked search terms related to the current query.
- **Search Metadata**: Deep-dive info including the query string, total results found, and the search URL.
- **Sponsored Products**: Promoted items appearing within the search results.

## Quick Start

### Prerequisites

- Node.js 14 or higher
- pip package manager (for Python) or npm (for Node.js)

### Installation

1. Install required dependencies:

```bash
npm install playwright cheerio
```

2. Get your ScrapeOps API key from [https://scrapeops.io/app/register/ai-scraper](https://scrapeops.io/app/register/ai-scraper)

3. Update the API key in the scraper:

```javascript
const API_KEY = "YOUR-API-KEY";
```

### Running the Scraper

1. Navigate to the scraper directory:

```bash
cd node/playwright/product_search
```

2. Edit the URLs in `scraper/beautylish_scraper_product_search_v1.js`:

```javascript
// In beautylish_scraper_product_search_v1.js
const url = "https://www.beautylish.com/shop/browse?q=mascara";
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

- `https://www.beautylish.com/shop/browse?q=[QUERY]`
- `https://www.beautylish.com/search?q=[QUERY]`
- General Beautylish search result pages using the `q` parameter.

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
- Note: CAPTCHA challenges may occur depending on site behavior and cannot be guaranteed to be resolved automatically.

## Output Schema

The scraper outputs data in JSONL format (one JSON object per line). Each object contains:

| Field | Type | Description |
| :--- | :--- | :--- |
| `breadcrumbs` | null | Navigation path (null if not present) |
| `pagination` | null | Pagination details (null if not present) |
| `products` | array | List of product objects found in search results |
| `recommendations` | null | Suggested items (null if not present) |
| `relatedSearches` | null | List of related search terms (null if not present) |
| `searchMetadata` | object | Object containing nested fields like query and total results |
| `sponsoredProducts` | null | List of sponsored items (null if not present) |

### Field Descriptions

- **breadcrumbs** (null): See field details
- **pagination** (null): See field details
- **products** (array): Contains a list of items found on the search result page.
- **recommendations** (null): See field details
- **relatedSearches** (null): See field details
- **searchMetadata** (object): Contains nested data such as `query`, `totalResults`, and `searchUrl`.
- **sponsoredProducts** (null): See field details

### Field Details

**searchMetadata Object:**
- `query` (string): The search term used.
- `totalResults` (number): The total number of items matching the query.
- `searchUrl` (string): The full URL of the search page.

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

This scraper uses **Playwright** with the `playwright-extra` stealth plugin to navigate Beautylish. It functions as follows:
1. **Browser Initialization**: Launches a headless Chromium instance with stealth settings to mimic real human behavior.
2. **Proxy Integration**: Routes traffic through ScrapeOps residential proxies to prevent IP-based blocking.
3. **Navigation**: Loads the search result URL and waits for the DOM to settle.
4. **Extraction**: Uses **Cheerio** to parse the page HTML for maximum speed. It targets product grids, metadata containers, and pagination elements using CSS selectors.
5. **Data Processing**: Cleans price strings, resolves relative URLs to absolute links, and filters out duplicates using a `DataPipeline` class.
6. **Output**: Saves results incrementally into a `.jsonl` file to ensure data safety even if the process is interrupted.

## Error Handling & Troubleshooting

- **Timeout Errors**: If pages load slowly, increase the `timeout` value in the `CONFIG` object.
- **Proxy Issues**: Ensure your ScrapeOps API key is active and has remaining credits.
- **Empty Results**: Beautylish may update their CSS classes. Check the selectors in the extraction logic if `products` returns an empty array.
- **Rate Limiting**: If you encounter 429 errors, decrease the `maxConcurrency` in the config.

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

- [Cheerio - Product Search](./node/cheerio-axios/product_search/README.md)
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