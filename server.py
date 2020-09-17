import socket
import pyautogui

def dt(s):
    answ = s.replace('H', ' ').replace('P', '')
    return answ

def transform(s):
    lib = {'left shift':'shift', 'return':'enter', 'left alt':'alt'}
    try:
        return lib[s]
    except:
        return s

print(transform('return'))
print(transform('w'))

pyautogui.FAILSAFE = False

IP = socket.gethostbyname(socket.gethostname())

sock = socket.socket()
sock.bind((IP, 9090))
print('Server now on', IP)
while True:
    sock.listen(1)
    conn, addr = sock.accept()

    print('connected:', addr)

    while True:
        try:
            data = conn.recv(3)
            argums = dt(conn.recv(100).decode())
            #print(data)
            if data == b'prs':
                key = argums
                print('pressed', key)
                pyautogui.keyDown(transform(key))
            if data == b'rel':
                key = argums
                print('released', key)
                pyautogui.keyUp(transform(key))
            if data == b'mmv':
                pos_s = argums
                pos = [int(x) for x in pos_s.split()]
                print(pos)
                pyautogui.move(*pos)
            if data == b'mpr':
                button = argums
                print('Mouse pressed', button)
                if button == '1':
                    pyautogui.mouseDown(button='left')
                if button == '3':
                    pyautogui.mouseDown(button='right')
                if button == 4:
                    pyautogui.scroll(1)
                if button == 5:
                    pyautogui.scroll(-1)
            if data == b'mrl':
                button = argums
                print('Mouse released', button)
                if button == '1':
                    pyautogui.mouseUp(button='left')
                if button == '3':
                    pyautogui.mouseUp(button='right')
            #sock.recv(9000)
        except Exception as E:
            print(E)
            if 'WinError' in E:
                break

    conn.close()
