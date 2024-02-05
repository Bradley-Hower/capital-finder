# LAB - Class 16

## Project: Capital Finder

## Author: Bradley Hower

Python Requests for HTTP requests. 

[https://requests.readthedocs.io/en/latest/](https://requests.readthedocs.io/en/latest/)

Uses `parse` method from `urllib` to parse out query strings from URL.

## Setup

Uses a serverless host. The one used in this project was [https://vercel.com/](https://vercel.com/).

When runing, try to make requirements.txt as clean as possible as this can cause issues.

## Run

To access, go to extension `api/capital-finder` in your capital projects. For example, "https://capital-finder-green.vercel.app/api/capital-finder".

### Locate Country

To search for the country to which a capital belongs, end the above with "?capital=" following by the capital city.

For example:

https://capital-finder-green.vercel.app/api/capital-finder?capital=paris

### Locate Capital

To search for the capital of a country, end the above with "?country=" following by the country.

For example:

https://capital-finder-green.vercel.app/api/capital-finder?country=france
