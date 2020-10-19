import requests
import bs4
import re
import numpy as np
import math


def extraction_from_link(database, link):
    counter = 1
    headers = {'Accept-Language': 'en-US,en;q=0.8'}
    res = requests.get(link, headers=headers)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    f = open("C:\MyBrain\DM\Project\movie_titles.txt", "a")

    for foo in soup.find_all('div', attrs={'class': 'lister-item-content'}):
        movie_title = foo.find('a', attrs={'href': re.compile("/title/")}).text
        genre = foo.find('span', attrs={'class': re.compile("genre")}).text
        rating = foo.find('span', attrs={'class': re.compile("ipl-rating-star__rating")}).text
        year = foo.find('span', attrs={'class': re.compile("lister-item-year text-muted unbold")}).text
        year = year.replace('(', '')
        year = year.replace(')', '')
        # print(f"{movie_title}  {genre}  {rating} {year}")
        database = np.vstack([database, [movie_title, year, rating, genre]])
        # f.write(movie_title + '\n')
        counter = counter + 1
    return database


def collect_data():
    print("Extracting data...")
    print("It might take some minutes...")
    print("!!! We extract only movies relased before 2011 !!!")
    list_of_movies = []
    database = np.array(["Title", "Year", "Rating", "Genre"])

    try:
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=1&sort=list_order,asc")
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?sort=list_order,asc&st_dt=&mode=detail&page=2")
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=3&sort=list_order,asc")
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=4&sort=list_order,asc")
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=5&sort=list_order,asc")
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=6&sort=list_order,asc")
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=7&sort=list_order,asc")
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=8&sort=list_order,asc")
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=9&sort=list_order,asc")
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=10&sort=list_order,asc")
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=11&sort=list_order,asc")
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=12&sort=list_order,asc")
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=13&sort=list_order,asc")
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=14&sort=list_order,asc")
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=15&sort=list_order,asc")
        database = extraction_from_link(database,
                                        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=16&sort=list_order,asc")
    except:
        print("\n\nError at extracting data from IMDB!")
        print("To run this program, you must have internet connection!\n\n")
    return database


def get_genre_for_movie(movie):
    coord = [movie[0], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # if "Action" in movie[3]:
    #     coord[1] == 1
    if movie[3].find("Action") != -1:
        coord[1] = 1
    if movie[3].find("Adventure") != -1:
        coord[2] = 1
    if movie[3].find("Animation") != -1:
        coord[3] = 1
    if movie[3].find("Children's") != -1:
        coord[4] = 1
    if movie[3].find("Comedy") != -1:
        coord[5] = 1
    if movie[3].find("Crime") != -1:
        coord[6] = 1
    if movie[3].find("Documentary") != -1:
        coord[7] = 1
    if movie[3].find("Drama") != -1:
        coord[8] = 1
    if movie[3].find("Fantasy") != -1:
        coord[9] = 1
    if movie[3].find("Film-noir") != -1:
        coord[10] = 1
    if movie[3].find("Horror") != -1:
        coord[11] = 1
    if movie[3].find("Musical") != -1:
        coord[12] = 1
    if movie[3].find("Western") != -1:
        coord[13] = 1
    if movie[3].find("Mystery") != -1:
        coord[14] = 1
    if movie[3].find("Romance") != -1:
        coord[15] = 1
    if movie[3].find("Sci-Fi") != -1:
        coord[16] = 1
    if movie[3].find("Thriller") != -1:
        coord[17] = 1
    if movie[3].find("War") != -1:
        coord[18] = 1

    problem = True
    for elem in range(1, len(coord)):
        if coord[elem] == 1:
            problem = False
            break
    if problem == True and coord[0] != "Title":
        print(coord)
    return coord


def choose_from_keyword_suggestions(database, find_titles):
    print("Select which you initially wanted?")
    for elem in range(len(find_titles)):
        print(
            f"{elem + 1} {find_titles[elem][0]} \n\t Year: {find_titles[elem][1]} \n\t Rating: {find_titles[elem][2]} \n\t Genre: {find_titles[elem][3]}")
    try:
        decide = int(input("Enter which one you choose? (enter the number of it): "))
        if not 0 < decide <= len(find_titles):
            raise Exception("Sorry")
    except:
        print(f"You must enter a number between 1 - {len(find_titles)}")
        return choose_from_keyword_suggestions(database, find_titles)
    if 0 < decide <= len(find_titles):
        return find_titles[decide - 1]
    else:
        return choose_from_keyword_suggestions(database, find_titles)


def find_movie_by_keyword(database):
    movie_key = input("Please enter a movie title: ")
    find_titles = []
    for elem in database:
        if movie_key in elem[0]:
            find_titles.append(elem)
    if len(find_titles) == 0:
        print("There is not such movie, please try again!")
        return find_movie_by_keyword(database)
    elif len(find_titles) == 1:
        print(
            f" Title: {find_titles[0][0]} \n\t Year: {find_titles[0][1]} \n\t Rating: {find_titles[0][2]} \n\t Genre: {find_titles[0][3]}")
        # print("Is this movie you are looking for? yes/no: ")
        decide = input("Is this movie you are looking for? yes/no: ")
        if decide == 'yes':
            return find_titles[0]
        else:
            print("Movie not found, try again!")
            return find_movie_by_keyword(database)
    else:
        return choose_from_keyword_suggestions(database, find_titles)


def get_prefered_movie(database):
    print("You can either enter a title or see all existing titles on IMDB and then choose one!")
    print(
        "If you cannot remember the hole title of a movie you can insert a keyword and the autocomplete will list all related titles (uppercase letters matter)")
    print("Option 1: enter a title/keyword")
    print("Option 2: see all existing titles")
    try:
        decide = int(input("Your option is: "))
    except:
        print("You must enter 1 or 2!")
        return get_prefered_movie(database)
    if decide == 1:
        return find_movie_by_keyword(database)
    elif decide == 2:
        return choose_a_movie(database)
    else:
        print("You must choose between 1, 2!")
        return get_prefered_movie(database)


def choose_a_movie(database):
    count = 1
    for elem in range(1, len(database)):
        print(f"{count}. {database[elem][0]}")
        count += 1
    try:
        answer = int(input("Choose a movie number: "))
    except:
        print(f"You must enter a number between 1 - {len(database)-1}!")
        return choose_a_movie(database)
    if answer < 1 or answer >= len(database):
        print(f"You must enter a number between 1 - {len(database)-1}!")
        return choose_a_movie(database)
    return database[answer]


def create_genre_coordinates(database):
    genre_database = np.array(["Title", "Action", "Adventure", "Animation",
                               "Children's", "Comedy", "Crime", "Documentary",
                               "Drama", "Fantasy", "Film-noir", "Horror", "Musical", "Western",
                               "Mystery", "Romance", "Sci-Fi", "Thriller", "War"])

    for elem in database:
        genre_database = np.vstack([genre_database, get_genre_for_movie(elem)])
    return genre_database


def get_specific_movie_genre(root_movie, genre_database):
    for elem in genre_database:
        if elem[0] == root_movie:
            return elem
    return []


def computeGenreSimilarity(genre_coord_root, genre_coord):
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(1, len(genre_coord_root)):
        x = int(genre_coord_root[i])
        y = int(genre_coord[i])
        sumxx += x * x
        sumyy += y * y
        sumxy += x * y

    return [genre_coord[0], sumxy / math.sqrt(sumxx * sumyy)]


def remove_unrelated_movies(cosine_database):
    related_cosine_database = np.array(["Titles", "Cosine"])
    for elem in cosine_database:
        if elem[1] != '0.0' and elem[1] != "Cosine":
            related_cosine_database = np.vstack(
                [related_cosine_database, elem])
    # print(related_cosine_database)
    return related_cosine_database


def computeYearSimilarity(movie1, movie2):
    try:
        diff = abs(int(movie1) - int(movie2))
    except:
        movie1 = int(re.sub("[^0-9]", "", movie1))
        movie2 = int(re.sub("[^0-9]", "", movie2))
        diff = abs(int(movie1) - int(movie2))
    sim = math.exp(-diff / 10.0)
    return sim


def get_title_year_from_database(databse, movie_title):
    my_list = []
    for elem in database:
        if movie_title == elem[0]:
            my_list.append(elem[0])
            my_list.append(elem[1])
            break
    # print(my_list)
    return my_list


def relative_year_relation(year_relation_for_movies, root_movie_year):
    year_relation = np.array(["Titles", "Year_Relation"])
    for elem in range(1, len(year_relation_for_movies)):
        year_relation = np.vstack([year_relation, [year_relation_for_movies[elem][0],
                                                   computeYearSimilarity(root_movie_year,
                                                                         year_relation_for_movies[elem][1])]])
    return year_relation


def select_specific_movies(database, related_cosine_database, root_movie):
    year_relation_for_movies = np.array(["Titles", "Year"])
    for elem in range(1, len(related_cosine_database)):
        year_relation_for_movies = np.vstack(
            [year_relation_for_movies, get_title_year_from_database(database, related_cosine_database[elem][0])])
    return relative_year_relation(year_relation_for_movies, root_movie[1])


def cosine_related_to_a_movie(root_movie, genre_database):
    root_move_genre = get_specific_movie_genre(root_movie, genre_database)
    cosine_database = np.array(["Titles", "Cosine"])
    for elem in range(2, len(genre_database)):
        if genre_database[elem][0] != root_movie:
            cosine_database = np.vstack(
                [cosine_database, computeGenreSimilarity(root_move_genre, genre_database[elem])])
    return remove_unrelated_movies(cosine_database)


def get_rating_for_movie(database, movie_title):
    for elem in database:
        if elem[0] == movie_title:
            return elem[2]
    return []


def get_specific_movie_rating(database, cosine_related_to_a_movie):
    rating_database = np.array(["Titles", "Rating"])
    # print(cosine_related_to_a_movie)
    for elem in range(1, len(cosine_related_to_a_movie)):
        rating_database = np.vstack(
            [rating_database,
             [cosine_related_to_a_movie[elem][0], get_rating_for_movie(database, cosine_related_to_a_movie[elem][0])]])
    return rating_database


def compute_final_score(cosine_table, year_table, ratings_for_selected_movies):
    recomender_table = np.array(["Title", "Score"])
    for elem in range(1, len(cosine_table)):
        recomender_table = np.vstack(
            [recomender_table, [cosine_table[elem][0],
                                (5 * float(cosine_table[elem][1]))
                                * float(year_table[elem][1])
                                * (3 * float(ratings_for_selected_movies[elem][1]))
                                / 10
                                ]])
    return recomender_table[recomender_table[:, 1].argsort()[::-1]]


def clean_database(database):
    for elem in database:
        elem[3] = elem[3].translate({ord('\n'): None})
    return database


def complete_specific_genre_database(memorize_genre, genre_database):
    specific_genre_database = np.array(["Title", "Action", "Adventure", "Animation",
                                        "Children's", "Comedy", "Crime", "Documentary",
                                        "Drama", "Fantasy", "Film-noir", "Horror", "Musical", "Western",
                                        "Mystery", "Romance", "Sci-Fi", "Thriller", "War"])
    for elem in genre_database:
        if len(memorize_genre) == 1:
            if elem[memorize_genre[0]] == '1':
                specific_genre_database = np.vstack([specific_genre_database, elem])
        elif len(memorize_genre) == 2:
            if elem[memorize_genre[0]] == '1' or elem[memorize_genre[1]] == '1':
                specific_genre_database = np.vstack([specific_genre_database, elem])
        elif len(memorize_genre) == 3:
            if elem[memorize_genre[0]] == '1' or elem[memorize_genre[1]] == '1' or elem[memorize_genre[2]] == '1':
                specific_genre_database = np.vstack([specific_genre_database, elem])
    return specific_genre_database


def select_from_genre_database(root_movie, genre_database):
    root_movie_genre = get_specific_movie_genre(root_movie[0], genre_database)
    memorize_genre = []
    for elem in range(1, len(root_movie_genre)):
        if root_movie_genre[elem] == '1':
            memorize_genre.append(elem)
    return complete_specific_genre_database(memorize_genre, genre_database)


def get_movie_by_name_from_database(movie_title, databse):
    for elem in database:
        if elem[0] == movie_title:
            return elem
    return []


def compute_to_add_details(final_recomandations_database, database):
    final_recomandations_database = final_recomandations_database[final_recomandations_database[:, 1].argsort()]
    final_database = np.array(["Titles", "Year", "Rating", "Genre"])
    for elem in range(len(final_recomandations_database)):
        if final_recomandations_database[elem][0] != "Title":
            final_database = np.vstack(
                [final_database, get_movie_by_name_from_database(final_recomandations_database[elem][0], database)])
    return final_database


def limit_final_recomandations(decide, final_recomandations_database):
    limited_final_database = np.array(["Title", "Score"])
    for elem in range(1, len(final_recomandations_database)):
        if elem == decide:
            break
        limited_final_database = np.vstack([limited_final_database, final_recomandations_database[elem]])
    return limited_final_database


def display_final_visualisation_ranking(root_movie, decide, final_visualisation_ranking):
    count = decide
    for elem in range(1, len(final_visualisation_ranking)):
        print(
            f"{count}. {final_visualisation_ranking[elem][0]}  \n\t Year: {final_visualisation_ranking[elem][1]}  \n\t Rating: {final_visualisation_ranking[elem][2]}  \n\t Genre: {final_visualisation_ranking[elem][3]}")
        count -= 1
    print("Above you can see the recommendations for:")
    print(
        f"\t Title: {root_movie[0]}  \n\t Year: {root_movie[1]}  \n\t Rating: {root_movie[2]}  \n\t Genre: {root_movie[3]}\n")


if __name__ == "__main__":

    database = collect_data()
    database = clean_database(database)
    genre_database = create_genre_coordinates(database)

    while True:
        root_movie = get_prefered_movie(database)
        genre_database_related_root_movie = select_from_genre_database(root_movie, genre_database)

        related_cosine_database = cosine_related_to_a_movie(root_movie[0], genre_database_related_root_movie)

        from_database_to_specific_year_database = select_specific_movies(database, related_cosine_database, root_movie)
        ratings_for_selected_movies = get_specific_movie_rating(database, related_cosine_database)
        final_recomandations_database = compute_final_score(related_cosine_database,
                                                            from_database_to_specific_year_database,
                                                            ratings_for_selected_movies)

        while True:
            print(
                f"How many of the {int(len(final_recomandations_database) / 2 - 1)} recommended movies do you want to be displayed?")
            try:
                decide = int(input("Your answer is: "))
            except:
                print(f"Enter a number between 1 - {int(len(final_recomandations_database) / 2 - 1)}")
                continue;
            if 0 < decide <= int(len(final_recomandations_database) / 2 - 1):
                break
            else:
                print(f"Enter a number between 1 - {int(len(final_recomandations_database) / 2 - 1)}")

        final_visualisation_ranking = limit_final_recomandations(decide + 1, final_recomandations_database)
        final_visualisation_ranking = compute_to_add_details(final_visualisation_ranking, database)
        display_final_visualisation_ranking(root_movie, decide, final_visualisation_ranking)

        decide = input("Type 'exit' to stop or anything else to continue:  ")
        if decide == "exit":
            break
        print("\n\n\n")
