import pandas as pd
import os

def transform_dataframe(df):
   """
   Transforms the given DataFrame by performing the following operations:
   
   1. Converts the 'price_euros' column to integers.
   2. Converts the 'mileage' column to integers.
   3. Converts the 'year' column to datetime objects with the format '%m/%Y', 
      setting the day to 1 by default.
   4. Renames the 'year' column to 'date'.
   5. Extracts the year from the 'date' column and stores it in a new 'year' column.
   
   Parameters:
   df (pandas.DataFrame): The input DataFrame to be transformed.
   
   Returns:
   pandas.DataFrame: The transformed DataFrame.
   """
   
   print("Starting transformation of DataFrame")
   
   # Convert 'price_euros' column to integers
   df['price_euros'] = df['price_euros'].astype(int)
   print("Converted 'price_euros' column to integers")
   
   # Convert 'mileage' column to integers
   df['mileage'] = df['mileage'].astype(int)
   print("Converted 'mileage' column to integers")
   
   # Convert 'year' column to datetime objects with the format '%m/%Y'
   df['year'] = pd.to_datetime(df['year'], format='%m/%Y') # By default, the day is set to 1
   print("Converted 'year' column to datetime objects with the format '%m/%Y'")

   # Rename the 'year' column to 'date'
   df.rename(columns={'year': 'date'}, inplace=True)
   print("Renamed 'year' column to 'date'")

   # Extract the year from the 'date' column and store it in a new 'year' column
   df['year'] = df['date'].dt.year # Extract the year from the date. Easier to work with
   print("Extracted year from 'date' column and stored in new 'year' column")
   
   # Define the path to the "data" folder
   data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')
   print(f"Data folder path: {data_folder}")
   
   # Create the "data" folder if it doesn't exist
   os.makedirs(data_folder, exist_ok=True)
   print("Created 'data' folder if it didn't exist")
   
   # Define the path to the output CSV file
   output_file = os.path.join(data_folder, 'transformed_data.csv')
   print(f"Output file path: {output_file}")
   
   # Export the DataFrame to a CSV file
   df.to_csv(output_file, index=False)
   print("Exported DataFrame to CSV file")
   
   print("Transformation complete")
   return df