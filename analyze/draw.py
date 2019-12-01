import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
class Draw:
    def __init__(self,bar_dict):
        self.bar_dict = bar_dict
        if len(bar_dict) != 0:
            self.draw_bar()

    def draw_bar(self):
        plt.bar(x=self.bar_dict['x'],height=self.bar_dict['y'],
                width=0.4)
        plt.title('查询条件为:'+self.bar_dict['title'])
        plt.xlabel(self.bar_dict['xlabel'])
        plt.ylabel(self.bar_dict['ylabel'])
        for i in range(len(self.bar_dict['x'])):
            plt.text(x=self.bar_dict['x'][i],y=self.bar_dict['y'][i],
                     s=self.bar_dict['y'][i])
        plt.show()

# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [1, 2, 3, 4, 5, 6, 7, 8]
#
# x2 = [1, 2, 3, 4, 5, 6, 7, 8]
# y2 = [8, 7, 6, 5, 4, 3, 2, 1]
#
# plt.bar(x=x, height=y, width=0.4, )
# plt.bar(x=[i + 0.5 for i in x2], height=y2, width=0.4)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
