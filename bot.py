# -*- coding: utf-8 -*-
import vk_api
import calc_def
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

def create_list_keyboard(lis):
    keyboard = VkKeyboard(one_time=True)
    for i in range(len(lis)-1):
        keyboard.add_button(lis[i], color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
    keyboard.add_button(lis[-1], color=VkKeyboardColor.DEFAULT)
    return(keyboard)
def create_float_keyboard(lis):
    keyboard = VkKeyboard(one_time=True)
    for i in range(len(lis)-1):
        for j in lis[i]:
            keyboard.add_button(j, color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
    for j in lis[-1]:
        keyboard.add_button(j, color=VkKeyboardColor.DEFAULT)    
    return(keyboard)
def funct(d,data,tF,tT,user_id,message_id,info):
    d[user_id]=message_id
    data[user_id]=info
    tF[user_id]=False
    tT[user_id]=True





def main():
    vk_session = vk_api.VkApi(token = 'aeb7a7e62e220a95cf2c76702cf1b9c50735ab93b688a95a203c98c678e3d60d48ec521967c551a9c7b40')
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    #Создание клавиатур
    key_rezka = create_float_keyboard([['А6 105*148','А5 148*210'],['А4 210*297','А3 297*420'],['визитка 5*9','дисконт 54*86'],['карманный календарь 7*10','билет 60*150'],['европолоса 99*210','Другой размер']])
    key_color = create_list_keyboard(['Цветная с одной стороны','Цветная с двух сторон','Чёрно-белая с одной стороны','Чёрно-белая с двух сторон','Цветная+Черно-белая'])
    key_plot = create_float_keyboard([['80гр','130гр','150гр','170гр'],['200гр','250гр','300гр','самоклейка']])
    key_fin = create_float_keyboard([['Добавить к заказу.','Удалить позицию.'],['Новый заказ.','Оформить заказ.']])
    key_main = create_list_keyboard(['Посчитать заказ','Информация'])
    key_admin = create_float_keyboard([['Цвет','Бумага'],['Резка'],['Выход']])
    color_number = {'Цветная с одной стороны':'4+0','Цветная с двух сторон':'4+4','Чёрно-белая с одной стороны':'1+0','Чёрно-белая с двух сторон':'1+1','Цветная+Черно-белая':'4+1'}
    forms = {'A6':8,'A5':4,'A4':2,'A3':1,'визитка':24,'дисконт':21,'календарь':16,'билет':12,'европолоса':6,'А6':8,'А5':4,'А4':2,'А3':1}
    rezka_number = {'А6 105*148':8,'А5 148*210':4,'А4 210*297':2,'А3 297*420':1,'визитка 5*9':24,'дисконт 54*86':21,'карманный календарь 7*10':16,'билет 60*150':12,'европолоса 99*210':6}
    #Данные
    user_id_rezka={}
    user_id_rezcount={}
    user_id_countlist={}
    user_id_color={}
    user_id_plotnost={}
    user_id_price={}
    user_id_zakaz={}
    user_id_reg={}
    #Флаги
    user_id_d={}
    user_id_admin={}
    user_id_td={}
    user_id_t={}
    user_id_t2={}
    user_id_t3={}
    user_id_t4={}
    user_id_t5={}
    user_id_to={}
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            user_id=event.user_id
            text = event.text
            mess = event.message_id
            if not(user_id_reg.get(user_id,False)):
                user_id_rezka[event.user_id]=0
                user_id_reg[user_id]=True
                user_id_countlist[event.user_id]=0
                user_id_color[event.user_id]=0
                user_id_plotnost[event.user_id]=0
                user_id_zakaz[event.user_id]=[]
#            print(text.split()[0])
            if event.text=='!Admin':
                user_id_admin[user_id]=True
                vk.messages.send(user_id=event.user_id,message='Вы вошли в режим администратора',keyboard=key_admin.get_keyboard())      
            elif event.text=='Выход' and user_id_admin.get(user_id,False):
                user_id_admin[user_id]=False
                vk.messages.send(user_id=event.user_id,message='Вы вышли из режима администратора',keyboard=key_main.get_keyboard())
            elif (text.split()[0] in ['color','rezka','paper']) and user_id_admin.get(user_id,False):
                if text.split()[0]=='color':
                    try:
                        calc_def.color[int(text.split()[1])-1][int(text.split()[2])-1] = int(text.split()[3])
                        calc_def.rewrite(calc_def.f,'color',calc_def.color)
                        vk.messages.send(user_id=event.user_id,message='Таблица успешно изменена',keyboard=key_admin.get_keyboard())
                    except:
                        vk.messages.send(user_id=event.user_id,message='Ошибка в команде',keyboard=key_admin.get_keyboard())                        
                elif text.split()[0]=='rezka':
                    try:
                        calc_def.rezka[int(text.split()[1])-1] = int(text.split()[2])
                        vk.messages.send(user_id=event.user_id,message='Таблица успешно изменена',keyboard=key_admin.get_keyboard())
                        calc_def.rewrite(calc_def.f,'rezka',calc_def.rezka)
                    except:
                        vk.messages.send(user_id=event.user_id,message='Ошибка в команде',keyboard=key_admin.get_keyboard())   
                elif text.split()[0]=='paper':
                    try:
                        calc_def.paper[int(text.split()[1])-1] = int(text.split()[2])
                        vk.messages.send(user_id=event.user_id,message='Таблица успешно изменена',keyboard=key_admin.get_keyboard())
                        calc_def.rewrite(calc_def.f,'paper',calc_def.paper)
                    except:
                        vk.messages.send(user_id=event.user_id,message='Ошибка в команде',keyboard=key_admin.get_keyboard())   
            elif text in ['Цвет','Бумага','Резка']:
                mess = calc_def.get_list(text)
                vk.messages.send(user_id=event.user_id,message=mess,keyboard=key_admin.get_keyboard())   
            elif event.text=='Начать':
                vk.messages.send(user_id=event.user_id,message='Добра вам! Я бот печатной мастерской "Постер Принт". Буду рад помочь вам посчитать цену на печать визиток, листовок, афиш, открыток и прочей подобной печати. ',keyboard=key_main.get_keyboard())
                user_id_d[event.user_id]=0
                user_id_t[event.user_id] = False
                user_id_t2[event.user_id]=False
                user_id_t3[event.user_id]=False
                user_id_t4[event.user_id]=False
                user_id_to[event.user_id]=False
                user_id_rezka[event.user_id]=0
                user_id_countlist[event.user_id]=0
                user_id_color[event.user_id]=0
                user_id_plotnost[event.user_id]=0
                user_id_zakaz[event.user_id]=[]
            elif event.text=='Добавить к заказу.':
                vk.messages.send(user_id=event.user_id,message='Выберите формат.',keyboard=key_rezka.get_keyboard())  
                user_id_t[event.user_id] = True
                user_id_d[event.user_id] = event.message_id
            elif event.text=='Удалить позицию.':
                vk.messages.send(user_id=event.user_id,message='Введите номер позиции для удаления',keyboard=key_fin.get_keyboard())
                user_id_td[user_id]=True
                user_id_d[event.user_id] = event.message_id
            elif (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_td.get(event.user_id,False):
                user_id_td[user_id]=False
                try:
                    del user_id_zakaz[user_id][int(text)-1]
                    vk.messages.send(user_id=event.user_id,message='Успешно',keyboard=key_fin.get_keyboard())
                    tytx=''
                    price=0
                    for i in range(len(user_id_zakaz[user_id])):
                        tytx = tytx + str(i+1) + user_id_zakaz[user_id][i] + '\n'
                        price = price + int(user_id_zakaz[user_id][i].split()[-2])
                    tytx = tytx + 'итого' + str(price) + 'руб'   
                    vk.messages.send(user_id=event.user_id,message=tytx,keyboard=key_fin.get_keyboard()) 
                except:
                    vk.messages.send(user_id=event.user_id,message='Пожалуйста введите верное значение',keyboard=key_fin.get_keyboard())                                              
            elif event.text=='Посчитать заказ':
                vk.messages.send(user_id=event.user_id,message='Выберите формат.',keyboard=key_rezka.get_keyboard())  
                user_id_t[event.user_id] = True
                user_id_d[event.user_id] = event.message_id
                user_id_zakaz[event.user_id]=[]
            #Обсчет заказа
            elif (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_t.get(event.user_id,False):
                if text=='Другой размер':
                    vk.messages.send(user_id=event.user_id,message='Напишите какое количество сможет разместиться на лист 300*450')
                    user_id_t[user_id]=False
                    user_id_to[user_id]=True 
                    user_id_d[user_id]=mess                   
                else:
                    vk.messages.send(user_id=event.user_id,message='Выберите плотность бумаги.',keyboard=key_plot.get_keyboard())  
                    funct(user_id_d,user_id_rezka,user_id_t,user_id_t2,user_id,mess,text)
                    user_id_rezcount[user_id]=rezka_number[text]
            elif (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_to.get(event.user_id,False):
                vk.messages.send(user_id=event.user_id,message='Выберите плотность бумаги.',keyboard=key_plot.get_keyboard())
                funct(user_id_d,user_id_rezka,user_id_to,user_id_t2,user_id,mess,text)
                user_id_rezcount[user_id]=text                                            
            elif (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_t2.get(event.user_id,False):
                vk.messages.send(user_id=event.user_id,message='Выберите конфигурацию цвета.',keyboard=key_color.get_keyboard())  
                funct(user_id_d,user_id_plotnost,user_id_t2,user_id_t3,user_id,mess,text)
            elif (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_t3.get(event.user_id,False):
                vk.messages.send(user_id=event.user_id,message='Теперь напишите сколько нужно напечатать.Тираж должен быть кратен '+str(rezka_number[user_id_rezka[user_id]]))  
                funct(user_id_d,user_id_color,user_id_t3,user_id_t4,user_id,mess,text)
            elif (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_t4.get(event.user_id,False):
                funct(user_id_d,user_id_countlist,user_id_t4,user_id_t5,user_id,mess,text)
                try:
                    print(user_id_rezcount[user_id],user_id_countlist[user_id])
                    user_id_price[user_id]= calc_def.calc_price(int(user_id_rezcount[user_id]),int(user_id_countlist[user_id]),user_id_color[user_id],user_id_plotnost[user_id],calc_def.rezka,calc_def.color,calc_def.paper)
                    user_id_zakaz[user_id].append('.'+user_id_rezka[user_id].split()[0]+','+color_number[user_id_color[user_id]]+' ('+user_id_color[user_id]+'), '+user_id_plotnost[user_id]+', '+str(user_id_countlist[user_id])+'шт - '+str(round(int(user_id_price[user_id])/int(user_id_countlist[user_id]))) + 'руб/шт тираж: '  + str(user_id_price[user_id])+' руб')
                    tytx=''
                    price=0
                    for i in range(len(user_id_zakaz[user_id])):
                        tytx = tytx + str(i+1) + user_id_zakaz[user_id][i] + '\n'
                        price = price + int(user_id_zakaz[user_id][i].split()[-2])
                    tytx = tytx + 'Итого: ' + str(price) + ' руб'
                    vk.messages.send(user_id=event.user_id,message=tytx,keyboard=key_fin.get_keyboard()) 
                except: 
                    vk.messages.send(user_id=event.user_id,message="В ваших данных ошибка. Пожалуйста, повторите попытку",keyboard=key_fin.get_keyboard())
            elif text.split(',')[0].strip() in forms:
                try:
                    vk.messages.send(user_id=event.user_id,message=calc_def.fast_calc(text),keyboard=key_fin.get_keyboard())
                    user_id_zakaz[user_id].append('.' + text + 'шт - '+ str(round(calc_def.fast_calc(text)[0]/calc_def.fast_calc(text)[1])) + 'руб/шт тираж: ' + str(calc_def.fast_calc(text)[0])+' руб')
                    tytx=''
                    price=0
                    for i in range(len(user_id_zakaz[user_id])):
                        tytx = tytx + str(i+1) + user_id_zakaz[user_id][i] + '\n'
                        price = price + int(user_id_zakaz[user_id][i].split()[-2])
                    tytx = tytx + 'Итого: ' + str(price) + ' руб'
                    vk.messages.send(user_id=event.user_id,message=tytx,keyboard=key_fin.get_keyboard()) 
                except:
                    vk.messages.send(user_id=event.user_id,message='Неверная команда',keyboard=key_fin.get_keyboard())                    
                
if __name__ == '__main__':
    main()
