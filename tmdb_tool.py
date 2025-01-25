import requests
import random
import argparse
import os
from dotenv import load_dotenv

load_dotenv()

def genres_input(genres):
    return [genre.strip().capitalize() for genre in genres.split(",") if genre.split()]
    
    
def get_genres(user_genres, only_ids=False):
    
    genres = {'Action': 28, 'Adventure': 12, 'Animation': 16, 'Comedy': 35, 'Crime': 80, 'Documentary': 99,
              'Drama': 18, 'Family': 10751, 'Fantasy': 14, 'History': 36, 'Horror': 27, 'Music': 10402,
              'Mystery': 9648, 'Romance': 10749, 'Science Fiction': 878, 'TV Movie': 10770, 'Thriller': 53,
              'War': 10752, 'Western': 37
            }
    
    if only_ids:
        return ", ".join(genre for genre in genres if genres[genre] in user_genres)
    
    else:
        if "Any" in user_genres:
            return random.choice(list(genres.values()))
        return "%2C".join(str(genres[genre_id]) for genre_id in genres if genre_id in user_genres)


def get_url(filter, genre):
    base_url = "https://api.themoviedb.org/3/discover/movie?include_adult=false"
    urls = {"popular": f"{base_url}&language=en-US&page=1&sort_by=popularity.desc&with_genres={genre}",
        "top rated": f"{base_url}&include_video=false&language=en-US&page=1&sort_by=vote_average.desc&with_genres={genre}&vote_count.gte=200",
        "upcoming": f"{base_url}&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres={genre}&with_release_type=2|3&release_date.gte={{min_date}}&release_date.lte={{max_date}}"
        }

    if filter in urls:
        return urls[filter]
    elif filter in ["now playing", "playing"]:
        return urls["upcoming"]
    else:
        raise ValueError("Typo in filters")


def format_overview(overview):
    overview_lines = []
    formatted_lines = ""
    
    for line in overview:
        
        formatted_lines += "".join(line)
        formatted_lines += " "
        
        if len(formatted_lines) > 60:
            overview_lines.append(formatted_lines)
            formatted_lines = ""
            
    overview_lines.append(formatted_lines)
    return "\n".join(overview_lines)

def format_movie_data(movie):
    title = movie['title']
    desc = format_overview(movie["overview"].split(" ")).strip()
    movie_genres = get_genres(movie["genre_ids"], True)
    release_date = movie["release_date"]
    rating = round(movie["vote_average"], 2)
    return f"\nMovie title: {title}\nOverview: {desc}\nGenres: {movie_genres}\nRelease Date: {release_date}\nRating: {rating}★"

def tmdb_tool(args):
    API_KEY = os.getenv("API_KEY")
    movie_genre = get_genres(genres_input(", ".join(args.genre)))
    
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
    }
    
    response = requests.get(get_url(" ".join(args.type).lower(), movie_genre), headers=headers)
    
    movie_list = response.json()['results']
    
    for movie in movie_list[:5]:
        print(format_movie_data(movie))

def main():
    parser = argparse.ArgumentParser(description="TMDB CLI Tool")
    parser.add_argument("--type", type=str, nargs="+", help="Specify the type of movie filter (e.g., 'popular', 'top rated', 'now playing').")
    parser.add_argument("--genre", type=str, nargs="+", help="Movie genre")
    
    args = parser.parse_args()
    
    if not args.type or not args.genre:
        return
    else:
        tmdb_tool(args)


if __name__ == '__main__':
    main()