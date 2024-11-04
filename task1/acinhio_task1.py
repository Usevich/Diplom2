import asyncio
import aiohttp
import time
import psutil

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    url = 'https://urban-university.ru'
    start_time = time.time()
    process = psutil.Process()
    memory_before = process.memory_info().rss

    tasks = []
    async with aiohttp.ClientSession() as session:
        for _ in range(50):
            task = asyncio.create_task(fetch(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks)

    memory_after = process.memory_info().rss
    end_time = time.time()
    process_time = end_time - start_time
    process_memory = (memory_after - memory_before)/(1024*1024)

    print(f"Время выполнения: {end_time - start_time} секунд")
    print(f"Использование памяти: {(memory_after - memory_before)/(1024*1024)} Мбайт")
    with open('acinhio_task1.log','a') as file:
        file.write(f'{process_time:.2f},{process_memory:.2f}\n')

    return process_time,process_memory
if __name__ == "__main__":
    asyncio.run(main())