from telegramapi import Bot

def test(bot: Bot, message):
    chatId = message['chat']['id']
    bot.send_message(chatId, 'Hello, ' + message['from']['first_name'])

    

if __name__ == '__main__':
    bot = Bot()
    bot.commands['/test'] = test
    
    #start listening
    try:
        bot.listen()
    except KeyboardInterrupt:
        print('Bye!')