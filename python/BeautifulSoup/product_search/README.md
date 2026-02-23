# Beautylish Product Search Scraper - BeautifulSoup (Python)

This efficient Python scraper allows you to extract comprehensive search result data from Beautylish using the BeautifulSoup library. It is designed to navigate search result pages, capturing product details, metadata, and pagination information while leveraging ScrapeOps for enhanced request reliability.

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

- **Search Metadata**: Query string, total results count, and search type
- **Products**: An array of product items found in the search results
- **Breadcrumbs**: Navigation hierarchy for the current search context
- **Pagination**: Information regarding current page and total pages available
- **Recommendations**: Suggested products based on the search intent
- **Related Searches**: Alternative search keywords and phrases
- **Sponsored Products**: Promoted items appearing within search results

## Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager (for Python) or npm (for Node.js)

### Installation

1. Install required dependencies:

```bash
pip install -r requirements.txt
```

2. Get your ScrapeOps API key from [https://scrapeops.io/app/register/ai-scraper](https://scrapeops.io/app/register/ai-scraper)

3. Update the API key in the scraper:

```python
API_KEY = "YOUR-API-KEY"
```

### Running the Scraper

1. Navigate to the scraper directory:

```bash
cd python/beautifulsoup/product_search
```

2. Edit the URLs in `scraper/beautylish_scraper_product_search_v1.py`:

```python
# In beautylish_scraper_product_search_v1.py
url = "https://example.com/product"
```

3. Run the scraper:

```bash
python beautylish_scraper_product_search_v1.py
```

The scraper will generate a timestamped JSONL file (e.g., `Beautylish_com_product_search_page_scraper_data_20260114_120000.jsonl`) containing all extracted data.

### Example Output

See `example-data/product_search.json` for a sample of the extracted data structure.

## Supported URLs

The scraper supports the following URL patterns:

- `https://www.beautylish.com`
- `https://www.beautylish.com/shop/browse?utm_source=internal_search&utm_campaign=Search+Beautylish+Products&q=hair+shampoo`
- `https://proxy.scrapeops.io/v1/?`

## Configuration

### Scraper Parameters

The scraper supports several configuration options. See the scraper code for available parameters.

### ScrapeOps Configuration

The scraper can use ScrapeOps for anti-bot protection and request optimization:

```python
# ScrapeOps proxy configuration
proxy_url = f"https://proxy.scrapeops.io/v1/?api_key={API_KEY}"
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
| `breadcrumbs` | null | List of navigational links |
| `pagination` | null | Data regarding page numbers and navigation |
| `products` | array | Array of product objects containing names, prices, and links |
| `recommendations` | null | Suggested items related to the search |
| `relatedSearches` | null | List of related search terms |
| `searchMetadata` | object | Object containing query, total results, and search URL |
| `sponsoredProducts` | null | List of paid/promoted product listings |

### Field Descriptions

- **breadcrumbs** (null): Navigation path leading to the current page results.
- **pagination** (null): Details about the current page index and total results pages.
- **products** (array): Contains a list of items extracted from the search grid.
- **recommendations** (null): Product suggestions based on user behavior or search similarity.
- **relatedSearches** (null): Keywords that users also searched for.
- **searchMetadata** (object): Contains nested data such as the search query and total count.
- **sponsoredProducts** (null): Products marked as advertisements in the search results.

### Field Details
The `searchMetadata` object includes:
- `query`: The search term used (string).
- `totalResults`: The number of items found (integer).
- `searchUrl`: The full URL used for the request (string).

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

This scraper uses a structured Python approach to extract data from Beautylish. It utilizes the `requests` library to fetch HTML content via the ScrapeOps Proxy API, ensuring that requests are routed through high-quality proxies to avoid IP bans. Once the HTML is retrieved, `BeautifulSoup` parses the document. The scraper identifies specific CSS selectors for product information and metadata. The data is then validated using Python `dataclasses` and passed through a `DataPipeline` that handles deduplication (using a hashing heuristic) and saves the results incrementally to a JSONL file.

## Error Handling & Troubleshooting

- **Missing Data**: If fields return `null`, Beautylish may have updated their HTML structure. Check the selectors in the code.
- **Connection Errors**: Ensure your ScrapeOps API key is active and correctly inserted.
- **Rate Limiting**: If you receive 429 status codes, reduce the concurrency in the `ThreadPoolExecutor`.
- **Duplicates**: The scraper uses a hash of the product list to prevent duplicate entries in the JSONL file.

### Debugging

Enable detailed logging:

```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

This will show:
- Request URLs and responses
- Extraction steps
- Parsing errors
- Retry attempts

### Retry Logic

The scraper includes retry logic with configurable retry attempts and exponential backoff.

## Alternative Implementations

This repository provides multiple implementations for scraping Beautylish product_search pages:

### Python Implementations

- [Playwright - Product Search](./python\playwright\product_search/README.md)
- [Selenium - Product Search](./python\selenium\product_search/README.md)

### Node.js Implementations

- [Cheerio - Product Search](./node\cheerio-axios\product_search/README.md)
- [Playwright - Product Search](./node\playwright\product_search/README.md)
- [Puppeteer - Product Search](./node\puppeteer\product_search/README.md)

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
- **Scraper Code**: See `scraper/beautylish_scraper_product_search_v1.py` for implementation details

## License

This scraper is provided as-is for educational and commercial use. Please ensure compliance with Beautylish's Terms of Service and robots.txt when using this scraper.