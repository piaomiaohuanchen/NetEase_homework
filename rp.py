import gym
class TimeLimitWrapper(gym.Wrapper):
    def __init__(self, env):
        super(TimeLimitWrapper, self).__init__(env)
        self._max_episode_steps = 100
        
        self._elapsed_steps = 0

    def step(self, ac):
        observation, reward, done, info = self.env.step(ac)
        self._elapsed_steps += 1
        if self._elapsed_steps >= self._max_episode_steps:
            done = True
        return observation, reward, done, info

    def reset(self, **kwargs):
        self._elapsed_steps = 0
        return self.env.reset(**kwargs)###


class Rewardshaping(gym.Wrapper):
    def __init__(self, env):
        super(Rewardshaping, self).__init__(env)


    def step(self, ac):
        observation, reward, done, info = self.env.step(ac)

        distance2 = 18 - observation[0] - observation[1]
        # if distance2 == self.distance:
        #     reward -= 0.05
        # else:
        #     reward += 0.05
        reward -= 0.05
        self.distance = distance2
        return observation, reward, done, info

    def reset(self, **kwargs):
        
        state = self.env.reset(**kwargs)###
        self.distance = 18 - state[0] - state[1]
        return state