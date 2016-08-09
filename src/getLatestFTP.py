import ftplib
import os
import socket

HOST = ''
DIRN = ''
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print 'Error: cannot reach "%s"' % HOST
        return
    print '*** Connected to host "%s"' % HOST

    try:
        f.login("user","passwd")
        f.dir()
    except ftplib.error_perm:
        print 'Error: cannot login successfully'
        f.quit()
        return
    print '*** Logged in successfully'

    try:
        f.cwd("")
        f.retrlines("LIST")
        f.retrbinary('RETR filename', open('filename','wb').write)
    except ftplib.error_perm:
        f.quit();
        return
    # try:
    #     f.cwd(DIRN)
    # except ftplib.error_perm:
    #     print 'Error: cannot CD to "%s"' % DIRN
    #     f.quit()
    #     return
    # print '*** Changed to "%s" folder' % DIRN


    f.quit()

main()