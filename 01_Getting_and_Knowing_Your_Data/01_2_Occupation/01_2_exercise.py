import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
df = pd.read_csv(url, sep='|')


# Step 4. See the first 25 entries
print(df[:25])

# Step 5. See the last 10 entries
print(df.tail(10))

# Step 6. What is the number of observations in the dataset?
print(df.shape[0])

# Step 7. What is the number of columns in the dataset?
print(df.shape[1])

# Step 8. Print the name of all the columns.
print(df.columns)

# Step 9. How is the dataset indexed?
print(df.index)

# Step 10. What is the data type of each column?
print(df.info())
print(df.dtypes)

# Step 11. Print only the occupation column
print(df['occupation'])

# Step 12. How many different occupations are in this dataset?
print(df['occupation'].drop_duplicates().count())
# OR
print(df['occupation'].nunique())

# Step 13. What is the most frequent occupation?
print(df['occupation'].value_counts().head(1))

# Step 14. Summarize the DataFrame.
print(df.describe())

# Step 15. Summarize all the columns
print(df.describe(include='all'))

# Step 16. Summarize only the occupation column
print(df.occupation.describe())

# Step 17. What is the mean age of users?
print(round(df['age'].mean()))

# Step 18. What is the age with least occurrence?
print((df['age'].value_counts().tail()))

