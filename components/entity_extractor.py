from rasa.nlu.components import Component
import datetime

from NamedEntityRecognition.lstm_predict import LSTMNER
from typing import Any, Dict, List, Optional, Text
class BiLSTMEntityExtractor(Component):
    """预训练情感分析组件"""

    name = "sentiment"
    provides = ["entities"]
    requires = []
    defaults = {}
    language_list = ["en","zh"]

    def __init__(self, component_config=None):
        super(BiLSTMEntityExtractor, self).__init__(component_config)
        self.lstm = LSTMNER()

    def train(self, training_data, cfg, **kwargs):
        """不需要实现该方法，因为预训练模型已经训练了。"""
        pass

    def convert_to_rasa(self, value):
        """将模型输出转换为 Rasa NLU 兼容的输出格式。"""

        entity = {"value": value,
                  "entity": "sentiment",
                  "extractor": "sentiment_extractor"}

        return entity

    def process(self, message, **kwargs):
        """检索文本消息，并将其传给分类器，
           将预测结果追加到 message 中。"""

        res = self.lstm.predict(message.text)
        key = '烦躁'


        print("jinru")
        entity = self.convert_to_rasa(key)
        print(datetime.datetime.now())
        message.set("entities", message.get("entities", [])+[entity], add_to_output=True)

    def persist(self,
                file_name: Text,
                model_dir: Text) -> Optional[Dict[Text, Any]]:
        """不需要实现该方法，因为预训练模型已经持久化了。"""

        pass