import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'Merhaba! Bana hava kirliliği hakkında istdiğini sor!')
    elif  message.content.startswith('hava kirliliği nedir'):
        cevap1="""Hava kirliliği, canlıların sağlığını olumsuz yönde etkileyen ve havadaki yabancı maddelerin, normalin üzerinde miktar ve yoğunluğa ulaşmasıdır. Hava kirliliği; havada katı, sıvı ve gaz şeklindeki yabancı maddelerin insan sağlığına, canlı hayatına ve ekolojik dengeye zarar verecek miktar, yoğunluk ve uzun sürede atmosferde bulunmasıdır. İnsanların çeşitli faaliyetleri sonucu meydana gelen üretim ve tüketim aktiviteleri sırasında ortaya çıkan atıklarla hava tabakası kirlenerek, yeryüzündeki canlı hayatını olumsuz yönde etkilemektedir.Hava kirliliği yüzünden her sene 7 milyon kişi ölmekte."""
        await message.channel.send(cevap1)
    elif  message.content.startswith("Hava kirliliğini önlemek için alınabilecek tedbirler?"):
        cevap2 = """
        Hükûmet
Kentlerde kömür kullanımı yasaklanmalı
Kömür santraller kapatılmalı
İnsanlar toplu taşımacılığa özendirilmeli, elektrikli toplu ulaşım araçlarında kullanılması yaygınlaştırılmalı
Kentlerde arabaların egzozlarından kaynaklanan kirliliğin azaltılması için önlemler alınmalıdır.
Karbon piyasası ya da vergisi yaratılmalı
Sanayi tesislerinin bacalarına filtre takılması sağlanmalı, ayrıca sanayi kuruluşları yer seçimi düzenli yapılmalı,
Günlük Hayatta
Kentlerde kömür kullanılmamalı
Kentlerde ya yürümeye ya bisiklet ya da elektrikli araçlar kullanılmalı"""
        await message.channel.send(cevap2)

    elif  message.content.startswith("hava kirliliğinin sonuçları nelerdir?"):
        cevap3 = """Kirli hava, insanlarda solunum yolu hastalıklarının artmasına sebep olmaktadır.[7] Örneğin; kurşunun kan hücrelerinin gelişmesini ve olgunlaşmasını engellediği, kanda ve idrarda birikerek sağlığı olumsuz yönde etkilediği, karbon monoksit (CO)'in ise, kandaki hemoglobin ile birleşerek oksijen taşınmasını aksattığı bilinmektedir. Bununla birlikte kükürt dioksit (SO2)'in, üst solunum yollarında keskin, boğucu ve tahriş edici etkileri vardır. Özellikle duman akciğerden alveollere kadar girerek olumsuz etki yapmaktadır. Cilt hastalıkları, saç dökülmesi, akciğer hastalıkları ve kansere yol açtığı somut bir gerçektir.[8] Ayrıca kükürt dioksit ve ozon bitkiler için zararlı olup; özellikle ozon, ürün kayıplarına sebep olmakta ve ormanlara zarar vermektedir. Kirli hava kilo yapar [9] ve genleri etkiler.[10] Azot dioksit(NO2) çocuklarda astım ve akciğer hastalıklarına yol açabiliyor.[11]

Sanayi, endüstri ve ısınmada kullanılan fosil yakıtlar ile ormanların tahribi ve arazi değişmesi sonucu, atmosferdeki karbondioksit miktarının %5 oranında arttığı tespit edilmiştir. Bunun ise küresel ısınmaya yol açabileceği öngörülmektedir.

300 milyon çocuk 'zehir soluyor'."""
        await message.channel.send(cevap3)

        elif  message.content.startswith("Hava kirliliği kaynakları nedir?"):
        cevap4 = """Isınmadan kaynaklanan hava kirliliği
Isınma amaçlı, düşük kalorili ve kükürt oranı yüksek kömürlerin [4] yaygın olarak kullanılması ve yanlış yakma tekniklerinin[kaynak belirtilmeli] uygulanması hava kirliliğine yol açar.

Motorlu taşıtlardan kaynaklanan hava kirliliği
Ayrıca bakınız: Türkiye'de çevre sorunları
Nüfus artışı ve gelir düzeyinin yükselmesine paralel olarak, sayısı hızla artan motorlu taşıtlardan çıkan egzoz gazları, hava kirliliğinde önemli bir faktör oluşturmaktadır, mesela partikül [5] ve azot dioksit.

Sanayiden kaynaklanan hava kirliliği
Sanayi tesislerinin kuruluşunda yanlış yer seçimi, çevrenin korunması açısından gerekli tedbirlerin alınmaması (baca filtresi, arıtma tesisi olmaması vb.), uygun teknolojilerin kullanılmaması, enerji üreten yakma ünitelerinde vasıfsız ve yüksek kükürtlü yakıtların kullanılması, hava kirliliğine sebep olur."""

        await message.channel.send(cevap4)

        
client.run("")
