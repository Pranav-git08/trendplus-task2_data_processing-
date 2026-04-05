import pandas as pd
import os
from datetime import datetime

# Step 1: Load the JSON File (4 marks)
# Using today's date to find the file from Task 1
today_str = datetime.now().strftime("%Y%m%d")
json_path = f"data/trends_{today_str}.json"

print(f" Starting Task 2: Data Processing ")

if not os.path.exists(json_path):
    print(f"Error: {json_path} not found. Did you run Task 1?")
else:
    # Loading the raw JSON into a DataFrame
    df = pd.read_json(json_path)
    print(f"Loaded {len(df)} stories from {json_path}")

    # Step 2: Clean the Data (10 marks)
    
    # 1. Remove duplicates based on 'post_id'
    df = df.drop_duplicates(subset=['post_id'])
    print(f"After removing duplicates: {len(df)}")

    # 2. Drop rows where essential data is missing
    df = df.dropna(subset=['post_id', 'title', 'score'])
    print(f"After removing nulls: {len(df)}")

    # 3. Clean up the title strings (stripping whitespace)
    df['title'] = df['title'].str.strip()

    # 4. Ensure correct data types (Integers)
    df['score'] = df['score'].astype(int)
    df['num_comments'] = df['num_comments'].astype(int)

    # 5. Filter out "low quality" stories with scores less than 5
    df = df[df['score'] >= 5]
    print(f"After removing low scores: {len(df)}")

    # Step 3: Save as CSV & Summary (6 marks)
    output_csv = "data/trends_clean.csv"
    df.to_csv(output_csv, index=False)
    
    print(f"Saved {len(df)} rows to {output_csv}")
    
    # Printing the required summary of stories per category
    print("\nStories per category:")
    print(df['category'].value_counts())

    print("\n  Task 2 Complete ") 