import requests

print("Starting test script...")
url = 'https://mariyahakoby-5000.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/emotionDetector'
data = {"text": "This is so frustrating and annoying!"}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()
    print("Response from emotionDetector endpoint:")
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error calling the API: {e}")

print("Request sent, awaiting response...")    