import random
import time
import threading

users = []
time_in_sec = 60


def menu():
    print("Welcome To The Quiz\n")
    print("----------------\n----------------\n----------------\n")
    print("1. Start Quiz\n2. Exit\n")
    select = input("Enter 1 To Start The Quiz\nEnter 2 To Exit\nType Here : ")
    if select == "1":
        start_quiz()
    elif select == "2":
        exit()
    else:
        "ERROR: Enter appropriate option"
        menu()


def timer():
    global time_in_sec, time_left
    while time_in_sec > 0:
        minutes, seconds = divmod(time_in_sec, 60)
        time_left = str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
        time.sleep(1)
        time_in_sec -= 1


def start_quiz():
    global users, time_in_sec
    time_in_sec = 60
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*\n*-*-*-*-*-*-*-*-*-*-*-*-*-*\n*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
    name = input("Enter Your Name : ")
    name = name.lower()
    if name in users:
        print("Sorry! You Cannot Attempt The Quiz Again")
        time_in_sec = 60
        menu()

    while name not in users:
        time_in_sec = 60
        users.append(name)
        timer_thread = threading.Thread(target=timer)
        timer_thread.start()
        new_game()
        break


def new_game():
    global time_in_sec
    score = 0
    qno = 1
    attempted = 0

    def score1():
        print("\n*****Quiz Has Ended*****")
        print("SCORE :", score)
        print("You Scored {} Out Of {}\n\n".format(score, attempted))
        while len(correct_ones) > 1:
            print("Your Answers For Questions ", " ".join(correct_ones), "Were Correct\n")
            break
        while len(correct_ones) == 1:
            print("Your Answer For Question ", " ".join(correct_ones[0]), "Was Correct\n")
            break
        while len(wrong_ones) > 1:
            print("Your Answers For Question ", " ".join(wrong_ones), "Were Wrong\n")
            break
        while len(wrong_ones) == 1:
            print("Your Answer For Question ", " ".join(wrong_ones[0]), "Was Wrong\n")
            break
        menu()

    def score2():
        print("\n*****Quiz Has Ended*****")
        print("Oops! Your Ran Out Of Time")
        print("SCORE :", score)
        print("You Have Attempted {} Questions".format(attempted))
        print("You Scored {} Out Of {}\n\n".format(score, attempted))
        while len(correct_ones) > 1:
            print("Your Answers For Questions ", " ".join(correct_ones), "Were Correct\n")
            break
        while len(correct_ones) == 1:
            print("Your Answer For Question ", " ".join(correct_ones[0]), "Was Correct\n")
            break
        while len(wrong_ones) > 1:
            print("Your Answers For Question ", " ".join(wrong_ones), "Were Wrong\n")
            break
        while len(wrong_ones) == 1:
            print("Your Answer For Question ", " ".join(wrong_ones[0]), "Was Wrong\n")
            break
        menu()

    questions = ["The ratio of width of our National flag to its length is",
                 "The words 'Satyameva Jayate' inscribed below the base plate of the emblem of India are taken from",
                 "'Kathakali' is a folk dance prevalent in which state",
                 "The last Mahakumbh of the 20th century was held at",
                 "The theory of economic drain of India during British imperialism was propounded by",
                 "Which Constitutional Article define `Municipalities' ?",
                 "The Constitution of India, was drafted and enacted in which language ?",
                 "Total No. of Schedule in Constitution of India is ",
                 "Constitution of India was enacted by the Constituent Assembly on ",
                 "DARPA, the agency that has funded a great deal of American AI research, is part of the Department of:",
                 "Indian Independence Act, passed by the British Parliament on ",
                 "A.M. turing developed a technique for determining whether a computer could or could not demonstrate the artificial Intelligence,, Presently, this technique is called",
                 "In which of the following festivals are boat races a special feature?",
                 "Who is the first Indian woman to win an Asian Games gold in 400m run?",
                 "Indian Council of Medical Research and which company join hands for development of COVID-19 vaccine called Covaxin?",
                 "Which NASA satellite has recently found the crashed Indian Moon lander Vikram?",
                 "Researchers of which country have recently discovered a massive black hole in the Milky Way?",
                 "What is the name of a robot created by India and UK to encourage children to wash their hands?",
                 "World Human Rights Day is observed on?",
                 "A new cheaper, quicker and pollution-free 'soil-to-soil technology' to manufacture 'biofuel' has been developed by researchers at",
                 "The first recipient of Nehru Award was", "On which day World Teachers Day is celebrated?"]
    random.shuffle(questions)
    current_options = []
    correct_ones = []
    wrong_ones = []
    solutions = {"The ratio of width of our National flag to its length is": "2:3",
                 "The words 'Satyameva Jayate' inscribed below the base plate of the emblem of India are taken from": "Mundak Upanishad",
                 "'Kathakali' is a folk dance prevalent in which state": "Karnataka",
                 "The last Mahakumbh of the 20th century was held at": "Haridwar",
                 "The theory of economic drain of India during British imperialism was propounded by": "Dadabhai Naoroji",
                 "Which Constitutional Article define `Municipalities' ?": "Article 243P",
                 "The Constitution of India, was drafted and enacted in which language ?": "English",
                 "Total No. of Schedule in Constitution of India is ": "12",
                 "Constitution of India was enacted by the Constituent Assembly on ": "26 Nov. 1949",
                 "DARPA, the agency that has funded a great deal of American AI research, is part of the Department of": "Defense",
                 "Indian Independence Act, passed by the British Parliament on": "18 July 1947",
                 "A.M. turing developed a technique for determining whether a computer could or could not demonstrate the artificial Intelligence,, Presently, this technique is called": "Turing Test",
                 "In which of the following festivals are boat races a special feature?": "Onam",
                 "Who is the first Indian woman to win an Asian Games gold in 400m run?": "Kamaljit Sandhu",
                 "Indian Council of Medical Research and which company join hands for development of COVID-19 vaccine called Covaxin?": "Bharat Biotech",
                 "Which NASA satellite has recently found the crashed Indian Moon lander Vikram?": "LRO",
                 "Researchers of which country have recently discovered a massive black hole in the Milky Way?": "China",
                 "What is the name of a robot created by India and UK to encourage children to wash their hands?": "Pepe",
                 "World Human Rights Day is observed on?": "December 10",
                 "A new cheaper, quicker and pollution-free 'soil-to-soil technology' to manufacture 'biofuel' has been developed by researchers at": "IIT-Kharagpur",
                 "The first recipient of Nehru Award was": "U Thant",
                 "On which day World Teachers Day is celebrated?": "5th October"}

    answers = [["3:5", "2:3", "2:4", "3:4"], ["Rigveda", "Satpath Brahmana", "Mundak Upanishad", "Ramayana"],
               ["Karnataka", "Orissa", "Kerala", "Manipur"], ["Nasik", "Ujjain", "Allahabad", "Haridwar"],
               ["Jawaharlal Nehru", "Dadabhai Naoroji", "R.C. Dutt", "M.K. Gandhi"],
               ["Article 243P", "Article 243Q", "Article 243T", "Article 343U"],
               ["Hindi", "English", "Tamil", "Telugu"], ["23", "17", "97", "12"],
               ["26 January 1950", "26 Nov. 1949", "20 Nov. 1950", "20 January 1949"],
               ["Defense", "Energy", "Education", "Justice"],
               ["18 July 1947", "20 July 1947", "14 August 1947", "20 July 1946"],
               ["Turing Test", "Algorithm", "Boolean Algebra", "Logarithm"],
               ["Pongal", "Navratri", "Rongali Bihu", "Onam"],
               ["Kamaljit Sandhu", "P.T.Usha", "K.Malleshwari", "M.L.Valsamma"],
               ["Lupin Limited", "Bharat Biotech", "Cipla Limited", "Biocon Limited3"],
               ["CALIPSO", "LRO", "Aura", "Landsat7"], ["Russia", "China", "USA", "India"],
               ["Miko", "Pepe", "Meme", "Chichi"], ["December 10", "September 5", "December 7", "April 8"],
               ["IIT-Gandhinagar", "IIT-Jamshedpur", "IIT-Kanpur", "IIT-Kharagpur"], ["U Thant", "Mother Teresa", "Martin Luther King", "Khan Abdul Ghaffar Khan"],
               ["5th October", "7th October", "4th October", "3rd October"]]
    for question in questions:
        if time_in_sec == 0:
            score2()
            break
        print("\r", "TIME REMAINING :", time_left)
        for value, key in solutions.items():
            if question == value:
                for answer in answers:
                    if key in answer:
                        random.shuffle(answer)
                        current_options = answer
                        print("{}. {}\n".format(qno, question))
                        print("1.", current_options[0], "    2.", current_options[1], "    3.", current_options[2],
                              "    4.", current_options[3], "\n")
                        if time_in_sec == 0:
                            score2()
                            break
                        entered_option = input("Enter Your Answer :")
                        if time_in_sec == 0:
                            score2()
                            break
                        attempted += 1
                        if entered_option == str((current_options.index(key) + 1)):
                            print("\nYour Answer is Correct")
                            score += 1
                            current_options.clear()
                            correct_ones.append(str(qno))
                            if qno == 20:
                                score1()
                                break
                            qno += 1
                        else:
                            print("Your Answer is Wrong\n")
                            print("Correct Answer is", key)
                            current_options.clear()
                            wrong_ones.append(str(qno))
                            if qno == 20:
                                score1()
                                break
                            qno += 1


menu()