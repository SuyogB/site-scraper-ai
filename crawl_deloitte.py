import asyncio
from crawl4ai import *

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www2.deloitte.com/us/en/insights/economy/asia-pacific/india-economic-outlook.html",
        )
        # Save the output to a text file with UTF-8 encoding
        with open("crawler_output.txt", "w", encoding="utf-8") as file:
            file.write(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())
