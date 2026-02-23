# Beautylish Product Data Scraper - Cheerio (Node.js)

The Beautylish Product Data Scraper is a high-performance Node.js tool designed to extract comprehensive product information from Beautylish.com. Utilizing the Cheerio and Axios libraries, it efficiently parses HTML to capture details like pricing, reviews, and specifications. It features built-in ScrapeOps integration to optimize request delivery and bypass common scraping hurdles.

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

- **Product Identity**: Name (string), Product ID (string), and Brand (string)
- **Pricing & Availability**: Current Price (number), Currency (string), and Stock Availability (string)
- **Content**: Full Description (HTML/string), Features (array of strings), and Videos (array)
- **Media**: Product Images (array of objects with URLs)
- **Social Proof**: Aggregate Rating (object with rating value and review count) and Reviews (array)
- **Technical Details**: Specifications (array of objects) and Serial Numbers (array)
- **Context**: Category (string/null), Seller Information (object), and Source URL (string)

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
cd node/cheerio-axios/product_data
```

2. Edit the URLs in `scraper/beautylish_scraper_product_data_v1.js`:

```javascript
// In beautylish_scraper_product_data_v1.js
const url = "https://www.beautylish.com/s/vital-proteins-vanilla-collagen-creamer-10-6-oz";
```

3. Run the scraper:

```bash
node beautylish_scraper_product_data_v1.js
```

The scraper will generate a timestamped JSONL file (e.g., `Beautylish_com_product_data_page_scraper_data_20260114_120000.jsonl`) containing all extracted data.

### Example Output

See `example-data/product_data.json` for a sample of the extracted data structure.

## Supported URLs

The scraper supports the following URL patterns:

- Product Pages: `https://www.beautylish.com/s/[product-slug]`
- Proxy Wrapped URLs: `https://proxy.scrapeops.io/v1/?...`

Examples:
- `https://www.beautylish.com/s/vital-proteins-vanilla-collagen-creamer-10-6-oz`

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
| `aggregateRating` | object | Object containing nested fields |
| `availability` | string | String value |
| `brand` | string | String value |
| `category` | null | null value |
| `currency` | string | String value |
| `description` | string | String value |
| `features` | array | Array of strings |
| `images` | array | Array of objects |
| `name` | string | String value |
| `preDiscountPrice` | null | null value |
| `price` | integer | Numeric value |
| `productId` | string | String value |
| `reviews` | array | Array |
| `seller` | object | Object containing nested fields |
| `serialNumbers` | array | Array |
| `specifications` | array | Array of objects |
| `url` | string | String value |
| `videos` | array | Array |

### Field Descriptions

- **aggregateRating** (object): Contains nested data including `ratingValue` and `reviewCount`.
- **availability** (string): Current stock status (e.g., "in_stock").
- **brand** (string): The manufacturer or brand name (e.g., Vital Proteins).
- **category** (null): Product category (if available).
- **currency** (string): The ISO currency code (e.g., USD).
- **description** (string): Detailed HTML or text product description.
- **features** (array): List of key product highlights or benefits.
- **images** (array): List of image objects containing URLs.
- **name** (string): Full product title.
- **preDiscountPrice** (null): Original price before any discounts.
- **price** (integer): Current selling price.
- **productId** (string): Unique identifier slug for the product.
- **reviews** (array): List of individual user reviews.
- **seller** (object): Details regarding the merchant or shipping entity.
- **serialNumbers** (array): List of identifiers like UPC or EAN.
- **specifications** (array): Technical details like size, weight, or ingredients.
- **url** (string): The canonical URL of the product page.
- **videos** (array): List of related video content URLs.

### Field Details
- **aggregateRating**: Includes `bestRating`, `ratingValue`, `reviewCount`, and `worstRating`.
- **specifications**: Typically contains objects with `label` and `value` keys.
- **images**: Contains absolute URLs to product photography.

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

The scraper follows a structured pipeline to ensure data integrity and performance:
1. **Network Layer**: Uses `Axios` to send HTTP GET requests. Requests are routed through the ScrapeOps Proxy API to manage IP rotation and headers.
2. **Parsing Layer**: Loads the returned HTML into `Cheerio`. It uses CSS selectors to locate structured data within the page.
3. **Data Extraction**: The `extractData` function maps HTML elements to a structured JSON object, converting relative URLs to absolute ones and cleaning up text strings.
4. **Data Pipeline**: Extracted items pass through a `DataPipeline` class which checks for duplicates using the `productId`.
5. **Storage**: Validated data is appended line-by-line to a `.jsonl` file to ensure low memory consumption even during large crawls.

## Error Handling & Troubleshooting

- **Empty Fields**: If a selector returns no data, ensure the Beautylish layout hasn't changed.
- **403/401 Errors**: Check if your ScrapeOps API key is valid and has remaining credits.
- **Timeout Errors**: Increase the `timeout` value in the `CONFIG` object if the network is slow.
- **Duplicate Prevention**: The scraper uses a `Set` to track `productId`s; if you restart the scraper, the set clears unless you implement a persistent cache.

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

This repository provides multiple implementations for scraping Beautylish Product Data pages:

### Python Implementations

- [BeautifulSoup - Product Data](./python/BeautifulSoup/product_data/README.md)
- [Playwright - Product Data](./python/playwright/product_data/README.md)
- [Selenium - Product Data](./python/selenium/product_data/README.md)

### Node.js Implementations

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
- **Scraper Code**: See `scraper/beautylish_scraper_product_data_v1.js` for implementation details

## License

This scraper is provided as-is for educational and commercial use. Please ensure compliance with Beautylish's Terms of Service and robots.txt when using this scraper.