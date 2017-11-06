import telepot
import time
from nanpy import ArduinoApi, SerialManager
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

connection = SerialManager(device='COM3') #or the port you are actually using
a = ArduinoApi(connection=connection)
a.pinMode(9, a.OUTPUT)
a.pinMode(10, a.OUTPUT)
a.pinMode(11, a.OUTPUT)
a.digitalWrite(9, 0)
a.digitalWrite(10, 0)
a.digitalWrite(11, 0)

r=0
g=0
b=0

def on_chat_message(msg): #create a customized keyboard
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="+", callback_data='/r+'), InlineKeyboardButton(text="+", callback_data='/g+'), InlineKeyboardButton(text="+", callback_data='/b+')],
                                     [InlineKeyboardButton(text="-", callback_data='/r-'), InlineKeyboardButton(text="-", callback_data='/g-'), InlineKeyboardButton(text="-", callback_data='/b-')]])

    bot.sendMessage(chat_id, 'Press to change the colour of the RGB LED\n \t \t \t Red \t \t \t \t \t \t \t \t Green \t \t \t \t \t \t \t \t \t \t Blue', reply_markup=keyboard)

def on_callback_query(msg): #change the RGB coordinates of the LED
    global r
    global g
    global b
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    
    if query_data == '/r+':
         if r==255:
                bot.answerCallbackQuery(query_id, text='Max value for red')
         else:
                    r+=1
                    a.analogWrite(11, r)
                    bot.answerCallbackQuery(query_id, text='(r, g, b)=(%d,%d,%d)' %(r,g,b))
    elif query_data == '/r-':
                        if r==0:
                            bot.answerCallbackQuery(query_id, text='Min avlue for red')
                        else:
                            r-=1
                            a.analogWrite(11, r)
                            bot.answerCallbackQuery(query_id, text='(r, g, b)=(%d,%d,%d)' %(r,g,b))
                
    elif query_data == '/g+':
            if g==255:
                bot.answerCallbackQuery(query_id, text='Max value for green')
            else:
                g+=1
                a.analogWrite(10, g)
                bot.answerCallbackQuery(query_id, text='(r, g, b)=(%d,%d,%d)' %(r,g,b))
    elif query_data == '/g-':
                        if g==0:
                            bot.answerCallbackQuery(query_id, text='Min value for green')
                        else:
                            g-=1
                            a.analogWrite(10, g)
                            bot.answerCallbackQuery(query_id, text='(r, g, b)=(%d,%d,%d)' %(r,g,b))
                
    elif query_data == '/b+':
            if b==255:
                bot.answerCallbackQuery(query_id, text='Max value for blue')
            else:
                b+=1
                a.analogWrite(9, b)
                bot.answerCallbackQuery(query_id, text='(r, g, b)=(%d,%d,%d)' %(r,g,b))
    elif query_data == '/b-':
                        if b==0:
                            bot.answerCallbackQuery(query_id, text='Min value for blue')
                        else:
                            b-=1
                            a.analogWrite(9, b)
                            bot.answerCallbackQuery(query_id, text='(r, g, b)=(%d,%d,%d)' %(r,g,b))

bot=telepot.Bot('*Insert your own TOKEN here*')
bot.message_loop({'chat': on_chat_message,
                  'callback_query': on_callback_query})
print ('Listening ...')

while 1:
    time.sleep(10)
