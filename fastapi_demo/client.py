import aiohttp
import asyncio


async def send_async_get_request(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                response.raise_for_status()  # Raises stored HTTP error, if one occurred.
                print(f"Success! Response from {url}:")
                data = await response.text()
                print(data)
        except aiohttp.ClientError as e:
            print(f"An HTTP client error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Replace with the actual URL you need to send an async GET request to
    url = "http://127.0.0.1:8000/ping"

    # Run the event loop to execute the async function
    asyncio.run(send_async_get_request(url))
