import telebot
#import os

bot = telebot.TeleBot('1169393172:AAHP_ljzjUs2OmENifNNJWuUH2yRg9h7ty0')
#token=os.environ.get('BOT_TOKEN')
#bot.run(str(token))
profile =[0,0,0,0,0,0,0,0,0,0,0,0]
a1=''
b=''
i=0
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
1.Самочувствие\n
введите первый ответ:
""")
    bot.register_next_step_handler(msg, samochustvie1_name_step)
  
  
def samochustvie1_name_step(message):
    global profile

    try:
        chat_id = message.chat.id
        a1 = message.text
        if a1=='0':
            profile[0]=profile[0]+0
        elif a1 == '1':
            profile[3]=profile[3]+4
            profile[4]=profile[4]+5
            profile[5]=profile[5]+3
            profile[6]=profile[6]+4
            profile[7]=profile[7]+3
            profile[9]=profile[9]+3
            profile[10]=profile[10]+3
        elif a1=='2':
            profile[2]=profile[2]+4
        elif a1=='3':
            profile[0]=profile[0]+4
            profile[1]=profile[1]+5
        elif a1=='4':
            profile[0]=profile[0]+4
            profile[1]=profile[1]+4
            profile[8]=profile[8]+4
        elif a1=='5':
            profile[2]=profile[2]+100
            profile[4]=profile[4]+5
        elif a1=='6':
            profile[5]=profile[5]+4
        elif a1=='7':
            profile[3]=profile[3]+4
        elif a1=='8':
            profile[0]=profile[0]+4
            profile[1]=profile[1]+4
        elif a1=='9':
            profile[2]=profile[2]+4
        elif a1=='10':
            profile[5]=profile[5]+4
            profile[10]=profile[10]+3
            profile[11]=profile[11]+5
        elif a1=='11':
            profile[8]=profile[8]+4
            profile[9]=profile[9]+4
            profile[10]=profile[10]+3
        elif a1=='12':
            profile[7]=profile[7]+3
        elif a1=='13':
            profile[0]=profile[0]+0
            
        msg = bot.reply_to(message, 'введите второй ответ:')
        bot.register_next_step_handler(msg, samochustvie2_name_step)
    except:
        bot.reply_to(message, 'oooops')
        
def samochustvie2_name_step(message):
    global profile
    global b
    try:
        chat_id = message.chat.id
        a1 = message.text
        if a1=='0':
            profile[0]=profile[0]+0
        elif a1 == '1':
            profile[3]=profile[3]+4
            profile[4]=profile[4]+5
            profile[5]=profile[5]+3
            profile[6]=profile[6]+4
            profile[7]=profile[7]+3
            profile[9]=profile[9]+3
            profile[10]=profile[10]+3
        elif a1=='2':
            profile[2]=profile[2]+4
        elif a1=='3':
            profile[0]=profile[0]+4
            profile[1]=profile[1]+5
        elif a1=='4':
            profile[0]=profile[0]+4
            profile[1]=profile[1]+4
            profile[8]=profile[8]+4
        elif a1=='5':
            profile[2]=profile[2]+100
            profile[4]=profile[4]+5
        elif a1=='6':
            profile[5]=profile[5]+4
        elif a1=='7':
            profile[3]=profile[3]+4
        elif a1=='8':
            profile[0]=profile[0]+4
            profile[1]=profile[1]+4
        elif a1=='9':
            profile[2]=profile[2]+4
        elif a1=='10':
            profile[5]=profile[5]+4
            profile[10]=profile[10]+3
            profile[11]=profile[11]+5
        elif a1=='11':
            profile[8]=profile[8]+4
            profile[9]=profile[9]+4
            profile[10]=profile[10]+3
        elif a1=='12':
            profile[7]=profile[7]+3
        elif a1=='13':
            profile[0]=profile[0]+0
        msg = bot.reply_to(message, """2.Настроение\n
введите первый ответ:
""")
        bot.register_next_step_handler(msg, nastroenie1_name_step)
        #b=str(profile)#преоброзование списка
        #bot.send_message(message.chat.id, b)
    except:
        bot.reply_to(message, 'oooops')
    
def nastroenie1_name_step(message):
    global profile

    try:
        chat_id = message.chat.id
        a1 = message.text
        if a1=='0':
            profile[0]=profile[0]+0
        elif a1 == '1':
            profile[2]=profile[2]+4
        elif a1 == '2':
            profile[5]=profile[5]+5
            profile[11]=profile[11]+4
        elif a1 == '3':
            profile[3]=profile[3]+4
            profile[8]=profile[8]+4
        elif a1 == '4':
            profile[0]=profile[0]+4
            profile[1]=profile[1]+4
            profile[2]=profile[2]+4
        elif a1 == '5':
            profile[2]=profile[2]+100
            profile[4]=profile[4]+4
            profile[6]=profile[6]+5
            profile[9]=profile[9]+3
        elif a1 == '6':
            profile[0]=profile[0]+2
            profile[4]=profile[4]+4
            profile[5]=profile[5]+4
            profile[9]=profile[9]+3
        elif a1 == '7':
            profile[1]=profile[1]+100
            profile[7]=profile[7]+5
        elif a1 == '8':
            profile[11]=profile[11]+5
        elif a1 == '9':
            profile[0]=profile[0]+100
            profile[10]=profile[10]+3
            profile[11]=profile[11]+4
        elif a1 == '10':
            profile[5]=profile[5]+4
            profile[8]=profile[8]+4
        elif a1 == '11':
            profile[0]=profile[0]+100
            profile[3]=profile[3]+5
        elif a1=='12':
            profile[0]=profile[0]+0
            
        msg = bot.reply_to(message, 'введите второй ответ:')
        bot.register_next_step_handler(msg, nastroenie2_name_step)
    except:
        bot.reply_to(message, 'oooops')

def nastroenie2_name_step(message):
    global profile

    try:
        chat_id = message.chat.id
        a1 = message.text
        if a1=='0':
            profile[0]=profile[0]+0
        elif a1 == '1':
            profile[2]=profile[2]+4
        elif a1 == '2':
            profile[5]=profile[5]+5
            profile[11]=profile[11]+4
        elif a1 == '3':
            profile[3]=profile[3]+4
            profile[8]=profile[8]+4
        elif a1 == '4':
            profile[0]=profile[0]+4
            profile[1]=profile[1]+4
            profile[2]=profile[2]+4
        elif a1 == '5':
            profile[2]=profile[2]+100
            profile[4]=profile[4]+4
            profile[6]=profile[6]+5
            profile[9]=profile[9]+3
        elif a1 == '6':
            profile[0]=profile[0]+2
            profile[4]=profile[4]+4
            profile[5]=profile[5]+4
            profile[9]=profile[9]+3
        elif a1 == '7':
            profile[1]=profile[1]+100
            profile[7]=profile[7]+5
        elif a1 == '8':
            profile[11]=profile[11]+5
        elif a1 == '9':
            profile[0]=profile[0]+100
            profile[10]=profile[10]+3
            profile[11]=profile[11]+4
        elif a1 == '10':
            profile[5]=profile[5]+4
            profile[8]=profile[8]+4
        elif a1 == '11':
            profile[0]=profile[0]+100
            profile[3]=profile[3]+5
        elif a1=='12':
            profile[0]=profile[0]+0
            
        msg = bot.reply_to(message,"""3.Сон и пробуждение ото сна\n
введите первый ответ:
""")
        bot.register_next_step_handler(msg, son1_name_step)
    except:
        bot.reply_to(message, 'oooops')

def son1_name_step(message):
    global profile

    try:
        chat_id = message.chat.id
        a1 = message.text
        if a1=='0':
            profile[0]=profile[0]+0
        elif a1 == '1':
            profile[0]=profile[0]+3
            profile[1]=profile[1]+4
        elif a1 == '2':
            profile[6]=profile[6]+4
            profile[11]=profile[11]+3
        elif a1 == '3':
            profile[5]=profile[5]+4
            profile[8]=profile[8]+4
            profile[9]=profile[9]+3
            profile[10]=profile[10]+3
        elif a1 == '4':
            profile[5]=profile[5]+4
            profile[7]=profile[7]+3
        elif a1 == '5':
            profile[2]=profile[2]+3
        elif a1 == '6':
            profile[0]=profile[0]+2
        elif a1 == '7':
            profile[3]=profile[3]+4
            profile[5]=profile[5]+4
            profile[6]=profile[6]+4
            profile[9]=profile[9]+3
            profile[10]=profile[10]+3
            profile[11]=profile[11]+3
        elif a1 == '8':
            profile[2]=profile[2]+4
        elif a1 == '9':
            profile[1]=profile[1]+5
        elif a1 == '10':
            profile[3]=profile[3]+4
        elif a1 == '11':
            profile[6]=profile[6]+4
            profile[7]=profile[7]+4
        elif a1 == '12':
            profile[3]=profile[3]+4
            profile[4]=profile[4]+4
        elif a1 == '13':
            profile[4]=profile[4]+4
        elif a1 == '14':
            profile[0]=profile[0]+0
            
        msg = bot.reply_to(message, 'введите второй ответ:')
        bot.register_next_step_handler(msg, son2_name_step)
    except:
        bot.reply_to(message, 'oooops')

def son2_name_step(message):
    global profile

    try:
        chat_id = message.chat.id
        a1 = message.text
        if a1=='0':
            profile[0]=profile[0]+0
        elif a1 == '1':
            profile[0]=profile[0]+3
            profile[1]=profile[1]+4
        elif a1 == '2':
            profile[6]=profile[6]+4
            profile[11]=profile[11]+3
        elif a1 == '3':
            profile[5]=profile[5]+4
            profile[8]=profile[8]+4
            profile[9]=profile[9]+3
            profile[10]=profile[10]+3
        elif a1 == '4':
            profile[5]=profile[5]+4
            profile[7]=profile[7]+3
        elif a1 == '5':
            profile[2]=profile[2]+3
        elif a1 == '6':
            profile[0]=profile[0]+2
        elif a1 == '7':
            profile[3]=profile[3]+4
            profile[5]=profile[5]+4
            profile[6]=profile[6]+4
            profile[9]=profile[9]+3
            profile[10]=profile[10]+3
            profile[11]=profile[11]+3
        elif a1 == '8':
            profile[2]=profile[2]+4
        elif a1 == '9':
            profile[1]=profile[1]+5
        elif a1 == '10':
            profile[3]=profile[3]+4
        elif a1 == '11':
            profile[6]=profile[6]+4
            profile[7]=profile[7]+4
        elif a1 == '12':
            profile[3]=profile[3]+4
            profile[4]=profile[4]+4
        elif a1 == '13':
            profile[4]=profile[4]+4
        elif a1 == '14':
            profile[0]=profile[0]+0
            
        msg = bot.reply_to(message,"""4. Аппетит и отношение к еде\n
введите первый ответ:
""")
        bot.register_next_step_handler(msg, ap1_name_step)
    except:
        bot.reply_to(message, 'oooops')

def ap1_name_step(message):
    global profile
    global b
    try:
        chat_id = message.chat.id
        a1 = message.text
        if a1=='0':
            profile[0]=profile[0]+0
        elif a1 == '1':
            profile[8]=profile[8]+4
        elif a1 == '2':
            profile[0]=profile[0]+2
            profile[2]=profile[2]+3
        elif a1 == '3':
            profile[4]=profile[4]+3
            profile[5]=profile[5]+3
            profile[6]=profile[6]+4
            profile[7]=profile[7]+3
            profile[9]=profile[9]+3
        elif a1 == '4':
            profile[2]=profile[2]+3
        elif a1 == '5':
            profile[2]=profile[2]+3
        elif a1 == '6':
            profile[3]=profile[3]+3
            profile[5]=profile[5]+3
            profile[8]=profile[8]+3
            profile[9]=profile[9]+3
            profile[11]=profile[11]+3
        elif a1 == '7':
            profile[3]=profile[3]+3
            profile[10]=profile[10]+5
        elif a1 == '8':
            profile[1]=profile[1]+3
            profile[4]=profile[4]+3
            profile[7]=profile[7]+3
        elif a1 == '9':
            profile[4]=profile[4]+4
            profile[10]=profile[10]+4
        elif a1 == '10':
            profile[6]+=4
            profile[7]+=4
        elif a1 == '11':
            profile[0]+=0
            

        msg = bot.reply_to(message, 'введите второй ответ:')
        bot.register_next_step_handler(msg, ap2_name_step)
    except:
        bot.reply_to(message, 'oooops')

def ap2_name_step(message):
    global profile

    try:
        if a1=='0':
            profile[0]=profile[0]+0
        elif a1 == '1':
            profile[8]=profile[8]+4
        elif a1 == '2':
            profile[0]=profile[0]+2
            profile[2]=profile[2]+3
        elif a1 == '3':
            profile[4]=profile[4]+3
            profile[5]=profile[5]+3
            profile[6]=profile[6]+4
            profile[7]=profile[7]+3
            profile[9]=profile[9]+3
        elif a1 == '4':
            profile[2]=profile[2]+3
        elif a1 == '5':
            profile[2]=profile[2]+3
        elif a1 == '6':
            profile[3]=profile[3]+3
            profile[5]=profile[5]+3
            profile[8]=profile[8]+3
            profile[9]=profile[9]+3
            profile[11]=profile[11]+3
        elif a1 == '7':
            profile[3]=profile[3]+3
            profile[10]=profile[10]+5
        elif a1 == '8':
            profile[1]=profile[1]+3
            profile[4]=profile[4]+3
            profile[7]=profile[7]+3
        elif a1 == '9':
            profile[4]=profile[4]+4
            profile[10]=profile[10]+4
        elif a1 == '10':
            profile[6]+=4
            profile[7]+=4
        elif a1 == '11':
            profile[0]+=0

        #print(profile)
        msg = bot.reply_to(message, """5. Отношение к болезни\n
введите первый ответ:
""")
        bot.register_next_step_handler(msg, bolezn_name_step)
        #b=str(profile)#преоброзование списка
        #bot.send_message(message.chat.id, b)
    except:
        bot.reply_to(message, 'oooops')
        b=str(profile)#преоброзование списка
        bot.send_message(message.chat.id, b)

def bolezn_name_step(message):
    global profile
    global b
    try:
        chat_id = message.chat.id
        a1 = message.text
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[2]+=100
            profile[3]+=4
        elif a1 == '2':
            profile[1]+=100
            profile[6]+=4
            profile[7]+=5
        elif a1 == '3':
            profile[2]+=5
        elif a1 == '4':
            profile[8]+=5
        elif a1 == '5':
            profile[0]+=100
            profile[2]+=100
            profile[3]+=5
        elif a1 == '6':
            profile[2]+=100
            profile[4]+=4
            profile[6]+=5
            profile[7]+=3
        elif a1 == '7':
            profile[9]+=4
            profile[10]+=4
            profile[11]+=4
        elif a1 == '8':
            profile[2]+=5
        elif a1 == '9':
            profile[1]+=5
        elif a1 == '10':
            profile[2]+=100
            profile[3]+=4
            profile[4]+=5
            profile[6]+=4
            profile[9]+=4
        elif a1 == '11':
            profile[2]+=5
        elif a1 == '12':
            profile[9]+=5
        elif a1 == '13':
            profile[5]+=5
            profile[11]+=4
        elif a1 == '14':
            profile[10]+=5
            profile[11]+=4
        elif a1 == '15':
            profile[0]+=5
            profile[1]+=5
        elif a1 == '16':
            profile[0]+=0
            
        msg = bot.reply_to(message, 'введите второй ответ:')
        bot.register_next_step_handler(msg, bolezn2_name_step)
    except:
        bot.reply_to(message, 'oooops')

def bolezn2_name_step(message):
    global profile

    try:
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[2]+=100
            profile[3]+=4
        elif a1 == '2':
            profile[1]+=100
            profile[6]+=4
            profile[7]+=5
        elif a1 == '3':
            profile[2]+=5
        elif a1 == '4':
            profile[8]+=5
        elif a1 == '5':
            profile[0]+=100
            profile[2]+=100
            profile[3]+=5
        elif a1 == '6':
            profile[2]+=100
            profile[4]+=4
            profile[6]+=5
            profile[7]+=3
        elif a1 == '7':
            profile[9]+=4
            profile[10]+=4
            profile[11]+=4
        elif a1 == '8':
            profile[2]+=5
        elif a1 == '9':
            profile[1]+=5
        elif a1 == '10':
            profile[2]+=100
            profile[3]+=4
            profile[4]+=5
            profile[6]+=4
            profile[9]+=4
        elif a1 == '11':
            profile[2]+=5
        elif a1 == '12':
            profile[9]+=5
        elif a1 == '13':
            profile[5]+=5
            profile[11]+=4
        elif a1 == '14':
            profile[10]+=5
            profile[11]+=4
        elif a1 == '15':
            profile[0]+=5
            profile[1]+=5
        elif a1 == '16':
            profile[0]+=0

        #print(profile)
        msg = bot.reply_to(message, """6. Отношение к лечению\n
введите первый ответ:
""")
        bot.register_next_step_handler(msg, lech_name_step)
        #b=str(profile)#преоброзование списка
        #bot.send_message(message.chat.id, b)
    except:
        bot.reply_to(message, 'oooops')
        b=str(profile)#преоброзование списка
        bot.send_message(message.chat.id, b)
#print (profile)

def lech_name_step(message):
    global profile
    global b
    try:
        chat_id = message.chat.id
        a1 = message.text
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[0]+=100
            profile[1]+=3
            profile[2]+=5
        elif a1 == '2':
            profile[3]+=4
            profile[5]+=3
            profile[8]+=3
        elif a1 == '3':
            profile[0]+=4
            profile[1]+=3
            profile[4]+=4
        elif a1 == '4':
            profile[0]+=100
            profile[6]+=4
            profile[7]+=4
        elif a1 == '5':
            profile[1]+=100
            profile[3]+=3
            profile[4]+=4
            profile[9]+=4
        elif a1 == '6':
            profile[7]+=4
            profile[10]+=4
            profile[11]+=3
        elif a1 == '7':
            profile[0]+=100
            profile[1]+=100
            profile[3]+=4
        elif a1 == '8':
            profile[9]+=4
        elif a1 == '9':
            profile[10]+=5
        elif a1 == '10':
            profile[10]+=5
            profile[11]+=4
        elif a1 == '11':
            profile[0]+=100
            profile[2]+=5
        elif a1 == '12':
            profile[1]+=2
            profile[6]+=4
            profile[7]+=4
        elif a1 == '13':
            profile[0]+=3
            profile[8]+=4
        elif a1 == '14':
            profile[5]+=4
            profile[11]+=5
        elif a1 == '15':
            profile[0]+=0
            
        msg = bot.reply_to(message, 'введите второй ответ:')
        bot.register_next_step_handler(msg, lech2_name_step)
    except:
        bot.reply_to(message, 'oooops')

def lech2_name_step(message):
    global profile

    try:
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[0]+=100
            profile[1]+=3
            profile[2]+=5
        elif a1 == '2':
            profile[3]+=4
            profile[5]+=3
            profile[8]+=3
        elif a1 == '3':
            profile[0]+=4
            profile[1]+=3
            profile[4]+=4
        elif a1 == '4':
            profile[0]+=100
            profile[6]+=4
            profile[7]+=4
        elif a1 == '5':
            profile[1]+=100
            profile[3]+=3
            profile[4]+=4
            profile[9]+=4
        elif a1 == '6':
            profile[7]+=4
            profile[10]+=4
            profile[11]+=3
        elif a1 == '7':
            profile[0]+=100
            profile[1]+=100
            profile[3]+=4
        elif a1 == '8':
            profile[9]+=4
        elif a1 == '9':
            profile[10]+=5
        elif a1 == '10':
            profile[10]+=5
            profile[11]+=4
        elif a1 == '11':
            profile[0]+=100
            profile[2]+=5
        elif a1 == '12':
            profile[1]+=2
            profile[6]+=4
            profile[7]+=4
        elif a1 == '13':
            profile[0]+=3
            profile[8]+=4
        elif a1 == '14':
            profile[5]+=4
            profile[11]+=5
        elif a1 == '15':
            profile[0]+=0

        #print(profile)
        msg = bot.reply_to(message, """7. Отношение к врачам и медперсоналу\n
введите первый ответ:
""")
        bot.register_next_step_handler(msg, med_name_step)
        #b=str(profile)#преоброзование списка
        #bot.send_message(message.chat.id, b)
    except:
        bot.reply_to(message, 'oooops')
        b=str(profile)#преоброзование списка
        bot.send_message(message.chat.id, b)
#print (profile)

def med_name_step(message):
    global profile
    global b
    try:
        chat_id = message.chat.id
        a1 = message.text
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[0]+=3
            profile[1]+=2
            profile[4]+=4
            profile[8]+=4
            profile[9]+=5
        elif a1 == '2':
            profile[9]+=5
        elif a1 == '3':
            profile[10]+=5
        elif a1 == '4':
            profile[0]+=100
            profile[4]+=4
            profile[6]+=3
            profile[10]+=4
            profile[11]+=4
        elif a1 == '5':
            profile[7]+=5
        elif a1 == '6':
            profile[2]+=100
            profile[3]+=5
            profile[8]+=4
        elif a1 == '7':
            profile[11]+=4
        elif a1 == '8':
            profile[1]+=100
            profile[3]+=4
            profile[4]+=4
        elif a1 == '9':
            profile[0]+=3
            profile[1]+=2
            profile[8]+=3
        elif a1 == '10':
            profile[10]+=4
            profile[11]+=4
        elif a1 == '11':
            profile[5]+=5
        elif a1 == '12':
            profile[2]+=5
        elif a1 == '13':
            profile[0]+=100
            profile[2]+=5
            profile[6]+=4
            profile[7]+=4
        elif a1 == '14':
            profile[0]+=0
            
        msg = bot.reply_to(message, 'введите второй ответ:')
        bot.register_next_step_handler(msg, med2_name_step)
    except:
        bot.reply_to(message, 'oooops')

def med2_name_step(message):
    global profile

    try:
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[0]+=3
            profile[1]+=2
            profile[4]+=4
            profile[8]+=4
            profile[9]+=5
        elif a1 == '2':
            profile[9]+=5
        elif a1 == '3':
            profile[10]+=5
        elif a1 == '4':
            profile[0]+=100
            profile[4]+=4
            profile[6]+=3
            profile[10]+=4
            profile[11]+=4
        elif a1 == '5':
            profile[7]+=5
        elif a1 == '6':
            profile[2]+=100
            profile[3]+=5
            profile[8]+=4
        elif a1 == '7':
            profile[11]+=4
        elif a1 == '8':
            profile[1]+=100
            profile[3]+=4
            profile[4]+=4
        elif a1 == '9':
            profile[0]+=3
            profile[1]+=2
            profile[8]+=3
        elif a1 == '10':
            profile[10]+=4
            profile[11]+=4
        elif a1 == '11':
            profile[5]+=5
        elif a1 == '12':
            profile[2]+=5
        elif a1 == '13':
            profile[0]+=100
            profile[2]+=5
            profile[6]+=4
            profile[7]+=4
        elif a1 == '14':
            profile[0]+=0

        #print(profile)
        msg = bot.reply_to(message, """8. Отношение к родным и близким\n
введите первый ответ:
""")
        bot.register_next_step_handler(msg, rod_name_step)
        #b=str(profile)#преоброзование списка
        #bot.send_message(message.chat.id, b)
    except:
        bot.reply_to(message, 'oooops')
        b=str(profile)#преоброзование списка
        bot.send_message(message.chat.id, b)
#print (profile)

def rod_name_step(message):
    global profile
    global b
    try:
        chat_id = message.chat.id
        a1 = message.text
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[0]+=100
            profile[2]+=100
            profile[4]+=4
            profile[6]+=4
        elif a1 == '2':
            profile[0]+=4
            profile[1]+=4
            profile[8]+=4
        elif a1 == '3':
            profile[1]+=3
            profile[2]+=4
        elif a1 == '4':
            profile[3]+=4
        elif a1 == '5':
            profile[2]+=100
            profile[4]+=4
            profile[9]+=5
        elif a1 == '6':
            profile[5]+=3
            profile[9]+=5
            profile[10]+=3
            profile[11]+=4
        elif a1 == '7':
            profile[8]+=5
        elif a1 == '8':
            profile[0]+=100
            profile[6]+=4
            profile[7]+=4
        elif a1 == '9':
            profile[6]+=5
            profile[8]+=4
        elif a1 == '10':
            profile[5]+=3
            profile[11]+=4
        elif a1 == '11':
            profile[10]+=4
        elif a1 == '12':
            profile[0]+=4
            profile[1]+=3
        elif a1 == '13':
            profile[0]+=0
            
        msg = bot.reply_to(message, 'введите второй ответ:')
        bot.register_next_step_handler(msg, rod2_name_step)
    except:
        bot.reply_to(message, 'oooops')

def rod2_name_step(message):
    global profile

    try:
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[0]+=100
            profile[2]+=100
            profile[4]+=4
            profile[6]+=4
        elif a1 == '2':
            profile[0]+=4
            profile[1]+=4
            profile[8]+=4
        elif a1 == '3':
            profile[1]+=3
            profile[2]+=4
        elif a1 == '4':
            profile[3]+=4
        elif a1 == '5':
            profile[2]+=100
            profile[4]+=4
            profile[9]+=5
        elif a1 == '6':
            profile[5]+=3
            profile[9]+=5
            profile[10]+=3
            profile[11]+=4
        elif a1 == '7':
            profile[8]+=5
        elif a1 == '8':
            profile[0]+=100
            profile[6]+=4
            profile[7]+=4
        elif a1 == '9':
            profile[6]+=5
            profile[8]+=4
        elif a1 == '10':
            profile[5]+=3
            profile[11]+=4
        elif a1 == '11':
            profile[10]+=4
        elif a1 == '12':
            profile[0]+=4
            profile[1]+=3
        elif a1 == '13':
            profile[0]+=0

        #print(profile)
        msg = bot.reply_to(message, """9. Отношение к работе(учёбе)\n
введите первый ответ:
""")
        bot.register_next_step_handler(msg, rab_name_step)
        #b=str(profile)#преоброзование списка
        #bot.send_message(message.chat.id, b)
    except:
        bot.reply_to(message, 'oooops')
        b=str(profile)#преоброзование списка
        bot.send_message(message.chat.id, b)
#print (profile)

def rab_name_step(message):
    global profile
    global b
    try:
        chat_id = message.chat.id
        a1 = message.text
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[2]+=100
            profile[6]+=4
            profile[7]+=3
        elif a1 == '2':
            profile[3]+=4
            profile[8]+=4
        elif a1 == '3':
            profile[0]+=100
            profile[1]+=100
            profile[6]+=4
            profile[7]+=5
        elif a1 == '4':
            profile[0]+=100
            profile[2]+=100
            profile[4]+=4
            profile[6]+=4
            profile[7]+=3
        elif a1 == '5':
            profile[3]+=4
            profile[8]+=4
        elif a1 == '6':
            profile[10]+=4
            profile[11]+=4
        elif a1 == '7':
            profile[1]+=100
            profile[4]+=4
            profile[9]+=4
            profile[10]+=4
            profile[11]+=4
        elif a1 == '8':
            profile[1]+=5
            profile[2]+=4
        elif a1 == '9':
            profile[0]+=4
            profile[8]+=5
        elif a1 == '10':
            profile[0]+=4
            profile[1]+=5
        elif a1 == '11':
            profile[5]+=4
        elif a1 == '12':
            profile[0]+=4
            profile[1]+=4
        elif a1 == '13':
            profile[2]+=3
        elif a1 == '14':
            profile[2]+=4
        elif a1 == '15':
            profile[0]+=0
            
        msg = bot.reply_to(message, 'введите второй ответ:')
        bot.register_next_step_handler(msg, rab2_name_step)
    except:
        bot.reply_to(message, 'oooops')

def rab2_name_step(message):
    global profile

    try:
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[2]+=100
            profile[6]+=4
            profile[7]+=3
        elif a1 == '2':
            profile[3]+=4
            profile[8]+=4
        elif a1 == '3':
            profile[0]+=100
            profile[1]+=100
            profile[6]+=4
            profile[7]+=5
        elif a1 == '4':
            profile[0]+=100
            profile[2]+=100
            profile[4]+=4
            profile[6]+=4
            profile[7]+=3
        elif a1 == '5':
            profile[3]+=4
            profile[8]+=4
        elif a1 == '6':
            profile[10]+=4
            profile[11]+=4
        elif a1 == '7':
            profile[1]+=100
            profile[4]+=4
            profile[9]+=4
            profile[10]+=4
            profile[11]+=4
        elif a1 == '8':
            profile[1]+=5
            profile[2]+=4
        elif a1 == '9':
            profile[0]+=4
            profile[8]+=5
        elif a1 == '10':
            profile[0]+=4
            profile[1]+=5
        elif a1 == '11':
            profile[5]+=4
        elif a1 == '12':
            profile[0]+=4
            profile[1]+=4
        elif a1 == '13':
            profile[2]+=3
        elif a1 == '14':
            profile[2]+=4
        elif a1 == '15':
            profile[0]+=0

        print(profile)
        msg = bot.reply_to(message, """10. Отношение к окружающим\n
введите первый ответ:
""")
        bot.register_next_step_handler(msg, okr_name_step)
        #b=str(profile)#преоброзование списка
        #bot.send_message(message.chat.id, b)
    except:
        bot.reply_to(message, 'oooops')
        b=str(profile)#преоброзование списка
        bot.send_message(message.chat.id, b)
#print (profile)

def okr_name_step(message):
    global profile
    global b
    try:
        chat_id = message.chat.id
        a1 = message.text
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[0]+= 100
            profile[6]+= 3
            profile[7]+= 5
        elif a1 == '2':
            profile[5]+= 3
            profile[6]+= 4
            profile[7]+= 4
        elif a1 == '3':
            profile[0]+= 100
            profile[5]+= 3
            profile[11]+= 4
        elif a1 == '4':
            profile[0]+= 4
            profile[1]+= 4
            profile[8]+= 4
        elif a1 == '5':
            profile[1]+= 4
            profile[2]+= 4
        elif a1 == '6':
            profile[0]+= 100
            profile[2]+= 100
            profile[4]+= 4
            profile[9]+= 4
            profile[10]+= 4
            profile[11]+= 4
        elif a1 == '7':
            profile[3]+= 3
            profile[8]+= 5
        elif a1 == '8':
            profile[2]+= 100
            profile[3]+= 2
            profile[4]+= 4
            profile[9]+= 4
        elif a1 == '9':
            profile[9]+= 4
        elif a1 == '10':
            profile[0]+= 4
            profile[1]+= 4
            profile[8]+= 4
        elif a1 == '11':
            profile[10]+= 5
        elif a1 == '12':
            profile[11]+= 4
        elif a1 == '13':
            profile[2]+= 4
        elif a1 == '14':
            profile[0]+= 0
            
        msg = bot.reply_to(message, 'введите второй ответ:')
        bot.register_next_step_handler(msg, okr2_name_step)
    except:
        bot.reply_to(message, 'oooops')

def okr2_name_step(message):
    global profile

    try:
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[0]+= 100
            profile[6]+= 3
            profile[7]+= 5
        elif a1 == '2':
            profile[5]+= 3
            profile[6]+= 4
            profile[7]+= 4
        elif a1 == '3':
            profile[0]+= 100
            profile[5]+= 3
            profile[11]+= 4
        elif a1 == '4':
            profile[0]+= 4
            profile[1]+= 4
            profile[8]+= 4
        elif a1 == '5':
            profile[1]+= 4
            profile[2]+= 4
        elif a1 == '6':
            profile[0]+= 100
            profile[2]+= 100
            profile[4]+= 4
            profile[9]+= 4
            profile[10]+= 4
            profile[11]+= 4
        elif a1 == '7':
            profile[3]+= 3
            profile[8]+= 5
        elif a1 == '8':
            profile[2]+= 100
            profile[3]+= 2
            profile[4]+= 4
            profile[9]+= 4
        elif a1 == '9':
            profile[9]+= 4
        elif a1 == '10':
            profile[0]+= 4
            profile[1]+= 4
            profile[8]+= 4
        elif a1 == '11':
            profile[10]+= 5
        elif a1 == '12':
            profile[11]+= 4
        elif a1 == '13':
            profile[2]+= 4
        elif a1 == '14':
            profile[0]+= 0

        #print(profile)
        msg = bot.reply_to(message, """11. Отношение к одиночеству\n
введите первый ответ:
""")
        bot.register_next_step_handler(msg, odin_name_step)
        #b=str(profile)#преоброзование списка
        #bot.send_message(message.chat.id, b)
    except:
        bot.reply_to(message, 'oooops')
        b=str(profile)#преоброзование списка
        bot.send_message(message.chat.id, b)
#print (profile)

def odin_name_step(message):
    global profile
    global b
    try:
        chat_id = message.chat.id
        a1 = message.text
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[0]+=100
            profile[2]+=100
            profile[7]+=4
            profile[8]+=3
            profile[10]+=3
        elif a1 == '2':
            profile[6]+=4
            profile[9]+=3
        elif a1 == '3':
            profile[0]+=4
            profile[1]+=4
        elif a1 == '4':
            profile[2]+=100
            profile[3]+=4
            profile[4]+=4
            profile[6]+=4
        elif a1 == '5':
            profile[5]+=4
            profile[10]+=3
            profile[11]+=4
        elif a1 == '6':
            profile[8]+=5
        elif a1 == '7':
            profile[0]+=3
            profile[1]+=3
        elif a1 == '8':
            profile[0]+=100
            profile[7]+=4
        elif a1 == '9':
            profile[0]+=3
            profile[2]+=2
            profile[5]+=3
            profile[10]+=2
        elif a1 == '10':
            profile[2]+=100
            profile[3]+=4
            profile[4]+=4
            profile[9]+=3
        elif a1 == '11':
            profile[0]+=0
            
        msg = bot.reply_to(message, 'введите второй ответ:')
        bot.register_next_step_handler(msg, odin2_name_step)
    except:
        bot.reply_to(message, 'oooops')

def odin2_name_step(message):
    global profile

    try:
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[0]+=100
            profile[2]+=100
            profile[7]+=4
            profile[8]+=3
            profile[10]+=3
        elif a1 == '2':
            profile[6]+=4
            profile[9]+=3
        elif a1 == '3':
            profile[0]+=4
            profile[1]+=4
        elif a1 == '4':
            profile[2]+=100
            profile[3]+=4
            profile[4]+=4
            profile[6]+=4
        elif a1 == '5':
            profile[5]+=4
            profile[10]+=3
            profile[11]+=4
        elif a1 == '6':
            profile[8]+=5
        elif a1 == '7':
            profile[0]+=3
            profile[1]+=3
        elif a1 == '8':
            profile[0]+=100
            profile[7]+=4
        elif a1 == '9':
            profile[0]+=3
            profile[2]+=2
            profile[5]+=3
            profile[10]+=2
        elif a1 == '10':
            profile[2]+=100
            profile[3]+=4
            profile[4]+=4
            profile[9]+=3
        elif a1 == '11':
            profile[0]+=0

        #print(profile)
        msg = bot.reply_to(message, """12. Отношение к будущему\n
введите первый ответ:
""")
        bot.register_next_step_handler(msg, future_name_step)
        #b=str(profile)#преоброзование списка
        #bot.send_message(message.chat.id, b)
    except:
        bot.reply_to(message, 'oooops')
        b=str(profile)#преоброзование списка
        bot.send_message(message.chat.id, b)
print (profile)

def future_name_step(message):
    global profile
    global b
    try:
        chat_id = message.chat.id
        a1 = message.text
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[2]+=100
            profile[4]+=4
            profile[6]+=5
            profile[7]+=3
        elif a1 == '2':
            profile[2]+=5
        elif a1 == '3':
            profile[0]+=3
            profile[2]+=4
        elif a1 == '4':
            profile[0]+=4
        elif a1 == '5':
            profile[2]+=4
        elif a1 == '6':
            profile[1]+=5
        elif a1 == '7':
            profile[0]+=100
            profile[6]+=4
            profile[7]+=5
        elif a1 == '8':
            profile[2]+=100
            profile[3]+=5
            profile[4]+=4
            profile[5]+=3
            profile[8]+=3
        elif a1 == '9':
            profile[10]+=5
            profile[11]+=4
        elif a1 == '10':
            profile[0]+=100
            profile[5]+=3
            profile[9]+=4
            profile[11]+=4
        elif a1 == '11':
            profile[2]+=100
            profile[3]+=5
            profile[5]+=3
            profile[8]+=4
            profile[9]+=3
        elif a1 == '12':
            profile[0]+=0
            
        msg = bot.reply_to(message, 'введите второй ответ:')
        bot.register_next_step_handler(msg, future2_name_step)
    except:
        bot.reply_to(message, 'oooops')

def future2_name_step(message):
    global profile

    try:
        
        if a1=='0':
            profile[0]+= 0
        elif a1 == '1':
            profile[2]+=100
            profile[4]+=4
            profile[6]+=5
            profile[7]+=3
        elif a1 == '2':
            profile[2]+=5
        elif a1 == '3':
            profile[0]+=3
            profile[2]+=4
        elif a1 == '4':
            profile[0]+=4
        elif a1 == '5':
            profile[2]+=4
        elif a1 == '6':
            profile[1]+=5
        elif a1 == '7':
            profile[0]+=100
            profile[6]+=4
            profile[7]+=5
        elif a1 == '8':
            profile[2]+=100
            profile[3]+=5
            profile[4]+=4
            profile[5]+=3
            profile[8]+=3
        elif a1 == '9':
            profile[10]+=5
            profile[11]+=4
        elif a1 == '10':
            profile[0]+=100
            profile[5]+=3
            profile[9]+=4
            profile[11]+=4
        elif a1 == '11':
            profile[2]+=100
            profile[3]+=5
            profile[5]+=3
            profile[8]+=4
            profile[9]+=3
        elif a1 == '12':
            profile[0]+=0

        #print(profile)
        msg = bot.reply_to(message, """Обработка
\n
""")
        bot.register_next_step_handler(msg, via_name_step)
        b=str(profile)#преоброзование списка
        bot.send_message(message.chat.id, b)
    except:
        bot.reply_to(message, 'oooops')
        b=str(profile)#преоброзование списка
        bot.send_message(message.chat.id, b)
print (profile)

def via_name_step(message):
    global profile
    global b
    global i

    for i in profile:#удаляем звёздочки
        if i >= 100:
            profile[profile.index(i)] = 0
          

    maximum=max(profile)#определяем максимальный пик
    max2=str(maximum)
    #msg = bot.reply_to(message,'максимум',max2)
    msg = bot.reply_to(message,'максимум:')
    msg = bot.reply_to(message,max2)

    x=maximum-7#определяем промежуток
    y=0

    msg = bot.reply_to(message,'макс минус семь=')
    msg = bot.reply_to(message,x)

    msg = bot.reply_to(message,'Тип личности:')

    if profile [0]>=x:#определяем типы
     msg = bot.reply_to(message,'/Гармоничный/')
     y+=1
    if profile[1]>=x:
     msg = bot.reply_to(message,'/Эргопатический/')
     y+=1
    if profile[2]>=x:
     msg = bot.reply_to(message,'/Анозогнозический/')
     y+=1
    if profile[3]>=x:
     msg = bot.reply_to(message,'/Тревожный/')
     y+=1
    if profile[4]>=x:
     msg = bot.reply_to(message,'/Ипохондрический/')
     y+=1
    if profile[5]>=x:
     msg = bot.reply_to(message,'/Неврастенический/')
     y+=1
    if profile[6]>=x:
     msg = bot.reply_to(message,'/Меланхолический/')
     y+=1
    if profile[7]>=x:
     msg = bot.reply_to(message,'/Апатический/')
     y+=1
    if profile[8]>=x:
     msg = bot.reply_to(message,'/Сенситивный/')
     y+=1
    if profile[9]>=x:
     msg = bot.reply_to(message,'/Эгоцентрический/')
     y+=1
    if profile[10]>=x:
     msg = bot.reply_to(message,'/Паранойяльный/')
     y+=1
    if profile[11]>=x:
     msg = bot.reply_to(message,'/Дисфорический/')
     y+=1

    if y==1:
        msg = bot.reply_to(message,'чистый')
    if 1<y<=3:
        msg = bot.reply_to(message,'смешанный')
    if y>3:
        msg = bot.reply_to(message,'диффузный')

    profile =[0,0,0,0,0,0,0,0,0,0,0,0]

    

bot.polling(none_stop=True, interval=0)
