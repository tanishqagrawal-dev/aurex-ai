#!/usr/bin/env python3
from huggingface_hub import InferenceClient
from dotenv import get_key
import sys

print("Starting test...", file=sys.stderr)

api_key = get_key('.env', 'HuggingFaceAPIKey')
print(f'API Key loaded: {bool(api_key)}', file=sys.stderr)

if api_key:
    print(f'API Key last 10 chars: {api_key[-10:]}', file=sys.stderr)

try:
    client = InferenceClient(token=api_key)
    print('Client initialized', file=sys.stderr)
    
    print('Testing text_to_image...', file=sys.stderr)
    sys.stderr.flush()
    
    image = client.text_to_image('a beautiful cat', model='black-forest-labs/FLUX.1-schnell')
    print(f'Image generated: {type(image)}', file=sys.stderr)
    
    image.save('test_image.jpg')
    print('Image saved successfully', file=sys.stderr)
    
except Exception as e:
    print(f'Error: {type(e).__name__}: {e}', file=sys.stderr)
    import traceback
    traceback.print_exc()
