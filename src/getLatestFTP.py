import ftplib
import os
import socket

HOST = 'ftp.objectivasoftware.com'
DIRN = 'ftp.objectivasoftware.com/Training'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print 'Error: cannot reach "%s"' % HOST
        return
    print '*** Connected to host "%s"' % HOST

    try:
        f.login("ftpuser1","write.o7a@bj")
        f.dir()
    except ftplib.error_perm:
        print 'Error: cannot login successfully'
        f.quit()
        return
    print '*** Logged in successfully'

    # try:
    #     f.cwd(DIRN)
    # except ftplib.error_perm:
    #     print 'Error: cannot CD to "%s"' % DIRN
    #     f.quit()
    #     return
    # print '*** Changed to "%s" folder' % DIRN


    f.quit()

main()