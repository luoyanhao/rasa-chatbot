import logging
from typing import List, Text, Any, Optional, Dict
from rasa_nlu_gao.classifiers import INTENT_RANKING_LENGTH

from rasa.nlu.components import Component
from rasa.nlu.model import Metadata
from rasa.nlu.training_data import Message

import os
import shutil
import kashgari
from kashgari.embeddings import BERTEmbedding
import kashgari.tasks.classification as clf
from kashgari.processors import ClassificationProcessor
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau

logger = logging.getLogger(__name__)


class RuleCauseClassifier(Component):
    provides = ["cause"]
    defaults = {
    }
    requires = ["tokens"]
    language_list = ["en", "zh"]

    def __init__(self,
                 component_config=None,
                 model = None):
        super(RuleCauseClassifier, self).__init__(component_config)

        self.xueye = ['学业','考试','挂科','学习']
        self.lianai = ['男友','男朋友','女友','女朋友','分手','失恋']
        self.renjiguanxi = ['吵架','同学','老师','导师','室友','舍友']
        self.shiying = []
        self.jiuye = ['面试','找工作','毕业','就业','实习','工作']

    def train(self, training_data, cfg, **kwargs):
        pass

    def process(self, message, **kwargs):
        tokens = message.get("tokens", [])
        res = set()
        for t in tokens:
            w = t.text
            if len(w) < 2:
                continue
            for temp in self.xueye:
                if temp == w:
                    res.add(0)
            for temp in self.lianai:
                if temp == w:
                    res.add(1)
            for temp in self.renjiguanxi:
                if temp == w:
                    res.add(2)
            for temp in self.shiying:
                if temp == w:
                    res.add(3)
            for temp in self.jiuye:
                if temp == w:
                    res.add(4)


        message.set("cause", list(res), add_to_output=True)

    def get_intent_score(self, message):
        intent_top_k = self.model.predict_top_k_class(
            [self.tokenizer.tokenize(message.text)],
            top_k = INTENT_RANKING_LENGTH
        )[0]

        if self.multi_label:
            intent_ranks = []
        else:
            intent_ranks = [{
                'name': intent_top_k['label'],
                'confidence': float(intent_top_k['confidence'])
            }]

        for item in intent_top_k['candidates']:
            intent_ranks.append({'name': item['label'], 'confidence': float(item['confidence'])})

        return intent_ranks

    def persist(self,
                file_name: Text,
                model_dir: Text) -> Optional[Dict[Text, Any]]:
        pass

