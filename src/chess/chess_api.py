import requests

# Base URL for Chess.com public API
CHESS_API_BASE = "https://api.chess.com/pub"

# Standard headers for the API request
# - accept: Expect JSON response
# - User-Agent: Helps identify the client making the request (good practice for APIs)
headers = {
    "accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Python/3.10 requests/2.31.0"
}

def get_player_profile(username):
    """
    Fetches the public profile information of a Chess.com player.

    Args:
        username (str): Chess.com username

    Returns:
        dict: JSON response containing player profile details such as
              name, title, rating, country, etc.

    Raises:
        HTTPError: If the API request fails (e.g., user not found, network issue)
    """
    # Construct API endpoint URL for player profile
    url = f"{CHESS_API_BASE}/player/{username}"
    
    # Send GET request to the API
    response = requests.get(url, headers=headers)
    
    # Raise an exception for HTTP errors (4xx, 5xx)
    response.raise_for_status()
    
    # Parse and return JSON response as Python dictionary
    return response.json()


def get_player_stats(username):
    """
    Fetches the game statistics of a Chess.com player.

    Args:
        username (str): Chess.com username

    Returns:
        dict: JSON response containing player statistics such as
              blitz, rapid, bullet ratings, win/loss records, etc.

    Raises:
        HTTPError: If the API request fails
    """
    # Construct API endpoint URL for player statistics
    url = f"{CHESS_API_BASE}/player/{username}/stats"
    
    # Send GET request to the API
    response = requests.get(url, headers=headers)
    
    # Raise an exception for HTTP errors
    response.raise_for_status()
    
    # Parse and return JSON response
    return response.json()