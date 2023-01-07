from tkinter import *
from PIL import ImageTk, Image
import warnings

warnings.filterwarnings('ignore')

start_go = Tk()
start_go.title("Main screen")
start_go.geometry("600x450")
cvs = Canvas(start_go)
cvs.config(width=600,height=450, bd=0, highlightthickness=0)
cvs.pack()


s1 = (300,225)
img4 = Image.open("C:/python-project1/bg.jpg")
img4 = ImageTk.PhotoImage(img4, master=start_go)
cvs.create_image(s1, image=img4)
cvs.pack()


def go_game():
    import creative_sejong
    # subprocess.call("creative_sejong.py", shell=True) -> 소스파일만 열리고 실행 -> 코드 폐기

def print_score():

    score_list_view = Tk()
    score_list_view.title("Score List")
    score_list_view.geometry("400x400")

    # 파일 읽기 모드로 열기
    file = open('ranking.txt', 'r', encoding='UTF8')
    label = Label(score_list_view)
    result = ""
    while True:
        line = file.readline()
        if not line:
            break
        result += line
    # 파일 닫기
    file.close()

    label.configure(text="Score List\n\n" + result)
    label.pack()

    score_list_view.mainloop()

def exit_start():
    start_go.destroy()


img1 = PhotoImage(file = "C:/python-project1/start.png")
img2 = PhotoImage(file = "C:/python-project1/searchlist.png")
img3 = PhotoImage(file = "C:/python-project1/close.png")


button1 = Button(start_go, image= img1, text="Start", command=go_game)
button2 = Button(start_go, image= img2, text="Search List", command=print_score)
button3 = Button(start_go, image= img3, text="Close", command=exit_start)

cvs.create_window(30,350, anchor= NW , window= button1)
cvs.create_window(225,350, anchor= NW , window= button2)
cvs.create_window(420,350, anchor= NW , window= button3)



start_go.mainloop()