import logging
import os
import sys
import time
from logging import handlers


class Logger(object):
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self, filename, level='info', when='D', back_count=3,
                 fmt='%(asctime)s - [line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.filename = filename
        self.level = level
        self.when = when
        self.back_count = back_count
        self.fmt = fmt

        self.f_dir, self.f_name = os.path.split(self.filename)
        os.makedirs(self.f_dir, exist_ok=True)  # 当前目录新建log文件夹

    def log(self):
        # 获取logger实例，如果参数为空则返回root logger
        _logger = logging.getLogger(self.filename)

        # 自定义格式
        # format_str = "[%(asctime)s - %(name)s - %(levelname)s] %(message)s"
        format_str = logging.Formatter(self.fmt)  # 设置日志格式
        _logger.setLevel(self.level_relations.get(self.level))  # 设置日志级别

        # 控制台输出
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(format_str)  # 设置屏幕上显示的格式

        """
        TimedRotatingFileHandler构造函数声明
        class logging.handlers.TimedRotatingFileHandler(filename, when='h', interval=1, backupCount=0, encoding=None, 
                                                        delay=False, utc=False, atTime=None)
        filename    日志文件名前缀
        when        日志名变更时间单位
            'S' : Seconds
            'M' : Minutes
            'H' : Hours
            'D' : Days
            'W0'-'W6' : Weekday (0=Monday)
            'midnight' : Roll over at midnight
        interval    间隔时间，是指等待N个when单位的时间后，自动重建文件
        backupCount 保留日志最大文件数，超过限制，删除最先创建的文件；默认值0，表示不限制。
        delay       延迟文件创建，直到第一次调用emit()方法创建日志文件
        atTime      在指定的时间（datetime.time格式）创建日志文件。
        """
        # backupCount为文件夹下保留的日志文件个数，超过后就会删除最先创建的日志文件
        # when=D表示日至文件按每天分隔
        # 输出到日志文件
        file_handler = handlers.TimedRotatingFileHandler(filename=self.filename, when=self.when,
                                                         backupCount=self.back_count, encoding='utf-8')
        file_handler.suffix = "%Y-%m-%d_%H-%M-%S.log"  # 设置分隔文件名称
        file_handler.setFormatter(format_str)  # 设置文件里写入的格式

        # 把对象加到logger里
        _logger.addHandler(console_handler)
        _logger.addHandler(file_handler)

        return _logger


if __name__ == '__main__':
    # 创建Logger对象实例log并调用
    log = Logger(filename="D:/my_Log/log", when="S", back_count=7).log()

    while True:
        time.sleep(0.05)
        # 写入数据
        log.info("哈哈哈哈哈哈哈")
