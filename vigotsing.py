from random import *
def arvud_loendis():
    """Ввод данных, вызов функций, показ ответов
    """
    s=[]
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
    s=generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    neg=[]
    pos=[]
    null=[]
    pos,neg,null=jagamine(s,pos,neg,null)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    s=lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    s.sort()
    print(s)
def vahetus(a:int,b:int):
    """ kui min on suuren kui max, siis vahetame neid omavahel
    :param int a: minimaalne arv, mis on suurem kui max
    :param int b: maksimaalne arv, mis on väiksem kui max
    :rtype int:
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """
    :param:int n: kui palju arvud on
    :param:list loend: arvude loend
    :param:int a: 
    :param:int b: макс значение
    :rtype list:
    """
    for i in range (n):
        loend.append(randint(a,b))
    return loend

def jagamine(loend:list,p:list,n:list,nol:list):
    """Добавление в разные списки переменной пр выполнении условий
    :param list loend: список с числами
    :param list p: список с числами больше нуля
    :param list n: список с числами меньше нуля
    :param list nol: список с нулевыми значениями
    :rtype list:
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)
    return p,n,nol

def keskmine(loend:list):
    """Вычисление среднего значения из списка
    :param list loend: список с числами
    :param int n: список с отрицательными/положительными числами
    :rtype float:
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend:list,el:float):
    """Добавление в список среднего значения и сортировка
    :param list loend: список с числами
    :param float el: средние значения 
    :rtype list:
    """
    loend.append(el)
    loend.sort()
    return loend
