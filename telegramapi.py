import requests
import time

KEY = open('.key').read().strip()

url = 'https://api.telegram.org/bot' + KEY + '/'

class Bot:
    def __init__(self):
        self.lastUpdateId = 0
        self.commands = {}
    
    def send_message(self, chat_id, text):
        url = 'https://api.telegram.org/bot{}/sendMessage'.format(KEY)
        data = {'chat_id': chat_id, 'text': text}
        requests.post(url, json=data)

    # get updates
    def get_updates(self):
        url = 'https://api.telegram.org/bot{}/getUpdates'.format(KEY)
        data = {'offset': self.lastUpdateId + 1}
        print(data, self.lastUpdateId)
        updates = requests.get(url, json=data).json()['result']
        
        if len(updates) > 0:
            self.lastUpdateId = updates[-1]['update_id']

        return updates
    
    def listen(self):
        while True:
            updates = self.get_updates()
            for update in updates:
                message = update.get('message')
                if message and 'text' in message:
                    for command, callback in self.commands.items():
                        if message['text'].startswith(command):
                            callback(self, message)
                            break
                else:
                    print('Unknown update:', update)
            
            #dont overload server
            time.sleep(1)

