import streamlit as st
from streamlit_echarts import st_echarts
import json
import websockets
import asyncio

st.title("test ECharts graph from websocket api")

options = {
    "xAxis": {
        "type": "value"
    },
    "yAxis": {
        "type": "value", "min": 0, "max": 100
    },
    "series": [{
        "data": [],
        "type": "line",
        "smooth": True
    }],
    "animation": False
}

async def main():
    ch_place = st.empty()

    data_history = []

    api_endpoint = "ws://127.0.0.1:8000/ws"

    try:
        async with websockets.connect(api_endpoint) as websocket:
            while True:
                msg = await websocket.recv()
                point = json.loads(msg)

                data_history.append(point["value"])

                options["series"][0]["data"] = data_history

                with ch_place:
                    st_echarts(options=options)

                if len(data_history) > 20:
                    break


    except Exception as e:
        st.error(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
