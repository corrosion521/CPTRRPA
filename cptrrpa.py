from tkinter import *
import pyautogui
import keyboard

'''
# 설계

1. 특정버튼(ex.a) 누를 시, 픽픽 캡쳐 기능(ex.ctrl+shift+alt+q)들어가도록 설계

2. gui 연결

3. ppt에 그림 들어가는 시점에 자동으로 ppt의 슬라이드 생성 후 넣기

'''

# 함수-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def capture():
    pyautogui.hotkey('ctrl', 'shift', 'alt', 'q')
    print("Ctrl+Shift+Alt+Q was pressed")


# 캡쳐 활성화/비활성화 상태 변수
capture_enabled = False

# 캡쳐 시작 함수


def start_capture():
    global capture_enabled
    capture_enabled = True
    button['state'] = DISABLED  # '캡쳐 시작' 버튼 비활성화
    button2['state'] = NORMAL   # '캡쳐 종료' 버튼 활성화
    keyboard.on_press(on_key_event)  # 'a' 키 감지 시작

# 캡쳐 종료 함수


def stop_capture():
    global capture_enabled
    capture_enabled = False
    button['state'] = NORMAL  # '캡쳐 시작' 버튼 활성화
    button2['state'] = DISABLED   # '캡쳐 종료' 버튼 비활성화
    keyboard.unhook_all()  # 'a' 키 감지 종료

# 키 이벤트 처리 함수


def on_key_event(e):
    if capture_enabled and e.event_type == keyboard.KEY_DOWN:
        if e.name == 'a':
            capture()
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 2. GUI 연결
tk = Tk()
label = Label(tk, text='Pick Pick Capture')
label.pack()

button = Button(tk, text='캡쳐 시작', command=start_capture)
button2 = Button(tk, text='캡쳐 종료', command=stop_capture,
                 state=DISABLED)  # 초기 상태: 비활성화

button.pack(side=LEFT, padx=10, pady=10)
button2.pack(side=LEFT, padx=10, pady=10)

tk.mainloop()
