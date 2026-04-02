# -*- coding: utf-8 -*-
"""
Quick test script to verify all backend modules are working
"""
import sys
import os
from dotenv import dotenv_values

# Set encoding to UTF-8
os.environ['PYTHONIOENCODING'] = 'utf-8'

print("=" * 60)
print("TESTING AUREX AI MODULES")
print("=" * 60)

# Test 1: Check environment variables
print("\n1. Testing Environment Variables...")
try:
    env_vars = dotenv_values(".env")
    cohere_key = "YES" if env_vars.get('CohereAPIKey') else "NO"
    groq_key = "YES" if env_vars.get('GroqAPIKey') else "NO"
    print(f"   [OK] Cohere API Key: {cohere_key}")
    print(f"   [OK] Groq API Key: {groq_key}")
    print(f"   [OK] Username: {env_vars.get('Username')}")
    print(f"   [OK] Assistant Name: {env_vars.get('Assistantname')}")
except Exception as e:
    print(f"   [ERROR] {str(e)[:100]}")

# Test 2: Test Cohere Model
print("\n2. Testing Cohere Model...")
try:
    import cohere
    co = cohere.Client(api_key=env_vars.get("CohereAPIKey"))
    # Test with a simple prompt
    stream = co.chat_stream(
        model='command-r-08-2024',
        message="test",
        temperature=0.7,
        preamble="You are an AI assistant."
    )
    response = ""
    for event in stream:
        if event.event_type == "text-generation":
            response += event.text
    print(f"   [OK] Cohere Model Response: {response[:50]}...")
except Exception as e:
    print(f"   [ERROR] {str(e)[:100]}")

# Test 3: Test Groq Chatbot
print("\n3. Testing Groq ChatBot...")
try:
    from groq import Groq
    client = Groq(api_key=env_vars.get("GroqAPIKey"))
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": "Say hello"}],
        max_tokens=100,
    )
    print(f"   [OK] Groq ChatBot Response: {completion.choices[0].message.content[:50]}...")
except Exception as e:
    print(f"   [ERROR] {str(e)[:100]}")

# Test 4: Check Frontend Files
print("\n4. Testing Frontend Files...")
try:
    from Frontend.GUI import GetMicrophoneStatus, GetAssistantStatus, SetMicrophoneStatus
    mic_status = GetMicrophoneStatus()
    ai_status = GetAssistantStatus()
    print(f"   [OK] Microphone Status: {mic_status}")
    print(f"   [OK] Assistant Status: {ai_status}")
    # Set mic to True for testing
    SetMicrophoneStatus("True")
    print(f"   [OK] Microphone set to True for testing")
except Exception as e:
    print(f"   [ERROR] {str(e)[:100]}")

print("\n" + "=" * 60)
print("TEST COMPLETE")
print("=" * 60)
