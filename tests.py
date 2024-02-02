import unittest
from movie_management import total_number_of_movies, get_average_score_of_all_movies, top_n_highest_rated_movies


class TestMovieManagement(unittest.TestCase):

    test_data = [
        {'imdbId': '1000', 'Imdb Link': 'http://www.imdb123.com', 'Title': 'Movie A', 'IMDB Score': '2.9', 'Genre': 'Action|Adventure|Family', 'Poster': 'https://images-na.com'},
        {'imdbId': '1001', 'Imdb Link': 'http://www.imdb123.com', 'Title': 'Movie B', 'IMDB Score': '1.9', 'Genre': 'Comedy|Adventure|Family', 'Poster': 'https://images-na.com'},
        {'imdbId': '1002', 'Imdb Link': 'http://www.imdb123.com', 'Title': 'Movie C', 'IMDB Score': '2.9', 'Genre': 'Horror|Adventure|Family', 'Poster': 'https://images-na.com'},
        {'imdbId': '1003', 'Imdb Link': 'http://www.imdb123.com', 'Title': 'Movie D', 'IMDB Score': '3.9', 'Genre': 'Music|Adventure|Family', 'Poster': 'https://images-na.com'},
        {'imdbId': '1004', 'Imdb Link': 'http://www.imdb123.com', 'Title': 'Movie E', 'IMDB Score': '4.9', 'Genre': 'Musical|Adventure|Family', 'Poster': 'https://images-na.com'},
        {'imdbId': '1005', 'Imdb Link': 'http://www.imdb123.com', 'Title': 'Movie F', 'IMDB Score': '5.9', 'Genre': 'Romance|Adventure|Family', 'Poster': 'https://images-na.com'},
        {'imdbId': '1006', 'Imdb Link': 'http://www.imdb123.com', 'Title': 'Movie G', 'IMDB Score': '6.9', 'Genre': 'Romedy|Adventure|Family', 'Poster': 'https://images-na.com'},
        {'imdbId': '1007', 'Imdb Link': 'http://www.imdb123.com', 'Title': 'Movie H', 'IMDB Score': '7.9', 'Genre': 'Sci-Fi|Adventure|Family', 'Poster': 'https://images-na.com'},
        {'imdbId': '1008', 'Imdb Link': 'http://www.imdb123.com', 'Title': 'Movie I', 'IMDB Score': '8.9', 'Genre': 'Thriller|Adventure|Family', 'Poster': 'https://images-na.com'},
        {'imdbId': '1009', 'Imdb Link': 'http://www.imdb123.com', 'Title': 'Movie J', 'IMDB Score': '9.9', 'Genre': 'Documentary|Adventure|Family', 'Poster': 'https://images-na.com'},
        ]
    def test_total_movies_count(self):

        total_count = total_number_of_movies(self.test_data)

        self.assertEqual(total_count, 10)
    
    def test_avarage_score_of_all_movies(self):

        avg_score = get_average_score_of_all_movies(self.test_data)
        self.assertEqual(avg_score, 5.6)
    
    def test_top_n_highest_rated_movies(self):
        
        highest_rated_movies = top_n_highest_rated_movies(self.test_data, 5)
        self.assertEqual(highest_rated_movies[0]['score'], "9.9")
    


if __name__ == '__main__':
    unittest.main()

