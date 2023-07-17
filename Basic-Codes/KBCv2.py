# This is the Second Version of KBC Game in which you can answers questions & win a certain amount of Money
print("""\n
--------------------------------------
               KBCv2
      Kaun Banega Crorepati
--------------------------------------""")
# https://in.indeed.com/viewjob?jk=f000a8dddd035fae&tk=1h31goipkjtuo800&from=serp&vjs=3

Questions_and_Answers = [["Which is the National Fruit ?","Mango","Peach","Apple","Kiwi",1],
                        ["The language of Lakshadweep. a Union Territory of India ?","Tamil","Hindi","Malayalam","Telugu",3],
                        ["Which planet in our solar system is known as the Red Planet ?","Venus","Mars","Earth","Pluto",2],
                        ["Which is the smallest bird in the World ?","Humming Bird","Ostrich","Sparrow","Hen",1],
                        ["Pongal is a popular festival of which state ?","Andhra Pradesh","Karnataka","Kerala","Tamil Nadu",4],
                        ["Who founded Gravity ?","Charles Babbage","Eistein","Alexander Graham Bell","Eisic Newton",4],
                        ["Which is the National Animal ?","Lion","Tiger","Cow","Dog",2],
                        ["September 27 is celebrated every year as","Teachers' Day","National Integration Day","World Tourism Day","International Literacy Day",3],
                        ["Which planet in our solar system is extinct ?","Venus","Sun","Pluto","Jupitor",3],
                        ["Which of the following is observed as Sports Day every year ?","22nd April","26th  july","29th August","2nd October",3],
                        ["Which of the following was the theme of the World Red Cross and Red Crescent Day ?","Dignity for all - focus on women","Dignity for all - focus on Children","Focus on health for all","Nourishment for all-focus on children",2],
                        ["Who invented the Telephone ?","Charles Babbage","Eistein","Alexander Graham Bell","Eisic Newton",3],
                        ["Ghototkach in Mahabharat was the son of","Duryodhana","Arjuna","Yudhishthir","Bhima",4]]

Payout = ["0","5,000","10,000","20,000","40,000","80,000","1,60,000","3,20,000","6,40,000","12,50,000","25,00,000","50,00,000","75,00,000","1,00,00,000"]

# print(len(Questions_and_Answers))

def KBCGame():
      for i in range(0,len(Questions_and_Answers)):
            print(f"\nThis Question is for {Payout[i+1]} Rs.")
            item = Questions_and_Answers[i]
            print (f"{i+1}. {item[0]}")
            print(f"1. {item[1]}\n2. {item[2]}\n3. {item[3]}\n4. {item[4]}")
            ans=int(input("Choose an Option : "))
            if ans == item[-1]:
                  print(f"The amount you won is Rs. {Payout[i+1]}")
            else:
                  print("Your Answer was Wrong !!!")
                  print(f"The Right Answer is {item[item[-1]]}")
                  if i <= 2:
                        print(f"The Final amount you won is Rs. 0")
                  elif i <= 7:
                        print(f"The Final amount you won is Rs. 20,000")
                  elif i <= 12:
                        print(f"The Final amount you won is Rs. 6,40,000")
                  else:
                        print(f"The Final amount you won is Rs. {Payout[i]}")
                  break

while True:
      print("\nDo you want to Play the Game ?\n1. Start\n2. Exit")
      inp = int (input("Choose an Option : "))
      if inp == 1:
            KBCGame()
      elif inp == 2:
            quit()
      else:
            print("Please !!! Choose a Right Option.")