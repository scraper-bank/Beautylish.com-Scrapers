# Beautylish Scrapers - Selenium (Python)

Effortlessly extract high-quality beauty product data, categories, and search results from Beautylish using these robust Python scrapers powered by Selenium. This suite provides reliable browser automation to navigate dynamic content and capture comprehensive product details with ease.

## Overview

This directory contains Python scrapers built with **Selenium**.

## Available Scrapers

- [Product Category](./product_category/README.md)
- [Product Data](./product_data/README.md)
- [Product Search](./product_search/README.md)

## Why Selenium?

Selenium is a powerful browser automation framework that is particularly well-suited for scraping modern web applications like Beautylish. While static scrapers might struggle with dynamic content, Selenium provides several distinct advantages:

- **JavaScript Execution**: Selenium operates a real browser instance, allowing it to render JavaScript-heavy components, lazy-loaded images, and interactive elements that are common in modern e-commerce storefronts.
- **Human-Like Interaction**: It can simulate real user behavior, such as scrolling, clicking buttons, and handling modal pop-ups, which helps in navigating complex site layouts.
- **DOM Persistence**: Since Selenium maintains a live connection to the browser's Document Object Model (DOM), it is highly effective for scraping pages where content updates dynamically without a full page refresh.
- **Flexibility**: With Python's Selenium bindings, you can easily integrate advanced logic, custom wait conditions (WebDriverWait), and sophisticated data cleaning workflows using BeautifulSoup in tandem.
- **Performance**: While slower than headless HTTP clients, Selenium's ability to accurately replicate the "browser experience" makes it the gold standard for reliability when dealing with sites that employ client-side rendering.

## Prerequisites

- **Python**: Python 3.7 or higher
- **pip**: pip
- **ScrapeOps API Key**: For anti-bot protection (free tier available)

## Installation

1. Navigate to the specific scraper directory:
```bash
cd product_category  # or product_data, product_search
```

2. Install dependencies:
```bash
pip install selenium beautifulsoup4
```

3. Get your ScrapeOps API key from [https://scrapeops.io/app/register/ai-scraper](https://scrapeops.io/app/register/ai-scraper)

4. Update the API key in the scraper file:
```python
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

### Python Alternatives
- [BeautifulSoup (Python)](../BeautifulSoup/README.md)
- [Playwright (Python)](../playwright/README.md)

### Node.js Alternatives
- [Puppeteer (Node.js)](../../node/puppeteer/README.md)
- [Playwright (Node.js)](../../node/playwright/README.md)
- [Cheerio (Node.js)](../../node/cheerio-axios/README.md)

## Project Structure

```
selenium/
- product_category/
  - example-data/
    - product_category.json
  - README.md
  - scraper/
    - beautylish_scraper_product_category_v1.py
- product_data/
  - example-data/
    - product_data.json
  - README.md
  - scraper/
    - beautylish_scraper_product_data_v1.py
- product_search/
  - example-data/
    - product_search.json
  - README.md
  - scraper/
    - beautylish_scraper_product_search_v1.py
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
- **Selenium Documentation**: https://www.selenium.dev/documentation/
- **Example Outputs**: See `example/` folders in each scraper directory

## License

This scraper is provided as-is for educational and commercial use. Please ensure compliance with Beautylish's Terms of Service and robots.txt when using these scrapers.