from time import sleep
from random import randint

status = "on"
money = 0
help_score = 2
jokers = ["A) 50/50", "B) Помощь зала", "C) Звонок другу"]

def ask_question(question, answers, correct, amount, audience, phone):
  print(question)
  sleep(1) 
  for answer in answers:
    print(answer)
    sleep(1)
  user_answer = input("Каков ваш ответ?(A-D или J для джокера) ")
  if user_answer.upper() == "J":
    use_joker(correct, amount, audience, phone)
  elif user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(2)        
  else:
    global help_score
    if help_score > 0:
      help()
      for answer in answers:
        print(answer)
        sleep(1)
      user_answer2 = input("Каков ваш ответ?(A-D или J для джокера) ")
      if user_answer2.upper() == "J":
        use_joker(correct, amount, audience, phone)
      elif user_answer2.upper() == correct:
        print(" ")
        correct_answer(amount)
        sleep(2)
      else:
        print(" ")
        game_over()
    else:
      print(" ")
      game_over()

def correct_answer(amount):
  sleep(1)
  print("Это...")
  sleep(1)
  print("ПРАВИЛЬНО!!!")
  print(" ")
  sleep(1)
  print("*👏👏👏*")  
  global money
  money = amount
  print(" ")
  sleep(1)
  print(f"Очень хорошо {name}, вы только что выиграли ${money}!")
  print(" ")
  sleep(1)

def use_joker(correct, amount, audience, phone):
  print(" ")  
  global jokers
  if len(jokers) == 0:
    print("Извините, но у вас не осталось джокеров!")
    sleep(2)
    user_answer = input("Каков будет ваш ответ? ")
    if user_answer.upper() == correct:
      print(" ")
      correct_answer(amount)
      sleep(2)
    else:
      print(" ")
      game_over()    
  else:    
    print("У вас есть следующие джокеры:")
    sleep(2)
    for joker in jokers:
      print(f"{joker}-Joker")
      sleep(1)
    joker_selection = input("Какого джокера вы хотели бы использовать?")
    if joker_selection.upper() == "A":
      jokers.remove("A) 50/50")
      jokerA(correct, amount)
    elif joker_selection.upper() == "B":
      jokers.remove("B) Помощь зала")
      jokerB(correct, amount, audience)
    elif joker_selection.upper() == "C":
      jokers.remove("C) Звонок другу")
      jokerC(correct, amount, phone)
    else:
        print('Вы можете выбрать только A,B,C!')
        use_joker(correct, amount, audience, phone)

def jokerA(correct, amount):
  answers = ["A", "B", "C", "D"]
  joker_answer = [correct]  
  answers.remove(correct)
  number = randint(0, 2)
  joker_answer.append(answers[number])
  joker_answer.sort()
  sleep(1)
  print(".")
  sleep(1)
  print("..")
  sleep(1)
  print("...")
  sleep(1)  
  print(f"Остальные варианты ответов {joker_answer[0]} и {joker_answer[1]}")
  sleep(3)
  user_answer = input("Каков будет ваш ответ? ")
  if user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(2)
  else:
    print(" ")
    game_over()

def jokerB(correct, amount, audience):
  sleep(1)
  print(".")
  sleep(1)
  print("..")
  sleep(1)
  print("...")
  sleep(1)
  print(f"Зрительское голосование таково: {audience}")
  sleep(3)
  user_answer = input("Каков будет ваш ответ? ")
  if user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(2)
  else:
    print(" ")
    game_over()

def jokerC(correct, amount, phone):
  sleep(1)
  print(".")
  sleep(1)
  print("..")
  sleep(1)
  print("...")
  sleep(1)
  print(f"Вот что сказал ваш телефонный Джокер:")
  sleep(1.5)
  print(phone)
  sleep(3)
  user_answer = input("Каков будет ваш ответ?")
  if user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(2)
  else:
    print(" ")
    game_over()

def help():
  global help_score
  help_score -= 1
  sleep(1.5)
  print(" ")
  print("...вы уверены, что это правильно?")
  sleep(2)
  print(" попробуйте снова:")
  sleep(2)    

def game_over():
  global status
  status = "off"
  print("Это...")
  sleep(1)
  print("неправильно!")
  print(" ")
  sleep(1)
  print(f"извините {name}, вы проиграли!")
  print(" ")
  print(" ")
  sleep(1)
  print("ИГРА ОКОНЧЕНА!")

question1 = "ПЕРВЫЙ,ВОПРОС НА $50: Кто из людей первым в мире полетел в космос?"
answers1 = ["A) Нил Армстронг", "B) Юрий Гагарин", "C) Валентина Терешкова", "D) Герман Титов"]
correct1 = "B"
amount1 = 50
audience1 = ["A: 0%", "B: 98%", "C: 0%", "D: 2%"]
phone1 = "Хаха, ты шутишь? Ответ - B!"

question2 = "ВОПРОС НА 100$: Сколько материков на земле?"
answers2 = ["A) 7", "B) 6", "C) 5", "D) 8"]
correct2 = "B"
amount2 = 100
audience2 = ["A: 2%", "B: 95%", "C: 2%", "D: 1%"]
phone2 = "Ну же! Я уверен, что ответ - B!"

question3 = "ТЕПЕРЬ ВОПРОС НА $200: Кто открыл Америку?"
answers3 = ["A) Диего Колон", "B) Васко да Гама", "C) Христофор Колумб", "D) Джеймс Кук"]
correct3 = "C"
amount3 = 200
audience3 = ["A: 15%", "B: 10%", "C: 75%", "D: 0%"]
phone3 = "О, эммм, разве это не C? Я думаю, что это C. Да, попробуйте C!"

question4 = "НАШ ВОПРОС ЗА $300: Сколько дней в високосном году?"
answers4 = ["A) 367", "B) 365", "C) 366", "D) 364"]
correct4 = "C"
amount4 = 300
audience4 = ["A: 28%", "B: 3%", "C: 68%", "D: 1%"]
phone4 = "Нуу...я думаю что правильный вариант C"

question5 = "ВОПРОС 500$: Кто нарисовал Мону Лизу?"
answers5 = ["A) Винсент Ван Гог", "B) Пабло Пикассо", "C) Сальвадор Дали", "D) Леонардо Да Винчи"]
correct5 = "D"
amount5 = 500
audience5 = ["A: 21%", "B: 12%", "C: 19%", "D: 48%"]
phone5 = "О, Мона Лиза... это A или D? Я думаю, D."

question6 = "$1,000 ВОПРОС: Сколько полос на флаге США?"
answers6 = ["A) 13", "B) 11", "C) 12", "D) 14"]
correct6 = "A"
amount6 = 1000
audience6 = ["A: 58%", "B: 4%", "C: 21%", "D: 17%"]
phone6 = "Я слышал про эти полосы, попробуйте вариант...A!"

question7 = "НАШ ВОПРОС НА 2 000$: Что было предложено Альберту Эйнштейну в 1952 году?"
answers7 = ["A) Золотой глобус", "B) Нобелевская премия", "C) Золотой бутс", "D) Стать президентом"]
correct7 = "D"
amount7 = 2000
audience7 = ["A: 4%", "B: 3%", "C: 11%", "D: 82%"]
phone7 = "В 1952 году Эйнштейну поступило предложение стать президентом Израиля.Правильный ответ - D"

question8 = "ДАЛЕЕ, ВОПРОС НА $4 000: Сколько элементов в таблице Менделеева?"
answers8 = ["A) 118", "B) 120", "C) 119", "D) 127"]
correct8 = "A"
amount8 = 4000
audience8 = ["A: 72%", "B: 12%", "C: 14%", "D: 2%"]
phone8 = "Эхх,химия...правильный ответ A"

question9 = "НАШ ВОПРОС НА $8,000: Что такое <<Кинофобия?>>"
answers9 = ["A) Боязнь Собак", "B) Боязнь кино и кинотеатров", "C) Боязнь снимать себя на камеру", "D) Боязнь кошек"]
correct9 = "A"
amount9 = 8000
audience9 = ["A: 48%", "B: 38%", "C: 14%", "D: 0%"]
phone9 = "Странное название, согласен. Правильный A!"

question10 = "СЕЙЧАС ЗА $16 000: Какое национальное животное у Шотландии?"
answers10 = ["A) Дракон", "B) Грифон", "C) Единорог", "D) Василиск"]
correct10 = "C"
amount10 = 16000
audience10 = ["A: 15%", "B: 8%", "C: 77%", "D: 0%"]
phone10 = "Я сам в шоке: верный C!"

question11 = "$32,000: В каком праздничном фильме снялся Дональд Трамп?"
answers11 = ["A) Гринч - похититель Рождества", "B) Крампус", "C) Один дома 2: Затерянный в Нью - Йорке", "D) Один дома"]
correct11 = "C"
amount11 = 32000
audience11 = ["A: 17%", "B: 42%", "C: 39%", "D: 2%"]
phone11 = "Чую что правильный ответ D!"

question12 = "ВОПРОС НА $64,000: Как называется корабль Джека Воробья из фильма <<Пираты Карибского моря>>?"
answers12 = ["A) Летучий Голландец ", "B) Месть Королевы Анны", "C) Черная жемчужина", "D) Титаник"]
correct12 = "C"
amount12 = 64000
audience12 = ["A: 19%", "B: 26%", "C: 28%", "D: 27%"]
phone12 = "Ты не смотрел этот фильм?((, правильный ответ - C"

question13 = "ВОПРОС НА $125,000: Кто основал Microsoft?"
answers13 = ["A) Билл Гейтс", "B) Стив Джобс", "C) Марк Цукерберг", "D) Илон Маск"]
correct13 = "A"
amount13 = 125000
audience13 = ["A: 38%", "B: 26%", "C: 21%", "D: 15%"]
phone13 = "Билл Гейтс!"

question14 = "НАШ ВОПРОС НА $500,000: В Англии существует закон, согласно которому за наезд на животное наказание строже, чем за наезд на людей. Считается, что животное беззащитно перед автомобилем, потому что…"
answers14 = ["A) Не может от него убежать", "B) Не разбирается в марках автомобилей", "C) Не знает сколько стоит эта машина", "D) Не знает правил дорожного движения"]
correct14 = "D"
amount14 = 500000
audience14 = ["A: 9%", "B: 31%", "C: 11%", "D: 49%"]
phone14 = "Я понятия не имею."

question15 = "И СЕЙЧАС: ПОСЛЕДНИЙ ВОПРОС НА $1,000,000!!!!! Почему кошки очень любят лизать руки программистам???)"
answers15 = ["A) Что??", "B) Они забывают их кормить", "C) Потому что руки очень нежные", "D) Потому что их руки пахнут <<мышкой>>)"]
correct15 = "D"
amount15 = 1000000
audience15 = ["A: 32%", "B: 11%", "C: 28%", "D: 29%"]
phone15 = "АХАХААХАА,ЧТО ЗА ВОПРОС?!"

print(" ")
print(" ")
print(" ")  
print("Леди и джентльмены!")
print(" ")
sleep(1.3)
print("Добро пожаловать на новую игру")
print(" ")
sleep(0.7)
print("КТО")
sleep(0.7)
print("ХОЧЕТ")
sleep(0.7)
print("СТАТЬ")
sleep(0.7)
print("МИЛЛИОНЕРОМ?!🤑🤑🤑")
print(" ")
sleep(1.3)
print("*👏аплодисменты👏*")
print(" ")
sleep(2.5)

print("НАШ ПЕРВЫЙ КАНДИДАТ СЕГОДНЯ - ....")
sleep(1.5)
print("...эхм...")
print(" ")
sleep(1.5)
name = input("Извините, я забыл ваше имя. Как вас зовут? (введите ваше имя) ")
print("Конечно же, это ваше имя!")
print(" ")
sleep(1.5)
print(f"Все дружно аплодируем нашему кандидату {name.upper()}!")
print(" ")
sleep(2)
print("*👏👏бурные аплодисменты👏👏*")
print(" ")
sleep(2)

print("Хорошо, давайте начнем. Сначала напомним, что у вас есть 3 джокера:")
sleep(2)
for joker in jokers:
  print(f"{joker}-Joker")
  sleep(1.5)
print("Вы можете использовать только ОДИН джокер для каждого вопроса.")
sleep(2.5)
print(" ")
print(" ")
print("Хорошо, ЕХАЛА!")
print(" ")
print(" ")
sleep(1.5)

ask_question(question1, answers1, correct1, amount1, audience1, phone1)

if status == "on":
  ask_question(question2, answers2, correct2, amount2, audience2, phone2)

if status == "on":
  ask_question(question3, answers3, correct3, amount3, audience3, phone3)

if status == "on":
  ask_question(question4, answers4, correct4, amount4, audience4, phone4)

if status == "on":
  ask_question(question5, answers5, correct5, amount5, audience5, phone5)

if status == "on":
  ask_question(question6, answers6, correct6, amount6, audience6, phone6)

if status == "on":
  ask_question(question7, answers7, correct7, amount7, audience7, phone7)

if status == "on":
  ask_question(question8, answers8, correct8, amount8, audience8, phone8)

if status == "on":
  ask_question(question9, answers9, correct9, amount9, audience9, phone9)

if status == "on":
  ask_question(question10, answers10, correct10, amount10, audience10, phone10)

if status == "on":
  ask_question(question11, answers11, correct11, amount11, audience11, phone11)

if status == "on":
  ask_question(question12, answers12, correct12, amount12, audience12, phone12)

if status == "on":
  ask_question(question13, answers13, correct13, amount13, audience13, phone13)

if status == "on":
  ask_question(question14, answers14, correct14, amount14, audience14, phone14)

if status == "on":
  ask_question(question15, answers15, correct15, amount15, audience15, phone15)

if status == "on":
  print("ПОЗДРАВЛЯЯЯЯЯЯЯЯЯЯЯЮЮЮЮЮ!!!!!")
  sleep(2)
  print(" ")
  print("ВЫ - ПОБЕДИТЕЛЬ ")
  sleep(2)
  print("ОДНОГО")
  sleep(1)
  print("МИЛЛИОНА!!")
  sleep(1)
  print("ДОЛЛАРОВ!!!!!!!!!!!!!!!!")
  print(" ")
  print(" ")
  sleep(2)
  print("НАШ НОВЫЙ ПОБЕДИТЕЛЬ...")
  print(" ")
  sleep(3)
  print("ЭТО...")
  print(" ")
  sleep(1.5)
  print("НОВЫЙ НЕЗАБЫВАЕМЫЙ МИЛЛИОНЕР: ")
  print(" ")
  sleep(3)
  print(f"{name.upper()}!!!")
  sleep(1.5)
  print(f"*👏👏👏*")
  sleep(1.5)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print("   ...")
  sleep(3)
  print(" ")
  print(" ")
  print(" ")
  print("КОНЕЦ")
