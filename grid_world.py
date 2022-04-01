from matplotlib.pyplot import stem
import gym
import numpy as np 

class Grid_world(gym.Env):
    def __init__(self,):
        super(Grid_world,self).__init__()
        self.action_space = gym.spaces.discrete.Discrete(4)
        self.observation_space = gym.spaces.box.Box(low = 0,high = 9,shape=(2,))
        self._mines = [(4,5),(4,6),(4,7),(5,2),(5,3),(5,4)]
        self._action = [(0,1),(0,-1),(-1,0),(1,0)]

    def reset(self,):
        self._workd=[[0]*10 for i in range(10)]
        self._position = (0,0)
        return np.array(self._position)
    
    def step(self,action):
        # print(action)
        new_action = (self._action[action][0]+self._position[0],self._action[action][1]+self._position[1])
        self._position = (max(min(9,new_action[0]),0),max(min(9,new_action[1]),0))
        if self._position == (9,9):
            return (np.array(self._position), 1.0, True, {})
        if self._position in self._mines:
            return (np.array(self._position), -1.0, True, {})
        return (np.array(self._position), 0.0, False, {})

        

    def render(self,mode='human'):
        for i in range(10):
            for j in range(10):
                if (i,j) == self._position:
                    print("A",end=' ')
                elif (i,j) in self._mines:
                    print("M",end=' ')
                elif (i,j) == (9,9):
                    print("G",end=' ')
                elif (i,j) == (0,0):
                    print("S",end=' ')
                else:
                    print("O",end=' ')
            print(" ")
        print('==============')

    def seed(self, seed=None):
        np.random.seed(seed)


a = Grid_world()
a.reset()


