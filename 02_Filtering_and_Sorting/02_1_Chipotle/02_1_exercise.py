import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
df = pd.read_csv(url, sep='\t')

print(df)
print(df.columns)

# Step 4. How many products cost more than $10.00?
df['price_in_float'] = df['item_price'].map(lambda x: float(x[1:]))
n = df[df['price_in_float'] > 10]['item_name'].value_counts().sum()
print(n)

# Step 5. What is the price of each item?
unique_items = df['item_name'].unique()

prices_dict = {}

for item in unique_items:
    item_filter = df['item_name'] == item

    price_per_unit = df[item_filter]['price_in_float'].iloc[0] / df[item_filter]['quantity'].iloc[0]

    prices_dict[item] = price_per_unit

for item, price_per_unit in prices_dict.items():
    print(f'{item} : {price_per_unit}')

# Step 6. Sort by the name of the item
print(df.sort_values('item_name'))

# Step 7. What was the quantity of the most expensive item ordered?
df['price_per_item'] = df['price_in_float'] / df['quantity']
max_price = df[df['price_per_item'] == df['price_per_item'].max()][['item_name', 'price_per_item']].iloc[0]
print(max_price)

# Step 8. How many times was a Veggie Salad Bowl ordered?
veggie_salad_bowl = df[df['item_name'] == 'Veggie Salad Bowl']
n = veggie_salad_bowl['quantity'].sum()
print(n)

# Step 9. How many times did someone order more than one Canned Soda?
canned_soda = df[(df['item_name'] == 'Canned Soda') & (df['quantity'] > 1)]
suma = canned_soda['quantity'].count()
print(suma)
