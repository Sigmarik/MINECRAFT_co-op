import socket
import pygame

print('connecting')
sock = socket.socket()
sock.connect(('localhost', 9090))
print('connected')

scr = pygame.display.set_mode([600, 600])
kg = True
while kg:
    mpos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kg = False
        if event.type == pygame.KEYDOWN:
            sock.send(b'prs')
            sock.send(pygame.key.name(event.key).encode())
        if event.type == pygame.KEYUP:
            sock.send(b'rel')
            sock.send(pygame.key.name(event.key).encode())
        if event.type == pygame.MOUSEBUTTONDOWN:
            sock.send(b'mpr')
            sock.send(str(event.button).encode())
        if event.type == pygame.MOUSEBUTTONUP:
            sock.send(b'mrl')
            sock.send(str(event.button).encode())
        if event.type == pygame.MOUSEMOTION:
            sock.send(b'mmv')
            sock.send((str(mpos[0] - 300) + ' ' + str(mpos[1] - 300)).encode())
pygame.quit()
sock.close()
