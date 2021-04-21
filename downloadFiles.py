import asyncio

import aiofiles
import aiohttp

list_nana = []
dest_file = '/media/HDD500/Nana/Nana_'

for i in range(53):
    urlBase = 'https://ns545982.ip-66-70-177.net/N/nana/'
    url = urlBase + '0' + str(i) + '.mp4' if i < 10 else urlBase + str(i) + '.mp4'
    list_nana.append(url)

list_nana.pop(0)
print (list_nana[0])

async def massRequest(list_nana, dest_file, session, nana):
    print("Iniciando..." + nana.partition('nana/')[2])
    print(nana)
    async with session.get(nana) as response:
        content = await response.read()
        if response.status != 200:
            print(f"Download failed: {response.status}")
        else:
            print(f"Downloading:" + dest_file + nana.partition('nana/')[2])
            async with aiofiles.open(dest_file + nana.partition('nana/')[2], "+wb") as f:
                await f.write(content)
            list_nana.remove(nana)


async def main(list_nana):
    async with aiohttp.ClientSession() as session:
        tasks = [massRequest(list_nana, dest_file, session, nana) for nana in list_nana]
        await asyncio.gather(*tasks)

asyncio.run(main(list_nana))