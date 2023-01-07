import pygame
import random
from PIL import Image, ImageTk
from tkinter import Tk, Button, Canvas, Label, Entry
import math
import time
import datetime
import warnings
warnings.filterwarnings('ignore')



pygame.init()


counter = 0  # 게임한 횟수 세기

cannonball_vx = 0
cannonball_vy = 0
cannonball_cx = -9999999999999
cannonball_cy = -9999999999999

global computer_specification

computer_specification = Tk()
computer_specification.title("Game")
computer_specification_w, computer_specification_h = (800, 800)
computer_specification.geometry(f"{computer_specification_w}x{computer_specification_h}")

# 배경 사운드
# pygame.mixer.init()
# pygame.mixer.music.load("C:/python-project1/background.mp3")
# pygame.mixer.music.play(-1)  # 배경음악 반복


# 저장기능의 구현

def save(regis_view, e, score):
    
    # pygame.mixer.music.stop()
    # 파일 쓰기 모드로 열기
    file = open('ranking.txt', 'a', encoding='UTF8')
    # 점수 입력
    result = "ID: " + e.get() + "     Time: " + str(datetime.datetime.now()) + "     SCORE: " + str(score) + "\n"
    file.write(result)
    # 파일 닫기
    file.close()
    
    regis_view.destroy()
    computer_specification.destroy()
    



def input_score(score):

    regis_view = Tk()
    regis_view.title("Save")
    regis_view.geometry("300x100")


    label = Label(regis_view)


    label.configure(text="user ID: ")
    label.pack()

    e = Entry(regis_view)
    e.pack()

    btn = Button(regis_view, text="저장", command=lambda:save(regis_view, e,score))
    btn.pack()

    cvs = Canvas(regis_view)
    cvs.config(width=300, height=100, bd=0, highlightthickness=0)
    cvs.pack()


    regis_view.mainloop()



# 입력기능의 구현


def press(event):
    global to_upper, to_lower, ok_sign, step
    if step == 1:
        if event.keysym == "Up":
            to_upper = True

        elif event.keysym == "Down":
            to_lower = True
# ------대포 위아래 구현
        if event.keysym == "space":
            ok_sign = True
            step = 2


def release(event):
    global to_upper, to_lower, ok_sign, cannonball_cx, cannonball_cy, cannonball_vx, cannonball_vy, cannonball, step

    if step == 1:
        if event.keysym == "Up":
            to_upper = False

        elif event.keysym == "Down":
            to_lower = False
# ------대포 위아래 구현
    if step == 2:
        if event.keysym == "space":
            ok_sign = False

            cannonball_cx = round(
                ordnance_cx + ordnance_w/2*math.cos(angle_current_value))
            cannonball_cy = round(
                ordnance_cy - ordnance_w/2*math.sin(angle_current_value))
        # 폭탄의 초기 위치 구현

            cannonball_vx = round(
                cannonball_v_max * energy/100 * math.cos(angle_current_value))
            cannonball_vy = round(-cannonball_v_max *
                                  energy/100 * math.sin(angle_current_value))
        # 폭탄의 초기 속도 구현

            cannonball = cvs.create_oval((cannonball_cx-cannonball_r, cannonball_cy-cannonball_r),
                                         (cannonball_cx+cannonball_r, cannonball_cy+cannonball_r), fill="black")
            step = 3


to_upper, to_lower, ok_sign = (False, False, False)
step = 1  # 시나리오 구성
hit = False
computer_specification.bind("<KeyPress>", press)
computer_specification.bind("<KeyRelease>", release)


cvs = Canvas(computer_specification)
cvs.config(width=computer_specification_w,
           height=computer_specification_h, bd=0, highlightthickness=0)
cvs.pack()
s1 = (400, 400)

img = Image.open("C:/python-project1/background1.png")

img = ImageTk.PhotoImage(img, master=computer_specification)
cvs.create_image(s1, image=img)


# background 구현
background_h = round(computer_specification_h * 1/5)
background_c = "#a6a6a7"
# cvs.create_rectangle((0, computer_specification_h-background_h), (computer_specification_w, computer_specification_h),fill=background_c,outline=background_c)
backgroundmiddle_h = round((computer_specification_h - background_h) * 1/8)
backgroundmiddle_c = "#954d33"
# cvs.create_rectangle((0, computer_specification_h-background_h-backgroundmiddle_h), (computer_specification_w, computer_specification_h-background_h),fill=backgroundmiddle_c,outline=backgroundmiddle_c)
backgroundtop_h = computer_specification_h-background_h-backgroundmiddle_h
backgroundtop_c = "#b5b5fd"
# cvs.create_rectangle((0, 0), (computer_specification_w, backgroundtop_h),fill=backgroundtop_c,outline=backgroundtop_c)


# angle 구현
angle_r = round(background_h/2)
angle_x = round(computer_specification_w/20)
angle_y = round(background_h/4)
angle_center = (angle_r + angle_x, computer_specification_h -
                background_h + angle_y + angle_r)
cvs.create_arc((angle_center[0]-angle_r, angle_center[1]-angle_r),
               (angle_center[0]+angle_r, angle_center[1]+angle_r), fill="#6666ff", extent=180)

angle_min = 30 * math.pi/180
angle_max = 90 * math.pi/180

cvs.create_line(angle_center, (angle_center[0]+angle_r*math.cos(
    angle_min), angle_center[1]-angle_r*math.sin(angle_min)), width=2)
cvs.create_line(angle_center, (angle_center[0]+angle_r*math.cos(
    angle_max), angle_center[1]-angle_r*math.sin(angle_max)), width=2)

cvs.create_arc((angle_center[0]-round(angle_r/5), angle_center[1]-round(angle_r/5)),
               (angle_center[0]+round(angle_r/5), angle_center[1]+round(angle_r/5)), fill="#ffcccc", extent=180)

angle_current_value = 45 * math.pi/180

angle_line = cvs.create_line(angle_center, (angle_center[0]+angle_r*math.cos(
    angle_current_value), angle_center[1]-angle_r*math.sin(angle_current_value)), fill="red", width=2)

# ordnance 구현
ordnance_w, ordnance_h = (round(min(computer_specification_w, computer_specification_h)/7),
                          round(min(computer_specification_w, computer_specification_h)/7))
ordnance_cx = round(computer_specification_w/40+ordnance_w)
ordnance_cy = backgroundtop_h-round(ordnance_h/2)

ordnance_img = Image.open("C:/python-project1/canon1.png")
ordnance_img = ordnance_img.resize((ordnance_w, ordnance_h), Image.ANTIALIAS)
ordnance_img = ordnance_img.rotate(angle_current_value*180/math.pi-30)
ordnance_img = ImageTk. PhotoImage(ordnance_img, master=computer_specification)
ordnance = cvs.create_image(ordnance_cx, ordnance_cy, image=ordnance_img)

# gage bar
input_power_mx = angle_x
input_power_my = angle_y

input_power_w = computer_specification_w - \
    angle_x - input_power_mx*2 - angle_r*2
input_power_h = background_h - input_power_my*2

input_power_x = angle_x + input_power_mx + angle_r*2
input_power_y = computer_specification_h - input_power_my - input_power_h

cvs.create_rectangle((input_power_x, input_power_y), (input_power_x +
                     input_power_w, input_power_y+input_power_h), fill="white")
# 큰게이지바의 배경 설정

power_gage_mx = round(input_power_h/8)
power_gage_my = power_gage_mx

power_gage_x = input_power_x + power_gage_mx
power_gage_y = input_power_y + power_gage_my

energy = 0
power_gage_w = (input_power_w - power_gage_mx*2)*energy/100
power_gage_h = input_power_h - power_gage_my*2
power_gage = cvs.create_rectangle((power_gage_x, power_gage_y), (
    power_gage_x+power_gage_w, power_gage_y+power_gage_h), width=0, fill="red")
# 작은 게이지바의 배경 설정

# cannonball
cannonball_r = 10
cannonball_v_max = 50
cannonball_ay = 1

# computer_specificationdbar
wind_vector_mx = input_power_mx
wind_vector_my = input_power_mx
wind_vector_w = wind_vector_mx*8
wind_vector_h = wind_vector_my*2

wind_vector_x = computer_specification_w - wind_vector_mx - wind_vector_w
wind_vector_y = wind_vector_my
cvs.create_rectangle((wind_vector_x, wind_vector_y), (wind_vector_x +
                     wind_vector_w, wind_vector_y + wind_vector_h), width=2, fill="white")
cvs.create_line((round(wind_vector_x + wind_vector_w/2), wind_vector_y),
                (round(wind_vector_x + wind_vector_w/2), wind_vector_y + wind_vector_h), width=5)

computer_specificationd = 0
computer_specificationd_ax_max = 0.2

computer_specificationd_ax = computer_specificationd_ax_max*computer_specificationd/100

base_vector_mx = round(wind_vector_h/10)
base_vector_my = base_vector_mx

if computer_specificationd >= 0:
    base_vector_x = round(wind_vector_x + wind_vector_w/2) + base_vector_mx
else:
    base_vector_x = round(wind_vector_x + wind_vector_w/2) - base_vector_mx

base_vector_y = wind_vector_y + base_vector_my

base_vector_w = (wind_vector_w/2 - 2*base_vector_mx) * \
    computer_specificationd/100
base_vector_h = wind_vector_h - 2*base_vector_my

base_vector = cvs.create_rectangle((base_vector_x, base_vector_y), (
    base_vector_x + base_vector_w, base_vector_y + base_vector_h), width=0, fill="blue")

# 적중의 여부는
# 거리가 > 포탄의 반지름과 과녘의 반지름보다 클 경우 맞추지 못했다고 추정가능!


# target
target_r = 40
target_range_x = (round((computer_specification_w/3)),
                  computer_specification_w-target_r)
target_range_y = (wind_vector_y+wind_vector_h +
                  target_r, backgroundtop_h-target_r)

target_cx = random.randrange(target_range_x[0], target_range_x[1])
target_cy = random.randrange(target_range_y[0], target_range_y[1])

target_img = Image.open("C:/python-project1/target1.png")
target_img = target_img.resize((target_r*2, target_r*2), Image.ANTIALIAS)
target_img = ImageTk. PhotoImage(target_img, master=computer_specification)
target = cvs.create_image(target_cx, target_cy, image=target_img)

# count box
scoreboard_x = wind_vector_mx
scoreboard_y = wind_vector_my
scoreboard_w = scoreboard_x*3
scoreboard_h = wind_vector_h
cvs.create_rectangle((scoreboard_x, scoreboard_y), (scoreboard_x +
                     scoreboard_w, scoreboard_y+scoreboard_h), fill="black", width=2)
count = 0
scoreboard = cvs.create_text((round(scoreboard_x + scoreboard_w/2), round(
    scoreboard_y+scoreboard_h/2)), fill="white", font=("Arial", 30), text=count)


# 게임오버
font_gameover = pygame.font.SysFont(None, 30)
text_gameover = font_gameover.render("GAME OVER", True, (255, 0, 0))


computer_specification.update()
play = True
while play:

    time.sleep(0.01)
    cvs.delete(angle_line)
    cvs.delete(ordnance)
    cvs.delete(power_gage)
    cvs.delete(base_vector)

    try:
        cvs.delete(cannonball)
    except:
        pass

    if step == 1:
        if to_upper == True and to_lower == False and angle_current_value <= angle_max:
            angle_current_value += 0.01

        elif to_lower == True and to_upper == False and angle_current_value >= angle_min:
            angle_current_value -= 0.01

    # -----여기부터 게이지바 구현
    if step == 2:
        if ok_sign == True and energy < 100:
            energy += 1

    if step == 3:

        computer_specificationd_ax = computer_specificationd_ax_max*computer_specificationd/100
        cannonball_vx += computer_specificationd_ax
        cannonball_vy += cannonball_ay
        cannonball_cx += cannonball_vx
        cannonball_cy += cannonball_vy

        distance = ((cannonball_cx-target_cx)**2 +
                    (cannonball_cy-target_cy)**2)**0.5

        if distance <= cannonball_r + target_r:
            hit = True

        if cannonball_cy >= backgroundtop_h or hit == True:
            counter += 1
            step = 1
            energy = 0
            computer_specificationd = random.randrange(-100, 101)

            if hit == True:
                cvs.delete(target)
                arget_cx = random.randrange(
                    target_range_x[0], target_range_x[1])
                target_cy = random.randrange(
                    target_range_y[0], target_range_y[1])

                target = cvs.create_image(
                    target_cx, target_cy, image=target_img)

                count += 1
                cvs.delete(scoreboard)
                scoreboard = cvs.create_text((round(scoreboard_x + scoreboard_w/2), round(
                    scoreboard_y+scoreboard_h/2)), fill="white", font=("Arial", 30), text=count)
                # 맞춘 경우에는 점수를 올리고 과녘의 재상산을 할 수 있도록 설정!

                hit = False

                # 게임오버 기능 구현

    if counter == 10:
        pygame.quit()
        input_score(count)
        computer_specification.destroy()


    angle_line = cvs.create_line(angle_center, (angle_center[0]+angle_r*math.cos(
        angle_current_value), angle_center[1]-angle_r*math.sin(angle_current_value)), fill="red", width=2)

    ordnance_img = Image.open("C:/python-project1/canon1.png")
    ordnance_img = ordnance_img.resize(
        (ordnance_w, ordnance_h), Image.ANTIALIAS)
    ordnance_img = ordnance_img.rotate(angle_current_value*180/math.pi-30)
    ordnance_img = ImageTk. PhotoImage(
        ordnance_img, master=computer_specification)
    ordnance = cvs.create_image(ordnance_cx, ordnance_cy, image=ordnance_img)

    power_gage_w = (input_power_w - power_gage_mx*2)*energy/100

    if computer_specificationd >= 0:
        base_vector_x = round(wind_vector_x + wind_vector_w/2) + base_vector_mx
    else:
        base_vector_x = round(wind_vector_x + wind_vector_w/2) - base_vector_mx

    base_vector_w = (wind_vector_w/2 - 2*base_vector_mx) * \
        computer_specificationd/100
    base_vector_h = wind_vector_h - 2*base_vector_my

    if computer_specificationd != 0:
        base_vector = cvs.create_rectangle((base_vector_x, base_vector_y), (
            base_vector_x + base_vector_w, base_vector_y + base_vector_h), width=0, fill="blue")

    # --- 바람벡터 구현

    if energy > 0:
        power_gage = cvs.create_rectangle((power_gage_x, power_gage_y), (
            power_gage_x+power_gage_w, power_gage_y+power_gage_h), width=0, fill="red")

    # ----- 게이지바 구현

    if step == 3:
        cannonball = cvs.create_oval((cannonball_cx-cannonball_r, cannonball_cy-cannonball_r),
                                     (cannonball_cx+cannonball_r, cannonball_cy+cannonball_r), fill="black")
    # ---- 폭탄 구현

    computer_specification.update()
