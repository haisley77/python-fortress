# 라이브러리 import
from tkinter import *
from PIL import Image, ImageTk
import math
import time

# 게임 윈도우 설정
win = Tk()
win.title("Fortress Game")
win_w, win_h = (800,800)
win.geometry(f"{win_w}x{win_h}")

# 이벤트 함수
def press(event):
    global up_go, down_go
    if event.keysym == "Up":
        up_go = True
    
    elif event.keysym == "Down":
        down_go = True
        
def release(event):
    global up_go, down_go
    if event.keysym == "Up":
        up_go = False
    
    elif event.keysym == "Down":
        down_go = False

up_go, down_go = (False, False)
win.bind("<KeyPress>", press)
win.bind("<KeyRelease>", release)

# 캔버스 설정
cvs = Canvas(win)
cvs.config(width=win_w, height=win_h, bd=0, highlightthickness=0)
cvs.pack()


# 게임 배경
bot_h = round(win_h * 1/5)
color_bot = "#d2a679"
cvs.create_rectangle((0,win_h-bot_h),(win_w,win_h),fill=color_bot, outline=color_bot)

mid_h = round((win_h-bot_h)/8)
color_mid = "#996633"
cvs.create_rectangle((0,win_h-bot_h-mid_h),(win_w,win_h-bot_h),fill=color_mid, outline=color_mid)


top_h = win_h-bot_h-mid_h
color_top = "#b3d9ff"
cvs.create_rectangle((0,0),(win_w,top_h),fill=color_top, outline=color_top)


# 각도기
angle_r = round(bot_h/2)
angle_margin_x = round(win_w/20)
angle_margin_y = round(bot_h/4)
angle_center = (angle_r + angle_margin_x, win_h-bot_h+angle_margin_y+angle_r)
cvs.create_arc((angle_center[0]-angle_r,angle_center[1]-angle_r), (angle_center[0]+angle_r,angle_center[1]+angle_r), extent=180, fill="#b3b3cc", width=1)

# math 함수 -> radian 단위
angle_min = 30 * math.pi / 180
angle_max = 90 * math.pi / 180

cvs.create_line(angle_center,(angle_center[0]+angle_r*math.cos(angle_min),angle_center[1]-angle_r*math.sin(angle_min)), width=2)
cvs.create_line(angle_center,(angle_center[0]+angle_r*math.cos(angle_max),angle_center[1]-angle_r*math.sin(angle_max)), width=2)

cvs.create_arc((angle_center[0]-round(angle_r/5),angle_center[1]-round(angle_r/5)), (angle_center[0]+round(angle_r/5),angle_center[1]+round(angle_r/5)), extent=180, fill="#ffff00")

angle_now = angle_min
angle_line = cvs.create_line(angle_center,(angle_center[0]+angle_r*math.cos(angle_now),angle_center[1]-angle_r*math.sin(angle_now)), width=2, fill="red")



# 탱크 이미지 설정
tank_img = Image.open("C:/Users/hahi1/python-fortress/canon1.png")
tank_img = tank_img.resize((120,120), Image.ANTIALIAS)
tank_img = tank_img.rotate(angle_now * 180 / math.pi - 20)
tank_img = ImageTk.PhotoImage(tank_img, master = win)
img_p = (120,500)
tank = cvs.create_image(img_p, image = tank_img)



win.update()

while True:
    # while 반복문을 0.01 sec 마다 실행f
    time.sleep(0.01)
    cvs.delete(angle_line)
    cvs.delete(tank)
    if up_go == True and down_go == False:
        if (angle_now <= angle_max):
            angle_now += 0.01
    if up_go == False and down_go == True:
        if (angle_now >= angle_min):
            angle_now -= 0.01
    
    angle_line = cvs.create_line(angle_center,(angle_center[0]+angle_r*math.cos(angle_now),angle_center[1]-angle_r*math.sin(angle_now)), width=2, fill="red")
    
    tank_img = Image.open("C:/Users/hahi1/python-fortress/canon1.png")
    tank_img = tank_img.resize((120,120), Image.ANTIALIAS)
    # 각도 단위 조정
    tank_img = tank_img.rotate(angle_now * 180 / math.pi - 20)
    tank_img = ImageTk.PhotoImage(tank_img, master = win)
    img_p = (120,500)
    tank = cvs.create_image(img_p, image = tank_img)
    win.update()