import webbrowser
import requests

def open_coffee_website():
    url = 'https://coffee-house2.netlify.app/'
    try:
        print("Checking website availability...")
        response = requests.get(url, timeout=1)  
        response.raise_for_status()  
        webbrowser.open(url)
        print("Opening the Coffee House website...")
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to open the website. {e}")
