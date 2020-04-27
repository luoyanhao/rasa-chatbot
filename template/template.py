import random


class TemplateWelcome():
    def __init__(self):
        self.sentence = [
            '您好，我是心理健康小助手，你有心理方面的问题可以向我咨询哦！'
        ]

    def getRandom(self):
        index = random.randint(0, len(self.sentence))
        return self.sentence[index]

class TemplateOther():
    def __init__(self):
        self.sentence = [
            '我只能接受心理方面的问题哦！',
            '你有什么不舒服的吗？',
            '你心理方面有什么异常吗？',
            '你身体方面有什么异常吗？'
        ]

    def getRandom(self):
        index = random.randint(0,len(self.sentence))
        return self.sentence[index]

class TemplateAsk():
    def __init__(self):
        self.sentence = [

            '你最近有##sym##的感觉么？',
            '近期有##sym##的情况吗？',
            '嗯嗯，那有出现##sym##的情况吗？',
            '好的，那你最近有##sym##的感受吗？',
            '最近存在##sym##的现象吗？',
            '这几天有感觉##sym##吗？'
        ]

    def getRandom(self, symptom):
        index = random.randint(0,len(self.sentence))
        template = self.sentence[index]
        return template.replace('##sym##', symptom)

class TemplateGuide():
    def __init__(self):
        self.sentence = [

            '好的，能详细聊聊吗？',
            '为什么会这样啊？',
            '你有感觉到是哪方面的原因吗？'
        ]

    def getRandom(self):
        index = random.randint(0,len(self.sentence))
        return self.sentence[index]

class TemplateDiagnose():
    def __init__(self):
        self.diagnose = [
            '据我评估，您可能遭受##dis##的困扰。',
            '据我初步估计，您可能有##dis##的症状。'
        ]
        self.other = [
            '据我评估，你可能只是心理方面有一些异常，没有很大问题，放宽心啦~',
            '不要有太大压力，你只是心理状态出现了一些小状况。'
        ]

    def getRandom(self, res, disease):
        if res:
            index = random.randint(0,len(self.diagnose))
            return self.diagnose[index].replace('##dis##', disease)
        else:
            index = random.randint(0,len(self.other))
            return self.diagnose[index]

class TemplateFileRecommend():
    def __init__(self):
        self.sentence = [
            '给您推荐几篇文章，缓解一下心情~',
            '我找到一下文章，可能会对你有帮助。'
        ]

    def getRandom(self):
        index = random.randint(0,len(self.sentence))
        return self.sentence[index] + '\n'

class TemplateMusicRecommend():
    def __init__(self):
        self.sentence = [
            '建议戴上耳机好好倾听一下这几首歌，调节一下心情！'
        ]

    def getRandom(self):
        index = random.randint(0,len(self.sentence))
        return self.sentence[index] + '\n'

class TemplateBye():
    def __init__(self):
        self.sentence = [
            '祝你早日摆脱心理问题的困扰哦'
        ]

    def getRandom(self):
        index = random.randint(0, len(self.sentence))
        return self.sentence[index]

class TemplateAgeAsk():
    def __init__(self):
        self.sentence = [

        ]

    def getRandom(self):
        index = random.randint(0,len(self.sentence))
        return self.sentence[index]

class TemplateGenderAsk():
    def __init__(self):
        self.sentence = [
            '你是小哥哥还是小姐姐啊',

        ]

    def getRandom(self):
        index = random.randint(0, len(self.sentence))
        return self.sentence[index]

class TemplatedurationAsk():
    def __init__(self):
        self.sentence = [

            '你好，这种情况持续多久了？',

        ]

    def getRandom(self):
        index = random.randint(0,len(self.sentence))
        return self.sentence[index]

class TemplateMusic():
    def __init__(self):
        self.sentence = [

            '如果仍感觉不适的话，我还可以给你推荐几首音乐哦',
        ]

    def getRandom(self):
        index = random.randint(0,len(self.sentence))
        return self.sentence[index]