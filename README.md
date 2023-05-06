# aiw-web-scraping

As part of your assessment, we require you to create two RPA bots that can scrape and collect data from
Amazon.com. Specifically, the first bot should automatically search for a specific product on Amazon and
scrape the list of products that match the search query, storing the data in a PostgreSQL database or any other
database of your choice. The second bot should then automatically retrieve the scraped data from the
database and scrape all the relevant data for each product and update the database. After listing out all the
products from search results, the first bot should trigger the second bot to start scraping details about these
products from the database. After completion, the second bot should again initiate the first bot for the second
product search. This way this cycle should run for five products.


## Prerequisites

[ ] Ubuntu

[ ] Python 3.9

[ ] PostgreSQL
## How to start
- Install Dependencies:
```bash
  pip install -r requirements
```
- Add a `.env` file as shown in `.env.example`
- Create postgres user or use existing by editing `.env`
```bash
sudo -u postgres psql
ALTER USER postgres PASSWORD 'abcd';
```
- Run the server with univorn
```bash
uvicorn app:app --port 8000 --reload
```
- Run the server with docker
```bash
docker compose up
```
- For Swagger UI, with the given link add "/docs", i.e., http://localhost:8010/docs
Here you can test the api endpoints.




