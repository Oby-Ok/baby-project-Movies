# Load original cleaned dataset
cleaned_data = pd.read_csv("../clean_data/cleaned_student_survey_Oby_2025-02-05.csv")

# Load the new fake dataset
fake_data = pd.read_csv("../data/fake_data.csv")

# Ensure "expected_salary" is the same type for merging
cleaned_data["expected_salary"] = cleaned_data["expected_salary"].astype(str)
fake_data["expected_salary"] = fake_data["expected_salary"].astype(str)

# Merge the datasets
merged_data = pd.merge(cleaned_data, fake_data, on="expected_salary", how="inner")

# Save the merged dataset
merged_data.to_csv("../data/merged_data.csv", index=False)
print("✅ Merging complete. Merged dataset saved as 'merged_data.csv'.")
