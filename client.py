import socket
import pygame

key_len = 100

def t(s):
    answ = s.replace(' ', 'H')
    delta_l = key_len - len(s)
    answ = answ + 'P' * delta_l
    return answ

print(len(t('abc def')))

print('connecting')
sock = socket.socket()
IP = input('Enter server IP -> ')
print('connecting 2')
sock.connect((IP, 9090))
print('connected')

def send(mail):
    #print(mail)
    sock.send(t(mail).encode())

scr = pygame.display.set_mode([600, 600])
kg = True
while kg:
    mpos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kg = False
        if event.type == pygame.KEYDOWN:
            sock.send(b'prs')
            send(pygame.key.name(event.key))
        if event.type == pygame.KEYUP:
            sock.send(b'rel')
            send(pygame.key.name(event.key))
        if event.type == pygame.MOUSEBUTTONDOWN:
            sock.send(b'mpr')
            send(str(event.button))
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button not in [4, 5]:
                sock.send(b'mrl')
                send(str(event.button))
        if event.type == pygame.MOUSEMOTION:
            sock.send(b'mmv')
            send((str(mpos[0] - 300) + ' ' + str(mpos[1] - 300)))
    pygame.display.update()
    pygame.mouse.set_pos([300, 300])
pygame.quit()
sock.close()
