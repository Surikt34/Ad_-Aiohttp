import aiohttp
import asyncio

BASE_URL = "http://localhost:8000/ads"

async def create_ad(title, description, owner):
    data = {
        "title": title,
        "description": description,
        "owner": owner
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(BASE_URL, json=data) as response:
            if response.status == 201:
                print("Ad created successfully:", await response.json())
            else:
                print("Failed to create ad:", response.status, await response.text())

async def get_ad(ad_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}/{ad_id}") as response:
            if response.status == 200:
                print("Ad details:", await response.json())
            else:
                print("Failed to get ad:", response.status, await response.text())

async def delete_ad(ad_id):
    async with aiohttp.ClientSession() as session:
        async with session.delete(f"{BASE_URL}/{ad_id}") as response:
            if response.status == 200:
                print("Ad deleted successfully:", await response.json())
            else:
                print("Failed to delete ad:", response.status, await response.text())

if __name__ == "__main__":
    # Пример использования функций
    asyncio.run(create_ad("Продам велосипед", "Горный велосипед, 21 скорость", "Андрей"))
    asyncio.run(get_ad(0))
    asyncio.run(delete_ad(0))
