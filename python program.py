import pandas as pd
df = pd.read_csv(r"C:\\Users\\admin\\Desktop\\dishwa\\dmw\\Practical 2\\NBA_2018-19_Season.csv", delimiter = ',', on_bad_lines='skip') #error_bad_lines = False

print("1. Average age of the players whi have played for NBA?\n")
avg = df['Age'].mean()
print(avg)

print("-----\n2. How many games has each player played?\n")
total_games_played = df[['Player', 'Games']]
print(total_games_played.head(10))

print("-----\n3. How many teams in total are there in NBA?\n")
print(len(df['Team'].unique()))

print("-----\n4. What is the minimum age of the player that has played for NBA?\n")
print(df['Age'].min())

print("-----\n5. What is the maximum age of the player that has played for NBA? His details?\n")
print(df[df.Age == df.Age.max()])

print("-----\n6. How many games have been organized in Eastern region?\n")
df2 = df[df['Conference']=='Eastern']
count = len(df2)
print(count)

print("-----\n7. How many regions (conference) are there where the games have been organized?\n")
df2 = df['Conference'].unique()
for x in df2:
    print(x)

print("-----\n8. Display the list of the player who have played in the team called Boston Celtics.\n")
df2 = df['Team']=='Boston Celtics'
player_list = df['Player'][df2].tolist()
for x in player_list:
    print(x)

print("-----\n9. What is the total number of games organized in each division?\n")
division = df['Division'].unique()
for x in division:
    print(x," ",end="")
    print(df['Division'][df['Division']==x].count())

print("-----\n10. Which player has scored the maximum number of goals?\n")
max = df['Field Goals'].max()
print(df.loc[df['Field Goals'] ==max]['Player'].to_string(index=False))

print("-----\n11. Which player has the lowest number of personal fouls?\n")
min = df['Personal Fouls'].min()
print(df.loc[df['Personal Fouls'] == min]['Player'].to_string(index=False))

print("-----\n12. Which players have attempted the 3-ponts field goals the highest number of times and what are the percentage of it?\n")
max = df['3-Point Field Goal Attempts'].max()
print(df.loc[df['3-Point Field Goal Attempts'] ==max][['Player','3-Point Field Goal Percentage']].to_string(index=False))

print("-----\n13. What is the average point scored by all the players?\n")
avg1 = df['Points'].mean()
print(avg1)
