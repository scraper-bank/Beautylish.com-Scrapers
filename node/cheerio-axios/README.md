# Beautylish Scrapers - Cheerio (Node.js)

Efficiently extract product information, search results, and category data from Beautylish using this high-performance Node.js scraping suite powered by Cheerio and Axios. These scrapers are designed to handle high-volume data extraction with minimal overhead.

## Overview

This directory contains Node.js scrapers built with **Cheerio**.

## Available Scrapers

- [Product Category](./product_category/README.md)
- [Product Data](./product_data/README.md)
- [Product Search](./product_search/README.md)

## Why Cheerio?

Cheerio is the industry standard for high-speed HTML parsing in the Node.js ecosystem. Unlike browser-based tools like Puppeteer or Playwright, Cheerio does not incur the overhead of a full browser engine, making it significantly faster and more resource-efficient for static HTML pages.

**Key Features and Capabilities:**
- **Blazing Performance**: By operating directly on the HTML source code, Cheerio processes pages orders of magnitude faster than headless browsers.
- **jQuery Syntax**: It implements a subset of core jQuery, providing a familiar and powerful API for selecting and manipulating DOM elements.
- **Low Resource Footprint**: Ideal for large-scale scraping projects where CPU and memory usage are critical constraints.
- **Seamless Integration**: Works perfectly with Axios for HTTP requests, allowing for precise control over headers, timeouts, and proxy configurations.

**When to use this stack:**
This stack is best suited for scenarios where the target content is present in the initial HTML source. It is the preferred choice for high-volume scraping of Beautylish product listings and metadata where performance and cost-efficiency are the primary goals.

## Prerequisites

- **Node.js**: Node.js 14 or higher
- **npm**: npm
- **ScrapeOps API Key**: For anti-bot protection (free tier available)

## Installation

1. Navigate to the specific scraper directory:
```bash
cd product_category  # or product_data, product_search
```

2. Install dependencies:
```bash
npm install cheerio axios
```

3. Get your ScrapeOps API key from [https://scrapeops.io/app/register/ai-scraper](https://scrapeops.io/app/register/ai-scraper)

4. Update the API key in the scraper file:
```node
API_KEY = 'YOUR-API-KEY'
```

## Anti-Bot Protection

All scrapers can integrate with **ScrapeOps** to help handle Beautylish's anti-bot measures:
- Proxy rotation (may help reduce IP blocking)
- Request header optimization (can help reduce detection)
- Rate limiting management

**Note**: Anti-bot measures vary by site and may change over time. CAPTCHA challenges may occur and cannot be guaranteed to be resolved automatically. Using proxies and browser automation can help reduce blocking, but effectiveness depends on the target site's specific anti-bot measures.

**Free Tier Available**: ScrapeOps offers a generous free tier perfect for testing and small-scale scraping.

## Output Format

All scrapers output data in **JSONL format** (one JSON object per line):
- Each line represents one product/result
- Efficient for large datasets
- Easy to process line-by-line
- Can be imported into databases or data processing tools

Example output files:
- `beautylish_com_product_category_page_scraper_data_20260114_120000.jsonl`
- `beautylish_com_product_page_scraper_data_20260114_120000.jsonl`
- `beautylish_com_product_search_page_scraper_data_20260114_120000.jsonl`

## Alternative Implementations

This repository provides multiple implementations for different use cases:

### Node.js Alternatives
- [Puppeteer (Node.js)](../puppeteer/README.md)
- [Playwright (Node.js)](../playwright/README.md)

### Python Alternatives
- [Selenium (Python)](../../python/selenium/README.md)
- [BeautifulSoup (Python)](../../python/BeautifulSoup/README.md)
- [Playwright (Python)](../../python/playwright/README.md)

## Project Structure

```
cheerio-axios/
- product_category/
  - example-data/
    - product_category.json
  - README.md
  - scraper/
    - beautylish_scraper_product_category_v1.js
- product_data/
  - example-data/
    - product_data.json
  - README.md
  - scraper/
    - beautylish_scraper_product_data_v1.js
- product_search/
  - example-data/
    - product_search.json
  - README.md
  - scraper/
    - beautylish_scraper_product_search_v1.js
```

## Best Practices

1. **Respect Rate Limits**: Use appropriate delays and concurrency settings
2. **Monitor ScrapeOps Usage**: Track your API usage in the ScrapeOps dashboard
3. **Handle Errors Gracefully**: Implement proper error handling and logging
4. **Validate URLs**: Ensure URLs are valid Beautylish pages before scraping
5. **Update Selectors**: Beautylish may change HTML structure; update selectors as needed
6. **Test Regularly**: Test scrapers regularly to catch breaking changes early
7. **Handle Missing Data**: Some products may not have all fields; handle null values appropriately

## Support & Resources

- **ScrapeOps Documentation**: [https://scrapeops.io/docs/intro/](https://scrapeops.io/docs/intro/)
- **Cheerio Documentation**: https://cheerio.js.org/
- **Example Outputs**: See `example/` folders in each scraper directory

## License

This scraper is provided as-is for educational and commercial use. Please ensure compliance with Beautylish's Terms of Service and robots.txt when using these scrapers.