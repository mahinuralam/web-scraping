# aiw-web-scraping
 
Prequisites
[ ] Ubuntu 
[ ] Python 3.9
[ ] PostgreSQL
How to start
Install Dependencies:
pip install -r requirements
Add a .env file as shown in .env.example

Create postgres user or use existing by editing .env

sudo -u postgres psql
ALTER USER postgres PASSWORD 'abcd';
Run the server with univorn
uvicorn app:app --port 8000 --reload
Run the server with docker
docker compose up
For Swagger UI, with the given link add "/docs", i.e., http://localhost:8010/docs
Here you can test the api endpoints.
