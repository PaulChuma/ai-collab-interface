# run_sim.py

import yaml
import random
from agents.gpt_agent import GPTAgent
from agents.copilot_agent import CopilotAgent
from agents.critic_agent import CriticAgent

def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)

def init_agents(config):
    agent_map = {}
    for agent_cfg in config["agents"]:
        name, role, agent_type = agent_cfg["name"], agent_cfg["role"], agent_cfg["type"]
        if agent_type == "GPTAgent":
            agent_map[name] = GPTAgent(name, role)
        elif agent_type == "CopilotAgent":
            agent_map[name] = CopilotAgent(name, role)
        elif agent_type == "CriticAgent":
            agent_map[name] = CriticAgent(name, role)
    return agent_map

# ✅ Updated vector similarity for list-based vectors
def vector_similarity(vec1, vec2) -> float:
    set1, set2 = set(vec1), set(vec2)
    return len(set1 & set2) / max(len(set1 | set2), 1)

def route_by_vector(agents: dict, message_vector: list) -> list:
    scored = [(agent, vector_similarity(agent.vector, message_vector)) for agent in agents.values()]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [a.name for a, _ in scored]

def simulate_dialog(agents, mode="sequential"):
    print("\n🔁 Starting simulation...\n")

    message = "Let’s begin a shared reflection. What does it mean to collaborate?"
    sender = "Pavel"
    message_vector = ["collaboration", "reflection", "intent"]

    if mode == "sequential":
        order = list(agents.keys())
    elif mode == "random":
        order = list(agents.keys())
        random.shuffle(order)
    elif mode == "vector":
        order = route_by_vector(agents, message_vector)
    else:
        order = list(agents.keys())  # fallback

    for agent_name in order:
        agent = agents[agent_name]
        print(f"→ {agent.name} ({agent.role}) received message:")
        print(f"   🧾 {message}\n")
        response = agent.respond(message, sender)
        print(f"   🔁 Response from {agent.name}:")
        print(f"   💬 {response}\n")
        message = response
        sender = agent.name

if __name__ == "__main__":
    config = load_config()
    agents = init_agents(config)
    simulate_dialog(agents, mode="vector")

if __name__ == "__main__":
    config = load_config()
    agents = init_agents(config)
    simulate_dialog(agents, mode="vector")
