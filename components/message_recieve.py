import logging
from typing import List, Text, Any, Optional, Dict
from DBService.models import User
from rasa.nlu.components import Component

import datetime
import os

from DBService.DBService import DBService

logger = logging.getLogger(__name__)



from DBService.models import  State
class UserInit(Component):
    provides = []

    defaults = {

    }
    language_list = ["en", "zh"]

    def __init__(self,
                 component_config=None,
                 model = None):
        super(UserInit, self).__init__(component_config)


    def train(self, training_data, cfg, **kwargs):
       pass

    def process(self, message, **kwargs):
        print(datetime.datetime.now())
        db = DBService()
        openid = message.text
        user = User.objects(user_id=openid)
        if len(user) == 0:
            print("new yonghu,add")
            new = User(user_id = openid)
            new.save()
            state = State(openid = openid, need_age=True, need_gender=True)
            state.save()
        else:
            now = datetime.datetime.now()
            state = State.objects(openid=openid)[0]
            last = state.last_dialog
            if (now - last).seconds > 100:
                print("new 对话")
                state.delete()
                state = State(openid = openid)
                state.save()

            else:
                state.last_dialog = datetime.datetime.now()
                state.save()




def persist(self,
                file_name: Text,
                model_dir: Text) -> Optional[Dict[Text, Any]]:
        model_path = os.path.join(model_dir, file_name)
        pass
