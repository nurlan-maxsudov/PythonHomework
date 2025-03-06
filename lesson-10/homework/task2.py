import requests

# api_url = "https://api.themoviedb.org/3/discover/movie/?api_key=2827a5657a4fabed058eb5608907faa0"

# genres = "Drama"

# parameters = {
#     "include_adult": True,
#     "language": "en-US",
#     "include_video": False,
#     "page": 1,
#     "with_genres": genres,
#     "sort_by": "popularity.desc"
# }

# response = requests.get(api_url, params=parameters)

# data = response.json()
# print(data)

import requests

genres ={
    "Action": 28,
    "Advanture": 12,
    "Animation": 16,
    "Comedy": 35,
    "Crime": 80,
    "Documentary": 90,
    "Drama": 18,
    "Fantasy": 14,
    "History": 36,
    "Horror": 27,
    "Family": 10751,
    "Romance": 10749
}

for key in genres.keys():
    print(f"{key}")

try:
    user_input = input("Choose a genre: ").capitalize()

    genre = genres[user_input]
except KeyError:
    print("Invalid genre selected. Please choose a valid genre from the list")
    exit()

parameters = {
    "include_adult": True,
    "include_video": False,
    "language": "en-US",
    "sort_by": "popularity.desc",
    "page": 1,
    "with_genres" : genre
}


url = "https://api.themoviedb.org/3/discover/movie?api_key=2827a5657a4fabed058eb5608907faa0"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyODI3YTU2NTdhNGZhYmVkMDU4ZWI1NjA4OTA3ZmFhMCIsIm5iZiI6MTc0MTIzNDcwMi4zMTMsInN1YiI6IjY3YzkyMjBlZTIyMDRmYzljMDBjY2E3NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hxDW7LTUATj1Kc4bXmxHLzM9lzDpp70hsacIr2Mkzho"
}

import random

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()["results"]


try:
    random_movie = random.randint(0, 19)
    
    title = data[random_movie]["title"]
    overiew = data[random_movie]["overview"]
    release_date = data[random_movie]["release_date"]
    
    print("Title: ", end="")
    print(title, end="\n")
    print("Overiew: ", end="")
    print(overiew, end="\n")
    print("Release_date: ", end="")
    print(release_date, end="\n")
except IndexError:
    print("No movies found for the selected genre.")
except KeyError as e:
    print(f"Error accessign movie data: {e}")
    
    

# print(title)
# print(overiew)