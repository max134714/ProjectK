import datetime
import time
import re

slovar_Month = {'январ': 1, 'феврал': 2,'март': 3,'апрел': 4,'май': 5, 'мая': 5,'июн': 6, 'июл': 7, 'август': 8, 'сентябр': 9, 'октябр': 10, 'ноябр': 11, 'декабр': 12,} #словарь для месяцев (как переменная)
slovar_week_days = {'понедельник': 1, 'вторник': 2,'сред': 3,'четверг': 4,'пятниц': 5, 'суббот': 6,'воскресен': 7} #словарь для дней недели (как переменная)
slovar_intervals = {'минут': 60, 'полчаса': 1800,'час': 3600,'ден': 86400,'недел': 6048000} #словарь для интервала времени (как переменная)




def  GetTimeNow(Year, Month, Day, hour, minute):   #функция для текущего времени 
      now = datetime.datetime.now()
      if Year == -1:
          Year = now.year
      if Month == -1:
          Month = now.month
      if Day == -1:
          Day = now.day
      if hour == -1:
          hour = now.hour
      if minute == -1:
           minute = now.minute
      strak={'year':  Year, 'month':   Month, 'day':  Day, 'hour':  hour, 'minute':  minute}   #созданный словарь для текущего  времени
      return " 'year': {year}, 'month': {month}, 'day': {day}, 'hour': {hour}, 'minute': {minute} ".format(**strak)   #возращаем нужную строку

def search_time(line): #Функция поиска времени
     try: #пытаемся   ищем время в строке
            j = time.strptime(line, "%H:%M")  #Определенного формата времени из строки "пользователя"
            hour = int(j.tm_hour)  #время в сообщении
            minute = int(j.tm_min)   #нашли время
     except:
            hour = -1
            minute = -1
     return  hour, minute

 

def search_month(line):
     
     Month = -1  
     for key in slovar_Month:    # ищем месяц в строке

            if line.find(key) != -1:   
                Month = slovar_Month[key] # определили нашли месяц
                break        
     return Month

def search_day_of_month(line):
    day = -1
    D = re.search('\d+', line)
                
    if (D != None):
        D = int(D.string)
        if 1 <= D <= 31:   #ищем день месяца
             day = D
    return day 

def search_year(line):
    Y = -1
    Year = re.search('\d+', line)
                
    if (Year != None):
        Year = int(Year.string)
        if 2022 <= Year:   #ищем день месяца
             Y = Year
    return Y               
                    
           
           

def Parser(message): # общая функция парсер
    

     Year = -1
     Month = -1
     Day_Month = -1  #день месяца 
     Day_Week = -1  #день недели для регулярного события
     hour = -1
     minute = -1

     line = message.split() #разбитие строки на список слов
     line_work = line #для удаления строк используемых под время

    #пробегаемся по списку для поиска времени
     for i in range(len(line_work)): 
        t = search_time(line_work[i])
        if t[0] != -1:
            hour = t[0]
            minute = t[1]
            line_work.remove(line_work[i])
            if line_work[i-1] == 'в':
                line_work.remove(line_work[i-1])
                
            break
    #пробегаемся по списку для поиска месяца и дня месяца
     for i in range(len(line_work)): 
        t = search_month(line_work[i])
        if t != -1:
            Month = t
            line_work.remove(line_work[i])
            #Теперь поищеем день 
            t1 = search_day_of_month(line_work[i-1])
            if t1 != -1:
               Day_Month = t1
               line_work.remove(line_work[i-1])
            break 
     #пробегаемся по списку для поиска года 
     for i in range(len(line_work)): 
        t = search_year(line_work[i])
        if t != -1:
            Year = t
            
            D = re.match('г.*', line_work[i+1])
            if D != None:
                line_work.remove(line_work[i+1])
            line_work.remove(line_work[i])
            break

                 
     vremie = GetTimeNow(Year, Month, Day_Month, hour, minute) # время на выходе парсера если что-то не введено вставляется текущее время
         
     deystvie = " ".join(line_work)
     return deystvie, vremie



#################################
print("Ввести напоминание")
#t = "Подписать служебку у начальника 13 мая 2025 г. в 16:15"

#t = "Подписать служебку у начальника 13 декабря  "
#t = "Начать собираться в 4:31"
#t = "Проснуться, улыбнуться, почистить зубы и помыться в 07:13"
#t = "Съездить на дачу 17 мая в 16:15"
#t = "Убраться в квартире через 90 минут"
#t = "Позвонить друзьям через 3 часа"
#t = "Приготовить покушать на 2-3 дня 3 сентября 2022 года в 06:01"
#t = "Перевод локального компьютера в режим гибернации завтра"
#t = "Выключить 13 декабря в 20:17"
#t = "Перевод локального компьютера в режим гибернации через 2 дня"
#t = 'Служебку подписать на питон 12 ноября утром'
#t = 'Служебку подписать на питон в четверг в 20:17'
#t = 'Служебку подписать на питон в среду'
#t = 'Служебку в отдел кадров в среду в 13:13'
#t = "В понедельник уроки"
#t = 'Поскольку все записи имеют один и тот же шаблон, внести данные, которые хотите извлечь из пары скобок 13 декабря 2022 года в 16:15'

#t = "Напомни про гречку через 14 минут"
#t = "Через 50 минут таймер установаить. дерзай"
#t = "Основы_Python_в_четверг_15:00 3 сентября 2022 года"
#t = " Основы_Python_в_четверг_15:00 в среду 15:00 "
#t = "13 1311"
#t = 1231
#t = "Сходить покушать на неделе в 13:13"
#t = "del_qustion_answer*как дела?*норма, как сам?"
#t = "Сходить покушать на неделе"
#t = "В следующем месяце Подписать служебку "
#t = "\d\de23 2\3 3r3556"
#t = "Подписать служебку по выходным"
#t = "Сходить в сауну каждое 28 число"
#t = "Подписать служебку по выходным в 20:19"
#t = "поздравить с др маму через год в 20:18"
#t = "поздравить с др маму через час"
#t = "тренировка каждый час в 20:19"
#t = "Подписать служебку 23 февраля"
#t = "Тренировка каждый понедельник"
#t = "Тренировка каждый год"


#str(input())
status = 'SUCCESS'
error = 'NO ERROR'

if None != re.match('\d+', t):
   status = 'ERROR'
   error = 'No Text '

cortej = Parser(t)

if len(cortej[0]) == 0:
    status = 'ERROR'
    error = 'No action '


if  status == 'ERROR':
    action = error 
else:
    action = cortej[0]

print(t)
result = 'MESSAGE={\'STATUS\':\''  + status + '\',\'DATE\':' + '{'+ cortej[1] + '}' + ',\'TEXT\':\'' + action + '\'}'
print(result)   
  