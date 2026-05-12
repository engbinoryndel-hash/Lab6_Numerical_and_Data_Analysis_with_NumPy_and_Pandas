import numpy as np # [cite: 42]

# Create a 1D array representing years of experience [cite: 43]
# Added 2 extra points per "Try It" instruction [cite: 57, 58]
years_exp = np.array([1, 3, 5, 7, 10, 12, 15]) # [cite: 44]
print("Years of Experience:", years_exp) # [cite: 45]

# Create a 2D array representing sample salaries (in thousands) [cite: 46]
# Added 2 extra points per "Try It" instruction [cite: 57, 58]
salaries = np.array([[50, 60, 70, 75], [80, 90, 100, 110]]) # [cite: 47]
print("Salary Matrix:\n", salaries) # [cite: 48]

# Create arrays of zeros and ones for placeholder analysis [cite: 49]
zeros_array = np.zeros((2, 2)) # [cite: 49]
ones_array = np.ones((2, 3)) # [cite: 50]
identity_matrix = np.eye(3) # 3x3 identity matrix [cite: 58]

print("Zeros Array:\n", zeros_array) # [cite: 52]
print("Ones Array:\n", ones_array) # [cite: 53]
print("Identity Matrix:\n", identity_matrix)
# Element-wise addition: Add 5 years to all values [cite: 60, 61]
exp_plus_5 = years_exp + 5 
print("Years + 5:", exp_plus_5) # [cite: 62]

# Element-wise multiplication: Multiply all values by 2 [cite: 63, 64]
exp_times_2 = years_exp * 2 
print("Years * 2:", exp_times_2) # [cite: 64]

# Dot product (simulate salary projections) [cite: 65]
sample1 = np.array([1, 2, 3]) # [cite: 66]
sample2 = np.array([4, 5, 6]) # [cite: 67]
dot_result = np.dot(sample1, sample2) # [cite: 68]
print("Dot Product:", dot_result) # [cite: 69]
# Access individual element [cite: 74]
print("First year of experience:", years_exp[0]) # [cite: 75]

# Slice arrays: Access first two elements of first row [cite: 76, 77]
print("First two salaries:", salaries[0, 0:2]) 

# Access all rows for a specific column (second column) [cite: 78]
print("Second column salaries:", salaries[:, 1])

# Negative indexing for the last element [cite: 79, 80]
print("Last year of experience:", years_exp[-1])
# Reshape 1D array into 2x3 matrix [cite: 85]
reshaped_exp = np.reshape(np.arange(1, 7), (2, 3))
print("Reshaped Experience Array:\n", reshaped_exp)

# Flatten 2D array back into 1D [cite: 86]
flattened_exp = reshaped_exp.flatten()
print("Flattened Array:", flattened_exp) # [cite: 87]

# Transpose the array [cite: 91, 92]
print("Transposed Array:\n", reshaped_exp.T)
# Add a bonus array to salaries using broadcasting [cite: 96]
# Note: bonus must match columns in salaries (4 columns now)
bonus = np.array([5, 10, 15, 20]) # [cite: 97]
salaries_with_bonus = salaries + bonus # [cite: 98]
print("Salaries after bonus: \n", salaries_with_bonus)
print("Mean experience:", np.mean(years_exp)) # [cite: 103]
print("Std deviation of experience:", np.std(years_exp)) # [cite: 105]
print("Max salary:", np.max(salaries), "Min salary:", np.min(salaries)) # [cite: 107]
print("Sum of all salaries:", np.sum(salaries)) # [cite: 109]
angles = np.array([0, np.pi/4, np.pi/2]) # [cite: 115]
print("Sine of angles:", np.sin(angles)) # [cite: 116]
print("Cosine of angles:", np.cos(angles)) # [cite: 117]

# Apply function along rows (sum salaries per person) [cite: 118]
salary_sums = np.apply_along_axis(np.sum, 1, salaries)
print("Sum of Salaries per person:", salary_sums)
import pandas as pd # [cite: 124]

# Create random data and convert to DataFrame [cite: 125, 126]
data = np.random.randint(1, 50, size=(5, 3)) # [cite: 125]
df_data = pd.DataFrame(data, columns=['X', 'Y', 'Z']) # [cite: 127]
print("Generated Data: \n", df_data)

# Apply NumPy transformations to columns [cite: 128]
df_data['Log_X'] = np.log(df_data['X'])
df_data['Sqrt_Y'] = np.sqrt(df_data['Y'])
print("DataFrame with NumPy Transformations:\n", df_data) # [cite: 129]
# Save to CSV 
df_data.to_csv('sample_data.csv', index=False)

# Load back into a new DataFrame [cite: 134]
df_imported = pd.read_csv('sample_data.csv')

# Summary statistics [cite: 135, 136]
print("Summary Statistics:\n", df_imported.describe())
print("Column Means:\n", df_imported.mean()) # [cite: 138]
# Load dataset and clean missing values [cite: 144, 151]
# Note: Ensure 'survey_results_public.csv' is in your directory
df_kaggle = pd.read_csv('survey_results_public.csv')
df_subset = df_kaggle[['Country', 'EdLevel', 'YearsCodePro', 'ConvertedComp']] # [cite: 150]
df_clean = df_subset.dropna() # [cite: 151]

# Categorize experience [cite: 153, 154]
df_clean['ExperienceLevel'] = np.where(df_clean['YearsCodePro'] >= '10', 'Senior', 'Junior')

# Group data and compute average salary [cite: 155, 156]
grouped_data = df_clean.groupby(['Country', 'ExperienceLevel'])['ConvertedComp'].mean()
print("Grouped Average Salary:\n", grouped_data.head()) # [cite: 157]