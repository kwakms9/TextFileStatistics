from tkinter import *
from tkinter import filedialog
import re
from tkinter import messagebox as msg

def load():
    filename = filedialog.askopenfilename(initialdir="/", title="Select txt", filetypes=(("txt파일", "*.txt"), ("모든파일", "*.*")))
    e1.delete(0,END)
    e1.insert(0,filename)
    return filename

def allCharCount(file):  #공백포함 개행문자X
    f =file
    f.seek(0)
    s = f.read().replace("\n","")

    count = 0
    for c in s:
        count+=1

    return str(count)

def charsCount(file):    #공백 미포함
    f =file
    f.seek(0)
    s = f.read().replace("\n","").replace(" ","")

    count = 0
    for c in s:
        count+=1

    return str(count)

def wordsCount(file):    #단어 수
    f =file
    f.seek(0)
    s = f.read().lower()
    s = re.sub("[^ a-zA-Z0-9\n]", "", s)
    s = s.replace("\n"," ").split(" ")
    if "" in s:
        s.remove("")

    count = 0
    for c in s:
        count+=1

    return str(count)

def wordKindCount(file):    #단어 종류
    f =file
    f.seek(0)
    s = f.read().lower()
    s = re.sub("[^ a-zA-Z0-9\n]", "",s)
    s = set(s.replace("\n"," ").split(" "))
    if "" in s:
        s.remove("")

    count = 0
    for c in s:
        count+=1

    return str(count)

def lineCount(file):    #단어 종류
    f =file
    f.seek(0)
    line = f.readline()

    count = 0
    while line != "":
        count += 1
        line = f.readline()

    return str(count)

def result(mode):
    if mode == "console":
        filename= input("파일이름 및 경로를 입력: ")

        try:
            f = open(filename, "r")
        except:
            print("잘 못된 파일입니다.")
            return

        all = allCharCount(f)
        chars = charsCount(f)
        words = wordsCount(f)
        kind = wordKindCount(f)
        line = lineCount(f)
        f.close()

        resultLabel = "글자(공백 포함)\t" + all + "자\n" + \
                      "글자(공백 제외)\t" + chars + "자\n" + \
                      "단어\t\t" + words + "자\n" + \
                      "단어 종류\t\t " + kind + "자\n" + \
                      "줄\t\t" + line + "줄\n"

        print(resultLabel)
    else:
        if e1.get() != "":
            filename = e1.get()
            try:
                f = open(filename,"r")
            except:
                msg.showerror('알림.', '잘 못된 파일입니다.')
                return
            all = allCharCount(f)
            chars = charsCount(f)
            words = wordsCount(f)
            kind = wordKindCount(f)
            line = lineCount(f)
            f.close()

            resultLabel = "글자(공백 포함)\t"+all+"자\n"+\
                          "글자(공백 제외)\t"+chars+"자\n"+\
                          "단어\t\t"+words+"자\n"+\
                          "단어 종류\t\t "+kind+"자\n"+\
                          "줄\t\t"+ line+"줄\n"

            l3['text'] = resultLabel
        else:
            msg.showwarning('알림.', '파일이 선택되지 않았습니다.')

mode = input("모드선택(console or gui): ")

if mode.lower() == "console":
    mode="console"
    result(mode)

elif mode.lower() == "gui":
    window = Tk()
    window.title("텍스트 파일 통계 처리 프로그램")
    window.geometry("400x250")
    f1 = Frame(window)

    l1 = Label(f1,text="파일 : ").grid(row=0,column=0)
    e1 = Entry(f1)
    e1.grid(row=0, column=1)
    b1 = Button(f1,text="선택", command=load).grid(row=0,column=2)
    b2 = Button(f1,text="통계확인", command= lambda : result(mode)).grid(row=0,column=3)

    l2 = Label(window,text="결과")
    l3 = Label(window,text="\n\n\n")

    f1.pack()
    l2.pack()
    l3.pack()
    window.mainloop()
else:
    print("잘 못된입력입니다.")