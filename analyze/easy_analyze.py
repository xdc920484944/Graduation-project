# 表层数据分析

# 需要得到的数据格式:{查询的职业:[详细职业名，公司名，详细地址，工资，时间，招聘URL，公司URL，城市]}


class Easy_Analyze:
    def __init__(self, data_dict):
        self.data_dict = data_dict
        self.result = {'职业': '', '城市': '', '总数': 0, '已处理数:': 0, '未处理数:': 0, '工资': []}
        self.analyze()

    def analyze(self):
        for k, v in self.data_dict.items():
            for i in v:
                self.result['城市'] = [i[7]]
                self.result['工资'].append([i[3]])
        self.result['总数'] = len(v)
        self.result['职业'] = k
        self.result['工资'] = self.class_salary(self.result['工资'])
        # print(self.result['工资'])

    # 按层级分类工资
    def class_salary(self, salary_list):
        deal_salaly, undeal_salary = self.transfroms_salary(salary_list)
        self.result['已处理数:'] = len(deal_salaly)
        self.result['未处理数:'] = len(undeal_salary)
        # print('无法处理的数据法解析的工资数据:', undeal_salary)
        # print('解析后的工资数据:', deal_salaly)

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

    # 把工资格式全部转换为千/月
    def transfroms_salary(self, salary_list):
        '''
        :param salary_list:
        :return: 处理后的工资:deal_salary   无法处理的数据:undeal_salary
        '''
        undeal_salary = []
        deal_salary = []
        for s in salary_list:
            if type(s) is list and type(s[0]) is str:
                s = s[0]
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
                deal_salary.append(s)
            else:
                undeal_salary.append(s)

        return deal_salary, undeal_salary


if __name__ == '__main__':
    pass
    # result = Easy_Analyze(data_dict=data_dict)
