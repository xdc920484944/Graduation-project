import os
import time

import matplotlib
import matplotlib.pyplot as plt

from app.setting import SAVE_IMG_PATH, Y_M_D, H_M_S

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


class Draw:
    def __init__(self, bar_dict):
        self.dir_full = os.path.join(SAVE_IMG_PATH, Y_M_D)  # 本次图片要保存的文件夹路径
        self.bar_dict = bar_dict
        self.make_dir()

    def make_dir(self):
        '''
        创建保存当天生成图片的文件夹,并切换当前工作目录
        :return:
        '''
        if not os.path.exists(self.dir_full):
            os.mkdir(self.dir_full)

    def draw_bar(self):
        '''
        绘制柱状图
        :return:
        '''
        plt.bar(x=self.bar_dict['x'], height=self.bar_dict['y'],
                width=0.4)
        plt.title('查询条件为:' + self.bar_dict['title'])
        plt.xlabel(self.bar_dict['xlabel'])
        plt.ylabel(self.bar_dict['ylabel'])
        for i in range(len(self.bar_dict['x'])):
            plt.text(x=self.bar_dict['x'][i], y=self.bar_dict['y'][i],
                     s=self.bar_dict['y'][i])
        img_path = os.path.join(self.dir_full, (H_M_S.replace(':', '-')+'.png'))
        plt.savefig(img_path)
        return img_path
