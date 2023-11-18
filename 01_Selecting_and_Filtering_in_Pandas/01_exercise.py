import pandas as pd

file_path = 'melb_data.csv'
df = pd.read_csv(file_path)

# 1. List of columns
print(df.columns)

# 2. From the list of columns, find a name of the column with the sales prices of the homes.
# Use the dot notation to extract this to a variable (as you saw above to create melbourne_price_data.)
df_price = df['Price']
print(df_price.head())

# 3. Use the head command to print out the top few lines of the variable you just created.
print(df_price.head())

# 4. Pick any two variables and store them to a new DataFrame (as you saw above to create two_columns_of_data.)
two_columns = ['Landsize', 'Distance']
df_two_columns = df[two_columns]
print(df_two_columns.head())

# 5. Use the describe command with the DataFrame you just created to see summaries of those variables.
print(df_two_columns.describe())
