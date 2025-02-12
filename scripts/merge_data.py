import pandas as pd

# Load the datasets
data1 = pd.read_csv("../data/data.csv")  # Main dataset
data2 = pd.read_csv("../data/new_data.csv")  # New dataset to merge

# Merge on the 'ID' column (assuming it's a common key)
merged_data = pd.merge(data1, data2, on="ID", how="inner")

# Save the merged dataset
merged_data.to_csv("../data/merged_data.csv", index=False)

print("Merged dataset saved as merged_data.csv")
