
import asyncio
import os
import sys

# Add src to path just in case, though we just need google.genai
sys.path.append(os.path.join(os.getcwd(), "src"))

try:
    from google import genai
    from ai_content.config import get_settings
except ImportError as e:
    print(f"Import error: {e}")
    sys.exit(1)

async def main():
    try:
        settings = get_settings().google
        api_key = settings.api_key
        if not api_key:
            print("No API key found in settings.")
            return

        client = genai.Client(api_key=api_key)
        
        print(f"Client type: {type(client)}")
        print(f"Async client type: {type(client.aio)}")
        
        print("\n--- client.aio.models attributes ---")
        for attr in dir(client.aio.models):
            if not attr.startswith("_"):
                print(attr)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
