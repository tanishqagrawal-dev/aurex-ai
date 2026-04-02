import asyncio
from PIL import Image
from io import BytesIO
from huggingface_hub import InferenceClient
from dotenv import get_key
import os
from time import sleep
import sys


# Function to open and display generated images
def open_images(prompt):
    folder_path = r"Data"
    prompt = prompt.replace(" ", "_")

    files = [f"{prompt}{i}.jpg" for i in range(1, 5)]

    for jpg_file in files:
        image_path = os.path.join(folder_path, jpg_file)

        try:
            img = Image.open(image_path)
            print(f"Opening image: {image_path}")
            sys.stdout.flush()
            img.show()
            sleep(1)

        except IOError:
            print(f"Unable to open {image_path}")
            sys.stdout.flush()


# HuggingFace API setup
api_key = get_key('.env', 'HuggingFaceAPIKey')
if not api_key:
    print("ERROR: HuggingFaceAPIKey not found in .env file")
    sys.stdout.flush()
    exit(1)

# Initialize InferenceClient with the API key
client = InferenceClient(token=api_key)
print("InferenceClient initialized successfully")
sys.stdout.flush()


# Generate images
async def generate_images(prompt: str):
    print(f"[DEBUG] Starting image generation for: {prompt}")
    sys.stdout.flush()
    tasks = []

    for i in range(4):
        async def generate_single(index):
            try:
                enhanced_prompt = f"{prompt}, quality=4K, sharpness=maximum, Ultra High details, high resolution"
                print(f"[DEBUG] Generating image {index + 1}...")
                sys.stdout.flush()
                
                # Use the text_to_image method which handles model selection
                image = await asyncio.to_thread(
                    client.text_to_image,
                    enhanced_prompt,
                    model="black-forest-labs/FLUX.1-schnell"
                )
                
                print(f"[DEBUG] Image {index + 1} generated successfully")
                sys.stdout.flush()
                return index, image
            except Exception as e:
                print(f"[ERROR] Error generating image {index + 1}: {e}")
                sys.stdout.flush()
                return index, None

        task = asyncio.create_task(generate_single(i))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    print(f"[DEBUG] All image generation tasks completed")
    sys.stdout.flush()

    for i, image in results:
        if image:
            try:
                filename = f"Data/{prompt.replace(' ', '_')}{i+1}.jpg"
                image.save(filename)
                print(f"[DEBUG] Successfully saved {filename}")
                sys.stdout.flush()
            except Exception as e:
                print(f"[ERROR] Failed to save image {i+1}: {e}")
                sys.stdout.flush()
        else:
            print(f"[DEBUG] Skipping image {i+1} (generation failed)")
            sys.stdout.flush()


# Wrapper function
def GenerateImages(prompt: str, open_images_flag=True):
    print(f"[DEBUG] GenerateImages called with prompt: {prompt}")
    sys.stdout.flush()
    try:
        asyncio.run(generate_images(prompt))
        if open_images_flag:
            print("[DEBUG] Image generation completed, opening images...")
            sys.stdout.flush()
            open_images(prompt)
            print("[SUCCESS] All images opened")
        else:
            print("[SUCCESS] Images generated successfully (skipping image display)")
        sys.stdout.flush()
    except Exception as e:
        print(f"[ERROR] Error in GenerateImages: {e}")
        sys.stdout.flush()
        import traceback
        traceback.print_exc()


# Main loop (listens for frontend trigger)
print("[START] ImageGeneration service starting...")
sys.stdout.flush()

while True:
    try:
        with open(r"Frontend\Files\ImageGeneration.data", "r") as f:
            Data: str = f.read().strip()

        print(f"[DEBUG] Read from ImageGeneration.data: '{Data}'")
        sys.stdout.flush()

        # Split from the right to get the last comma (Status)
        parts = Data.rsplit(",", 1)
        if len(parts) != 2:
            print(f"[WARN] Invalid data format: {Data}")
            sys.stdout.flush()
            sleep(1)
            continue
            
        Prompt, Status = parts
        Prompt = Prompt.replace("generate image ", "").strip()
        Status = Status.strip()

        print(f"[DEBUG] Parsed - Prompt: '{Prompt}', Status: '{Status}'")
        sys.stdout.flush()

        if Status == "True":
            print(f"[ACTION] GENERATING IMAGES for: {Prompt}")
            sys.stdout.flush()
            
            # Skip opening images when run as subprocess (no display available)
            open_images_flag = not (sys.stdout != sys.__stdout__)
            GenerateImages(prompt=Prompt, open_images_flag=open_images_flag)
            print("[SUCCESS] Images generated successfully!")
            sys.stdout.flush()

            with open(r"Frontend\Files\ImageGeneration.data", "w") as f:
                f.write("False,False")
            
            print("[INFO] Reset trigger file to False,False")
            sys.stdout.flush()
            break

        else:
            print(f"[DEBUG] Status is {Status}, waiting...")
            sys.stdout.flush()
            sleep(1)

    except FileNotFoundError as e:
        print(f"[ERROR] ImageGeneration.data file not found: {e}")
        sys.stdout.flush()
        sleep(1)
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        sys.stdout.flush()
        import traceback
        traceback.print_exc()
        sleep(1)