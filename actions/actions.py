# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# Import the beautifulsoup 
# and request libraries of python.
import requests
import bs4
import json

class ActionFindHospital(Action):

    def name(self) -> Text:
        return "action_find_hospital"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query = tracker.latest_message['text']

        print(query)

        url = 'https://google.com/search?q=' + query
        request_result=requests.get(url)
  
        soup = bs4.BeautifulSoup(request_result.text, "html.parser")
        hospitals = soup.find_all("div", {"class": "BNeawe deIvCb AP7Wnd"})

        hospital_name = []
        for hospital in hospitals[:-1]:
            hospital_name.append(hospital.text)
            print(hospital.text)

        json_reply = json.dumps(hospital_name)

        print(json_reply)

        dispatcher.utter_message(json_message = json_reply)

        return []
