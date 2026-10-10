isim = ""

def cevap_ver(mesaj):
    global isim
    mesaj = mesaj.lower()

    if "adım" in mesaj:
        isim = mesaj.split()[-1]
        return f"Memnun oldum {isim}! Sana nasıl yardımcı olabilirim?"

    elif "nasılsın" in mesaj:
        return "İyiyim, sen nasılsın?"

    elif "kötüyüm" in mesaj or "canım sıkkın" in mesaj:
        return "Üzgün hissetmene üzüldüm... İstersen anlatabilirsin, seni dinlerim."

    elif "python" in mesaj:
        return "Python öğrenmen harika! Başlangıç seviyesinde misin yoksa proje yapmaya başladın mı?"

    elif "para" in mesaj:
        return "Para kazanmak istiyorsan sana uygulama fikirleri verebilirim. Ne tür şeyler hoşuna gider?"

    elif "sen kimsin" in mesaj:
        return "Ben senin geliştirdiğin akıllı chatbotum 😎"

    elif isim != "":
        return f"{isim}, bunu tam anlayamadım ama biraz daha açıklarsan yardımcı olurum."

    else:
        return "Bunu tam anlayamadım ama biraz daha açık yazabilir misin?"
    

while True:
    kullanici = input("Sen: ")  
    if kullanici.lower()=="çıkış":
        print("Bot:Görüşürüz!")
        break
    cevap = cevap_ver(kullanici)
    print("Bot:", cevap)

