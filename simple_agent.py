"""
Docstring dfsdfs dfsd.

fsdfsdfsd fds
fsd
"""
from pysc2.agents import base_agent
from pysc2.lib import actions
from time import sleep


class SimpleAgent(base_agent.BaseAgent):
    ''' stop being annoying docstring '''
    def step(self, obs):
        super(SimpleAgent, self).step(obs)

        sleep(0.5)
        return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])
