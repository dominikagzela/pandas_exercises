import pandas as pd

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
df = pd.read_csv(url, sep=',')

# print(df)
print(df.columns)

# Step 4. Select only the Goal column.
goal_column = df['Goals']
print(goal_column)

# Step 5. How many team participated in the Euro2012?
count_teams = df['Team'].count()
print(count_teams)

# Step 6. What is the number of columns in the dataset?
number_of_column = df.shape[1]
print(number_of_column)

# Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = df[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline)

# Step 8. Sort the teams by Red Cards, then to Yellow Cards
teams_sorted = discipline.sort_values(by=['Red Cards', 'Yellow Cards'])
print(teams_sorted)

# Step 9. Calculate the mean Yellow Cards given per Team
yellow_cards = discipline['Yellow Cards'].mean()
print(round(yellow_cards, 2))

# Step 10. Filter teams that scored more than 6 goals
goals_more_than_6 = df[df['Goals'] > 6][['Team', 'Goals']]
print(goals_more_than_6)

# Step 11. Select the teams that start with G
teams_start_with_G = df[df['Team'].str.startswith('G')]
print(teams_start_with_G)

# Step 12. Select the first 7 columns
first_7_columns = df.head(7)
print(first_7_columns)

# Step 13. Select all columns except the last 3.
all_columns_minus_three = df.iloc[:, :-3]
print(all_columns_minus_three)

# Step 14. Present only the Shooting Accuracy from England, Italy and Russia
# 1) solution:
shooting_accuracy_for_3_countries = df[df['Team'].isin(['England', 'Italy', 'Russia'])][['Team', 'Shooting Accuracy']]
print(shooting_accuracy_for_3_countries)

# 2) solution:
shooting_accuracy_for_3_countries_2 = df.loc[df['Team'].isin(['England', 'Italy', 'Russia']), ['Team', 'Shooting Accuracy']]
print(shooting_accuracy_for_3_countries_2)
