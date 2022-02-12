# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict


class ValidateRestaurantForm(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        # required_slots = ["name", "number"]
        required_slots = ["my_name", "my_service", "my_breed"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # the slot is not filled yet. Request the user to fill this slot next
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]


class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self, dispatcher, tracker: Tracker, domain: DomainDict,
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            template="utter_submit_details",
            Name=tracker.get_slot("my_name"),
            Service=tracker.get_slot("my_service"),
            Breed=tracker.get_slot("my_breed")
        )

