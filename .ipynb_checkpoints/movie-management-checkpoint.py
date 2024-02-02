
import csv
from os.path import abspath

def main():
    movie_data_file = open(abspath("movies.csv"), encoding="utf8", errors="ignore")
    csv_data = csv.DictReader(movie_data_file)
    rows = []
    print(next(csv_data))
    # for row in csv_data:
        # print(row["imdbId"])
    





if __name__ == "__main__":
    main()