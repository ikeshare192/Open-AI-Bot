from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from lojackbot import ask, append_interaction_to_chatlog

app = Flask(__name__)
app.config['SECRET_KEY'] = "jdksafjkdl;as"

@app.route('/lojackbot', methods = ['POST'])

def lojackbot():
    incoming_msg = request.values['Body']
    chat_log = session.get("chat_log")

    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chatlog(incoming_msg, answer,
                                                         chat_log)

    r = MessagingResponse()
    r.message(answer)
    return str(r)

'''
if __name__ == '__main__':
    app.run()
'''