from fastapi import FastAPI
import asyncio

app = FastAPI()

count = 0

async def repeated_task():
    global count
    while True:
        # 这里放置你想每5秒执行一次的代码
        print(f"统计最近5秒内请求个数: {count}")
        count = 0
        await asyncio.sleep(5)  # 等待5秒


@app.on_event("startup")
async def on_startup():
    asyncio.create_task(repeated_task())  # 创建后台任务


@app.get("/ping")
async def stat_ping():
    global count
    count += 1
