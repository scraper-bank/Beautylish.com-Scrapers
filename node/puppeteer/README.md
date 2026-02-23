# Beautylish Scrapers - Puppeteer (Node.js)

Effortlessly extract high-quality beauty product data from Beautylish using these robust Puppeteer scrapers written in Node.js. Designed for scalability and reliability, these tools allow you to bypass complex layouts and dynamic content to gather product details, search results, and category listings.

## Overview

This directory contains Node.js scrapers built with **Puppeteer**.

## Available Scrapers

- [Product Category](./product_category/README.md)
- [Product Data](./product_data/README.md)
- [Product Search](./product_search/README.md)

## Why Puppeteer?

Puppeteer is a powerful Node.js library that provides a high-level API to control headless Chrome or Chromium. It is the ideal choice for scraping Beautylish for several reasons:

- **Dynamic Content Rendering**: Beautylish utilizes modern frontend frameworks that often require JavaScript execution to display prices, reviews, and inventory status. Puppeteer handles this natively by rendering the full page just like a real user.
- **Granular Browser Control**: Unlike simple HTTP clients, Puppeteer allows for complex user interactions such as clicking "Load More" buttons, handling hover states, and navigating through paginated results.
- **Performance & Speed**: Puppeteer is built on the DevTools protocol, offering faster execution and lower overhead compared to older automation tools like Selenium.
- **Stealth Capabilities**: When combined with ScrapeOps, Puppeteer can mimic human-like behavior, such as realistic mouse movements and scrolling, which is critical for maintaining access to high-value retail data.
- **Developer Ecosystem**: Being a Node.js-based tool, it integrates seamlessly with the vast npm ecosystem, allowing for easy data post-processing using libraries like Cheerio for lightning-fast DOM parsing once the page is loaded.

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
npm install puppeteer cheerio
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
- [Playwright (Node.js)](../playwright/README.md)
- [Cheerio (Node.js)](../cheerio-axios/README.md)

### Python Alternatives
- [Selenium (Python)](../../python/selenium/README.md)
- [BeautifulSoup (Python)](../../python/BeautifulSoup/README.md)
- [Playwright (Python)](../../python/playwright/README.md)

## Project Structure

```
puppeteer/
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
- **Puppeteer Documentation**: https://pptr.dev/
- **Example Outputs**: See `example/` folders in each scraper directory

## License

This scraper is provided as-is for educational and commercial use. Please ensure compliance with Beautylish's Terms of Service and robots.txt when using these scrapers.