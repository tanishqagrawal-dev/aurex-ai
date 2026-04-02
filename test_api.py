import requests
from dotenv import get_key

api_key = get_key('.env', 'HuggingFaceAPIKey')
url = 'https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium'
headers = {'Authorization': f'Bearer {api_key}'}
payload = {'inputs': 'a cat'}

print(f'API Key exists: {bool(api_key)}')
print(f'API Key last 10 chars: {api_key[-10:] if api_key else "NONE"}')
print(f'Testing URL: {url}')

try:
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    print(f'Response status: {response.status_code}')
    print(f'Response headers: {dict(response.headers)}')
    if response.status_code != 200:
        print(f'Error response: {response.text[:200]}')
    else:
        print(f'Response size: {len(response.content)} bytes')
except Exception as e:
    print(f'Exception: {e}')
