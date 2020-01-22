import jieba


def key_word(data_str):
    loss_list = ['等', '、', '\n', '\t', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '的', '和', '：', '，', '.', '。',
                 '与',
                 '/', ' ', ')', '；', '有', '公司']
    get_list = ['python', '经验', 'Linux', 'PaaS', 'IaaS', 'django', 'Javascript', 'CSS', 'html', 'Bootstrap', 'Jquery ',
                'github', 'XPath', 'HTTP', 'TCP', 'IP', '爬虫', 'scrapy', 'pyspider', 'MySQL', 'Redis', 'MongoDB', '学历',
                'web', 'BUG', 'SQL', '正则', 'flask', 'tornado', 'redis', '线程']

    text = data_str
    _set = set(list(jieba.cut(text)))
    word_dict = {}
    for i in _set:
        num = list(jieba.cut(text)).count(i)
        if num >= 5 and i not in loss_list:
            word_dict[i] = num
    return word_dict
