# run_sim.py

import yaml
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

def simulate_dialog(agents, mode="sequential"):
    print("\n🔁 Starting simulation...\n")

    message = "Let’s begin a shared reflection. What does it mean to collaborate?"
    sender = "Pavel"

    order = list(agents.keys()) if mode == "sequential" else random.shuffle(list(agents.keys()))
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
    simulate_dialog(agents, mode="sequential")
