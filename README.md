# TMDB-Tool
This script is a command-line tool that fetches movies from TMDB by type (e.g., popular) and genre (e.g., Action). It displays the title, overview, genres, release date, and rating.

## Features
- Fetches movie data for **popular**, **top-rated**, **upcoming**, and **now playing** categories.
- Allows users to specify movie genres (e.g., Action, Comedy, Drama).
- Displays formatted movie details, including title, overview, genres, release date, and rating.
- Handles API key securely using .env file.

## Usage 
To run the tool, use the following command:
python tmdb_tool.py --type <type> --genre <genre>
 
### Command-Line Arguments
- --type: The type of movies to fetch. Options include:
- popular
- top rated
- upcoming
- now playing (or playing)
- --genre: The genres of movies to filter by. Provide a comma-separated list, e.g., Action, Comedy.
 
### Examples
1. Fetch popular movies in the Comedy genre:
   python tmdb_tool.py --type popular --genre Comedy
 
2. Fetch top-rated Action and Adventure movies:
   python tmdb_tool.py --type top rated --genre Action, Adventure
 
3. Fetch upcoming Drama movies:
   python tmdb_tool.py --type upcoming --genre Drama
 
## Notes
- Make sure your API key is valid; otherwise, the tool won't work.
- The format_overview function wraps long movie descriptions for better terminal display.
 - If Any is passed as the genre, the tool will select a random genre.
