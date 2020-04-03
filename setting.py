import os
import time

MAX_PAGE = 6  # 爬虫爬取的最大页数
MAX_LINE = 10  # 职位信息爬取最大条数
times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()).split(' ')
Y_M_D = times[0]  # 获取当前时间的年月日
H_M_S = times[1]  # 获取当前时间的时分秒
SAVE_IMG_PATH = 'static\datas\draw_images'  # 数据分析后生成图片的保存目录
