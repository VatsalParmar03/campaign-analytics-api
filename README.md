Campaign Analytics API

A Django REST API for managing marketing campaigns with full CRUD functionality, third-party API integration, and reporting endpoints. The project is deployed live and designed to be production-ready.

Features -

Campaign Management (CRUD)

Create, read, update, delete campaigns

Fields: name, budget, clicks, impressions

External API Integration

Fetches live Bitcoin price from CoinGecko

Gracefully handles rate limits and failures

Reporting & Analytics

Aggregated campaign metrics:

Total campaigns

Total budget

Total clicks

Total impressions

Average CTR

Live Deployment

Hosted on Render

Automatic migrations on deploy

Tech Stack -

Python

Django

Django REST Framework

SQLite (demo) / PostgreSQL-ready

Gunicorn

Render (deployment)

Live API Endpoints -

Campaign CRUD -

https://campaign-analytics-api.onrender.com/api/campaigns/


External API (CoinGecko) -

https://campaign-analytics-api.onrender.com/api/external/crypto/


Reporting API -

https://campaign-analytics-api.onrender.com/api/reports/campaign-summary/

Local Setup
git clone https://github.com/VatsalParmar03/campaign-analytics-api

cd campaign-analytics-api

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

🔹 Notes

External API rate limits are handled gracefully

Root URL intentionally returns 404 (API-only backend)

Automatic migrations are run during deployment
