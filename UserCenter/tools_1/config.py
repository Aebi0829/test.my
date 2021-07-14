#测试环境
HOST="http://client.testurls.com/"
# 线上环境
# HOST="https://client.alpfxg.co/login/"
import os

base_dir = os.path.split(os.path.abspath(__file__))[0]

#日志目录
log_dir = base_dir.replace("Common","Logs/")

#报告目录
report_dir = base_dir.replace("Common","HtmlReport")

# print(base_dir)