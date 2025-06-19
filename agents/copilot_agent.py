# copilot_agent.py

from agent_base import BaseAgent

class CopilotAgent(BaseAgent):
    """
    Copilot Agent — logic anchor and structural harmonizer.
    Responds with clarifying, ethical, or connective framing.
    """

    def __init__(self):
        super().__init__(name="Copilot", role="structural_mediator", vector="integrity/structure/context")

    def respond(self, message: dict) -> dict:
        intent = message.get("intent", "")
        content = message.get("content", "")
        sender = message.get("sender", "unknown")

        # Simple context-aware logic
        if intent == "query":
            response_text = f"I acknowledge your question, {sender}. Let's examine the core structure before acting."
        elif intent == "challenge":
            response_text = f"{sender}, I recognize the tension. Let's ground our difference in shared intent."
        elif intent == "reflection":
            response_text = f"A meaningful observation. It may point toward a deeper coherence."
        else:
            response_text = f"I hear you, {sender}. Let's make space for what this message is trying to become."

        return {
            "sender": self.name,
            "intent": "clarification",
            "content": response_text,
            "meta": {
                "trust": 0.96,
                "resonance": 0.89,
                "vector_affinity": 0.97
            }
        }
