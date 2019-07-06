import time

# def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     time.sleep(sleep_time)
#     print('OK {}'.format(url))

# def main(urls):
#     for url in urls:
#         crawl_page(url)

# main(['url_1', 'url_2', 'url_3', 'url_4'])

# import asyncio

# async def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     await asyncio.sleep(sleep_time)
#     print('OK {}'.format(url))

# async def main(urls):
#     for url in urls:
#         await crawl_page(url)

# asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))

# import asyncio

# async def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     await asyncio.sleep(sleep_time)
#     print('OK {}'.format(url))

# async def main(urls):
#     tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
#     for task in tasks:
#         await task

# asyncio.run(main(['url_1', 'url_8', 'url_3', 'url_4']))

# import asyncio

# async def worker_1():
#     print('worker_1 start')
#     await asyncio.sleep(1)
#     print('worker_1 done')

# async def worker_2():
#     print('worker_2 start')
#     await asyncio.sleep(2)
#     print('worker_2 done')

# async def main():
#     task1 = asyncio.create_task(worker_1())
#     task2 = asyncio.create_task(worker_2())
#     print('before await')
    
#     print('awaited worker_1')
    
#     print('awaited worker_2')
#     await task1
#     await task2

# asyncio.run(main())

import asyncio

async def worker_1():
    await asyncio.sleep(1)
    return 1

async def worker_2():
    await asyncio.sleep(2)
    return 2 / 0

async def worker_3():
    await asyncio.sleep(3)
    return 3

async def main():
    task_1 = asyncio.create_task(worker_1())
    task_2 = asyncio.create_task(worker_2())
    task_3 = asyncio.create_task(worker_3())

    await asyncio.sleep(2)
    task_3.cancel()

    res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
    print(res)

asyncio.run(main())
