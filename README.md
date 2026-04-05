# TrendPulse - Task 2: Data Processing

### Project Overview
In this part of the project, I used *Pandas* to take the messy JSON data from Task 1 and turn it into a clean, structured CSV file.

### Cleaning Steps Performed:
1. **Loading**: Read the JSON file into a Pandas DataFrame.
2. **Duplicates**: Removed any rows that had the same `post_id`.
3. **Null Handling**: Dropped any stories that were missing titles, scores, or IDs.
4. **Data Types**: Converted `score` and `num_comments` into integers to make sure they work for math later.
5. **Quality Filter**: Filtered out any stories with a score less than 5 to keep only the trending ones.
6. **Formatting**: Used `.str.strip()` to remove any extra spaces from the story titles.

### Files Included:
- task2_data_processing.py`: The Python script using Pandas.
- data/trends_clean.csv`: The final cleaned data.
- data/trends_20260405.json`: The original raw data used as input.

### Requirements:
- pandas
- os
- datetime

### How to use:
Run python task2_data_processing.py`. The console will show you exactly how many rows were removed at each step and give a final summary of stories per category.
