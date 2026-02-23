# Beautylish Product Data Scraper - Puppeteer (Node.js)

The Beautylish Product Data Scraper is a robust web scraping solution designed to extract comprehensive product information from Beautylish.com. Built with Node.js and the Puppeteer framework, it features stealth browser automation and integrated proxy support to efficiently collect data like pricing, reviews, and detailed specifications.

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

- **Product Name (string)**: The full title of the product.
- **Brand (string)**: The manufacturer or brand name.
- **Price (number)**: The current selling price in USD.
- **Availability (string)**: Current stock status (e.g., "in_stock").
- **Description (string)**: Detailed product description including HTML formatting.
- **Aggregate Rating (object)**: Nested data including rating value and review count.
- **Images (array)**: A list of product image objects and URLs.
- **Features (array)**: Key product highlights and benefits.
- **Specifications (array)**: Technical details and product attributes.
- **Product ID (string)**: The unique identifier/slug for the product.
- **Reviews (array)**: User-submitted reviews and ratings.
- **Seller (object)**: Information about the product vendor.
- **Serial Numbers (array)**: GTIN, MPN, or SKU information if available.
- **URL (string)**: The source canonical URL of the product page.

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
cd node/puppeteer/product_data
```

2. Edit the URLs in `scraper/beautylish_scraper_product_data_v1.js`:

```javascript
// In beautylish_scraper_product_data_v1.js
const url = "https://example.com/product";
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

- `https://www.beautylish.com`
- `https://www.beautylish.com/s/vital-proteins-vanilla-collagen-creamer-10-6-oz`

Example URL: `https://www.beautylish.com/s/vital-proteins-vanilla-collagen-creamer-10-6-oz`

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
| `videos` | null | null value |

### Field Descriptions

- **aggregateRating** (object): Contains nested data
- **availability** (string): in_stock
- **brand** (string): Vital Proteins
- **category** (null): The product category path (if available)
- **currency** (string): USD
- **description** (string): Text content (truncated)
- **features** (array): Contains a list of string items
- **images** (array): Contains a list of object items
- **name** (string): Vital Proteins Vanilla Collagen Creamer 10.6 oz
- **preDiscountPrice** (null): Original price before discounts
- **price** (integer): The current numerical price
- **productId** (string): vital-proteins-vanilla-collagen-creamer-10-6-oz
- **reviews** (array): Contains a list of items
- **seller** (object): Contains nested data
- **serialNumbers** (array): Contains a list of items
- **specifications** (array): Contains a list of object items
- **url** (string): https://www.beautylish.com/s/vital-proteins-vanilla-collagen-creamer-10-6-oz
- **videos** (null): Video links associated with the product

### Field Details

- **aggregateRating**: Includes `ratingValue` (e.g., 4) and `reviewCount`.
- **specifications**: Array of objects containing key-value pairs for product attributes.
- **images**: List of objects containing image URLs and metadata.

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

The scraper uses **Puppeteer** to launch a headless browser, which is essential for handling any JavaScript-rendered content on Beautylish. To avoid detection, it utilizes the `puppeteer-extra-plugin-stealth`. 

1. **Navigation**: The scraper visits the provided product URL using Puppeteer.
2. **Extraction**: Once the page is loaded, the HTML is passed to **Cheerio** for fast and efficient parsing of structured data using CSS selectors.
3. **Processing**: The `extractData` function maps HTML elements to the JSON schema, handling complex structures like nested ratings and feature lists.
4. **Data Pipeline**: Extracted items are passed through a `DataPipeline` class which checks for duplicates and saves the data to a `.jsonl` file in real-time.
5. **Proxy Support**: All requests are routed through ScrapeOps Residential Proxies to ensure high success rates.

## Error Handling & Troubleshooting

- **Timeout Errors**: If the page fails to load within the `CONFIG.timeout` period, try increasing the timeout value or reducing concurrency.
- **Selector Failures**: If Beautylish updates its website layout, the extraction logic in `extractData` may need adjustment.
- **Proxy Issues**: Ensure your ScrapeOps API key is active and has remaining credits.
- **Rate Limiting**: If you encounter 429 errors, increase the delay between requests or lower the `maxConcurrency`.

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

- [Cheerio - Product Data](./node/cheerio-axios/product_data/README.md)
- [Playwright - Product Data](./node/playwright/product_data/README.md)

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