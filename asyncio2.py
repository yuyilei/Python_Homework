import asyncio
 
async def do_some_work(x):
    print("Waiting " + str(x))
    await asyncio.sleep(x)
 
loop = asyncio.get_event_loop()
loop.run_until_complete(do_some_work(3))