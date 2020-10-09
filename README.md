# hack-a-thing-2-tmonfre

For this hack-a-thing, I build a python server using flask that exposes some functions for web crawling using `scrapy`, and wraps the [Google Civic Information API](https://developers.google.com/civic-information). It is hosted on Heroku at [https://cs98-hack-a-thing-2.herokuapp.com](https://cs98-hack-a-thing-2.herokuapp.com).

It exposes the following routes:

### `GET /elections`

Retrieves information on elections in the United States.

### `GET /elections/voter-info`

Expects query parameters for address and election ID (which comes from the above route). Retrieves information on polling places and races for the given election and address.

### `GET /elections/representative-info`

Expects query parameter for address. Retrieves information on elected representatives at that address.

### `GET /crawler/content`

Expects query parameter for url. Retrieves HTML content of website.

### `GET /crawler/text`

Expects query parameter for url. Retrieves in line article text of website

### `GET /crawler/links`

Expects query parameter for url. Retrieves all links on page.

### `GET /crawler/keyword`

Expects query parameters for url and keyword. Retrieves all links on page that use keyword (either in text or link).

### `GET /crawler/google`

Expects query parameter for keyword. Retrieves links to google search results (first two pages) for that keyword.

### `GET /crawler/google-text`

Expects query parameter for keyword. Retrieves article content for first page of google search results for that keyword.

## What I Learned

My primary takeaway from this tutorial/hack was learning how to build a server with python and how to handle routing/data management. I also learned how to use `scrapy` for web crawling, and learned a lot about what xpaths are and how to use them to my advantage. I also learned how to host a flask server on Heroku.

I valued this exercise because knowing how to build a web server with the same interface as a node server but a completely different stack is really valuable, since I can now run different operations on different servers based on what stack is best, but interface with both in the same way. I would definitely use this tech stack again.

## What Didn't Work

I struggled a bit with getting the app hosted on Heroku and running the web crawler programmatically instead of via the command line. It was also challenging to figure out how to pass parameters to the spiders programmatically.

## Tutorials I Followed

- [https://www.pluralsight.com/guides/web-scraping-with-scrapy](https://www.pluralsight.com/guides/web-scraping-with-scrapy)
- [https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3](https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3)
- [https://github.com/dali-lab/blabl-server](https://github.com/dali-lab/blabl-server)
- [https://developers.google.com/civic-information/docs/using_api#voterinfoquery-response:](https://developers.google.com/civic-information/docs/using_api#voterinfoquery-response:)

I worked alone on this (without a partner).
