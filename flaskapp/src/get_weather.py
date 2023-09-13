import requests


def get_weather(ort, plz):
    api_key = 'deb143ec8c4f97aab4a9368f770ef498'
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'

    # Konstruieren Sie die API-Anfrage-URL
    complete_url = f"{base_url}q={ort},{plz}&appid={api_key}"

    # Anfrage an OpenWeatherMap senden
    response = requests.get(complete_url)
    data = response.json()

    # Wetterdaten aus der Antwort extrahieren (hier als Beispiel)
    wetterdaten = {
        'ort': ort,
        'plz': plz,
        'temperatur': data['main']['temp'],
        'wetter': data['weather'][0]['description']
    }

    return wetterdaten
