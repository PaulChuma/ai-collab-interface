# agents/agent_base.py

from abc import ABC, abstractmethod

class Agent(ABC):
    """
    Abstract base class for all agents in the system.
    """

    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    @abstractmethod
    def respond(self, message: str, sender: str) -> str:
        """
        Handle incoming message and return a response.
        """
        pass

    def describe(self) -> str:
        """
        Returns a brief description of the agent.
        """
        return f"{self.name} — {self.role}"
