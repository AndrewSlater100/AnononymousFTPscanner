#Scans FTP servers that have no credentials

import ftplib

def anonCreds(host):
    try:
        ftp = ftplib.FTP(host)
        ftp.login('Anonymous')
        print(' FTP Anonymous Login on ' + str(host) + ' was successful.')
        ftp.quit()
        return True
    except Exception:
        print(' FTP Anonymous Login on ' + str(host) + ' has failed.')

        return False
    
if __name__ == '__main__':
    anonCreds('')
