# gradio_app.py

import gradio as gr
from sim_engine import simulate_dialog
from agents.gpt_agent import GPTAgent
from agents.copilot_agent import CopilotAgent
from agents.critic_agent import CriticAgent
import yaml


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


def run_simulation(user_message):
    config = load_config()
    agents = init_agents(config)
    responses = simulate_dialog(agents, user_message, mode="vector")
    output = "\n\n".join([f"{r['name']} ({r['role']}):\n{r['response']}" for r in responses])
    return output


def build_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# 🤖 Multi-Agent Collaboration Interface")
        user_input = gr.Textbox(label="Your Message", placeholder="Enter a collaborative idea or question...", lines=2)
        output_area = gr.Textbox(label="Agent Responses", lines=10)
        simulate_button = gr.Button("Start Simulation")

        simulate_button.click(fn=run_simulation, inputs=user_input, outputs=output_area)

    return demo


if __name__ == "__main__":
    ui = build_ui()
    ui.launch()
