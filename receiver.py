import socket
import tqdm
import os

# cihazın IP adresi
SERVER_HOST = "192.168.1.56"
SERVER_PORT = 300

# her seferinde 4096 bayt alır
BUFFER_SIZE = 4096

SEPARATOR = "<SEPARATOR>"

# server soketi oluşturur
# TCP socket
s = socket.socket()
# socketi yerel adrese bağla
s.bind((SERVER_HOST, SERVER_PORT))
# sunucunun bağlantıları kabul etmesini sağla
# 5 burada yeni bağlantıları reddetmeden önce sistemin
# izin vereceği kabul edilmemiş bağlantıların sayısıdır
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
# varsa bağlantıyı kabul et
client_socket, address = s.accept() 
# bu kod yürütülürse gönderenin bağlandığı anlamına gelir
print(f"[+] {address} is connected.")

# dosya bilgilerini al
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
filename = os.path.basename(filename)
# integer'e dönüştür
filesize = int(filesize)
#dosyayı soketten almaya ve dosya akışına yazmaya başla
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    for _ in progress:
        # soketten 1024 bayt oku (al)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:    
            # hiçbir şey alınmadı
            # dosya aktarımı tamam
            break
        # az önce aldığımız baytları dosyaya yaz
        f.write(bytes_read)
        # ilerleme çubuğunu güncelle
        progress.update(len(bytes_read))

# alıcı socketi kapat
client_socket.close()
# server socketi kapat
s.close()
