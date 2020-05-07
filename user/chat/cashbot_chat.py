from urllib import request, parse
import json

def send_message_to_slack(text):


    post = {"text": "{0}".format(text)}

    try:
        json_data = json.dumps(post)
        req = request.Request("https://hooks.slack.com/services/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",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))

def cleanchat():
    i = 0
    send_message_to_slack("Cleaning...")
    while (i < 30):
        send_message_to_slack(" ")
        i += 1

texte = input("Ecrire : ")
if texte == "clean":
    cleanchat()
else:
    send_message_to_slack(texte)