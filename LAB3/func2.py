#ex1
# Write a function that takes a single movie and 
# returns True if its IMDB score is above 5.5
def check_score_greater(movie):
    return movie['imdb'] > 5.5
movie_title = input(" название фильма: ")
movie_imdb = float(input("IMDB рейтинг фильма: "))
movie = {'title': movie_title, 'imdb': movie_imdb}

# Проверка
if check_score_greater(movie):
    print(f"Фильм '{movie_title}' имеет хороший рейтинг! (Рейтинг выше 5.5)")
else:
    print(f"Фильм '{movie_title}' имеет низкий рейтинг. (Рейтинг ниже или равен 5.5)")


    
# Could change movie title from Dark Knight to any other
# and change to the corresponding element # from 2 to 
# whichever movie you want to see is above 5.5 or not


#ex2
# Write a function that returns a sublist of movies 
# with an IMDB score above 5.5. 
def filter_good_movies(movies):
    # Filter the list to include only movies with an IMDB score greater than 5.5
    return [movie for movie in movies if movie['imdb'] > 5.5]

movies = [
    {'title': 'Movie A', 'imdb': 6.7},
    {'title': 'Movie B', 'imdb': 4.3},
    {'title': 'Movie C', 'imdb': 7.8},
    {'title': 'Movie D', 'imdb': 5.4}
]

good_movies = filter_good_movies(movies)

print(good_movies)


#ex3
def return_movie_category(movies, cat_name):
    out_list = []
    for i in movies:
        curr_cat = i['category']
        if cat_name.lower() == curr_cat.lower():
            out_list.append(i)
    return out_list

movies = [
    {'title': 'Movie A', 'imdb': 6.7, 'category': 'Thriller'},
    {'title': 'Movie B', 'imdb': 4.3, 'category': 'Drama'},
    {'title': 'Movie C', 'imdb': 7.8, 'category': 'Thriller'},
    {'title': 'Movie D', 'imdb': 5.4, 'category': 'Comedy'}
]

print('Movies in the Thriller category are:')
out_list = return_movie_category(movies, 'Thriller')
for movie in out_list:
    print(f"Title: {movie['title']}, IMDB: {movie['imdb']}")

#ex4
# Write a function that takes a list of movies and computes 
# the average IMDB score.
def avg_imdb_score(movies): 
    total_score = 0
    total_movies = len(movies)
   
    for movie in movies:
        total_score += movie['imdb']
    

    if total_movies > 0:  
        avg_score = total_score / total_movies
    else:
        avg_score = 0  
    
    return avg_score

movies = [
    {'title': 'Movie A', 'imdb': 6.7},
    {'title': 'Movie B', 'imdb': 4.3},
    {'title': 'Movie C', 'imdb': 7.8},
    {'title': 'Movie D', 'imdb': 5.4}
]

print('Average IMDB score of all the movies is:')
avg_score = avg_imdb_score(movies)
print(avg_score)

#ex5# Function to filter movies by category
def return_movie_category(movies, cat_name):
    out_list = []
    for i in movies:
        curr_cat = i['category']
        if cat_name.lower() == curr_cat.lower():
            out_list.append(i)
    return out_list

# Function to calculate average IMDB score
def avg_imdb_score(movies): 
    total_score = 0
    total_movies = len(movies)
    
    # Summing up the IMDB scores of all the movies
    for movie in movies:
        total_score += movie['imdb']
    
    # Calculate average score
    if total_movies > 0:  
        avg_score = total_score / total_movies
    else:
        avg_score = 0  
    
    return avg_score

# Function to calculate average IMDB score for a specific category
def avg_imdb_acc_to_cat(movies, cat_name): 
    cat_movies = return_movie_category(movies, cat_name)  
    avg_score = avg_imdb_score(cat_movies)  
    return avg_score

# Sample movie list
movies = [
    {'title': 'Movie A', 'imdb': 6.7, 'category': 'Thriller'},
    {'title': 'Movie B', 'imdb': 4.3, 'category': 'Drama'},
    {'title': 'Movie C', 'imdb': 7.8, 'category': 'Thriller'},
    {'title': 'Movie D', 'imdb': 5.4, 'category': 'Comedy'},
    {'title': 'Movie E', 'imdb': 6.0, 'category': 'Thriller'}
]

# Compute and print the average IMDB score for a specific category
print('Average IMDB score of movies in the Thriller category is:')
avg_score_thriller = avg_imdb_acc_to_cat(movies, 'Thriller')
print(avg_score_thriller)
