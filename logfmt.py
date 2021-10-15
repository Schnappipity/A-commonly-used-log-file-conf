import os
import sys
import socket
import logging.handlers

hostname = socket.gethostname()
cur_file_name = sys._getframe(0).f_code.co_filename             # __file__
cur_path = os.path.abspath(os.path.dirname(cur_file_name))

# 指定logger输出格式
formatter = logging.Formatter(
    hostname + '\t' + '%(asctime)s' + '\t' + '%(levelname)s' + '\t' + '%(name)s %(filename)s:%(lineno)s - %(message)s'
)


# 文件日志
info_file_handler = logging.handlers.RotatingFileHandler(os.path.join(cur_path, './logs/info.log'), 'a', 200*1024*1024, 5)
info_file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
warn_file_handler = logging.handlers.RotatingFileHandler(os.path.join(cur_path, './logs/warn.log'), 'a', 200*1024*1024, 5)
warn_file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
error_file_handler = logging.handlers.RotatingFileHandler(os.path.join(cur_path, './logs/root.log'), 'a', 200*1024*1024, 5)
error_file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式


# 控制台日志
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.formatter = formatter  # 也可以直接给formatter赋值
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.formatter = formatter  # 也可以直接给formatter赋值

ilog_info = logging.getLogger("info")
ilog_info.addHandler(stdout_handler)
ilog_info.addHandler(info_file_handler)
ilog_info.setLevel(logging.INFO)

ilog_warn = logging.getLogger("warn")
ilog_warn.addHandler(stdout_handler)
ilog_warn.addHandler(warn_file_handler)
ilog_warn.setLevel(logging.WARNING)

ilog = logging.getLogger("error")
ilog.addHandler(stderr_handler)
ilog.addHandler(error_file_handler)
ilog.setLevel(logging.ERROR)
