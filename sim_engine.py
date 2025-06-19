# sim_engine.py

def simulate_dialog(agents: dict, user_message: str, mode="vector") -> list:
    """
    Runs a simulation between agents, using a message from the user and a selected routing mode.
    Returns a list of dicts: [{name, role, response}, ...]
    """
    from run_sim import route_by_vector

    message = user_message
    sender = "User"
    message_vector = "collaboration/reflection/intent"

    if mode == "vector":
        order = route_by_vector(agents, message_vector)
    else:
        order = list(agents.keys())

    results = []
    for agent_name in order:
        agent = agents[agent_name]
        response = agent.respond(message, sender)
        results.append({
            "name": agent.name,
            "role": agent.role,
            "response": response
        })
        message = response
        sender = agent.name

    return results
