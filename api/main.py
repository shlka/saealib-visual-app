import logging
import random
import asyncio

from fastapi import FastAPI, WebSocket, WebSocketDisconnect


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fastapi_app")

app = FastAPI()

@app.websocket("/ws")
async def websocket_test(websocket: WebSocket):
    await websocket.accept()
    logger.info("Client connected")

    try:
        x = 0

        while True:
            data = {
                "name": x,
                "value": [x, random.randint(0,100)]
            }
            await websocket.send_json(data)
            logger.info(f"send: {data}")
            
            x += 1

            await asyncio.sleep(0.1)

    except WebSocketDisconnect:
        logger.info("Client disconnected")
