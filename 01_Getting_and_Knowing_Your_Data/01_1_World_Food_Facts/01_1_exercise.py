import pandas as pd

file_path = 'food_facts.tsv'
df = pd.read_csv(file_path, sep='\t')

# Step 4. See the first 5 entries
print(df.head(5))
print(df.loc[:4])

# Step 5. What is the number of observations in the dataset?
print(df.shape[0])

# Step 6. What is the number of columns in the dataset?
print(df.shape[1])

# Step 7. Print the name of all the columns.
print(df.columns)

# Step 8. What is the name of 105th column?
print(df.columns[104])

# Step 9. What is the type of the observations of the 105th column?
print(df.dtypes['-glucose_100g'])

# Step 10. How is the dataset indexed?
print(df.index)

# Step 11. What is the product name of the 19th observation?
print(df['product_name'][18])
# OR
index_of_column = df.columns.get_loc('product_name')
print(df.values[18][index_of_column])
# OR
print(df['product_name'].loc[18])
