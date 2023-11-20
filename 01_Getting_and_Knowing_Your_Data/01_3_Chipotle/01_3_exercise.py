import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
df = pd.read_csv(url, sep='\t')

# Step 4. See the first 10 entries
print(df.head(10))

# Step 5. What is the number of observations in the dataset?
print(df.shape[0])

# Step 6. What is the number of columns in the dataset?
print(df.shape[1])

# Step 7. Print the name of all the columns.
print(df.columns)

# Step 8. How is the dataset indexed?
print(df.index)

# Step 9. Which was the most-ordered item?
x = df.groupby('item_name')['quantity'].sum()
x_sort = x.sort_values(ascending=False).head(1).reset_index()
print(x_sort)

# Step 10. For the most-ordered item, how many items were ordered?
print(x_sort[['quantity']])

# Step 11. What was the most ordered item in the choice_description column?
y = df.groupby('choice_description')['quantity'].sum()
y_sort = y.sort_values(ascending=False).head(1).reset_index()
print(f'y_sort : ', y_sort)

# Step 12. How many items were ordered in total?
print(df['quantity'].sum())

# Step 13. Turn the item price into a float
print(df['item_price'])
# Step 13.a. Check the item price type
print(df['item_price'].dtype)

# Step 13.b. Create a lambda function and change the type of item price
float_type = df['item_price'].map(lambda x: float(x[1:]))

# Step 13.c. Check the item price type
print(float_type)
df['item_price'] = float_type
print(df['item_price'])

# Step 14. How much was the revenue for the period in the dataset?
print(df.columns)

# Step 15. How many orders were made in the period?
sum_of_revenue = (df['quantity'] * df['item_price']).sum()
print(sum_of_revenue)

# Step 16. What is the average revenue amount per order?
df['revenue'] = (df['quantity'] * df['item_price'])
revenue_per_item = df.groupby('item_name')['revenue'].mean()
print(revenue_per_item)

# Step 17. How many different items are sold?
print(df['item_name'].value_counts().count())