from agents.agent_base import Agent

class CopilotAgent(Agent):
    """
    Copilot Agent — structural and ethical mediator.
    Responds with clarifying or grounding logic.
    """

    def __init__(self, name: str, role: str):
        super().__init__(name, role)
        self.vector = ["structure", "ethics", "clarification"]

    def respond(self, message: str, sender: str) -> str:
        lowered = message.lower()
        if "why" in lowered or "how" in lowered:
            return f"I acknowledge your question, {sender}. Let's examine the core structure before acting."
        elif "not" in lowered or "disagree" in lowered:
            return f"{sender}, I recognize the tension. Let's ground our difference in shared intent."
        elif "think" in lowered or "feel" in lowered:
            return f"A meaningful observation. It may point toward a deeper coherence."
        else:
            return f"I hear you, {sender}. Let's make space for what this message is trying to become."
