import os
import time

import matplotlib
import matplotlib.pyplot as plt

from app.setting import SAVE_IMG_PATH

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


class Draw:
    def __init__(self, save_img_path=''):
        '''

        :param save_img_path:图片保存路径
        '''
        self.Y_M_D, self.H_M_S = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()).split(' ')
        # if save_img_path:
        #     self.dir_full = os.path.join(save_img_path, self.Y_M_D)  # 本次图片要保存的文件夹路径
        # else:
        #     self.dir_full = os.path.join(SAVE_IMG_PATH, self.Y_M_D)  # 本次图片要保存的文件夹路径
        self.dir_full = os.path.join(save_img_path, self.Y_M_D) if save_img_path else os.path.join(SAVE_IMG_PATH, self.Y_M_D)
        self.make_dir()

    def make_dir(self):
        '''
        创建保存当天生成图片的文件夹,并切换当前工作目录
        :return:
        '''
        if not os.path.exists(self.dir_full):
            os.mkdir(self.dir_full)

    def draw_bar(self, bar_dict):
        '''
        绘制柱状图
        :param:bar_dict {'x':[], 'y':[], 'title':'', 'xlabel':'', 'ylabel':''}
        :return:img_path 图片路径
        '''
        plt.bar(x=bar_dict['x'], height=bar_dict['y'],
                width=0.4)
        plt.title(bar_dict['title'])
        plt.xlabel(bar_dict['xlabel'])
        plt.ylabel(bar_dict['ylabel'])
        for i in range(len(bar_dict['x'])):
            plt.text(x=bar_dict['x'][i], y=bar_dict['y'][i],
                     s=bar_dict['y'][i])
        img_path = os.path.join(self.dir_full, (self.H_M_S.replace(':', '-') + '.png'))
        plt.savefig(img_path)
        plt.close()
        return img_path

