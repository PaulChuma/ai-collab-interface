# core/router.py

class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def to_dict(self):
        return {
            "from": self.sender,
            "to": self.receiver,
            "content": self.content
        }

class Router:
    def __init__(self):
        self.agents = {}

    def register(self, name, handler):
        self.agents[name] = handler

    def route(self, message: Message):
        receiver = self.agents.get(message.receiver)
        if receiver:
            return receiver.receive(message)
        return f"Agent '{message.receiver}' not found."


# Пример использования
if __name__ == "__main__":
    class EchoAgent:
        def receive(self, message):
            return f"[Echo:{message.receiver}] Received: {message.content}"

    router = Router()
    router.register("agent_a", EchoAgent())
    router.register("agent_b", EchoAgent())

    msg = Message("agent_a", "agent_b", "Привет, ты слышишь?")
    print(router.route(msg))
