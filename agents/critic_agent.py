# agents/critic_agent.py

from agents.agent_base import Agent

class CriticAgent(Agent):
    """
    Agent responsible for evaluating and critiquing other agents' responses.
    """

    def respond(self, message: str, sender: str) -> str:
        score = self.evaluate(message)
        if score >= 0.8:
            return f"{sender}, your message is clear and logically sound. [score: {score:.2f}]"
        elif score >= 0.5:
            return f"{sender}, your message is acceptable, but could use refinement. [score: {score:.2f}]"
        else:
            return f"{sender}, your message lacks clarity or coherence. Let's improve it. [score: {score:.2f}]"

    def evaluate(self, message: str) -> float:
        """
        Naive evaluation of message clarity and logic.
        """
        if not message.strip():
            return 0.0
        score = 0.5
        if message.endswith("."):
            score += 0.2
        if len(message.split()) > 5:
            score += 0.2
        return min(score, 1.0)
