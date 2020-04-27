import logging
from rasa.nlu.tokenizers import Token, Tokenizer
from typing import List, Text, Any, Optional, Dict
import datetime
import os
import jieba
from rasa.nlu.extractors import EntityExtractor

from DBService.models import Reference
logger = logging.getLogger(__name__)


class RuleEntityExtractor(EntityExtractor):
    provides = ["entity"]

    defaults = {}
    requires = ["tokens"]
    language_list = ["en", "zh"]

    def __init__(self,
                 component_config=None,
                 model = None):
        super(RuleEntityExtractor, self).__init__(component_config)


    def train(self, training_data, cfg, **kwargs):
       pass
    def convert_to_rasa(self, value):
        """将模型输出转换为 Rasa NLU 兼容的输出格式。"""

        entity = {"value": value,
                  "entity": "sentiment",
                  "extractor": "sentiment_extractor"}

        return entity
    def process(self, message, **kwargs):
        tokens = message.get("tokens", [])
        res = []
        for t in tokens:
            w = t.text
            if len(w) < 2:
                continue
            key = Reference.objects(key = w)
            if len(key) == 0: continue
            res.append({'value':key[0].value,  'entity':key[0].type})

        extracted = self.add_extractor_name((res))
        print(datetime.datetime.now())
        message.set("entities",
                message.get("entities", []) + extracted,
                add_to_output=True)
    def persist(self,
                file_name: Text,
                model_dir: Text) -> Optional[Dict[Text, Any]]:
        model_path = os.path.join(model_dir, file_name)


