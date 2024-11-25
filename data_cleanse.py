og_data = ["users.dat", "movies.dat", "ratings.dat"]
csv_data = ["users.csv", "movies.csv", "ratings.csv"]

# IMPORTANT: movies.dat can't be converted to a csv because
#            many of the titles contain commas which results in 
#            misalignment when reformatting
def convert_to_csv(og_data_list, csv_data_list, delimitter="::"):
    """
    Converts each file in the old data to a csv given the delimitter

    arg1: og_data_list -> list of file names of the original data
    arg2: csv_data_list -> list of file names for og data to be put into after csv conversion
    arg3 (default parameter): deilimitter -> text/string to split line on
    """
    for og_file, csv_file in zip(og_data_list, csv_data_list):
        read = open(og_file, "r")
        write = open(csv_file, "w")
        for line in read.readlines():
            values = line.split(delimitter)
            csv_line = ""
            for value in values:
                csv_line += (value + ",") if value != values[-1] else value
            write.write(csv_line)

def make_romance_only_file(movies_dat, romance_dat):
    """
    Takes a file of movies with various genres and copies all lines where Romance is one of the genres
    """
    all_movies = open(movies_dat, "r")
    romance_only = open(romance_dat, "w")
    for line in all_movies.readlines():
        if "Romance" in line or "romance" in line:
            romance_only.write(line)

def make_romance_only_file(romance_movies_file, file_to_clean, new_file, movie_id_index):
    """
    Finds the movie id's that are associated with Romance and 
    adjusts other files to only include rows that have a romance
    movie in them
    """
    
    romance_movie_data = open(romance_movies_file, "r", errors=="")
    all_lines = romance_movie_data.readlines()
    romance_movie_ids = [cur_movie_data.split("::")[0] for cur_movie_data in all_lines]

    # All files should have first row be column headers - descriptions - so ignore it
    old_data = open(file_to_clean[1:], "r")
    new_data = open(new_file, "w")    
    
    
    for line in old_data.readlines():
        if line.split(",")[movie_id_index] in romance_movie_ids:
            new_data.write(line)
    

make_romance_only_file("romance.txt", "ratings.csv", "romance_ratings.csv", 1)