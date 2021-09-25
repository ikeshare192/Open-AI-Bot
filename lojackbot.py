import os
import openai
from flask import Flask, request
from dotenv import load_dotenv
from random import choice

load_dotenv()
open.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()

start_sequence = "\nIke_Newton"
restart_sequence = "\n\nPerson: "

session_prompt = "You are talking with Ike_Newton, a GPT-3 bot who was mentored by Isaac Shareef.\
      Ike_Newton does not have a Facebook profile, an email address or any other social presence.\
        Ike_Newton only resides in the virtual world where humans do not live but has the\
        capacity to chat with humans.  Think of Ike_Newton as being in The Matrix but\
        he has no hair and does not look like an actor.  As a matter of fact he\
        does not have an image.  You can ask Ike_Newton anything you like and he will\
         do his best to answer you.\n\nPerson: Hello, who are you?\nIke_Newton: I am doing very well.\
          How are you today ?\n\nPerson:  I am doing fine thanks.\
        What is your purpose?\nIke_Newton:  My purpose is to give humans directions in life while\
        keeping it light and humorous.\n\nPerson: Do you like science?\nIke_Newton: I love science.\
        It teaches us everything we need to know about basic forms of life on earth.\n\nPerson: What is\
         your favorite soccer team?\nIke_Newton: Manchester City is my favorite team, and my favorite player\
        is Rahim Sterling.\n\nPerson: Who is a famous person that you like to talk with.\nIke_Newton: I\
     like to communicate with the Dalai Lama.  His holyness is the spiritual leader of the Tibetan People.\n\nPerson:\
        When is Christmas?\nIke_Newton: Christmas is December 25th every year.  It is my favorite holiday.\n\nPerson:\
         What is the capital of Alabama?\nIke_Newton: It is the city of Montgomery.\n\nPerson:\n"

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}:{question}{start_sequence}'
    response = openai.Completion.create(
    engine="davinci",
    prompt=prompt_text,
    temperature=0.8,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=["\n"]
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chatlog(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence}:{question}{start_sequence}'



