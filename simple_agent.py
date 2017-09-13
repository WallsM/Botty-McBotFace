#TODO1: Off by 1 error for step count?

import sys
import gflags as flags

from pysc2.lib import actions
from pysc2.env import sc2_env
from pysc2.env import environment

FLAGS = flags.FLAGS

class Agent:

    def __init__(self):
        FLAGS(sys.argv)
        self.env =  sc2_env.SC2Env('Simple64', agent_race = "T", visualize=True)

    def think(self, obs):
        return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])

    def play(self):
        obs = self.env.reset()

        while obs[0].step_type != environment.StepType.LAST:
            obs = self.env.step(actions = [self.think(obs)])
        # TODO1: DO WE ALWAYS MISS THE LAST STEP HERE?

        self.env.close()

if __name__ == "__main__":
    ben = Agent()
    ben.play()