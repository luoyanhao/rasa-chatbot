# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from template.template import TemplateWelcome, TemplateAsk, TemplateOther


#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []
#
#
class ActionWelcome(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        template = TemplateWelcome()
        text = template.getRandom()
        dispatcher.utter_message(text)

        return []

class ActionSymptomAsk(Action):

    def name(self):  # type: () -> Text
        return "action_sym_ask"

    def run(
        self,
        dispatcher,  # type: CollectingDispatcher
        tracker,  # type: Tracker
        domain,  # type:  Dict[Text, Any]
    ):  # type: (...) -> List[Dict[Text, Any]]

        template = TemplateAsk()

        sym = tracker.get_slot()
        text = template.getRandom()
        dispatcher.utter_message(text)

        return []

class ActionOther(Action):

    def name(self):  # type: () -> Text
        return "action_other"

    def run(
        self,
        dispatcher,  # type: CollectingDispatcher
        tracker,  # type: Tracker
        domain,  # type:  Dict[Text, Any]
    ):  # type: (...) -> List[Dict[Text, Any]]

        template = TemplateOther()

        text = template.getRandom()
        dispatcher.utter_message(text)

        return[]