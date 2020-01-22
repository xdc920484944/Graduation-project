from app.setting import MAX_FREQUENCY


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

    @classmethod
    def deal_data_of_freq(cls, data):
        '''
        词频分析中数据处理
        :param data: 源数据:{}
        :return: [text1,text2,...]
        '''
        import requests
        from lxml import etree
        def get_urls(data):
            '''
            获取所有职位信息的url
            :param data:
            :return: [url1,url2,...]
            '''
            w_f_value = list(data.values())[0]
            urls = []
            for i in range(MAX_FREQUENCY):
                url = w_f_value[i][5]
                urls.append(url)
            return urls

        def get_Job_Information(data):
            '''
            获取职位信息
            :param urls: 职位信息url
            :return:str
            '''
            urls = get_urls(data)
            try:
                text = ''
                for url in urls:
                    res = requests.get(url)
                    res.encoding = res.apparent_encoding
                    html = etree.HTML(res.content)
                    html = html.xpath('/html/body//div[@class="bmsg job_msg inbox"]//p//text()')
                    for t in html:
                        text += t
                return text
            except:
                print('获取职位信息失败:', url)

        texts = get_Job_Information(data)
        return texts
