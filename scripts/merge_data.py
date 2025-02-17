import pandas as pd

# Load datasets
cleaned_data = pd.read_csv("../clean_data/cleaned_student_survey_Oby_2025-02-05.csv")
new_data = pd.read_csv("../data/Statistics_Survey2025.csv")

# Perform an inner merge on a common key (modify key as needed)
merged_data = pd.merge(cleaned_data, new_data, on="ID", how="inner")

# Save the merged dataset
merged_data.to_csv("../data/merged_data.csv", index=False)

print(" Merging complete. Merged dataset saved as 'merged_data.csv'.")
