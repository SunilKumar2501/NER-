import requests
def ner(text):

    url = "https://named-entity-extraction1.p.rapidapi.com/api/lingo"

    payload = {
	"extractor": "en",
	"text": text
    }
    headers = {
	"x-rapidapi-key": "9fde98c4c2mshce9debf60b79934p1aa736jsne4a055ad9d42",
	"x-rapidapi-host": "named-entity-extraction1.p.rapidapi.com",
	"Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()


def emotional(text):
    url2 = "https://text-to-emotions2.p.rapidapi.com/predict-emotions"
    header2 = {"x-rapidapi-key": "9fde98c4c2mshce9debf60b79934p1aa736jsne4a055ad9d42",
               "x-rapidapi-host": "text-to-emotions2.p.rapidapi.com",
               "Content-Type": "application/json"
               }
    # Prepare the data to be sent in the request body
    data = {
        "text": text
    }
    # Make the POST request to the API
    response = requests.post(url2, headers=header2, json=data)

    # Print the response in JSON format
    return response.json()


