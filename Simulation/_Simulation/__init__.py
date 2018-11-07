from gym.envs.registration import register

register(
    id="Simulation-v0",
    entry_point="_Simulation.envs:SimulationEnv"
)