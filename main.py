import random
while True:
    # Kullanıcıdan isminin alınması
    name = input('Adınızı giriniz: ')
    # Oyun başlangıcı mesajının yazdırılması
    print('Merhaba ' + name + '. Gizli yazılmış şehri bul ve karakteri asılmaktan kurtar!')
    # Şehirler listesi
    sehirler = ['adana', 'adıyaman', 'afyonkarahisar', 'ağrı', 'aksaray', 'amasya', 'ankara', 'antalya', 'ardahan', 'artvin', 'aydın', 'balıkesir', 'bartın', 'batman', 'bayburt', 'bilecik', 'bingöl', 'bitlis', 'bolu', 'burdur', 'bursa', 'çanakkale', 'çankırı', 'çorum', 'denizli', 'diyarbakır', 'düzce', 'edirne', 'elazığ', 'erzincan', 'erzurum', 'eskişehir', 'gaziantep', 'giresun', 'gümüşhane', 'hakkari', 'hatay', 'ığdır', 'ısparta', 'istanbul', 'izmir', 'kahramanmaraş', 'karabük', 'karaman', 'kars', 'kastamonu', 'kayseri', 'kilis', 'kırıkkale', 'kırklareli', 'kırşehir', 'kocaeli', 'konya', 'kütahya', 'malatya', 'manisa', 'mardin', 'mersin', 'muğla', 'muş', 'nevşehir', 'niğde', 'ordu', 'osmaniye', 'rize', 'sakarya', 'samsun', 'şanlıurfa', 'siirt', 'sinop', 'sivas', 'şırnak', 'tekirdağ', 'tokat', 'trabzon', 'tunceli', 'uşak', 'van', 'yalova', 'yozgat', 'zonguldak']
    # Rastgele bir şehir seçimi
    sehir = random.choice(sehirler)
    # Girilen harflerin tutulacağı değişken
    girilen_harfler = ''
    # Can sayısı
    can = 10
    # Oyun döngüsü
    while can > 0:
        tahmin_edilecek_kalan_harf = 0
        # Seçilen şehir için harflerin kontrolü ve yazdırılması
        for harf in sehir:
            if harf in girilen_harfler:
                print(harf, end=' ')
            else:
                print('-', end=' ')
                tahmin_edilecek_kalan_harf += 1
        print('\n')
        # Kazanma durumu kontrolü
        if tahmin_edilecek_kalan_harf == 0:
            print('KAZANDIN!!!')
            break
        # Tahminin alınması
        tahmin = input('Küçük harf giriniz: ')
        girilen_harfler += tahmin
        # Hatalı tahmin durumu ve can sayısının azaltılması
        if tahmin not in sehir:
            can -= 1
            print(f'Karakterin {can} canı kaldı')
        # Kaybetme durumu
        if can == 0:
            print('Karakter öldü!')
            print(f"Şehrin adı: {sehir}")
    # Yeni oyun seçeneği
    devam = input('Yeni oyun oynamak istiyor musunuz? (evet/hayır): ')
    if devam.lower() == 'hayır':
        break
