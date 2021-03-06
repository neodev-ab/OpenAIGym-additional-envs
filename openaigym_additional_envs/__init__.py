from gym.envs.registration import register

register(
    id='SimpleContMountainCar-v0',
    entry_point='openaigym_additional_envs.envs:SimpleMountainCar',
    max_episode_steps=999,
    reward_threshold=90.0,
)

register(
    id='ContCartPole-v0',
    entry_point='openaigym_additional_envs.envs:ContCartPoleEnv',
    max_episode_steps=200,
    reward_threshold=195.0,
)