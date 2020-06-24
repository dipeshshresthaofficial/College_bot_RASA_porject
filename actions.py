# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
import smtplib
#
#
class ActionDisplayCourse(Action):

    def name(self) -> Text:
        return "action_display_course"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Inside actions")
        conn = sqlite3.connect('college2.db')
        user_message = str((tracker.latest_message)['text'])

        print("User message : ", user_message)
        if "UG" in user_message:
            exe_str = "Select course_name from courses where program is '{0}'".format('UG')
        elif 'PG' in user_message:
            exe_str = "Select course_name from courses where program is '{0}'".format('PG')

        try:
            content = conn.execute(exe_str)
            content_text = ''
            content_text += "We offer following courses for now:\n\n"
            for index, value in enumerate(content):
                content_text += str(index + 1) + ") " + str(value[0]) + "\n"

            content_text += "Enter item number (eg : 1 or 2 or 3 ...)"
            dispatcher.utter_message(text=content_text)

        except:
            content_text = "Sorry system run into trouble.. Can you please check again?"
            dispatcher.utter_message(text=content_text)

        return []

class ActionDisplayCourseInfo(Action):

    def name(self) -> Text:
        return "action_display_course_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Inside actions")
        conn = sqlite3.connect('college2.db')
        user_message = str((tracker.latest_message)['text'])
        messages = []

        for event in (list(tracker.events))[:15]:
            if event.get("event") == "user":
                messages.append(event.get("text"))

        user_message = messages[-1]
        print("All messages till now : \n",messages)
        print("user_message : ",user_message)
        program=""

        if "UG" in user_message:
            exe_str = "Select description,duration,fee,syllabus_link from courses where program is '{0}'".format('UG')
            program+="Under Graduate"
        elif 'PG' in user_message:
            exe_str = "Select description,duration,fee,syllabus_link from courses where program is '{0}'".format('PG')
            program+="Post Graduate"

        try:

            content = conn.execute(exe_str)
            content_text = ''
            user_input = str((tracker.latest_message)['text'])
            print(type(user_input))
            user_input = int(user_input)
            print(user_input)
            
            for index, value in enumerate(content):
                if(index+1)==user_input:
                    content_text += str(value[0]) + "\n\n"+"Total Duration: "+str(value[1])+"\n\n"+"Total Fee: "+str(value[2])+"\n\n"+"You can find the syllabus here: "+str(value[3])

            content_text+="\n1) Enroll"+"\n2) Exit"
            content_text += "Enter item number (eg : 1 or 2 ...)"
            dispatcher.utter_message(text=content_text)
        except:
            ontent_text = "Sorry system run into trouble.. Can you please check again?"
            dispatcher.utter_message(text=content_text)

        return []
