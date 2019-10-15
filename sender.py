import socket
import tqdm
import os
import argparse

SEPARATOR = "<SEPARATOR>"

BUFFER_SIZE = 1024 * 4


def send_file(filename, host, port):
    # dosya boyutunu al
    filesize = os.path.getsize(filename)
    # client socketi oluştur
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    # dosya adı ve boyutunu gönder
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # dosyayı göndermeye başla
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        for _ in progress:
            # dosyadaki baytları oku
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # dosya aktarımı yapıldı
                break
            # yoğun ağlarda yayını sağlamak için sendall kullan
            s.sendall(bytes_read)
            # göze hitap etmesi için koyulan ilerleme barını güncelle
            progress.update(len(bytes_read))

    # oluşturulan socketi kapat
    s.close()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Basit bir dosya aktarıcı")
    parser.add_argument("file", help="Gönderilecek dosyanın adı")
    parser.add_argument("host", help="Alıcının IP adresi")
    parser.add_argument("-p", "--port", help="Kullanılacak port, varsayılan 300", default=300)
    args = parser.parse_args()
    filename = args.file
    host = args.host
    port = args.port
    send_file(filename, host, port)
