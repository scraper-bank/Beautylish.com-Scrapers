# Beautylish Scrapers - Node.js

[![Node.js](https://img.shields.io/badge/Node.js-14+-339933?logo=node.js&logoColor=white)](https://nodejs.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)
[![ScrapeOps](https://img.shields.io/badge/ScrapeOps-Integrated-orange.svg)](https://scrapeops.io)

Comprehensive Node.js web scraping tools for Beautylish.com using Cheerio, Playwright, and Puppeteer to extract product details, search results, and category data.

Automate data collection from Beautylish using this robust suite of Node.js scrapers. Supporting high-performance HTTP requests with Cheerio-Axios and full browser automation via Playwright and Puppeteer, these tools allow you to extract rich beauty product information, pricing, and inventory data efficiently.

## 📊 What Data You Can Scrape

These Node.js scrapers extract data from Beautylish.com:

*   **Product Data**: Extract detailed information including product names, brands, prices, descriptions, ingredients, and high-resolution image URLs.
*   **Product Search**: Scrape search result pages to gather product listings, ratings, and basic pricing for specific search queries.
*   **Product Category**: Collect all items listed within specific beauty categories (e.g., Makeup, Skincare) to build comprehensive catalogs.

## 📁 Scraper Structure

Each scraper type in the Beautylish repository follows this structure:

```
{framework}/
├── product_data/
│   ├── scraper/
│   │   └── beautylish_scraper_product_v1.js
│   ├── example/
│   │   └── product.json
│   └── README.md
├── product_search/
│   ├── scraper/
│   │   └── beautylish_scraper_product_search_v1.js
│   ├── example/
│   │   └── product_search.json
│   └── README.md
├── product_category/
│   ├── scraper/
│   │   └── beautylish_scraper_product_category_v1.js
│   ├── example/
│   │   └── product_category.json
│   └── README.md
├── reviews/          # Coming soon
└── sellers/          # Coming soon
```

Each scraper directory contains:
- `scraper/` - Implementation files
- `example/` - Sample JSON output files
- `README.md` - Detailed documentation for that scraper

## 🚀 Features

- **Multiple Framework Support**: Cheerio (cheerio-axios), Playwright, and Puppeteer
- **Production-Ready**: Battle-tested scrapers with error handling and retry logic
- **Anti-Bot Protection**: Optional ScrapeOps support that may help with proxy rotation and request optimization
- **Comprehensive Data Extraction**: Product data, search results, and category listings
- **JSONL Output Format**: Efficient, line-by-line JSON output for easy processing
- **Well-Documented**: Detailed READMEs for each scraper with examples and troubleshooting
- **Active Maintenance**: Regular updates to handle Beautylish's changing HTML structure

## 📋 Requirements

- **Node.js**: Node.js 14 or higher
- **npm**: npm
- **ScrapeOps API Key**: Free tier available at [https://scrapeops.io/app/register/ai-scraper](https://scrapeops.io/app/register/ai-scraper)
- **Virtual Environment** (recommended): For dependency isolation

## 🎯 Quick Start

1. **Choose a framework** based on your needs (see comparison below)
2. **Navigate to the framework directory** and follow its README for setup
3. **Get your ScrapeOps API key** from [https://scrapeops.io/app/register/ai-scraper](https://scrapeops.io/app/register/ai-scraper)

For framework-specific setup and usage, see:
- [Cheerio](./cheerio-axios/README.md)
- [Playwright](./playwright/README.md)
- [Puppeteer](./puppeteer/README.md)

## 📚 Supported Frameworks

| Framework | Type | Best For | Performance | Complexity | JavaScript Support |
|-----------|------|----------|-------------|------------|-------------------|
| **Cheerio** | HTTP | Fast, static data extraction | Very Fast | Easy | No |
| **Playwright** | Browser | Modern web apps, SPAs | Medium | Medium | Yes |
| **Puppeteer** | Browser | Chrome-specific automation | Medium | Medium | Yes |

### Framework Documentation

- **Cheerio**: [README](./cheerio-axios/README.md) | [Official Docs](https://cheerio.js.org/)
- **Playwright**: [README](./playwright/README.md) | [Official Docs](https://playwright.dev/)
- **Puppeteer**: [README](./puppeteer/README.md) | [Official Docs](https://pptr.dev/)

## 🛡️ Anti-Bot Protection

All scrapers can integrate with **ScrapeOps** to help handle Beautylish's anti-bot measures:

- **Proxy Rotation**: May help distribute requests across multiple IP addresses
- **Request Header Optimization**: May optimize headers to reduce detection
- **Rate Limiting Management**: Built-in rate limiting and retry logic

**Note**: Anti-bot measures vary by site and may change over time. CAPTCHA challenges may occur and cannot be guaranteed to be resolved automatically. Using proxies and browser automation can help reduce blocking, but effectiveness depends on the target site's specific anti-bot measures.

**Free Tier Available**: ScrapeOps offers a generous free tier perfect for testing and small-scale scraping.

Get your API key at [https://scrapeops.io/app/register/ai-scraper](https://scrapeops.io/app/register/ai-scraper)

## 📦 Output Format

All scrapers output data in **JSONL format** (one JSON object per line):

- **Efficient**: Each line is a complete JSON object
- **Streamable**: Process line-by-line without loading entire file
- **Database-Friendly**: Easy to import into databases
- **Large Dataset Support**: Handles millions of records efficiently

Example output file: `beautylish_com_product_page_scraper_data_20260114_120000.jsonl`

## 🤔 Choosing the Right Framework

Selecting the right tool for Beautylish depends on your specific scale and data requirements:

- **Use Cheerio (HTTP)** if you need maximum speed and the data is present in the initial HTML source. It is the most resource-efficient method and ideal for scraping thousands of pages quickly.
- **Use Playwright or Puppeteer (Browser)** if Beautylish uses heavy JavaScript to render content, such as dynamic pricing, infinite scroll, or content that only appears after user interaction.
- **Performance vs. Capability**: HTTP libraries (Cheerio) are significantly faster and cheaper to run but cannot execute JS. Browser automation (Playwright/Puppeteer) is more robust for bypassing certain client-side checks but requires more CPU and RAM.
- **Node.js Advantage**: Node.js is particularly strong for scraping due to its non-blocking I/O, making it excellent for handling many concurrent requests or browser instances.

## ⚠️ Common Issues & Solutions

- **Installation Problems**: Ensure you run `npm install` in the specific framework directory. For Playwright/Puppeteer, ensure browser binaries are downloaded (`npx playwright install`).
- **Dependency Conflicts**: Use a clean `node_modules` folder and ensure your Node version matches the requirements (v14+).
- **Anti-bot Blocking**: If you receive 403 Forbidden errors, integrate the ScrapeOps Proxy SDK or rotate your User-Agents.
- **Selector Changes**: Beautylish may update its CSS classes. If data returns as `null`, verify the selectors in the `scraper/` files against the live site.
- **Memory Issues**: Browser automation can leak memory. Always ensure `browser.close()` is called in a `finally` block.

## 🔗 Alternative Implementations

This repository also provides Python implementations:

- [Python Scrapers](../python/README.md)

## 📖 Best Practices

1. **Use Virtual Environments**: Isolate dependencies per project
2. **Respect Rate Limits**: Use appropriate delays and concurrency settings
3. **Monitor ScrapeOps Usage**: Track your API usage in the ScrapeOps dashboard
4. **Handle Errors Gracefully**: Implement proper error handling and logging
5. **Validate URLs**: Ensure URLs are valid Beautylish pages before scraping
6. **Update Selectors Regularly**: Beautylish may change HTML structure
7. **Test Regularly**: Test scrapers regularly to catch breaking changes early
8. **Handle Missing Data**: Some products may not have all fields; handle null values appropriately
9. **Browser Management**: For browser automation, ensure proper cleanup and resource management
10. **Use JSONL Format**: Efficient for large datasets and streaming processing

## 📚 Resources & Documentation

### Framework Documentation
- **Cheerio**: [https://cheerio.js.org/](https://cheerio.js.org/)
- **Playwright**: [https://playwright.dev/](https://playwright.dev/)
- **Puppeteer**: [https://pptr.dev/](https://pptr.dev/)

### External Resources
- **ScrapeOps Documentation**: [https://scrapeops.io/docs/intro/](https://scrapeops.io/docs/intro/)
- **Node.js Documentation**: https://nodejs.org/docs/

### Project Resources
- **Root README**: [../README.md](../README.md) - Overview of all implementations
- **Framework READMEs**: See individual framework directories for specific guides
- **Scraper READMEs**: See individual scraper directories for detailed documentation

## ⚖️ License

This scraper is provided as-is for educational and commercial use. Please ensure compliance with Beautylish's Terms of Service and robots.txt when using these scrapers.

See [LICENSE](../LICENSE) for full license details.

## ⚠️ Disclaimer

This software is provided for educational and commercial purposes. Users are responsible for ensuring their use complies with:

- Beautylish's Terms of Service
- Beautylish's robots.txt
- Applicable laws and regulations
- Rate limiting and respectful scraping practices

The authors and contributors are not responsible for any misuse of this software.