import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    response = requests.get(url)
    response.raise_for_status()  # Raises error for bad response

    j = response.json()
    print("\nRandom Joke")
    print("-" * 90)
    print(j["setup"])
    print(j["punchline"])

if __name__ == "__main__":
    get_random_joke()
