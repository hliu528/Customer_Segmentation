import pandas as pd

# Load the original CSV file
df = pd.read_csv('C://customer_segmentation.csv')

# Calculate the index to split the dataframe in half
split_index = len(df) // 2

# Split the dataframe into two at the split index
df1 = df.iloc[:split_index]
df2 = df.iloc[split_index:]

# Save the split dataframes to new CSV files
df1.to_csv('customer_segmentation_1.csv', index=False)
df2.to_csv('customer_segmentation_2.csv', index=False)