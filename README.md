Demographic Data Analyzer

This project analyzes demographic data from the 1994 U.S. Census database, following the freeCodeCamp Data Analysis with Python project.

📂 Dataset

The dataset is downloaded directly from freeCodeCamp’s GitHub repository using the requests module and saved locally as adult.data.csv.

Each record contains attributes such as age, education, occupation, race, sex, hours-per-week, native country, and salary level (>50K or <=50K).

## Steps Performed

1. Dataset Loading

Fetched dataset from the freeCodeCamp URL using requests.

Loaded into a Pandas DataFrame with column names for clarity.



2. Demographic Analysis

Counted individuals by race.

Calculated the percentage of people with a Bachelor’s degree.

Determined the percentage of rich (>50K) individuals:

With higher education (Bachelors, Masters, Doctorate).

With lower education.


Found the minimum working hours per week and calculated what % of those working minimum hours are rich.

Found the country with the highest percentage of rich people and that percentage.

Identified the most common occupation among rich (>50K) people in India.



3. Functions & Methods Used

pandas.read_csv for loading data.

value_counts, filtering with conditions, and isin.

Percentage calculations using Pandas Series operations.




📊 Key Results

Race count: Distribution of people by race.

% with Bachelors degree: ~X% (calculated from dataset).

% rich with higher education: ~X%.

% rich with lower education: ~X%.

Minimum working hours: X hrs/week.

% rich among minimum workers: ~X%.

Country with highest % of rich people: {Country} (~X%).

Most popular occupation among rich in India: {Occupation}.


🚀 Technologies Used

Python

Pandas

Requests
