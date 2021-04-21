import aiohttp
import asyncio

url = "???"

idPedidos = "?"

token = "?"

errorPed = "Sem erros"

async def massRequest(ped, token, errorPed, session):
    async with session.get(url, headers={"authorization": token}, params={"idPedido": ped}) as response:
        body = await response.json()
        if response.status == 500:
            errorPed = ped
    print("\nNúmero da requisição:",((len(asyncio.Task.all_tasks()) - 1) - len(asyncio.all_tasks())), "\nStatus code:", response.status, "\nCorpo da resposta:", body)
    return errorPed

async def main(idPedidos):
    async with aiohttp.ClientSession() as session:
        tasks = [massRequest(ped, token, errorPed, session) for ped in idPedidos]
        errors = await asyncio.gather(*tasks)
        errorsList = list(dict.fromkeys(errors))
        if len(errorsList) >= 2:
            errorsList.remove('Sem erros')
        print("\nCom erro:", errorsList)
asyncio.run(main(idPedidos))