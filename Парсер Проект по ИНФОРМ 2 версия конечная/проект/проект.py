import datetime
import time
import re


from calendar import monthrange


slovar_Month = {'январ': 1, 'феврал': 2,'март': 3,'апрел': 4,'май': 5, 'мая': 5,'июн': 6, 'июл': 7, 'август': 8, 'сентябр': 9, 'октябр': 10, 'ноябр': 11, 'декабр': 12,} #словарь для месяцев (как переменная)
slovar_week_days = {'понедельник': 1, 'вторник': 2,'сред': 3,'четверг': 4,'пятниц': 5, 'суббот': 6,'воскресен': 7} #словарь для дней недели (как переменная)
slovar_intervals = {'минут': 1, 'полчаса': 30,'час': 60,'ден': 1440,'дня': 1440,'недел': 10080, 'месяц': 43920 , 'год': 525600 } #словарь для интервала времени (как переменная



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
      try:
        Year = int(Year.string)
        if 2022 <= Year:   #ищем день месяца
             Y = Year
      except: 
             Y = -1 
    return Y               
        
#Функция обнаружения конструкции через
def search_cherez(message):
    status = False
    my_time = datetime.datetime.now()
    for i in range(len(message)):
        if message[i] == 'через':
            N = re.search('\d+', message[i+1])
            d = 1
            if None != N:
                N = int(N.string)
                d = 2 
            else:
                N = 1
                
            for key in slovar_intervals:
                 if message[i+d].find(key) != -1:
                     status = True
                     dt = datetime.timedelta(minutes = slovar_intervals[key] * N)
                     my_time = my_time + dt
                     message.remove(message[i])
                     message.remove(message[i])
                     if d == 2: 
                        message.remove(message[i])
                     break
            break
    return status, my_time


# словарь для регулярных интервалов
slovar_regular_intervals = {'год': 'year', 'месяц': 'month', 'неделю': 'week', 'день': 'day', 'дня':'days', 'час': 'hour', 'часа':'hours'}
#словарь для дней недели регулярных
slovar_regular_weekdays = {'понедельник': 'Monday', 'вторник': 'Thuesday','сред': 'Wednesday','четверг': 'Thursday','пятниц': 'Friday', 'суббот': 'Saturday','воскресен': 'Sunday','выходной':'Sunday'} 

# функция поиска регулярных 
def search_regul(message):
   message = message.split() #разбитие строки на список слов
   status = False
   Out = ' '
   for i in range(len(message)):
       if re.search('кажд', message[i]) != None:
           K = re.search('\d+', message[i+1])
           if None != K:
               d = 2
           else:
               d = 1
           for key in slovar_regular_intervals: # ищем в словаре для регулярных интервалов
              if message[i+d].find(key) != -1:
                  status = True
                  if d == 1:
                      Out = '\'' + slovar_regular_intervals[key] + '\'' # строка  на выходе
                      message.remove(message[i]) # удаляем 2  слова
                      message.remove(message[i])
                  else:
                      Out = '\'' + K.string + slovar_regular_intervals[key] + '\'' # строка на выходе с числом
                      message.remove(message[i]) # удаляем 3  слова
                      message.remove(message[i])
                      message.remove(message[i])
                  # нашли регулярный интервал
                  break  # прекращаем поиск по словарю регулярных интервалов
                  
               # если не нашили - поищем день недели
           if status == False:
                 if d == 1:
                    for key in slovar_regular_weekdays: # ищем в словаре для регулярных дней недели
                            if message[i+d].find(key) != -1:
                                status = True
                                Out = '\'day_of_week\':\'' + slovar_regular_weekdays[key] + '\''
                                message.remove(message[i]) # удаляем 2  слова
                                message.remove(message[i])
                                status = True
                                break # прекращаем поиск по словарю для регулярных дней недели
           break # прекращаем искать слово каждый

   hour = -1
   minute = -1
   for i in range(len(message)): 
                 t = search_time(message[i])
                 if t[0] != -1:
                       hour = t[0]
                       minute = t[1]
                       message.remove(message[i])#удаление
                       if message[i-1] == 'в':
                            message.remove(message[i-1])
                       break # нашли выходим из цикла
   now = datetime.datetime.now()
   if hour == -1:
         hour = now.hour
   if minute == -1:
           minute = now.minute

       
   strak={ 'hour':  hour, 'minute':  minute}   #созданный словарь для текущего  времени
   vremie =  "'hour': {hour}, 'minute': {minute} ".format(**strak)   #возращаем нужную строку
   if status:
           status1 = 'SUCCESS'
   else:
       status1 = 'ERROR'

   if len(message) == 0:
         status1 = 'ERROR'
         action = 'No action '
   else:
         status1 = 'SUCCESS'
   action = " ".join(message) # склеиваем оставшиеся слова через пробел в одну строку
        
   result = 'MESSAGE={\'STATUS\':\''  + status1 + '\',\'DATE\':' + '{'+ vremie + '}' + ',\'TEXT\':\'' + action + '\'}' + '\'PARAMS\':{\'repeat_always\':' +  Out +'},'

   return status, result
               

def search_fix(message):

    Year = -1      # по умолчанию год не нашли
    Month = -1     # по умолчанию месяц не нашли
    Day_Month = -1  # по умолчанию день месяца ек нашли 
    Day_Week = -1   # день недели не нашли
    hour = -1      # по умолчанию часа нет
    minute = -1    # по умолчанию месяца нет

    line = message.split() #разбитие строки на список слов

    #  ищем однократные со словом "через"
    T = search_cherez(line)
    if T[0]:
            # нашли однократные со словом "через"
            Year = T[1].year
            Month = T[1].month 
            Day_Month = T[1].day
            hour = T[1].hour
            minute = T[1].minute
            # уходим в конец программы
    else:
            # со словом "через" не нашли 
            #ищем времяt  %H:%N
    
            for i in range(len(line)): 
                 t = search_time(line[i])
                 if t[0] != -1:
                       hour = t[0]
                       minute = t[1]
                       line.remove(line[i])#удаление
                       if line[i-1] == 'в':
                            line.remove(line[i-1])
                       break # нашли выходим из цикла

            #ищем месяца и день месяца
            for i in range(len(line)): 
                    t = search_month(line[i])
                    if t != -1:
                        Month = t
                        line.remove(line[i])
                    #Теперь поищеем день 
                        t1 = search_day_of_month(line[i-1])
                        if t1 != -1:
                            Day_Month = t1
                            line.remove(line[i-1])
                        break #  нашли выходим из цикла

            #ищем год 
            for i in range(len(line)): 
                t = search_year(line[i])
                if t != -1:
                    Year = t
                    D = re.match('г.*', line[i+1])
                    if D != None:
                        line.remove(line[i+1])
                        line.remove(line[i])
                    break  # нашли выходим из цикла

     
    vremie = GetTimeNow(Year, Month, Day_Month, hour, minute) # время на выходе парсера если что-то не введено вставляется текущее время

    # Проверка на пустое действие
    if len(line) == 0:
         status = 'ERROR'
         action = 'No action '
    else:
         status = 'SUCCESS'
         action = " ".join(line) # склеиваем оставшиеся слова через пробел в одну строку
    
         # проверка на только цифры в сообщении
    if None != re.match('\d+', action):
          status = 'ERROR'
          error = 'No Text '

    
    result = 'MESSAGE={\'STATUS\':\''  + status + '\',\'DATE\':' + '{'+ vremie + '}' + ',\'TEXT\':\'' + action + '\'}'
    if status == 'SUCCESS':
        status = True
    else:
        status = False 

    return status, result   



def Parser(message): # общая функция парсер

     status = 'ERROR'   # по умолчанию ничего не нашли
     error = 'No Text '  # по умолчанию вразумительного текста нет
    

     # сначала ищем регулярные события
     K =  search_regul(message)
     if K[0]:
          # Регулярность обнар
          result = K[1]
          return result 
     else:
        # регулярных не нашли
            t = search_fix(message)
            if t[0]:
                result = t[1]
                
     return result 



#################################
print("Ввести напоминание")
#t = "Подписать служебку у начальника 13 мая 2025 г. в 16:15"

#t = "Подписать служебку у начальника 13 декабря  "
#t = "Начать собираться в 4:31"
#t = "Проснуться, улыбнуться, почистить зубы и помыться в 07:13"
#t = "Съездить на дачу 17 мая в 16:15"
#t = "Убраться в квартире через 90 минут"
#t = "Позвонить друзьям через 3 часа"
#t = "Выключить 13 декабря в 20:17"
#t = "Приготовить покушать на 2-3 дня 3 сентября 2022 года в 06:01"
#t = 'Служебку подписать на питон 12 ноября утром'
#t = 'Поскольку все записи имеют один и тот же шаблон, внести данные, которые хотите извлечь из пары скобок 13 декабря 2022 года в 16:15'
#t = "Напомни про гречку через 14 минут"
#t = "Через 50 минут таймер установаить. дерзай"
#t = "Перевод локального компьютера в режим гибернации через 2 дня"
#t = "13 1311"
#t = 1231
#t = "del_qustion_answer*как дела?*норма, как сам?"
#t = "поздравить с др маму через год в 20:18"
#t = "поздравить с др маму через 3 года в 20:18"
#t= "сделать уроки каждый день"
#t = "Тренировка каждый понедельник"
#t = "Тренировка каждый год"
#t = "поздравить с др маму через час"
#t = "тренировка каждый час в 20:19"



#t = "Перевод локального компьютера в режим гибернации завтра"
#t = 'Служебку подписать на питон в четверг в 20:17'
#t = 'Служебку подписать на питон в среду'
#t = 'Служебку в отдел кадров в среду в 13:13'
#t = "В понедельник уроки"
#t = " Основы_Python_в_четверг_15:00 в среду 15:00 "
#t = "Основы_Python_в_четверг_15:00 3 сентября 2022 года"
#t = "Сходить покушать на неделе в 13:13"
#t = "Сходить покушать на неделе"
#t = "В следующем месяце Подписать служебку "
#t = "\d\de23 2\3 3r3556"
#t = "Подписать служебку по выходным"
#t = "Сходить в сауну каждое 28 число"
#t = "Подписать служебку по выходным в 20:19"




#t = "Подписать служебку 23 февраля"


# ВВОД СТРОКИ ПОЛЬЗОВАТЕЛЕМ
# t = str(input())

print(t)

result = Parser(t)

print(result)   
  