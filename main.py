import myLog
import logging

from Environment import Environment
from GA import GA

### 创建日志文件 ###
myLog.initLogging('myLog.log')
logging.info('Log Start!')

### 环境初始化 ###
env = Environment()
env.Initialize()
env.displayEnvironment()

### 遗传算法 ###
m_GA = GA(env, 50, 50, 0.1, 0.01, 0.3)
m_GA.Run()
m_GA.Display()
