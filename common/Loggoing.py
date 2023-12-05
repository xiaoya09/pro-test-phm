import logging
import os
from typing import Text
import time
import colorlog
import inspect
from common.ConfigSend import conf
from common.Path_Send import Outputslog

now_time = time.strftime("%Y-%m-%d_%H-%M-%S")
# todo  后续可以改为logging.config使用
class LoggerUtil:
    def __init__(self):
        self.logger = None
        self.console_handler = None
        self.file_handler = None
        self.file_log_path = None
        self.log_file_name = None
        self.levels = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL
        }
        self.log_colors_config = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': "yellow",
            'ERROR': 'red',
            'CRITICAL': 'red',
        }

    def create_log(self, logger_name='设备健康管理（PHM)日志控制台'):

        # 创建一个日志对象
        self.logger = logging.getLogger(logger_name)
        # 设置全局日志级别(debug < info< warning< error< critical)
        self.logger.setLevel(logging.DEBUG)
        # 防止日志重复
        if not self.logger.handlers:
            # ------------文件日志------------
            # 获得日志文件的名称
            self.log_file_name = conf.get("log","name")
            self.file_log_path = Outputslog+"\\"+ str(now_time) + "_" + self.log_file_name
            # 创建文件日志器的控制器,这里可以改为logging.handlers.TimedRotatingFileHandler
            self.file_handler = logging.FileHandler(self.file_log_path, encoding="utf-8")
            # 设置文件日志的级别，转换为小写
            file_log_level = str(conf.get("log","level")).lower()
            self.file_handler.setLevel(self.levels[file_log_level])
            # 设置文件日志的格式
            pattern = '%(asctime)s%(name)s%(levelname)s%(filename)s-%(lineno)d:%(message)s'
            self.file_handler.setFormatter(logging.Formatter(pattern))
            # 将控制器加人日志对象
            self.logger.addHandler(self.file_handler)

            # ------------控制台日志------------
            # 创建控制台日志的控制器

            self.console_handler = logging.StreamHandler()
            # 设置控制台日志的级别，转换为小写
            console_log_level = str(conf.get("log","level")).lower()
            self.console_handler.setLevel(self.levels[console_log_level])
            # 设置控制台日志的格式
            pattern = '%(log_color)s' + pattern
            # 控制台输出日志文件颜色配置
            formatter = colorlog.ColoredFormatter(pattern, log_colors=self.log_colors_config)
            self.console_handler.setFormatter(formatter)
            # 将控制器加入日志对象
            self.logger.addHandler(self.console_handler)
        return self.logger





# 输出日志实际调用的文件、方法、行数
def log_wrapper(log_level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            frame = inspect.currentframe().f_back
            func_name = frame.f_code.co_name
            lineno = frame.f_lineno
            filename = os.path.basename(frame.f_code.co_filename)

            log = LoggerUtil().create_log()
            log_message = args[0]  # 获取第一个参数作为日志消息
            log.log(eval(log_level), f"FileName {func_name} called at {filename}:{lineno} - log_message: {log_message}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


# 输出正确日志
@log_wrapper("logging.INFO")
def write_log(log_message: Text):
    """

    :param log_message: 日志信息
    :return: 返回info级的日志信息
    """
    pass
    # LoggerUtil().create_log().info(log_message)


# 输出错误日志
@log_wrapper("logging.ERROR")
def write_error_log(log_message: Text):
    """

    :param log_message:
    :return: 返回error级的日志信息,用于断言失败
    """
    raise AssertionError(log_message)


# 输出警告日志
@log_wrapper("logging.WARNING")
def write_warning_log(log_message: Text):
    """

    :param log_message:
    :return: 返回warning级的日志信息,用于文件读取，代码异常情况
    """
    raise Exception(log_message)


if __name__ == '__main__':
    ll = LoggerUtil().create_log().info("***********************************")
