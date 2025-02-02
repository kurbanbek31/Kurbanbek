#ex1
# Write a function that takes a single movie and 
# returns True if its IMDB score is above 5.5

def check_score_greater(movie): 
    if(movie['imdb']>5.5):
        return True
    else:
        return False

    
# Could change movie title from Dark Knight to any other
# and change to the corresponding element # from 2 to 
# whichever movie you want to see is above 5.5 or not
print ''
print 'Checking if Dark Knight is greater than 5.5'
print ''
is_greater=check_score_greater(movies[2])
if(is_greater):
    print 'True'
else :
    print 'False'

#ex2
# Write a function that returns a sublist of movies 
# with an IMDB score above 5.5. 

def sublist_movies_high_score(movies): 
    out_list=[];
    for i in range(0,len(movies)):
        curr_movie=movies[i];
        if curr_movie['imdb']>5.5:
            out_list.append(curr_movie)
    return out_list

print ''
print 'List of movies with an IMDB score > 5.5: '
print ''
out_list=sublist_movies_high_score(movies)
print out_list

#ex3
def return_movie_category(movies,cat_name): 
    out_list=[]
    for i in movies:
        curr_cat=i['category']
        if cat_name.lower()==curr_cat.lower():
            out_list.append(i)
    return out_list

# You could change to any category you'd like
print ''
print 'Movies in the Thriller are: '
print ''
out_list=return_movie_category(movies,'Thriller')
print out_list

#ex4
# Write a function that takes a list of movies and computes 
# the average IMDB score.

def avg_imdb_score(movies): 
    avg_score=0
    tot_movies=len(movies)
    for i in movies:
        avg_score=avg_score+i['imdb']
    avg_score=avg_score/tot_movies
    return avg_score

print ''
print 'Average IMDB score of all the movies is: '
s1=avg_imdb_score(movies)
print s1

#ex5
# Write a function that takes a category and computes

def avg_imdb_acc_to_cat(movies,cat_name): 
    cat_movies=return_movie_category(movies,cat_name)
    avg_score=avg_imdb_score(cat_movies)
    return avg_score

print ''
print 'Average IMDB of movies in the Thriller category is: '
s2=avg_imdb_acc_to_cat(movies,'Thriller')
print s2
