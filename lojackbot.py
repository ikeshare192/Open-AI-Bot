import os
import openai
from flask import Flask, request
from dotenv import load_dotenv
from random import choice

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
completion = openai.Completion()

start_sequence = "\nIke_Newton"
restart_sequence = "\n\nPerson:"


start_chat_log = '''
Human: Hello, how are you?
AI: I am doing great. How can I help you today?
Human: I want to learn how to fly?
AI:  What do you currently do for a living?
Human: I am a nurse
AI: Do you want to become a professional pilot?
Human: Yes, I want to be a United Pilot.
AI: Have you any idea on how to fly?
Human: I have only been a passenger.
'''


def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
    engine="davinci",
    stop = ['\nHuman'],
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    best_of=1
    )
    answer = response.choices[0].text.strip()
    return answer

def append_interaction_to_chatlog(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Human: {question}\nAI {answer}\n'
