from tkinter import *
import pyautogui
import keyboard

# 전역변수---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
key_lists = []
capture_keys = [None] * 5  # 캡쳐 단축키 5개 저장 리스트
listboxes = []  # Listbox 위젯 저장 리스트
button_sets = []  # 단축키 설정 버튼 저장 리스트

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 함수-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def capture(index):
    pyautogui.hotkey('ctrl', 'shift', 'alt', 'q')
    print(f"Ctrl+Shift+Alt+Q was pressed (from Listbox {index+1})")


# 캡쳐 활성화/비활성화 상태 변수
capture_enabled = False

# 캡쳐 시작 함수


def start_capture():
    global capture_enabled
    capture_enabled = True
    button['state'] = DISABLED  # '캡쳐 시작' 버튼 비활성화
    button2['state'] = NORMAL  # '캡쳐 종료' 버튼 활성화
    for i, key in enumerate(capture_keys):
        if key:
            keyboard.on_press(lambda e, idx=i: on_key_event(e, idx))  # 키 감지 시작
        else:
            print(f"Listbox {i+1}의 캡쳐 단축키를 먼저 설정해주세요.")

# 캡쳐 종료 함수


def stop_capture():
    global capture_enabled
    capture_enabled = False
    button['state'] = NORMAL  # '캡쳐 시작' 버튼 활성화
    button2['state'] = DISABLED  # '캡쳐 종료' 버튼 비활성화
    keyboard.unhook_all()  # 키 감지 종료

# 키 이벤트 처리 함수


def on_key_event(e, index):
    global capture_keys
    if capture_enabled and e.event_type == keyboard.KEY_DOWN:
        if e.name == capture_keys[index]:
            capture(index)

# 단축키 설정 함수


def set_keys(index):
    global capture_keys
    selected_key = listboxes[index].get(ACTIVE)
    if selected_key:
        capture_keys[index] = selected_key
        # 버튼 이름 변경
        button_sets[index]['text'] = f'단축키 설정 {index+1}: {selected_key}'
        print(f"Listbox {index+1}의 캡쳐 단축키가 '{selected_key}'(으)로 설정되었습니다.")
    else:
        print(f"Listbox {index+1}에서 단축키를 선택해주세요.")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 2. GUI 연결
tk = Tk()
tk.title("Auto Capture")  # 창 제목 설정

# 제목 레이블 제거 (창 제목으로 대체)
# label = Label(tk, text='Auto Capture', width=30, height=30)
# label.pack()

# Listbox 5개 생성
for i in range(5):
    label = Label(tk, text=f'캡쳐 인식 키 {i+1}')  # listboxes[i] 제거
    label.pack()

    listbox = Listbox(tk, height=3)  # height 옵션으로 높이 조절
    # Common keys (most reliable approach)
    common_keys = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        'space', 'enter', 'backspace', 'tab', 'shift', 'ctrl', 'alt', 'caps_lock', 'esc',
        'up', 'down', 'left', 'right', 'insert', 'delete', 'home', 'end', 'page_up', 'page_down',
        'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
        '.', ',', ';', '\'', '[', ']', '\\', '/', '-', '=', '`'  # Punctuation
    ]
    for key in common_keys:
        listbox.insert(END, key)

    listbox.pack()
    listboxes.append(listbox)  # listbox 위젯을 listboxes 리스트에 추가

    button_set = Button(
        tk, text=f'단축키 설정 {i+1}', command=lambda idx=i: set_keys(idx))
    button_set.pack()
    button_sets.append(button_set)  # 버튼 위젯을 button_sets 리스트에 추가

button = Button(tk, text='캡쳐 시작', command=start_capture)
button2 = Button(tk, text='캡쳐 종료', command=stop_capture,
                 state=DISABLED)  # 초기 상태: 비활성화

button.pack(side=LEFT, padx=10, pady=10)
button2.pack(side=LEFT, padx=10, pady=10)

tk.mainloop()
