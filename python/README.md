# Beautylish Scrapers - Python

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)
[![ScrapeOps](https://img.shields.io/badge/ScrapeOps-Integrated-orange.svg)](https://scrapeops.io)

Comprehensive Python-based web scrapers for Beautylish.com using BeautifulSoup, Playwright, and Selenium to extract product data, search results, and category listings.

This repository provides a robust suite of Python scrapers designed to extract high-quality beauty product data from Beautylish. Utilizing industry-standard frameworks like BeautifulSoup for speed and Playwright/Selenium for dynamic content, these tools enable seamless extraction of product details, pricing, and availability while integrating with ScrapeOps for enhanced proxy rotation and anti-bot bypass.

## 📊 What Data You Can Scrape

These Python scrapers extract data from Beautylish.com:

*   **Product Data**: Extract detailed information from individual product pages, including brand names, descriptions, prices, ingredients, and high-resolution image URLs.
*   **Product Search**: Automate search queries to capture all products matching specific keywords, including their ranking and basic listing details.
*   **Product Category**: Scrape entire category branches (e.g., Skincare, Makeup) to build comprehensive catalogs of available items within specific departments.

## 📁 Scraper Structure

Each scraper type in the Beautylish repository follows this structure:

```
{framework}/
├── product_data/
│   ├── scraper/
│   │   └── beautylish_scraper_product_v1.py
│   ├── example/
│   │   └── product.json
│   └── README.md
├── product_search/
│   ├── scraper/
│   │   └── beautylish_scraper_product_search_v1.py
│   ├── example/
│   │   └── product_search.json
│   └── README.md
├── product_category/
│   ├── scraper/
│   │   └── beautylish_scraper_product_category_v1.py
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

- **Multiple Framework Support**: BeautifulSoup, Playwright, Selenium
- **Production-Ready**: Battle-tested scrapers with error handling and retry logic
- **Anti-Bot Protection**: Optional ScrapeOps support that may help with proxy rotation and request optimization
- **Comprehensive Data Extraction**: Product data, search results, and category listings
- **JSONL Output Format**: Efficient, line-by-line JSON output for easy processing
- **Well-Documented**: Detailed READMEs for each scraper with examples and troubleshooting
- **Active Maintenance**: Regular updates to handle Beautylish's changing HTML structure

## 📋 Requirements

- **Python**: Python 3.7 or higher
- **pip**: pip
- **ScrapeOps API Key**: Free tier available at [https://scrapeops.io/app/register/ai-scraper](https://scrapeops.io/app/register/ai-scraper)
- **Virtual Environment** (recommended): For dependency isolation

## 🎯 Quick Start

1. **Choose a framework** based on your needs (see comparison below)
2. **Navigate to the framework directory** and follow its README for setup
3. **Get your ScrapeOps API key** from [https://scrapeops.io/app/register/ai-scraper](https://scrapeops.io/app/register/ai-scraper)

For framework-specific setup and usage, see:
- [BeautifulSoup](./BeautifulSoup/README.md)
- [Playwright](./playwright/README.md)
- [Selenium](./selenium/README.md)

## 📚 Supported Frameworks

| Framework | Type | Best For | Performance | Complexity | JavaScript Support |
|-----------|------|----------|-------------|------------|-------------------|
| BeautifulSoup | HTTP Library | Speed & Static Content | Very Fast | Easy | No |
| Playwright | Browser Automation | Modern SPAs & Stealth | Medium | Medium | Yes |
| Selenium | Browser Automation | Legacy Support & Testing | Slower | Medium | Yes |

### Framework Documentation

- **BeautifulSoup**: [README](./BeautifulSoup/README.md) | [Official Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- **Playwright**: [README](./playwright/README.md) | [Official Docs](https://playwright.dev/)
- **Selenium**: [README](./selenium/README.md) | [Official Docs](https://www.selenium.dev/documentation/)

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

Choosing the right tool depends on your specific requirements for the Beautylish scrapers:

*   **Use BeautifulSoup** if you need high-speed extraction and the data is present in the initial HTML source. It uses significantly fewer resources and is ideal for large-scale category scraping where JavaScript execution isn't required.
*   **Use Playwright** for the best balance of speed and capability. It is highly recommended for pages where content (like reviews or related products) loads dynamically. Playwright is generally faster and more reliable than Selenium in modern Python environments.
*   **Use Selenium** if you have existing infrastructure built around it or require specific browser-driven debugging features. While slower than Playwright, it is a robust industry standard.
*   **Performance vs. Capability**: HTTP-based scrapers (BeautifulSoup) are 5-10x faster but cannot interact with buttons or wait for JS-rendered elements. Browser-based tools (Playwright/Selenium) handle complex interactions at the cost of higher CPU/RAM usage.

## ⚠️ Common Issues & Solutions

*   **Installation Problems**: Ensure you have run `pip install -r requirements.txt`. For Playwright, remember to run `playwright install` to download the necessary browser binaries.
*   **Dependency Conflicts**: We strongly recommend using a virtual environment (`python -m venv venv`) to avoid conflicts with other Python projects.
*   **Anti-Bot Blocking**: If you receive 403 Forbidden errors, it is likely Beautylish's bot protection. Enable ScrapeOps proxy rotation in the configuration to bypass these filters.
*   **Selector Changes**: If a scraper returns empty data, Beautylish may have updated their website layout. Check the `README.md` in the specific scraper folder for updated CSS selectors or XPath tips.
*   **Browser Automation Challenges**: If using Playwright or Selenium in a Docker container or server, ensure you are running in "headless" mode and have installed the necessary Linux dependencies (libgbm, etc.).

## 🔗 Alternative Implementations

This repository also provides Node.js implementations:

- [Node.js Scrapers](../node/README.md)

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
- **BeautifulSoup**: [Official Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- **Playwright**: [Official Docs](https://playwright.dev/python/docs/intro)
- **Selenium**: [Official Docs](https://www.selenium.dev/documentation/)

### External Resources
- **ScrapeOps Documentation**: [https://scrapeops.io/docs/intro/](https://scrapeops.io/docs/intro/)
- **Python Documentation**: https://docs.python.org/3/

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