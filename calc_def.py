# -*- coding: utf-8 -*-
import math
import shelve
f = shelve.open('database.db','c')
for i in f.keys():
    print(i)
color=f['color']
paper=f['paper']
rezka=f['rezka']
final_text=f['oforml']
start_text=f['start']
def rewrite(f,adress,ls):
    f[adress]=ls
def get_list(name):
    laf = ['4+0 ','4+4 ','1+0 ','1+1 ','4+1 ']
    result=''
    j=0
    i=0
    if name=='Цвет':
        result='до 5л, 5-10л, 10-50л, 50-100л, 100-250л\n'
        for i in range(5):
            result=result + laf[i] +'['
            for j in color[i]:
                result=result+str(j)+', '
            result='Строки - красочность. Столбцы - тираж.\nЧтобы изменить цену за печать одного листа А3 в таблице, нужно использовать команду:\n\ncolor Х Y Z\nХ - номер строки\nY - номер столбца\nZ - новое значение\n\nНапример, команда: color 2 3 40\nвыберет 2 строку, 3 столбец и изменит его на значение 40.\n\n\n'+result+']\n'
    elif name=='Резка':
        result='90гр, 130гр, 150гр, 170гр, 200гр, 250гр, 300гр, самоклейка\n'
        result=result+'['
        for i in rezka:
            result=result+str(i)+', '
        result='Чтобы изменить стоимость бумаги в таблице, нужно использовать команду: paper Y Z, где\nY - номер столбца\nZ - новое значение\n\nНапример, команда: paper 3 40\nвыберет 3 столбец и изменит его на значение 40.\n\n\n'+result+']\n'
    elif name=='Бумага':
        result='2 части (А4), 3-4(А5), 5-6, 7-8(А6), 9-10, 11-16(А7), 17-24, 25-30, 31-40, 41-70 \n'
        result=result+'['
        for i in paper:
            result=result+str(i)+', '
        result='Чтобы изменить цену резки в таблице нужно использовать команду: rezka Y Z, где\nY - номер столбца\nZ - новое значение\n\nНапример, команда: rezka 3 40\nвыберет 3 столбец и изменит его на значение 40.\n\n\n'+result+']\n'
    return(result)
def calc_price(rezka_answer,count_lists,color_per,paper_plot,rezka,color,paper):
    price=0
    rezka_answer=int(rezka_answer)

#    print(count_lists)
    t=0
    if (count_lists>5) and (count_lists<10):
        t=1
    if (count_lists>=10) and (count_lists<50):
        t=2
    if (count_lists>=50) and (count_lists<100):
        t=3
    if (count_lists>=100) and (count_lists<250):
        t=4
    if (count_lists>=250):
        t=5
    count_lists=math.ceil(count_lists/rezka_answer)
    #Перевод цвета
    if color_per=='Цветная с одной стороны':
        color_per=1
    elif color_per=='Цветная с двух сторон':
        color_per=2
    elif color_per=='Чёрно-белая с одной стороны':
        color_per=3
    elif color_per=='Чёрно-белая с двух сторон':
        color_per=4
    elif color_per=='Цветная+Черно-белая':
        color_per=5
    #Перевод плотности
    if paper_plot=='80гр':
        paper_plot=1
    elif paper_plot=='130гр':
        paper_plot=2
    elif paper_plot=='150гр':
        paper_plot=3
    elif paper_plot=='170гр':
        paper_plot=4
    elif paper_plot=='200гр':
        paper_plot=5
    elif paper_plot=='250гр':
        paper_plot=6
    elif paper_plot=='300гр':
        paper_plot=7
    elif paper_plot=='самоклейка':
        paper_plot=8
    #Перевод резки
    """
    if rezka_answer=='A4(2 части)':
        rezka_answer=1
    elif rezka_answer=='А5(4 части)':
        rezka_answer=2
    elif rezka_answer=='99*210(6 частей)':
        rezka_answer=3
    elif rezka_answer=='А6(8 частей)':
        rezka_answer=4
    elif rezka_answer=='10 частей':
        rezka_answer=5
    elif rezka_answer=='А7(16 частей)':
        rezka_answer=6
    elif rezka_answer=='визитка5*9(30 частей)':
        rezka_answer=7
    """
    if rezka_answer>=1 and rezka_answer<=2:
        rezka_answer=1
    elif rezka_answer>=3 and rezka_answer<=4:
        rezka_answer=2
    elif rezka_answer>=5 and rezka_answer<=6:
        rezka_answer=3
    elif rezka_answer>=7 and rezka_answer<=8:
        rezka_answer=4    
    elif rezka_answer>=9 and rezka_answer<=10:   
        rezka_answer=5
    elif rezka_answer>=11 and rezka_answer<=16:
        rezka_answer=6
    elif rezka_answer>=17 and rezka_answer<=24:     
        rezka_answer=7 
    elif rezka_answer>=25 and rezka_answer<=30:
        rezka_answer=8
    elif rezka_answer>=31 and rezka_answer<=40:
        rezka_answer=9
    elif rezka_answer>=41 and rezka_answer<=70:   
        rezka_answer=10
    print(color_per,t)        
    price=price+color[color_per-1][t]*count_lists
    print(color[color_per-1][t])
    price=price+paper[paper_plot-1]*count_lists
    print(paper[paper_plot-1])
    price=price+rezka[rezka_answer-1]
    print(color[color_per-1][t]+paper[paper_plot-1])
    return(str(price))



def fast_calc(text):
    form = {'А6 105*148':8,'А5 148*210':4,'А4 210*297':2,'А3 297*420':1,'визитка 5*9':24,'дисконт 54*86':21,'карманный календарь 7*10':16,'билет 60*150':12,'европолоса 99*210':6,'А6':8,'А5':4,'А4':2,'A3':1,'визитка':24,'дисконт':21,'календарь':16,'билет':12,'европолоса':6,'А6':8,'A5':4,'А4':2,'А3':1}
    colorr = {'4+0':'Цветная с одной стороны','4+4':'Цветная с двух сторон','1+0':'Чёрно-белая с одной стороны','1+1':'Чёрно-белая с двух сторон','4+1':'Цветная+Черно-белая'}
    mass = text.split(',')
    for i in range(len(mass)):
        mass[i] = mass[i].strip()
    if mass[0] in form:
        ress = calc_price(form[mass[0]],int(mass[3]),colorr[mass[1]],mass[2],rezka,color,paper)
        return(int(ress),int(mass[3]))
    else:
        return('Неверно введены аргументы')
#print(calc_price(1,5,'Цветная с одной стороны','170гр',rezka,color,paper))
print(fast_calc('A5  , 4+4     ,200гр  ,    80'))
