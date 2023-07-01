
q1 = """ Q1: In the UK, the abbreviation NHS stands for National what Service?
The Options are:
1: Humanity
2: Health
3: Honour
4: Household

Choose & type in the final answer no: & Hit Enter """

q2 = """Q2: Which Disney character famously leaves a glass slipper behind at a royal ball?
The Options are:
1: Pocahontas
2: Sleeping Beauty
3: Cinderella
4: Elsa
Choose & type in the final answer no: & Hit Enter """


q3 = """Q3: What name is given to the revolving belt machinery in an airport that delivers checked luggage from the plane to baggage reclaim?
The Options are:
1: Hangar
2: Terminal
3: Concourse
4: Carousel
Choose & type in the final answer no: & Hit Enter """

q4 = """Q4: Which of these brands was chiefly associated with the manufacture of household locks?
The Options are:
1: Phillips
2: Flymo
3: Chubb
4: Ronseal
Choose & type in the final answer no: & Hit Enter """

q5 = """Q5: The hammer and sickle is one of the most recognisable symbols of which political ideology?"
The Options are:
1: Republicanism
2: Communism
3: Conservatism
4: Liberalism
Choose & type in the final answer no: & Hit Enter """

q6 = """Q6: Which toys have been marketed with the phrase “robots in disguise”?"
The Options are:
1: Bratz Dolls
2: Sylvanian Families
3: Hatchimals
4: Transformers
Choose & type in the final answer no: & Hit Enter """

questions = [q1, q2, q3, q4, q5, q6]
answers = [2, 3, 3, 1, 2, 4]
user_answer = [2, 3, 3, 1, 2, 4]
price = 1000

while True:
    start = input("""Welcome! You are now playing KBC. 
Press "Enter" to proceed 
Enter "Quit" anytime to exit from KBC and take whatever amount that you have won """)
    if start == "":
        break




for i in range(len(questions)):


    print(questions[i])

    y = int(input(""))

    user_answer.pop(i)
    user_answer.insert(i, y)

    if answers == user_answer:
        print("Right answer")
        print(f"You have won {price*((i*i)+1)}$ ")

    elif y == 0:
        break

    else:
        print("Wrong answer")
        break







# ran_ques = random.choice(questions)

# import time
#
#
# text = "Hello, this is a test text to see if all works fine."
# for char in text:
#     print (char)
#     time.sleep(4)










