
import csv
from tempfile import NamedTemporaryFile
from os.path import abspath

import logging

from matplotlib import pyplot as plt


def top_n_highest_rated_movies(movies_data, number = 10):

    """
        This function takes list of movies and integer for top N movies as an arguments, 
        sort it by IMDB ID and IMDB Sore and returns a dictionary containing movie ids 
        and score respectively.
    """

    movie_score = {}
    for score in movies_data:
        movie_score[score['imdbId']] = score['IMDB Score']

    sorted_movies = sorted(movie_score.items(), key=lambda x: x[1], reverse=True)

    top_n_highest_rated_movies = []
    for i in range(min(number, len(sorted_movies))):
        movie_id, score = sorted_movies[i]
        title = [movie_title['Title'] for movie_title in movies_data if movie_title['imdbId'] == movie_id]
        genre = [movie_title['Genre'] for movie_title in movies_data if movie_title['imdbId'] == movie_id]
        top_n_highest_rated_movies.append({"Title": title[0], "score": score, "Genre": genre[0]})
        print(f"{i + 1}. {title[0]}: {score}")
    
    return top_n_highest_rated_movies

def total_number_of_movies(movies_data):
    """
        Get the total number of movies from csv file.
    """
    return len(movies_data)

def get_average_score_of_all_movies(movies_data):

    """
        This function return average score of all the movies from csv file and returns as float.
    """

    sum_of_score = 0
    for movie in movies_data:
        if not len(movie['IMDB Score']) == 0:
            sum_of_score += float(movie['IMDB Score'])
    
    average_score_of_all_movies = sum_of_score / total_number_of_movies(movies_data)

    print(f"Average score of all movies:{average_score_of_all_movies: .2f}")

    return average_score_of_all_movies


def filter_movies_by_genre(movies_data, genre):

    movies_genre = []

    for movie in movies_data:
        movie_genres = str(movie['Genre']).split('|')
        if genre in movie_genres:
            movies_genre.append(movie)
            print(f"{movie['Title']}: {movie['Genre']}")

    return movies_genre

def find_and_display_unique_genre(movies_data):

    all_unique_genre = set()
    for movie in movies_data:
        if not len(movie['Genre']) == 0:
            movie_genres = str(movie['Genre']).split('|')
            all_unique_genre.update(movie_genres)

    print("Unique Genres:")
    for unique_genre in sorted(all_unique_genre):
        print(unique_genre) 

def update_movie_rating(movies_data, movie_id, movie_score):

    """
       Function update_movie_rating takes three arguments, movies_data, movie_id, and movie_score.
       It updates the score of a movie by movie_id and updates it in to csv file.
    """

    updated_movie = []

    for movie in movies_data:
        if movie_id == movie['imdbId']:
            row = {
                "imdbId": movie["imdbId"], 
                "Imdb Link": movie["Imdb Link"], 
                "Title": movie["Title"],
                "IMDB Score": movie_score,
                "Genre": movie["Genre"],
                "Poster": movie["Poster"]
            }
            updated_movie.append(row)
        updated_movie.append(movie)

    try:
        with open(abspath("movies.csv"), "w", newline='', encoding="utf-8") as csvfile:
            fieldnames = ["imdbId", "Imdb Link", "Title", "IMDB Score", "Genre", "Poster"]
            writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames) 
            writer.writerow(dict((heads, heads) for heads in fieldnames))
            writer.writerows(updated_movie)      
    except FileNotFoundError as exc:
        logging.error(f"Exception occurred while writing to CSV file with Error {exc}")

    csvfile.close()

    print("File updated!")

def recommend_movie(rows):
    """
        This function takes movies list and recommends movie based on users preferred Genre and highest rating for that genre.
    """
    movies_by_genre = filter_movies_by_genre(rows, "Action")

    top_highest_rated_movies = top_n_highest_rated_movies(movies_by_genre, 5)

    for recommended_movie in top_highest_rated_movies:
        print(f"{recommended_movie['Title']} - {recommended_movie['score']} - {recommended_movie['Genre']}")


def plot_distribution_chart(rows):
    scores = [float(row['IMDB Score']) for row in rows if not len(row['IMDB Score']) == 0]

    plt.hist(scores, bins=10, color='skyblue', edgecolor='black')
    plt.title('Distribution of Movie Scores')
    plt.xlabel('Scores')
    plt.ylabel('Number of Movies')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
def main():

    try:
        movie_data_file = open(abspath("movies.csv"), encoding="utf8", errors="ignore")
    
    except (FileNotFoundError, AttributeError) as exc:
        logging.error(f"Exception occurred while reading CSV file with error: {exc}")
    
    # Task 1
    csv_data = csv.DictReader(movie_data_file)
    rows = []
    for row in csv_data:
        rows.append(row)

    print(rows[1:10])
    
    total_movies = total_number_of_movies(rows)
    print(f"Total number of movies: {total_movies}")

    # # Task 2
    get_average_score_of_all_movies(rows)
    top_n_highest_rated_movies(rows, 10)

    # Task 3
    filter_movies_by_genre(rows, "Comedy")
    find_and_display_unique_genre(rows)
        
    # Task 4
    update_movie_rating(rows, "114709", "8.5")
    recommend_movie(rows)
        
    # Task 5
    plot_distribution_chart(rows)
    

if __name__ == "__main__":
    main()