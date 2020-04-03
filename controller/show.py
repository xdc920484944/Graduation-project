class SHOW:
    @classmethod
    def deal_data_of_hist(cls, keys, values):
        '''
        绘制柱状图前的数据整理
        :param keys: result的所有key
        :param values: result的所有value
        :return:return {'x': x坐标, 'y': y坐标, 'num': 数据条数, 'title': 图像标题, 'xlabel': x轴标题, 'ylabel': y轴标题}
        '''
        title = str(keys[0]) + str(values[0]) + '     ' + str(keys[1]) + str(values[1][0])
        data_num = '数据条数:' + str(values[3])
        x = list(values[5].keys())
        y = list(values[5].values())
        xlabel = '工资级'
        ylabel = '数量'
        return {'x': x, 'y': y, 'num': data_num, 'title': title, 'xlabel': xlabel, 'ylabel': ylabel}
