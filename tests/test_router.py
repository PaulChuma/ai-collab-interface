# tests/test_router.py

from core.router import Router, Message

def test_routing():
    class MockAgent:
        def receive(self, msg):
            return f"Got it: {msg.content}"

    router = Router()
    router.register("test_agent", MockAgent())

    msg = Message("x", "test_agent", "ping")
    result = router.route(msg)

    assert result == "Got it: ping"
