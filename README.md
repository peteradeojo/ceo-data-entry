# Google Scraper

## Installation

```sh
> pip install -r requirements.txt
```

## Running
Copy and paste the list of email addresses into `emails.txt`

The easiest way to run this application is to use the `make`  command
```sh
> make
```

### Without `make`
```sh
> python prep.py
> python browser.py companies.txt
> python soup4.py not_found.txt # This is a backup script that will attempt to find missing data using beautifulsoup
```

# License
MIT