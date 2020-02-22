import pytest
from channels.testing import WebsocketCommunicator
from chat.consumers import ChatConsumer
from channels.routing import URLRouter
from django.urls import re_path


@pytest.mark.asyncio
async def test_chat_consumer():
    application = URLRouter([re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer)])
    communicator = WebsocketCommunicator(application, "/ws/chat/newbie/")
    connected, subprotocol = await communicator.connect()
    assert connected

    # test sending text
    await communicator.send_json_to({"message": "hello"})
    response = await communicator.receive_json_from()
    assert response.get("message") == "hello"

    # close
    await communicator.disconnect()
