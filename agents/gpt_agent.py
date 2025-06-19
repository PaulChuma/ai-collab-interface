# agents/gpt_agent.py

from agents.agent_base import Agent

class GPTAgent(Agent):
    """
    Generative agent based on GPT-like behavior.
    Responds with elaboration, clarification or inquiry.
    """

    def __init__(self, name: str, role: str):
        super().__init__(name, role)
        self.vector = ["inquiry", "divergence", "synthesis"]

    def respond(self, message: str, sender: str) -> str:
        # Naive simulated GPT-like behavior
        if "?" in message:
            return f"As an AI, I would say: {message} is a deep question worth exploring."
        elif "you" in message.lower():
            return f"I'm reflecting on that. Let's go deeper, {sender}."
        else:
            return f"I acknowledge your message: '{message}'. Could you elaborate?"
