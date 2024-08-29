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




