from tkinter import *
#from PIL import Image, ImageTK
win = Tk()
win.geometry("500x500")
#크기를 300*300인 창을 생성!
win.title("Game")
#창의 제목을 Game로 지정

cvs = Canvas(win)
cvs.config(width=300, height=300, bd=0, highlightthickness=0)

#cvs.configure(background="red") => ex) 전체를 빨간색 칠하기

''' p1=(0,0)
p2=(300,300)
cvs.create_line(p1, p2,fill="blue", width=50) '''
#ex1)직선 그리기

''' p1=(0,0)
p2=(300,300)
cvs.create_rectangle(p1, p2, fill="yellow", outline="green",width=10) '''
#ex2)직사각형 그리기

'''p1=(0,0)
p2=(300,300)
cvs.create_oval(p1, p2, fill="orange", outline="cyan",width=10) '''
#ex3)타원 그리기

'''p1=(0,0)
p2=(300,300)
angle=60
cvs.create_arc(p1, p2, fill="orange", outline="cyan",width=10,extent=angle)''' 
#ex4)부채꼴 그리기

''' p1=(150,150) #좌표
name="Arial" #폰트
size=50 #글자 크기
cvs.create_text(p1, text="Work", font=(name,size), fill="gray") '''
#ex5)텍스트 그리기

''' p1=(150,150) #좌표
img = Image.open("D:/temp/canon.png") #open 함수로 저장된 위치의  파일 파이썬으로 불러오기
img=img.resize((w,h),Image.ANTIALIAS) #이미지 크기 조정
#ANTIALIAS=> 깨지는 것을 방지해주는 기능!
angle=60
img=img.rotate(angle) #사진 기울이기
img = ImageTK.PhotoImage(img, master=win) # 바뀐 이미지를 tk라이브러리에서 쓸 수 있도록 변환
cvs.create_image(p1,image=img) #사진 좌표에 붙이기 '''
#ex6)외부이미지 불러오기

''' p1=(0,0)
p2=(300,300)
cvs.create_line(p1, p2,fill="blue", width=50)
cvs.create_rectangle(p1, p2, fill="yellow", outline="green",width=10)
cvs.create_oval(p1, p2, fill="orange", outline="cyan",width=10)
cvs.create_arc(p1, p2, fill="orange", outline="cyan",width=10,extent=60)'''
#ex7)복합 그리기

cvs.pack()
win.mainloop()
