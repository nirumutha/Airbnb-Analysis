London Airbnb Market Analysis for Investors 🏡
Project Overview
This project is a deep-dive analysis of the London Airbnb market. The goal was to act as a data consultant for a potential real estate investor, using a large, real-world dataset to answer key business questions and provide a strategic guide to entering the London short-term rental market.

The analysis focuses on three core areas:

Geographic Analysis: Identifying the most expensive and potentially profitable London boroughs.

Property Analysis: Understanding the value and market share of different property types (e.g., entire homes vs. private rooms).

Competitive Analysis: Assessing the market landscape to see if it's dominated by individual hosts or professional businesses.

Data Source
The data for this project is from Inside Airbnb, an independent, non-commercial project that scrapes and provides publicly available data from the Airbnb website.

Dataset: listings.csv for London, UK (latest version).

Link: http://insideairbnb.com/london/

Size: The dataset contains detailed information on over 50,000 listings and more than 80 columns.

Tools Used
SQL (SQLite): Used for all data cleaning, transformation, and analysis. The database was managed using DB Browser for SQLite.

Tableau Public: Used for creating all visualizations and the final interactive dashboard.

Analysis Process
The project followed a standard data analysis workflow:

1. Data Loading and Cleaning:
The raw listings.csv file was imported into a SQLite database. A key cleaning step involved using SQL functions like REPLACE and CAST to convert the price column from a text field (e.g., "$297.00") into a numerical data type that could be used for mathematical calculations.

2. Exploratory Data Analysis (EDA) with SQL:
I wrote a series of SQL queries to answer the core business questions. For example, to identify the most expensive neighbourhoods, I used the following query:

SQL

SELECT
  neighbourhood_cleansed,
  AVG(CAST(REPLACE(REPLACE(price, '$', ''), ',', '') AS REAL)) AS average_price,
  COUNT(id) AS number_of_listings
FROM
  listings
WHERE
  price IS NOT NULL
GROUP BY
  neighbourhood_cleansed
ORDER BY
  average_price DESC;
3. Visualization with Tableau:
The SQLite database was connected to Tableau Public. The results of the SQL analysis were then visualized to create an interactive dashboard presenting the key findings in an easy-to-understand format.

Key Insights & Findings
The analysis uncovered three "killer" insights that are critical for any potential investor:

💎 The Real Luxury Hotspots: While Kensington and Westminster are famously pricey, the data reveals that the City of London and Lambeth actually command the highest average nightly rates (over £360)! This is a surprising insight for investors looking beyond the obvious.

🔑 The "Price of Privacy" is Massive: An 'Entire home/apt' isn't just slightly more expensive—it demands a staggering 115% price premium over a 'Private room'. This quantifies the immense value renters place on having their own space and provides a clear guide on property types.

🏢 The Rise of the "Mega-Host": The market isn't just homeowners. It's a professional playground. My analysis uncovered that the top 10 hosts manage over 2,500 listings combined, with single entities controlling nearly 500 properties. This shows that the competition is professional, large-scale, and sophisticated.
