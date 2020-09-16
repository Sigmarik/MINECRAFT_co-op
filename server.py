import socket
import pyautogui

def transform(s):
    lib = {'left shift':'shift', 'return':'enter', 'left alt':'alt'}
    try:
        return lib[s]
    except:
        return s

sock = socket.socket()
sock.bind(('', 9090))
while True:
    sock.listen(1)
    conn, addr = sock.accept()

    print('connected:', addr)

    while True:
        try:
            data = conn.recv(1024)
            #print(data)
            if data == b'prs':
                key = conn.recv(1024).decode()
                print('pressed', key)
                pyautogui.keyDown(transform(key))
            if data == b'rel':
                key = conn.recv(1024).decode()
                print('released', key)
                pyautogui.keyUp(transform(key))
            if data == b'mmv':
                pos_s = conn.recv(1024).decode()
                pos = [int(x) for x in pos_s.split()]
                print(pos)
                pyautogui.move(*pos)
            if data == b'mpr':
                button = conn.recv(1024).decode()
                print('Mouse pressed', button)
                if button == 1:
                    pyautogui.mouseDown(button='left')
                if button == 3:
                    pyautogui.mouseDown(button='right')
                if button == 4:
                    pyautogui.scroll(1)
                if button == 5:
                    pyautogui.scroll(-1)
            if data == b'mrl':
                button = conn.recv(1024).decode()
                print('Mouse released', button)
                if button == 1:
                    pyautogui.mouseUp(button='left')
                if button == 3:
                    pyautogui.mouseUp(button='right')
        except Exception as E:
            print(E)
            break

    conn.close()
