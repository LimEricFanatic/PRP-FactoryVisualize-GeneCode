import myLog
import logging

from Environment import Environment
from GASA import GASA

### 创建日志文件 ###
myLog.initLogging('myLog.log')
logging.info('Log Start!')

### 环境初始化 ###
env = Environment()
env.Initialize()
env.displayEnvironment()

### 遗传算法 ###
m_GASA = GASA(env, 20, 50, 0.3, 0.01, 100, 1, 0.7)
m_GASA.Run()
m_GASA.Display()
