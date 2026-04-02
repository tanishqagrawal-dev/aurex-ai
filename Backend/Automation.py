# Import required libraries
from AppOpener import close, open as appopen
from webbrowser import open as webopen
from pywhatkit import search, playonyt
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from rich import print
from groq import Groq
import webbrowser
import subprocess
import requests
import keyboard
import asyncio
import os

# Load environment variables from the .env file
env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey")

# Define CSS classes for parsing specific elements in HTML content
classes = ["zCubwf", "hgKElc", "LTKOO sY7ric", "Z0LcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", "tw-Data-text tw-text-small tw-ta", "IZ6rdc", "05uR6d LTKOO", "vlzY6d", "webanswers-webanswers_table__webanswers-table", "dDoNo ikb4Bb gsrt", "sXLa0e", "LWkfKe", "VQF4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]

# Define a user-agent for making web requests
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"

# Initialize the Groq client
client = Groq(api_key=GroqAPIKey)

# Predefined responses
professional_responses = [
    "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.",
    "I'm at your service for any additional questions or support you may need-don't hesitate to ask.",
]

# List to store chatbot messages
messages = []

# System message
SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ.get('Username')}. You're a content writer. You have to write content like letters, codes, applications, essays, notes, songs, poems etc."}]

# Function to perform a Google search
def GoogleSearch(Topic):
    search(Topic)
    return True

# Function to generate content using AI and save it
def Content(Topic):

    def OpenNotepad(File):
        try:
            default_text_editor = 'notepad.exe'
            proc = subprocess.Popen([default_text_editor, File])
            print(f"[OK] Notepad opened: {File}")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to open notepad: {e}")
            return False

    def ContentWriterAI(prompt):
        try:
            messages.append({"role": "user", "content": f"{prompt}"})

            # Call with reduced max tokens for faster response
            completion = client.chat.completions.create(
                model="mixtral-8x7b-32768",
                messages=SystemChatBot + messages,
                max_tokens=1024,
                temperature=0.7,
                top_p=1,
                stream=True,
                stop=None
            )

            Answer = ""
            chunk_count = 0
            
            for chunk in completion:
                chunk_count += 1
                if chunk_count > 500:  # Safety limit to prevent infinite loops
                    break
                if chunk.choices[0].delta.content:
                    Answer += chunk.choices[0].delta.content

            Answer = Answer.replace("</s>", "")
            # Truncate if response is too long
            if len(Answer) > 1500:
                Answer = Answer[:1500] + "\n\n... (content truncated)"
            
            messages.append({"role": "assistant", "content": Answer})
            return Answer
            
        except Exception as e:
            print(f"[ERROR] Content generation failed: {e}")
            raise

    try:
        Topic_clean = Topic.replace("Content ", "").strip()
        print(f"[INFO] Generating content for: {Topic_clean}")
        
        # Generate content with timeout protection
        ContentByAI = ContentWriterAI(Topic_clean)
        
        # Create safe filename
        safe_filename = Topic_clean.lower().replace(' ', '_').replace('?', '').replace('!', '').replace('.', '')[:25]
        if not safe_filename:
            safe_filename = "generated_content"
            
        file_path = rf"Data\{safe_filename}.txt"
        
        # Ensure Data directory exists
        os.makedirs("Data", exist_ok=True)
        
        # Write to file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(ContentByAI)
        
        print(f"[OK] Content saved to: {file_path}")
        
        # Open in notepad
        OpenNotepad(file_path)
        return True
        
    except Exception as e:
        print(f"[ERROR] Content function failed: {str(e)[:100]}")
        return False

# Function to search YouTube
def YouTubeSearch(Topic):
    Url4Search = f"https://www.youtube.com/results?search_query={Topic}"
    webbrowser.open(Url4Search)
    return True

# Function to play YouTube video
def PlayYoutube(query):
    playonyt(query)
    return True

# Function to open apps or webpages
def OpenApp(app, sess=requests.session()):
    try:
        appopen(app, match_closest=True, output=True, throw_error=True)
        return True

    except:

        def extract_links(html):
            if html is None:
                return []
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('a', {'jsname': 'UWckNb'})
            return [link.get('href') for link in links]

        def search_google(query):
            url = f"https://www.google.com/search?q={query}"
            headers = {"User-Agent": useragent}
            response = sess.get(url, headers=headers)

            if response.status_code == 200:
                return response.text
            else:
                print("Failed to retrieve search results.")
                return None

        html = search_google(app)

        if html:
            link = extract_links(html)[0]
            webopen(link)

        return True

# Function to close an application
def CloseApp(app):
    if "chrome" in app:
        pass
    else:
        try:
            close(app, match_closest=True, output=True, throw_error=True)
            return True
        except:
            return False
# Function to execute system-level commands
def System(command):

    # Mute system volume
    def mute():
        keyboard.press_and_release("volume mute")

    # Unmute system volume
    def unmute():
        keyboard.press_and_release("volume mute")

    # Increase volume
    def volume_up():
        keyboard.press_and_release("volume up")

    # Decrease volume
    def volume_down():
        keyboard.press_and_release("volume down")

    # Execute commands
    if command == "mute":
        mute()

    elif command == "unmute":
        unmute()

    elif command == "volume up":
        volume_up()

    elif command == "volume down":
        volume_down()

    return True


# Async function to translate & execute commands
async def TranslateAndExecute(commands: list[str]):

    funcs = []

    for command in commands:

        if command.startswith("open "):

            if "open it" in command:
                pass

            elif "open file" == command:
                pass

            else:
                fun = asyncio.to_thread(OpenApp, command.removeprefix("open "))
                funcs.append(fun)

        elif command.startswith("general "):
            pass

        elif command.startswith("realtime "):
            pass

        elif command.startswith("close "):
            fun = asyncio.to_thread(CloseApp, command.removeprefix("close "))
            funcs.append(fun)

        elif command.startswith("play "):
            fun = asyncio.to_thread(PlayYoutube, command.removeprefix("play "))
            funcs.append(fun)

        elif command.startswith("content "):
            fun = asyncio.to_thread(Content, command.removeprefix("content "))
            funcs.append(fun)

        elif command.startswith("google search "):
            fun = asyncio.to_thread(GoogleSearch, command.removeprefix("google search "))
            funcs.append(fun)

        elif command.startswith("youtube search "):
            fun = asyncio.to_thread(YouTubeSearch, command.removeprefix("youtube search "))
            funcs.append(fun)

        elif command.startswith("system "):
            fun = asyncio.to_thread(System, command.removeprefix("system "))
            funcs.append(fun)

        else:
            print(f"No Function Found. For {command}")

    results = await asyncio.gather(*funcs)

    for result in results:
        if isinstance(result, str):
            yield result
        else:
            yield result


# Main automation runner
async def Automation(commands: list[str]):

    async for result in TranslateAndExecute(commands):
        pass

    return True
