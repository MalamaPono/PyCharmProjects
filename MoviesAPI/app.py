# Keep in mind that requests module is different from urllib request module.
# The requests module has different methods like .text to get the data from the response
# where as request module in urllib uses the .read() method to get the data from a response object.
# In this project I decided to use the requests module just for practice since many of my other
# projects have been using urllib.

# .text method in requests module already decodes the binary data received from the api
# and returns a string format of the data returned

import requests
import json
tastedive_baseurl = 'https://tastedive.com/api/similar?'
omdb_baseurl = 'http://www.omdbapi.com/?'

def get_movies_from_tastedive(find_similar):
    params = {}
    params['q'] = find_similar
    params['limit'] = 5
    params['type'] = 'movies'
    response = requests.get(tastedive_baseurl,params=params)
    str_data = response.text
    data = json.loads(str_data)
    return data

def extract_movie_titles(data):
    movie_titles = []

    movies_list = data['Similar']['Results']
    for movie in movies_list:
        movie_titles.append(movie['Name'])

    return movie_titles

def get_related_titles(movie_titles):
    final_titles_list = movie_titles[:]
    for title in movie_titles:
        related_movies = get_movies_from_tastedive(title)
        related_movies_titles = extract_movie_titles(related_movies)
        for movie_title in related_movies_titles:
            if movie_title not in final_titles_list:
                final_titles_list.append(movie_title)
    return final_titles_list

def get_movie_data(movie_title):
    params = {}
    params['t'] = movie_title
    params['r'] = 'json'
    params['apikey'] = 'a99fe0a2'
    # apikey key, value must be appended to the very end of the url
    response = requests.get(omdb_baseurl, params=params)
    str_data = response.text
    data = json.loads(str_data)
    return data

def get_movie_rating(movie_data):
    ratings = movie_data['Ratings']
    rotten_tomatoes = 0
    for rating in ratings:
        if rating['Source'] == 'Rotten Tomatoes':
           percent = rating['Value']
           rotten_tomatoes = int(percent.replace('%',''))
    return rotten_tomatoes

def get_sorted_recommendations(movie_title):
    data = get_movies_from_tastedive(movie_title)
    movie_titles = extract_movie_titles(data)
    final_titles_list = get_related_titles(movie_titles)

    # now sort the final list of movie titles by their rotten tomato rating
    ratings = []
    for title in final_titles_list:
        ratings.append(get_movie_rating(get_movie_data(title)))

    tuples = list(zip(ratings,final_titles_list))
    tuples = sorted(tuples,reverse=True)

    sorted_titles = []
    for entry in tuples:
        sorted_titles.append(entry[1])

    return sorted_titles

sorted_titles = get_sorted_recommendations("Black Panther")
print(sorted_titles)


