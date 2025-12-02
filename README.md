# AI Company Brochure Generator

An AI-powered agent that navigates a company's website, intelligently selects relevant pages (like "About Us" or "Careers"), scrapes the content, and generates a cohesive marketing brochure using OpenAI's GPT-4o-mini.

## Features

- **Smart Navigation:** Doesn't just scrape the home page; asks the AI which sub-links are relevant to a brochure.
- **Web Scraping:** Uses `BeautifulSoup` to clean HTML and extract readable text.
- **Content Synthesis:** Aggregates multiple pages into a single context.
- **Streaming Output:** Writes the brochure to the console in real-time.

## Project Structure

```text
company_brochure/
├── .env                  # API Key configuration
├── config.py             # Global constants & API setup
├── website.py            # Web scraping logic
├── generator.py          # AI logic (Prompts & Brochure generation)
├── main.py               # Entry point script
└── requirements.txt      # Dependencies
```

## How to Run

1.  Run the script in your terminal:
    ```bash
    python main.py
    ```
2.  Follow the prompts:
    ```text
    Enter the Company Name: Anthropic
    Enter the Website URL (including https://): [https://anthropic.com](https://anthropic.com)
    ```
3.  The AI will begin scraping and streaming the brochure immediately.
