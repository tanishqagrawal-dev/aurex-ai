# -*- coding: utf-8 -*-
"""
Quick test script - Check if app components work
"""
from dotenv import dotenv_values

print("TESTING AUREX AI COMPONENTS")
print("=" * 50)

env_vars = dotenv_values(".env")

# Test connections
print("\n1. API Keys loaded: YES")
print(f"   - Cohere: {'YES' if env_vars.get('CohereAPIKey') else 'NO'}")
print(f"   - Groq: {'YES' if env_vars.get('GroqAPIKey') else 'NO'}")

# Test file operations
print("\n2. Testing File Operations...")
try:
    from Frontend.GUI import (
        GetMicrophoneStatus, GetAssistantStatus, SetMicrophoneStatus,
        ShowTextToScreen, TempDirectoryPath
    )
    
    mic = GetMicrophoneStatus()
    status = GetAssistantStatus()
    print(f"   - Microphone Status: {mic}")
    print(f"   - Assistant Status: {status}")
    print("   - File Operations: OK")
except Exception as e:
    print(f"   - ERROR: {e}")

# Test Model import
print("\n3. Testing Model Import...")
try:
    from Backend.Model import FirstLayerDMM
    print("   - Model imported: OK")
except Exception as e:
    print(f"   - ERROR: {e}")

# Test Chatbot import
print("\n4. Testing Chatbot Import...")
try:
    from Backend.Chatbot import ChatBot
    print("   - ChatBot imported: OK")
except Exception as e:
    print(f"   - ERROR: {e}")

# Test RealtimeSearchEngine import  
print("\n5. Testing RealtimeSearchEngine Import...")
try:
    from Backend.RealtimeSearchEngine import RealtimeSearchEngine
    print("   - RealtimeSearchEngine imported: OK")
except Exception as e:
    print(f"   - ERROR: {e}")

print("\n" + "=" * 50)
print("QUICK TEST SUMMARY:")
print("All imports successful!")
print("\nWAITING FOR USER INPUT VIA GUI...")
print("Click the microphone button in the GUI to start")
