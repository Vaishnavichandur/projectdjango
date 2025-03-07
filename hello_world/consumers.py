import json
from channels.generic.websocket import AsyncWebsocketConsumer

class HelloWorldConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket Connected!")  # Debugging
        await self.accept()
        await self.send(text_data=json.dumps({"message": "Hello, World!"}))

    async def disconnect(self, close_code):
        print(f"WebSocket Disconnected: {close_code}")  # Debugging

    async def receive(self, text_data):
        print(f"Received: {text_data}")  # Debugging
        await self.send(text_data=json.dumps({"message": "You sent: " + text_data}))
