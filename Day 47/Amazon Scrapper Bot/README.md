# Day 47 – Amazon Price Tracker

A Python script that tracks Amazon product prices and sends email alerts when prices change.

---

## Features
- Scrapes product name & price from Amazon
- Sends email alerts via Gmail SMTP
- Uses environment variables for security

---

## Tech Stack
- Python
- Requests
- BeautifulSoup
- SMTP
- dotenv

---

## Setup

### Install dependencies
```bash
pip install requests beautifulsoup4 python-dotenv
````

### Create `.env` file

```env id="xv8m2a"
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

---

## Run

```bash id="q9r2lw"
python main.py
```

---

## ⚠️ Notes

* Use Gmail App Password (not normal password)
* Amazon may block scraping requests

---
