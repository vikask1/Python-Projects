import tkinter
from tkinter import *
import random


questions = [
    "Who among the following considered as the 'father of artificial intelligence'?",
    " Halley's comet completes one revolution around the sun in:",
    "The unit of electric power is",
    "The International Literacy Day is observed on",
    "The Taj Mahal is located in  ?",
    "An identity theft scheme in computer is known as?",
    "Which of the following is not a coastal city of india ?",
    "In electrical motor",
    "Which of the following has pH value 7?",
    "How the quality of printer is measured?",
    "Who has been appointed as the President of Microsoft India?",
    "National Centre for Radio Astrophysics is located in which of the following city?",
    "Chemical name of Aspirin is",
    "The Electronic Voting Machines used in the Indian elections can record a maximum of ___________ votes.",
]

answers_choice = [
    ["Charles Babbage", "Lee De Forest", "John McCarthy", "JP Eckert"],
    [
        "40 years",
        "45 years",
        "60 years",
        "76 years",
    ],
    [
        "Ampere",
        "Volt",
        "Coulomb",
        "Watt",
    ],
    [
        "Sep 8",
        "Nov 28",
        "May 2",
        "Sep 22",
    ],
    [
        "Patna",
        "Delhi",
        "Benaras",
        "Agra",
    ],
    [
        "Vishing",
        "Fhishing",
        "Phishing",
        "Jacking",
    ],
    [
        "Bengaluru",
        "Kochin",
        "Mumbai",
        "Vishakhapatnam",
    ],
    [
        "Heat is converted into electrical energy",
        "Electrical energy is converted into heat",
        "Electrical energy is converted into mechanical energy",
        "Mechanical energy is converted into electrical energy",
    ],
    [
        "Pure water",
        " Neutral Solution",
        "Basic Solution",
        "Acidic Solution",
    ],
    [
        "Dots per Inch",
        "Strike per Inch",
        " Words per Inch",
        " Alphabet per strike",
    ],
    [
        "Rich Lesser",
        "Muhtar Kent",
        "Anant Maheshwari",
        "Sundar Pichai",
    ],
    [
        "Jaipur",
        "Chennai",
        "Hyderabad",
        "Pune",
    ],
    [
        "Acetylsalicylic acid",
        "Sodium bicarbonate",
        "Potassium aluminium sulphate",
        "Ethyl alcohol",
    ],
    [
        "1500",
        "2000",
        "2500",
        "3000",
    ],
]

answers = [2, 1, 3, 0, 3, 2, 0, 2, 1, 0, 2, 3, 0, 1]

user_answer = []

indexes = []


def gen():
    global indexes
    while len(indexes) < 5:
        x = random.randint(0, 13)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Denmark", 40),
        background="deep sky blue",
        foreground="midnight blue",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="five.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Are Excellent !!")
        background = "midnight blue"
    elif score >= 10 and score < 20:
        img = PhotoImage(file="three.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better !!")
        background = "midnight blue"
    else:
        img = PhotoImage(file="one.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Should Work Hard !!")
        background = "midnight blue"
    labelscore = Label(
        root, font=("Impact", 40), background="hot pink", foreground="midnight blue"
    )
    labelscore.pack()
    labelscore.configure(text="SCORE-" + score_str + "/25")


score_str = ""


def calc():
    global indexes, user_answer, answers, score, score_str
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    score_str = str(score)
    showresult(score)


ques = 1


def selected():
    global radiovar, user_answer
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text=questions[indexes[ques]])
        r1["text"] = answers_choice[indexes[ques]][0]
        r2["text"] = answers_choice[indexes[ques]][1]
        r3["text"] = answers_choice[indexes[ques]][2]
        r4["text"] = answers_choice[indexes[ques]][3]
        ques += 1
    else:

        calc()


def startquiz():
    root.config(background="hot pink")
    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(
        root,
        text=questions[indexes[0]],
        font=("Peace sans", 20),
        width=500,
        justify="center",
        wraplength=400,
        foreground="deep sky blue",
        background="midnight blue",
    )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][0],
        font=("Proxima Nova", 20),
        value=0,
        variable=radiovar,
        command=selected,
        background="deep sky blue",
        foreground="midnight blue",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Proxima Nova", 20),
        value=1,
        variable=radiovar,
        command=selected,
        background="deep sky blue",
        foreground="midnight blue",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Proxima Nova", 20),
        value=2,
        variable=radiovar,
        command=selected,
        background="deep sky blue",
        foreground="midnight blue",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Proxima Nova", 20),
        value=3,
        variable=radiovar,
        command=selected,
        background="deep sky blue",
        foreground="midnight blue",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()


root = tkinter.Tk()
root.title("QuizMinds")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0, 0)


img1 = PhotoImage(file="large_quizminds.png")

labelimage = Label(
    root,
    image=img1,
    background="#ffffff",
)
labelimage.pack(pady=(40, 0))

labeltext = Label(
    root,
    text="QuizMinds",
    font=("Lithograph", 24, "bold"),
    background="#ffffff",
)
labeltext.pack(pady=(0, 50))

img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command=startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text="Read The Rules And\nClick Start Once You Are ready",
    background="#ffffff",
    font=("Consolas", 14),
)
lblInstruction = Label(
    root,
    text="Read The Rules And Click Start Once You Are ready\nDAV Model School Durgapur Computer Project",
    background="#ffffff",
    font=("impact", 14),
    justify="center",
    foreground="green",
)
lblInstruction.pack(pady=(10, 10))

lblRules = Label(
    root,
    text="This quiz contains 10 questions\nYou will get 20 seconds to solve a question\nOnce you select a radio button that will be a final choice\nHence think before you select",
    width=100,
    font=("Times", 14),
    background="midnight blue",
    foreground="deep sky blue",
)

lblRules.pack()

root.mainloop()
