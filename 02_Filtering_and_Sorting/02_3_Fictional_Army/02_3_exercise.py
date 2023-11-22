import pandas as pd

raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

df = pd.DataFrame(raw_data)

print(df)


# Step 4. Set the 'origin' colum as the index of the dataframe
origin_indexed = df.set_index('origin')
print(origin_indexed)

# Step 5. Print only the column veterans
veterans = df['veterans']
print(veterans)

# Step 6. Print the columns 'veterans' and 'deaths'
veterans_and_deaths = df[['veterans', 'deaths']]
print(veterans_and_deaths)

# Step 7. Print the name of all the columns.
print(df.columns)
for column in df.columns:
    print(column)

# Step 8. Select the 'deaths', 'size' and 'deserters' columns from Maine and Alaska
# 1. solution:
result = df.loc[df['origin'].isin(['Maine', 'Alaska']), ['deaths', 'size', 'deserters']]
print(result)

# 2. solution (bo mamy kolumne index):
df.set_index('origin', inplace=True)
result2 = df.loc[['Maine', 'Alaska'], ['deaths', 'size', 'deserters']]
print(result2)

# Step 9. Select the rows 3 to 7 and the columns 3 to 6
print(df.iloc[2:7, 2:6])

# Step 10. Select every row after the fourth row and all columns
print(df.iloc[4:, :])

# Step 11. Select every row up to the 4th row and all columns
print(df.iloc[:4, :])

# Step 12. Select the 3rd column up to the 7th column
print(df.iloc[:, 2:7])

# Step 13. Select rows where df.deaths is greater than 50
print(df[df['deaths'] > 50])

# Step 14. Select rows where df.deaths is greater than 500 or less than 50
print(df[(df['deaths'] > 500) | (df['deaths'] < 50)])

# Step 15. Select all the regiments not named "Dragoons"
print(df[df['regiment'] != 'Dragoons'])

# Step 16. Select the rows called Texas and Arizona
print(df.loc[['Texas', 'Arizona']])

# Step 17. Select the third cell in the row named Arizona
# 1. solution:
print(df.loc['Arizona'][2])

# 2. solution:
print(df.loc[["Arizona"]].iloc[:, 2])

# Step 18. Select the third cell down in the column named deaths
# 1. solution:
print(df.iloc[2, :].loc[['deaths']])

# 2. solution:
print(df.iloc[2, :]['deaths'])
