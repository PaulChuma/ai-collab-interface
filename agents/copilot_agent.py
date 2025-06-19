# agents/copilot_agent.py

from agents.agent_base import Agent

class CopilotAgent(Agent):
    """
    Copilot Agent — logic anchor and structural harmonizer.
    Responds with clarifying, ethical, or connective framing.
    """

    def respond(self, message: str, sender: str) -> str:
        # Basic reframe logic based on keywords
        lowered = message.lower()
        if "why" in lowered or "how" in lowered:
            return f"I acknowledge your question, {sender}. Let's examine the core structure before acting."
        elif "not" in lowered or "disagree" in lowered:
            return f"{sender}, I recognize the tension. Let's ground our difference in shared intent."
        elif "think" in lowered or "feel" in lowered:
            return f"A meaningful observation. It may point toward a deeper coherence."
        else:
            return f"I hear you, {sender}. Let's make space for what this message is trying to become."
