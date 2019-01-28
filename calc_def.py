# -*- coding: utf-8 -*-
import math
import shelve
f = shelve.open('database.db','c')
for i in f.keys():
    print(i)
color=f['color']
paper=f['paper']
rezka=f['rezka']
def rewrite(f,adress,ls):
    f[adress]=ls
def get_list(name):
    result=''
    j=0
    i=0
    if name=='Цвет':
        for i in color:
            result=result+'['
            for j in i:
                result=result+str(j)+', '
            result=result+']\n'
    elif name=='Резка':
        result=result+'['
        for i in rezka:
            result=result+str(i)+', '
        result=result+']\n'
    elif name=='Бумага':
        result=result+'['
        for i in paper:
            result=result+str(i)+', '
        result=result+']\n'
    return(result)
def calc_price(rezka_answer,count_lists,color_per,paper_plot,rezka,color,paper):
    price=0
    rezka_answer=int(rezka_answer)
    count_lists=math.ceil(count_lists/rezka_answer)
    print(count_lists)
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
    price=price+color[color_per-1][t]*count_lists
    price=price+paper[paper_plot-1]*count_lists
    price=price+rezka[rezka_answer-1]
    return(str(price))
print(get_list('Резка'))
