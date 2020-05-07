import jieba

# 表层数据分析
# 需要得到的数据格式:{查询的职业:[职业名，公司名，详细地址，工资，时间，招聘URL，公司URL，城市]}
# {搜索关键字:[[职位名(0),公司名(1),薪资(2),发布时间(3),职位链接(4),公司链接(5),福利(6),要求(7),城市(8)], [],...]}
class Data_Analyze:
    def __init__(self, web):
        '''
        分类传入的数据
        :param data_dict:
        :return result:{已处理数:[],未处理数:[]}
        '''
        self.result = {'职业:': '', '城市:': '', '总数:': 0, '已处理数:': 0, '未处理数:': 0, '工资:': []}
        self.web = web

    def deal_data_freq(self, texts):
        '''
        将职位内容以精准模式切片
        :param texts:str
        :return:dict {k1:v1, k2:v2, ...}
        '''
        loss_list = ['等', '、', '\n', '\t', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '的', '和', '：', '，', '.',
                     '。', '与', '/', ' ', ')', '；', '有', '公司', ':', '\xa0', '及', '）', '以上', '-']
        eng_list = ['PYTHON', 'LINUX', 'HBASE', 'IAAS', 'DJANGO', 'JAVASCRIPT', 'CSS', 'HTML', 'BOOTSTRAP', 'JQUERY ',
                    'GITHUB', 'XPATH', 'HTTP', 'TCP', 'IP', 'SCRAPY', 'PYSPIDER', 'MYSQL', 'REDIS', 'MONGODB', 'WEB',
                    'BUG', 'SQL', 'FLASK', 'TORNADO', 'REDIS', 'HTML', 'JAVASCRIPT', 'CSS']

        chi_list = ['经验', '爬虫', '学历', '正则', '线程']
        _list = list(jieba.cut(texts))
        _set = set(_list)
        _dict = {}
        word_dict = {}
        for i in _set:
            k = i.upper() if i.isalpha() else i
            num = _list.count(i)
            if k in eng_list or k in chi_list:
                _dict[i] = num
            elif num >= 6 and i not in loss_list:
                _dict[i] = num

        keys = list(_dict.keys())
        values = list(_dict.values())
        word_dict['x'] = keys
        word_dict['y'] = values
        word_dict['title'] = '词频分析结果'
        word_dict['xlabel'] = '词名'
        word_dict['ylabel'] = '次数'
        return word_dict

    def sort_salary(self, data_dict):
        '''
        工资分级
        :param data_dict:
        :return:
        '''
        for k, v in data_dict.items():
            if self.web == '51job':
                for i in v:
                    self.result['城市:'] = [i[7]]
                    self.result['工资:'].append([i[3]])
            elif self.web == 'tc':
                for i in v:
                    self.result['城市:'] = [i[8]]
                    self.result['工资:'].append([i[2]])
        self.result['总数:'] = len(v)
        self.result['职业:'] = k
        self.result['工资:'] = self.class_salary(self.result['工资:'])
        return self.result

    def class_salary(self, salary_list):
        '''
        按层级分类工资
        :param salary_list: 工资列表
        :return: dict
        '''
        deal_salaly, undeal_salary = self.transfroms_salary(salary_list)
        self.result['已处理数:'] = len(deal_salaly)
        self.result['未处理数:'] = len(undeal_salary)
        salary_level = {'低于3000/月': 0, '3000-6000/月': 0, '6000-9000/月': 0, '9000-12000/月': 0, '1.2W-2W/月': 0,
                        '2W-5W/月': 0, '5W-10W/月': 0, '大于10W/月': 0}
        for s in deal_salaly:
            average_salary = (s[0] + s[1]) / 2
            if average_salary < 3:
                salary_level['低于3000/月'] += 1
            elif average_salary < 6:
                salary_level['3000-6000/月'] += 1
            elif average_salary < 9:
                salary_level['6000-9000/月'] += 1
            elif average_salary < 12:
                salary_level['9000-12000/月'] += 1
            elif average_salary < 20:
                salary_level['1.2W-2W/月'] += 1
            elif average_salary < 50:
                salary_level['2W-5W/月'] += 1
            elif average_salary < 100:
                salary_level['5W-10W/月'] += 1
            elif average_salary < 200:
                salary_level['大于10W/月'] += 1
        return salary_level

    def transfroms_salary(self, salary_list):
        '''
        把工资格式全部转换为千/月
        :param salary_list:
        :return: 处理后的工资:deal_salary   无法处理的数据:undeal_salary
        '''
        undeal_salary = []
        deal_salary = []
        for s in salary_list:
            if type(s) is list and type(s[0]) is str:
                s = s[0]
                if self.web == '51job':
                    if s is None:
                        undeal_salary.append(s)
                    elif '元/天' in s:
                        s = s.replace('元/天', '')
                        s = [float(s[0]) / 1000 * 30, float(s[0]) / 1000 * 30]
                    elif '千/月' in s:
                        s = s.replace('千/月', '').split('-')
                        s = [float(s[0]), float(s[1])]
                    elif '万/月' in s:
                        s = s.replace('万/月', '').split('-')
                        s = [float(s[0]) * 10, float(s[1]) * 10]
                    elif '十万/月' in s:
                        s = s.replace('十万/月', '').split('-')
                        s = [float(s[0]) * 100, float(s[1]) * 100]
                    elif '千/年' in s:
                        s = s.replace('千/年', '').split('-')
                        s = [float(s[0]) / 12, float(s[1]) / 12]
                    elif '万/年' in s:
                        s = s.replace('万/年', '').split('-')
                        s = [float(s[0]) / 1.2, float(s[1]) / 1.2]
                    elif '十万/年' in s:
                        s = s.replace('十万/年', '').split('-')
                        s = [float(s[0]) * 100 / 12, float(s[1]) * 100 / 12]
                    else:
                        undeal_salary.append(s)
                    if len(s) == 2:
                        deal_salary.append(s)
                elif self.web == 'tc':
                    if '面议' in s:
                        undeal_salary.append(s)
                    elif '元/月' in s:
                        s = s.replace('元/月', '').split('-')
                        s = s.append(s[0]) if len(s) == 1 else s  # 处理 XXX元/月
                        deal_salary.append([float(s[0])/1000, float(s[1])/1000])
            else:
                undeal_salary.append(s)

        return deal_salary, undeal_salary


if __name__ == '__main__':
    Data_Analyze(data_dict='').transfroms_salary(salary_list=['1.5千以下/月'])
