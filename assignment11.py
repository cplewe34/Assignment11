import pandas as pd

print("VIDEO GAME CATALOG MANAGER")

#Data on the games
df = pd.read_csv("video_games_raw.csv")


#user puts a numebr and the program will check if it is a valid input
while True:
    try:
        row_number = int(input("Enter a row number to inspect: "))
        if row_number < 0 or row_number >= len(df):
            raise IndexError
        break
    except ValueError:
        print("Please enter a whole number.")
    except IndexError:
        print("That row does not exist. Enter a number from 0 to", len(df) - 1)


#game uses the row number from the user to display the game information
game = df.iloc[row_number]
print("Selected Game:")
print("Title:", game["Title"])
print("Platform:", game["Platform"])
print("Genre:", game["Genre"])
print("Rating:", game["Rating"])
print("Current Status:", game["Status"])


#user inputs if they are playing the game or not 
while True:
    new_status = input("Enter a new status (Backlog or Completed or Playing or Dropped):\n").strip().capitalize()
    if  new_status == "Backlog" or new_status == "Completed" or new_status == "Playing" or new_status == "Dropped":
        break
    print("Invalid status. Please enter Backlog or Completed or Playing or Dropped.")

#updates if the user is playing the game or not
df.at[df.index[row_number], "Status"] = new_status

#adds a new column named recomended and starts them all at no
df["Recommended"] = "No"
#if a game meets the criteria it is changed to a yes
df.loc[(df["Rating"] >= 8) & (df["Price"] <= 40), "Recommended"] = "Yes"

# prints all recommended games using query to search for yes in recommended
print("Recommended Games:")
recommended = df.query("Recommended == 'Yes'")
print(recommended[["Title", "Platform", "Price", "Rating"]])

#saves updated data to new dataframe
df.to_csv("video_games_cleaned.csv", index=False)

print("The catalog has been updated.")
print("Saved as video_games_cleaned.csv.")