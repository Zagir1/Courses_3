import requests

def dog_pic():
    response = requests.get("https://random.dog/woof.json")
    dog = response.json()
    return dog['url']
