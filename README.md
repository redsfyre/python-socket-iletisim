# BIL-303 Veri İletişimi Dersi Ödevi

### Python ile socket kullanarak ağ üzerinde veri transferi yapmak

Çalıştırmak için
- `pip3 install -r requirements.txt`.
- ### Server için ( alıcı ):
    - 
        ```
        python3 receiver.py
        ```
- ### Client için ( gönderici ):
    - 
        ```
        C:\> python sender.py --help
        kullanım: sender.py [-h] [-p PORT] file host

        Basit bir dosya aktarıcı

        Zorunlu argümanlar:
        file                  Gönderilecek dosyanın adı
        host                  Alıcının IP adresi

        Opsiyonel argümanlar:
        -h, --help            bu yardım mesajını gösterir ve çıkar
        -p PORT, --port PORT  Kullanılacak port, varsayılan 300
        ```
        Mesela `data.txt` dosyasını `192.168.1.101` adresine göndermek istiyorsanız:
        ```
        python3 sender.py data.txt 192.168.1.101
        ```
## Hata almanız durumunda:
   Cihazınızda python 3+ ve pip kurulu olmadığı müddetçe transferi gerçekleştiremezsiniz.
   
   Buraya kadar gelmenizden python kullandığınızı ve cihazınızda geçerliliğini yitirmek üzere olan python 2.7'nin yerine python 3+ kurulu olduğunu tahmin ediyorum
   
   Linux işletim sistemlerinin yeni sürümlerinde python 3+ ve pip varsayılan olarak kurulu gelebiiyor ancak eğer bu durum sizin için geçerli değilse veya Windows kullanıyor ve pip kurmakta sorun yaşıyorsanız lütfen şu orjinal python dökümantasyonunu kullanın:
   https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip

Debian tabanlı dağıtımlarda:

    $ sudo apt-get update
    $ sudo apt-get install python3-pip
    $ pip3 --version
    
Arch tabanlı dağıtımlarda:

    $ sudo pacman -S python-pip
    $ pip3 --version
