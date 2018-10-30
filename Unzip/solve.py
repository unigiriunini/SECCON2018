import zipfile
import zlib

with zipfile.ZipFile('./flag.zip', 'r') as zf:
    for password in range(1540644768, 1000000000, -1):
        try:
            print(str(password).encode())
            zf.extractall(pwd = str(password).encode())
            print(password)
            break
        except RuntimeError:
            if(password % 10000000 == 0):
                print(password)
            continue
        except zlib.error as e:
            print(e)
            continue
        except zipfile.BadZipFile as e:
            print(e)
            continue
