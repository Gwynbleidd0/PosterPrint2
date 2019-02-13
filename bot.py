# -*- coding: utf-8 -*-
import vk_api
import calc_def
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

def create_list_keyboard(lis,one_time):
    if one_time:
        keyboard = VkKeyboard(one_time=True)
    else:
        keyboard = VkKeyboard()        
    for i in range(len(lis)-1):
        keyboard.add_button(lis[i], color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
    keyboard.add_button(lis[-1], color=VkKeyboardColor.DEFAULT)
    return(keyboard)
def create_float_keyboard(lis,one_time):
    if one_time:
        keyboard = VkKeyboard(one_time=True)
    else:
        keyboard = VkKeyboard()        
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
    key_rezka = create_float_keyboard([['А6 105*148','А5 148*210'],['А4 210*297','А3 297*420'],['визитка 50*90','дисконт 54*86'],['карманный календарь 70*100','билет 60*150'],['европолоса 99*210','Другой размер']],True)
    key_color = create_list_keyboard(['Цветная с одной стороны','Цветная с двух сторон','Чёрно-белая с одной стороны','Чёрно-белая с двух сторон','Цветная+Черно-белая'],True)
    key_plot = create_float_keyboard([['80гр','130гр','150гр','170гр'],['200гр','250гр','300гр','самоклейка']],False)
    key_fin = create_float_keyboard([['Добавить к заказу.','Удалить позицию.'],['Новый заказ.','Оформить заказ.']],False)
    key_main = create_list_keyboard(['Посчитать заказ','Информация'],False)
    key_admin = create_float_keyboard([['Цвет','Бумага','Резка'],['Start','Final'],['Выход']],False)
    color_number = {'Цветная с одной стороны':'4+0','Цветная с двух сторон':'4+4','Чёрно-белая с одной стороны':'1+0','Чёрно-белая с двух сторон':'1+1','Цветная+Черно-белая':'4+1'}
    forms = {'A6':8,'A5':4,'A4':2,'A3':1,'визитка':24,'дисконт':21,'календарь':16,'билет':12,'европолоса':6,'А6':8,'А5':4,'А4':2,'А3':1}
    rezka_number = {'А6 105*148':8,'А5 148*210':4,'А4 210*297':2,'А3 297*420':1,'визитка 50*90':24,'дисконт 54*86':21,'карманный календарь 70*100':16,'билет 60*150':12,'европолоса 99*210':6}
    plotnost=['80гр','130гр','150гр','170гр','200гр','250гр','300гр','самоклейка']
    colorol = ['Цветная с одной стороны','Цветная с двух сторон','Чёрно-белая с одной стороны','Чёрно-белая с двух сторон','Цветная+Черно-белая']
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
    user_id_t6={}
    user_id_tS={}
    user_id_tF={}
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and (event.text!='' or user_id_t6[user_id]):
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
            elif user_id_admin.get(user_id,False):
                if (text.split()[0] in ['color','rezka','paper']):
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
                elif text.split()[0]=='Start':
                    user_id_tS[user_id]=True
                    vk.messages.send(user_id=event.user_id,message='Введите текст приветствия')
                    vk.messages.send(user_id=event.user_id,message='Текущий текст:\n'+calc_def.start_text,keyboard=key_main.get_keyboard())
                    user_id_d[event.user_id] = event.message_id
                elif text.split()[0]=='Final':
                    user_id_tF[user_id]=True
                    vk.messages.send(user_id=event.user_id,message='Введите текст оформления')
                    vk.messages.send(user_id=event.user_id,message='Текущий текст:\n'+calc_def.final_text)
                    user_id_d[event.user_id] = event.message_id
                elif (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_tF.get(event.user_id,False):
                    try:
                        user_id_tF[user_id]=False
                        calc_def.final_text=text
                        calc_def.rewrite(calc_def.f,'oforml',calc_def.final_text)
                        vk.messages.send(user_id=event.user_id,message='Успешно',keyboard=key_admin.get_keyboard())
                    except:
                        vk.messages.send(user_id=event.user_id,message='Ошибка в команде',keyboard=key_admin.get_keyboard())                
                elif (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_tS.get(event.user_id,False):
                    try:
                        user_id_tS[user_id]=False
                        calc_def.start_text=text
                        calc_def.rewrite(calc_def.f,'start',calc_def.final_text)
                        vk.messages.send(user_id=event.user_id,message='Успешно',keyboard=key_admin.get_keyboard())
                    except:
                        vk.messages.send(user_id=event.user_id,message='Ошибка в команде',keyboard=key_admin.get_keyboard())                                              
                elif text in ['Цвет','Бумага','Резка']:
                    mess = calc_def.get_list(text)
                    vk.messages.send(user_id=event.user_id,message=mess,keyboard=key_admin.get_keyboard())   
            elif event.text=='Начать':
                vk.messages.send(user_id=event.user_id,message=calc_def.start_text,keyboard=key_main.get_keyboard())
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
            elif event.text=='Оформить заказ.':
                vk.messages.send(user_id=event.user_id,message=calc_def.final_text)
                user_id_t6[user_id]=True
                user_id_d[event.user_id] = event.message_id
            elif (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_t6.get(event.user_id,False):
                vk.messages.send(user_id=event.user_id,message='Готово, мы с вами свяжемся')
                horus=''
                priceo=0
                for i in range(len(user_id_zakaz[user_id])):
                    horus = horus + str(i+1) + user_id_zakaz[user_id][i] + '\n'
                    priceo = priceo + int(user_id_zakaz[user_id][i].split()[-2])
                horus = horus + 'Итого: ' + str(priceo) + ' руб'   
                vk.messages.send(user_id=130685714,message=horus,forward_messages=mess)
                user_id_t6[user_id]=False
            elif event.text=='Новый заказ.':
                vk.messages.send(user_id=event.user_id,message='Создан новый заказ',keyboard=key_main.get_keyboard())
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
                    user_id_td[user_id]=False 
                except:
                    vk.messages.send(user_id=event.user_id,message='Пожалуйста введите верное значение',keyboard=key_fin.get_keyboard())                                              
            elif event.text=='Посчитать заказ':
                vk.messages.send(user_id=event.user_id,message='Выберите формат.',keyboard=key_rezka.get_keyboard())  
                user_id_t[event.user_id] = True
                user_id_d[event.user_id] = event.message_id
                user_id_zakaz[event.user_id]=[]
            #Обсчет заказа
            elif (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_t.get(event.user_id,False):
                if text in rezka_number.keys() or text=='Другой размер':
                    if text=='Другой размер':
                        vk.messages.send(user_id=event.user_id,message='Напишите какое количество сможет разместиться на лист 300*450')
                        user_id_t[user_id]=False
                        user_id_to[user_id]=True 
                        user_id_d[user_id]=mess                   
                    else:
                        vk.messages.send(user_id=event.user_id,message='Выберите плотность бумаги.\n\n\n80гр - обычная тонкая бумага\n130-170гр - обычно на такой бумаге печатаются листовки\n170гр-200гр - используется для листовых календарей\n300гр - плотная бумага для визиток, открыток, дипломов\nсамоклейка - бумажная самоклейка, боится воды. Для улицы требуется другая печать, она у нас тоже есть.',keyboard=key_plot.get_keyboard())  
                        funct(user_id_d,user_id_rezka,user_id_t,user_id_t2,user_id,mess,text)
                        user_id_rezcount[user_id]=rezka_number[text]
                else:
                    vk.messages.send(user_id=event.user_id,message='Неверный вариант',keyboard=key_rezka.get_keyboard())  
            elif (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_to.get(event.user_id,False):
                vk.messages.send(user_id=event.user_id,message='Выберите плотность бумаги.',keyboard=key_plot.get_keyboard())
                funct(user_id_d,user_id_rezka,user_id_to,user_id_t2,user_id,mess,text)
                user_id_rezcount[user_id]=text                                            
            elif (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_t2.get(event.user_id,False):
                if text in plotnost:
                    vk.messages.send(user_id=event.user_id,message='Выберите конфигурацию цвета.',keyboard=key_color.get_keyboard())  
                    funct(user_id_d,user_id_plotnost,user_id_t2,user_id_t3,user_id,mess,text)
                else:
                    vk.messages.send(user_id=event.user_id,message='Неверный вариант',keyboard=key_plotonost.get_keyboard())                      
            elif (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_t3.get(event.user_id,False):
                if text in colorol:
                    if rezka_number.get(user_id_rezka[user_id],1)!=1 and rezka_number.get(user_id_rezka[user_id],2)!=2:
                        ls=''
                        for i in range(1,4):
                            ls=ls+str(rezka_number[user_id_rezka[user_id]]*i)+', '
                        ls=ls+str(rezka_number[user_id_rezka[user_id]]*5)+' штук...'
                        vk.messages.send(user_id=event.user_id,message='Теперь напишите сколько нужно напечатать.\nТираж должен быть кратен '+str(rezka_number[user_id_rezka[user_id]])+': '+ls)
                    else:
                        vk.messages.send(user_id=event.user_id,message='Теперь напишите сколько нужно напечатать.')
                    funct(user_id_d,user_id_color,user_id_t3,user_id_t4,user_id,mess,text)
                else:
                    vk.messages.send(user_id=event.user_id,message='Неверный вариант',keyboard=key_color.get_keyboard())       
            elif (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_t4.get(event.user_id,False):
                funct(user_id_d,user_id_countlist,user_id_t4,user_id_t5,user_id,mess,text)
                try:
                    print(user_id_rezcount[user_id],user_id_countlist[user_id])
                    user_id_price[user_id]= calc_def.calc_price(int(user_id_rezcount[user_id]),int(user_id_countlist[user_id]),user_id_color[user_id],user_id_plotnost[user_id],calc_def.rezka,calc_def.color,calc_def.paper)
                    user_id_zakaz[user_id].append('.'+user_id_rezka[user_id].split()[0]+','+color_number[user_id_color[user_id]]+' ('+user_id_color[user_id]+'), '+user_id_plotnost[user_id]+', '+str(user_id_countlist[user_id])+'шт - '+str(round(int(user_id_price[user_id])/int(user_id_countlist[user_id]),2)) + 'руб/шт тираж: '  + str(user_id_price[user_id])+' руб')
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
#                    vk.messages.send(user_id=event.user_id,message=calc_def.fast_calc(text),keyboard=key_fin.get_keyboard())
                    user_id_zakaz[user_id].append('.' + text + 'шт - '+ str(round(calc_def.fast_calc(text)[0]/calc_def.fast_calc(text)[1])) + 'руб/шт тираж: ' + str(calc_def.fast_calc(text)[0])+' руб')
                    answ1=''
                    price=0
                    for i in range(len(user_id_zakaz[user_id])):
                        answ1 = answ1 + str(i+1) + user_id_zakaz[user_id][i] + '\n'
                        price = price + int(user_id_zakaz[user_id][i].split()[-2])
                    answ1 = answ1 + 'Итого: ' + str(price) + ' руб'
                    vk.messages.send(user_id=event.user_id,message=answ1,keyboard=key_fin.get_keyboard()) 
                except:
                    vk.messages.send(user_id=event.user_id,message='Неверная команда',keyboard=key_fin.get_keyboard())                    
                
if __name__ == '__main__':
    main()
