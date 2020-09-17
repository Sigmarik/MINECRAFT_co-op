import socket
from socket import AF_INET, SOCK_DGRAM
import pygame

key_len = 100

def t(s):
    answ = s.replace(' ', 'H')
    delta_l = key_len - len(s)
    answ = answ + 'P' * delta_l
    return answ

print(len(t('abc def')))

print('connecting')
sock = socket.socket(AF_INET, SOCK_DGRAM)
IP = input('Enter server IP -> ')
addr = (IP, 9090)
print('connected')

def send(mail):
    #print(mail)
    sock.sendto(t(mail).encode(), addr)

scr = pygame.display.set_mode([600, 600])
kg = True
while kg:
    mpos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kg = False
        if event.type == pygame.KEYDOWN:
            sock.sendto(b'prs', addr)
            send(pygame.key.name(event.key))
        if event.type == pygame.KEYUP:
            sock.sendto(b'rel', addr)
            send(pygame.key.name(event.key))
        if event.type == pygame.MOUSEBUTTONDOWN:
            sock.sendto(b'mpr', addr)
            send(str(event.button))
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button not in [4, 5]:
                sock.sendto(b'mrl', addr)
                send(str(event.button))
        if event.type == pygame.MOUSEMOTION:
            sock.sendto(b'mmv', addr)
            send((str(mpos[0] - 300) + ' ' + str(mpos[1] - 300)))
    pygame.display.update()
    pygame.mouse.set_pos([300, 300])
pygame.quit()
sock.close()
