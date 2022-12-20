import requests
import csv

"""This will fetch fantasy premier league classic league data based on the league id selected and 
generate a csv file that includes most recent gameweek points along with the rank and total classic score"""
ultimate_league_id = 376769
s12_league_id = 376750
TOTAL_PAGES = 0
option = int(input("select '1' for Ultimate league and '2' for S12 classic league: "))

if option == 1:
    league_id = ultimate_league_id
    TOTAL_PAGES = 4

if option == 2:
    league_id = s12_league_id
    TOTAL_PAGES = 5
else:
    KeyError

# Set the URL for the export API
url = f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/?event=1"

# Initialize an empty list to store the data
standings = []

# Indicate if there are more pages of data
more_pages = True

# Set the starting page number
page = 1

while more_pages:
    # Make a request to the API
    params = {"page_standings": page}
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # If the request was successful, get the data from the response
        data = response.json()
        # print(data)

        # Extract the relevant data from the response
        standings += data["standings"]["results"]

        # Check if there are more pages
        more_pages = data["standings"]["has_next"]
        print(f"page {page} completed")
        page += 1

        # set the page value equal to the total pages + 1, so that it will end gathering the data
        if page > TOTAL_PAGES:
            print("All pages completed")
            more_pages = False
    else:
        # If the request was not successful, print an error message and break the loop
        print(f"Error fetching data: {response.status_code}")
        more_pages = False

if option == 1:
    # Write the data to a CSV file
    with open("ultimateleague_standings.csv", "w", newline="") as csvfile:

        fieldnames = [
            "Position",
            "Player",
            "Team_id",
            "Gameweek Point",
            "Points",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for standing in standings:
            row = {
                "Position": standing["rank"],
                "Player": standing["player_name"],
                "Team_id": standing["entry"],
                "Gameweek Point": standing["event_total"],
                "Points": standing["total"],
            }
            writer.writerow(row)
        print("Completed")
        print("work is done check ultimateleague_standings.csv")
if option == 2:
    # Write the data to a CSV file
    with open("classicleague_standings.csv", "w", newline="") as csvfile:

        fieldnames = [
            "Position",
            "Player",
            "Team_id",
            "Gameweek Point",
            "Points",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for standing in standings:
            row = {
                "Position": standing["rank"],
                "Player": standing["player_name"],
                "Team_id": standing["entry"],
                "Gameweek Point": standing["event_total"],
                "Points": standing["total"],
            }
            writer.writerow(row)
        print("Completed")
        print("work is done check classicleague_standings.csv")
