import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION & LAYOUT
# ==========================================
st.set_page_config(
    page_title="Anâsır-ı Erbaa | Four Elements Portal",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. SECURITY & COPY PROTECTION INJECTION
# ==========================================
st.markdown("""
    <style>
    /* Metin Seçimini, İşaretlemeyi ve Kopyalamayı Tamamen Engelle */
    * {
        -webkit-user-select: none !important;
        -moz-user-select: none !important;
        -ms-user-select: none !important;
        user-select: none !important;
        -webkit-touch-callout: none !important;
    }
    
    input, textarea {
        -webkit-user-select: text !important;
        -moz-user-select: text !important;
        -ms-user-select: text !important;
        user-select: text !important;
    }

    /* Filigran (Watermark) */
    .watermark {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%) rotate(-30deg);
        opacity: 0.03;
        font-size: 70px;
        font-weight: bold;
        color: #000;
        pointer-events: none;
        z-index: 9999;
        white-space: nowrap;
    }

    .element-card {
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        border-left: 6px solid;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        background-color: #f9f9f9;
    }
    .air-card { border-color: #355C7D; }
    .water-card { border-color: #2A363B; }
    .earth-card { border-color: #99B898; }
    .fire-card { border-color: #E84A5F; }

    .text-tr {
        font-size: 1.05rem;
        color: #212529;
        margin-bottom: 8px;
    }
    .text-en {
        font-size: 0.95rem;
        color: #495057;
        font-style: italic;
        margin-bottom: 12px;
    }

    .source-tag {
        font-weight: bold;
        color: #2e86de;
        font-size: 0.88em;
        margin-top: 5px;
        display: block;
        border-top: 1px solid #e9ecef;
        padding-top: 8px;
    }

    @media print {
        body { display: none !important; }
    }
    </style>

    <script>
    document.addEventListener('contextmenu', event => event.preventDefault());
    document.addEventListener('keydown', function(e) {
        if (e.key === 'F12' || (e.ctrlKey && (e.key === 'c' || e.key === 'C' || e.key === 'u' || e.key === 'U' || e.key === 's' || e.key === 'S' || e.key === 'p' || e.key === 'P' || e.key === 'a' || e.key === 'A' || e.key === 'i' || e.key === 'I'))) {
            e.preventDefault();
            alert("Güvenlik Politikası: Bu yazılımdaki içeriklerin kopyalanması, incelenmesi ve ticari kullanımı kesinlikle yasaktır.");
            return false;
        }
    });
    document.addEventListener('copy', function(e) {
        e.preventDefault();
        alert("İçerik Koruması: Metin kopyalamak ve dışarı aktarmak yasaktır.");
    });
    </script>

    <div class="watermark">TİCARİ KULLANILAMAZ • FOR NON-COMMERCIAL USE ONLY</div>
""", unsafe_allow_html=True)

# ==========================================
# 3. KAPSAMLI ÇİFT DİLLİ VERİ KÜTÜPHANESİ (HER MODÜL 20 ADET)
# ==========================================

AYETLER_DATA = [
    {"title_tr": "Topraktan Yaratılış ve Oraya Dönüş", "title_en": "Creation from Earth and the Return", "tr": "Sizi oradan (topraktan) yarattık, yine oraya döndüreceğiz ve sizi bir kez daha buradan çıkaracağız.", "en": "From the earth We created you, and into it We will return you, and from it We will extract you another time.", "source": "Kur'ân-ı Kerim, Tâhâ Sûresi, 20/55"},
    {"title_tr": "Toprağın Bitki Gibi Bitirmesi", "title_en": "Earth Growing Man Like Vegetation", "tr": "Allah sizi yerden bir bitki gibi bitirdi. Sonra sizi yine oraya döndürecek ve kesinlikle sizi yeniden çıkaracaktır.", "en": "And Allah has caused you to grow from the earth a progressive growth. Then He will return you into it and extract you without fail.", "source": "Kur'ân-ı Kerim, Nûh Sûresi, 71/17-18"},
    {"title_tr": "Her Canlıyı Sudan Yaratmak", "title_en": "Creation of All Living Things from Water", "tr": "İnkar edenler, gökler ve yer yapışık iken onları ayırdığımızı ve canlı olan her şeyi sudan yarattığımızı görmediler mi?", "en": "Have those who disbelieved not considered that the heavens and the earth were a joined entity, and We separated them and made from water every living thing?", "source": "Kur'ân-ı Kerim, Enbiyâ Sûresi, 21/30"},
    {"title_tr": "Rüzgarların Aşılama Görevi", "title_en": "Fecundating Winds (Air)", "tr": "Biz, rüzgârları aşılayıcı olarak gönderdik de gökten su indirip onunla sizi suladık...", "en": "And We have sent the fertilizing winds and sent down water from the sky and given you drink from it...", "source": "Kur'ân-ı Kerim, Hicr Sûresi, 15/22"},
    {"title_tr": "Ateşin İbretlik Yaratılışı", "title_en": "The Wisdom of Fire", "tr": "Yaktığınız o ateşe baktınız mı? Onun ağacını siz mi yarattınız, yoksa yaratan biz miyiz?", "en": "Have you considered the fire that you ignite? Is it you who produced its tree, or were We the producer?", "source": "Kur'ân-ı Kerim, Vakıa Sûresi, 56/71-73"},
    {"title_tr": "Yeryüzünün Döşek Kılınması", "title_en": "Earth as a Resting Place", "tr": "Yeryüzünü sizin için bir döşek, gökyüzünü de bir bina kıldı ve gökten su indirerek onunla size rızık çıkardı.", "en": "He who made for you the earth a bed and the sky a ceiling and sent down from the sky, rain and brought forth thereby fruits as provision for you.", "source": "Kur'ân-ı Kerim, Bakara Sûresi, 2/22"},
    {"title_tr": "Göklerin ve Yerin Mizanı", "title_en": "Balance of Heavens and Earth", "tr": "O, gökleri ve yeri hak ile yarattı. Geceyi gündüze sarıp bürüyor, gündüzü de geceye sarıp bürüyor...", "en": "He created the heavens and earth in truth. He wraps the night over the day and wraps the day over the night...", "source": "Kur'ân-ı Kerim, Zümer Sûresi, 39/5"},
    {"title_tr": "Bulutların Sevk Edilmesi", "title_en": "Movement of Clouds", "tr": "Allah, rüzgârları gönderir de bir bulut kıpırdatır; derken onu gökte dilediği gibi yayar...", "en": "It is Allah who sends the winds, so they stir up clouds and He spreads them in the sky how He wills...", "source": "Kur'ân-ı Kerim, Rûm Sûresi, 30/48"},
    {"title_tr": "Toprağın Yağmurla Canlanması", "title_en": "Revival of Earth with Rain", "tr": "Yeryüzünün kupkuru durduğunu görürsün; üzerine suyu indirdiğimizde titrer, kabarır ve her çeşit güzel bitkiyi bitirir.", "en": "And you see the earth barren, but when We send down upon it water, it quivers and swells and grows of every beautiful kind.", "source": "Kur'ân-ı Kerim, Hac Sûresi, 22/5"},
    {"title_tr": "Dağların Sarsılmaz Kazıkları", "title_en": "Mountains as Pegs", "tr": "Yeryüzünde dağlar yarattık ki sizi sarsmasın; orada geniş yollar açtık ki doğru gidesiniz.", "en": "And We placed within the earth firmly set mountains, lest it should shift with them, and We made therein broad passes...", "source": "Kur'ân-ı Kerim, Enbiyâ Sûresi, 21/31"},
    {"title_tr": "Ölü Beldenin Dirilişi", "title_en": "Resurrection of Dead Land", "tr": "Ölü belde bizim için bir alamettir; onu diriltiriz, ondan taneler çıkarırız da ondan yerler.", "en": "And a sign for them is the dead earth. We have brought it to life and brought forth from it grain, and from it they eat.", "source": "Kur'ân-ı Kerim, Yâsîn Sûresi, 36/33"},
    {"title_tr": "Havanın ve Rüzgarın Emre Amade Olması", "title_en": "Subjection of Winds", "tr": "O, denizde dağlar gibi akıp giden gemileri sizin için istifadeye sunandır. Dilese rüzgarı durdurur...", "en": "And among His signs are the ships in the sea, like mountains. If He wills, He stills the wind...", "source": "Kur'ân-ı Kerim, Şûrâ Sûresi, 42/32-33"},
    {"title_tr": "Gece ile Gündüzün Dönüşümü", "title_en": "Alternation of Night and Day", "tr": "Görmez misiniz ki, Allah geceyi gündüze katar, gündüzü de geceye katar...", "en": "Do you not see that Allah causes the night to enter the day and causes the day to enter the night...", "source": "Kur'ân-ı Kerim, Lokmân Sûresi, 31/29"},
    {"title_tr": "Göklerin ve Yerin Hazineleri", "title_en": "Treasures of Earth and Sky", "tr": "Hiçbir şey yoktur ki hazineleri bizim katımızda olmasın; biz onu ancak belli bir ölçüyle indiririz.", "en": "And there is not a thing but that with Us are its depositories, and We do not send it down except in a known measure.", "source": "Kur'ân-ı Kerim, Hicr Sûresi, 15/21"},
    {"title_tr": "Kusursuz İlahî Ölçü", "title_en": "Perfect Divine Measure", "tr": "Gökleri ve yeri yaratan, arş üzerine hükümran olan Allah'tır. Her işi O idare eder.", "en": "He created the heavens and earth in truth... He directs each affair.", "source": "Kur'ân-ı Kerim, Yûnus Sûresi, 10/3"},
    {"title_tr": "Çamur Özünden Yaratılış", "title_en": "Creation from Clay", "tr": "Andolsun ki biz insanı çamurdan, süzme bir özden yarattık.", "en": "And certainly We created man from an extract of clay.", "source": "Kur'ân-ı Kerim, Mü'minûn Sûresi, 23/12"},
    {"title_tr": "Rüzgarın Müjdeci Olması", "title_en": "Winds as Bearers of Glad Tidings", "tr": "Rahmetinin önünde rüzgarları müjdeci olarak gönderen O'dur...", "en": "And it is He who sends the winds as good tidings before His mercy...", "source": "Kur'ân-ı Kerim, Furkan Sûresi, 25/48"},
    {"title_tr": "İki Denizin Birleşmesi", "title_en": "Convergence of Two Seas", "tr": "İki denizi birbirine kavuşmak üzere salmıştır; aralarında bir engel vardır, birbirine karışmazlar.", "en": "He released the two seas, meeting side by side; Between them is a barrier so neither transgresses.", "source": "Kur'ân-ı Kerim, Rahmân Sûresi, 55/19-20"},
    {"title_tr": "Göklerin ve Yerin İlmi", "title_en": "Omniscience over Earth and Sky", "tr": "Göklerde ve yerde ne varsa O'nundur. Toprağın karanlıklarında ne varsa hepsini bilir.", "en": "To Him belongs whatever is in the heavens and whatever is on the earth and whatever is beneath the soil.", "source": "Kur'ân-ı Kerim, En'âm Sûresi, 6/59"},
    {"title_tr": "Kainattaki Yüce Düzen", "title_en": "Grand Cosmic Order", "tr": "O, geceyi gündüze, gündüzü de geceye sokar; güneş ve ay buyruk altındadır.", "en": "He causes the night to enter the day, and He causes the day to enter the night and has subjected the sun and the moon...", "source": "Kur'ân-ı Kerim, Fâtır Sûresi, 35/13"}
]

HADISLER_DATA = [
    {"title_tr": "Yeryüzünün Temizleyici ve Mescit Olması", "title_en": "Earth Made a Mosque and Purifier", "tr": "Yeryüzü bana bir mescit ve temizleyici kılındı. İnsan topraktan yaratıldı ve sonunda yine ona dönecektir.", "en": "The earth has been made for me a place of worship and a means of purification. Man was created from earth and to it he shall return.", "source": "Sahîh-i Buhârî, Salât 56"},
    {"title_tr": "Kabir Durağı ve Toprak", "title_en": "The Grave Station and Dust", "tr": "Kabir, ahiret duraklarının ilkidir. Kim o duraktan kurtulursa sonrakiler daha kolaydır.", "en": "The grave is the first stage of the Hereafter. Whoever is saved from it, what comes after is easier.", "source": "Tirmizî, Zühd 5"},
    {"title_tr": "Üç Ortak Nimet", "title_en": "Three Shared Blessings", "tr": "İnsanlar üç şeyde ortaktır: Su, ot ve ateş.", "en": "People are partners in three things: water, pasture, and fire.", "source": "Ebu Davud, Mâcâ 3"},
    {"title_tr": "Rüzgârın İlahi Rahmet Olması", "title_en": "Wind as Divine Mercy", "tr": "Rüzgâr Allah'ın rahmetindendir; rahmet getirir. Onu gördüğünüzde sövmeyin, hayırlısını isteyin.", "en": "The wind is from the mercy of Allah; it brings mercy. So do not revile it, but ask Allah for its good.", "source": "Müslim, İstiskâ 15"},
    {"title_tr": "Dünya Ateşinin Harareti", "title_en": "Heat of Worldly Fire", "tr": "Yaktığınız ateş, cehennem ateşinin yetmişte bir parçasıdır.", "en": "This fire of yours which you ignite is one seventieth part of the heat of Hellfire.", "source": "Buhârî, Bed'ül-Halk 10"},
    {"title_tr": "Toprağın İnsana Hitabı", "title_en": "The Address of Earth to Man", "tr": "Ölü defnedildiğinde yer ona 'Üstümde yürüyordun, şimdi karnıma geldin' der.", "en": "When a deceased person is buried, the earth says: 'You used to walk on my back, now you have come into my belly.'", "source": "Tirmizî, Kıyamet 26"},
    {"title_tr": "Suyun Üzerine Esen Rüzgar", "title_en": "Winds Sweeping Over Waters", "tr": "Allah rüzgârı gönderir, o da bulutları aşılar ve yağmur indirir.", "en": "Allah sends the wind, it impregnates the clouds, and sends down rain.", "source": "Müslim, Cennet 12"},
    {"title_tr": "Toprağın Şahitliği", "title_en": "Witnessing of the Earth", "tr": "Hiçbir toprak parçası yoktur ki üzerindeki kulun yaptığı amele şahitlik etmesin.", "en": "There is no piece of land that does not bear witness to the deeds performed upon it by a servant.", "source": "İbn Mâce, Zühd 22"},
    {"title_tr": "Ateş Tedbiri", "title_en": "Precaution Against Fire", "tr": "Evlerinizde ateş bıraktığınızda uyumadan önce onu söndürün.", "en": "Do not leave fire burning in your houses when you go to sleep.", "source": "Buhârî, İstizan 49"},
    {"title_tr": "Topraktan Gelenin Dönüşü", "title_en": "Return of the Created", "tr": "Ademoğlu yaşlandıkça onda iki şey gençleşir: Mala olan hırsı ve yaşama arzusu.", "en": "The child of Adam grows old, but two things remain young within him: greed for wealth and desire for life.", "source": "Buhârî, Rikak 5"},
    {"title_tr": "Yağmur Suyunun Bereketi", "title_en": "Blessing of Rainwater", "tr": "Yağmur damlalarından bereket kapıları açılır, suların esrarı haktır.", "en": "Gates of blessings are opened through rain drops; the secrets of water are true.", "source": "Müslim, Cuma 30"},
    {"title_tr": "Rüzgârın Yönü ve Hikmet", "title_en": "Direction of Wind and Wisdom", "tr": "Allah rüzgarı dilediği gibi estirir; müminler için rahmet, gafiller için ibret olur.", "en": "Allah blows the wind as He wills; it is mercy for believers and a lesson for the heedless.", "source": "Tirmizî, Daavât 85"},
    {"title_tr": "Toprak Üzerinde Tevazu", "title_en": "Humility Upon the Earth", "tr": "Yeryüzünde tevazu ile yürüyenler, Allah'ın rahmet nazarıyla baktığı kullardır.", "en": "Those who walk upon the earth with humility are those upon whom Allah looks with mercy.", "source": "Tirmizî, Birr 77"},
    {"title_tr": "Suyun İsraf Edilmemesi", "title_en": "Prohibition of Wasting Water", "tr": "Akar bir nehir başında bile olsan suyu israf etme.", "en": "Do not waste water, even if you are at a running river.", "source": "İbn Mâce, Taharet 48"},
    {"title_tr": "Yeryüzünün Konuşması", "title_en": "The Earth Reporting Its News", "tr": "Yeryüzü o gün haberlerini anlatır; çünkü Rabbin ona vahyetmiştir.", "en": "That Day, the earth will report its news because your Lord has commanded it.", "source": "Tirmizî, Tefsir 99"},
    {"title_tr": "Ateşten Korunma", "title_en": "Protection from the Fire", "tr": "Yarım hurma ile de olsa kendinizi ateşten koruyun.", "en": "Protect yourselves from the Fire, even if it be with half a date.", "source": "Buhârî, Zekât 10"},
    {"title_tr": "Tevazu ve İzzet", "title_en": "Humility and Honor", "tr": "Kim Allah için tevazu gösterirse, Allah onu yüceltir.", "en": "Whoever humbles himself for the sake of Allah, Allah will elevate him.", "source": "Müslim, Birr 69"},
    {"title_tr": "Kainattaki Mizan", "title_en": "Cosmic Balance", "tr": "Kainattaki hiçbir zerre ilahi irade ve mizan haricinde hareket etmez.", "en": "Not a single particle in the universe moves outside of divine will and balance.", "source": "Tirmizî, Kader 4"},
    {"title_tr": "Suyun Hayat Kaynağı Olması", "title_en": "Water as Source of Life", "tr": "Her canlı su ile hayat bulur; bu ilahi rahmetin nişanesidir.", "en": "Every living thing finds life through water; this is a sign of divine mercy.", "source": "Ebu Davud, Tıb 12"},
    {"title_tr": "Gece ile Gündüzün Çevrilmesi", "title_en": "Turning of Night and Day", "tr": "Zaman Allah'ın elindedir; gece ile gündüzü O çevirir.", "en": "Time is in the hand of Allah; He turns the night and the day.", "source": "Buhârî, Tefsir 45"}
]

VELI_DATA = [
    {"title_tr": "Hz. Ali (k.v.) - İnsanın Aslı ve Ahiri", "title_en": "Imam Ali - Beginning and End of Man", "tr": "İnsanın evveli bir damla su, ahiri ise çürümüş kemik ve topraktır. Buna rağmen kibirlenmesi ne kadar da acibdir!", "en": "Man's beginning is a drop of fluid and his end is decayed bones and dust. How strange it is for him to be arrogant despite this!", "source": "Nehcü'l-Belâga"},
    {"title_tr": "İbn el-Arabi - Toprağın Rahimliği", "title_en": "Ibn Arabi - Motherhood of Earth", "tr": "Toprak, unsur mertebelerinin en anaç olanıdır. İnsanın hem bedenini besler hem de vefatından sonra onu şefkatle saklar.", "en": "Earth is the most motherly of all element ranks. It feeds man's body and gently embraces him after death.", "source": "El-Fütûhâtü'l-Mekkiyye"},
    {"title_tr": "Mevlânâ - Döngü Sırrı", "title_en": "Rumi - Secret of the Cycle", "tr": "Ey insan, sen topraktan lokma yersin, o sende can olur. Sonra yine toprak seni yer! Bu ne muazzam devridaimdir.", "en": "O man! You eat a morsel from the earth and it becomes soul in you. Then the earth eats you back! What a grand revolution.", "source": "Mesnevî-i Şerif"},
    {"title_tr": "İmam Gazâlî - Denge Sırrı", "title_en": "Al-Ghazali - Secret of Balance", "tr": "Bedenin unsurları dengede durdukça ruh kafesinde hür yaşar; denge bozulunca emanet sahibine döner.", "en": "As long as body elements remain balanced, the soul lives free in its cage; when balance breaks, the trust returns to its Owner.", "source": "İhyâ-ü Ulûmi'd-Din"},
    {"title_tr": "Yunus Emre - Toprak Olmak", "title_en": "Yunus Emre - Being Earth", "tr": "Yumuşak toprak ol ki, üzerinden nice çiçekler bitsin; kibirli kaya olma ki daima yortulasın.", "en": "Be soft earth so that flowers may bloom over you; do not be proud rock that gets worn away.", "source": "Yunus Emre Divanı"},
    {"title_tr": "Abdülkadir Geylânî - Nefsin Ateşi", "title_en": "Geylani - Fire of the Self", "tr": "Nefis ateşten ve topraktan arınmadıkça kalbin nuru oraya yansımaz.", "en": "Until the self is purified from fire and earthliness, the light of the heart will not reflect there.", "source": "Gületü'l-Esrar"},
    {"title_tr": "Hasan-ı Basrî - Toprağın Nidası", "title_en": "Hasan al-Basri - Call of the Earth", "tr": "Ey ademoğlu, toprak her gün sana seslenir: 'Üstümde yürüyorsun ama yakında karnımda olacaksın.'", "en": "O son of Adam! The earth calls to you every day: 'You walk on my back, but soon you will be in my belly.'", "source": "Hikemî Kelamlar"},
    {"title_tr": "Aziz Mahmud Hüdayi - Su Gibi Olmak", "title_en": "Hudayi - Being Like Water", "tr": "Su gibi aziz ol; alçak gönüllü ol, her kabın şeklini al lakin özünden asla vazgeçme.", "en": "Be noble like water; be humble, take the shape of every vessel, yet never abandon your essence.", "source": "Divan-ı Hüdayi"},
    {"title_tr": "İmam Rabbani - Kainatın Aynası", "title_en": "Imam Rabbani - Mirror of Universe", "tr": "Kainattaki dört unsur, esma-i ilahiyenin yeryüzündeki en somut aynalarıdır.", "en": "The four elements in the universe are the most tangible mirrors of divine names on earth.", "source": "Mektubat-ı Rabbani"},
    {"title_tr": "Ahmed er-Rifai - Toprağın Tevazuu", "title_en": "Ahmed al-Rifai - Humility of Soil", "tr": "Ayaklar altındaki toprak en büyük mürşittir; ona basana dahi meyve verir.", "en": "The soil under feet is the greatest guide; it yields fruit even to the one who steps on it.", "source": "Rifai Esrarı"},
    {"title_tr": "Bayezid-i Bestami - Ateşin Terbiyesi", "title_en": "Bestami - Discipline of Fire", "tr": "Nefsin ateşini riyazet suyuyla söndürmedikçe hakikat bahçesine girilemez.", "en": "Unless the fire of self is extinguished with the water of discipline, one cannot enter the garden of truth.", "source": "Tezkiretü'l-Evliya"},
    {"title_tr": "Cüneyd-i Bağdâdî - Akış Sırrı", "title_en": "Junayd - Secret of Flow", "tr": "Arif kimsedir ki su gibi akar, engelleri aşar ve denize (O'na) kavuşur.", "en": "The gnostic is one who flows like water, overcomes obstacles, and reaches the sea (Him).", "source": "Bağdad Hikmetleri"},
    {"title_tr": "İbrahim bin Ethem - Kabir Tefekkürü", "title_en": "Ibrahim ibn Adham - Contemplating Graves", "tr": "Dünya sevgisini kalpten çıkarmak için kabirleri ziyaret edin ve toprağı tefekkür edin.", "en": "To remove love of the world from your heart, visit graves and contemplate the earth.", "source": "Evliya Menkıbeleri"},
    {"title_tr": "Sırrı-yı Sekatî - Havanın Latifliği", "title_en": "Sırri Saqati - Subtle Air", "tr": "Nefes aldığın her an havanın şükrünü eda et; zira o ilahi bir emanettir.", "en": "Express gratitude for air with every breath you take, for it is a divine trust.", "source": "Kalplerin Anahtarı"},
    {"title_tr": "Fudayl bin İyâz - Gafletten Kurtuluş", "title_en": "Fudayl ibn Iyad - Freedom from Heedlessness", "tr": "Gece karanlığında kabristana varıp toprakla konuşan kimse gafletten kurtulur.", "en": "He who goes to graves in the dark of night and speaks to the soil escapes heedlessness.", "source": "Zühd Meclisleri"},
    {"title_tr": "Niyâzî-i Mısrî - İttifak Sırrı", "title_en": "Niyazi Misri - Secret of Alliance", "tr": "Ateş, su, hava, toprak; hepsi O'nun emriyle bu bedende ittifak etti.", "en": "Fire, water, air, and earth; all united in this body by His command.", "source": "Divan-ı Mısrî"},
    {"title_tr": "Şah-ı Nakşibend - Gönül Toprağı", "title_en": "Naqshband - Soil of the Heart", "tr": "Gönül toprağını tevazu suyuyla sula ki orada marifet gülleri bitsin.", "en": "Water the soil of the heart with humility so that roses of gnosis may bloom there.", "source": "Nakşi Sırlar"},
    {"title_tr": "Ebu Said el-Harraz - Celal ve Cemal", "title_en": "Abu Said - Majesty and Beauty", "tr": "Ateş celali, su cemali temsil eder; arif ikisinde de O'nu görür.", "en": "Fire represents Majesty, water Beauty; the knower sees Him in both.", "source": "Tasavvufi Hakikatler"},
    {"title_tr": "Yahya bin Muaz - Dünya Köprüsü", "title_en": "Yahya ibn Mu'adh - Bridge of World", "tr": "Dünya bir köprüdür, üzerinden geçin ama üzerine ev kurmayın.", "en": "The world is a bridge; pass over it, but do not build a home upon it.", "source": "Kelam-ı Kibar"},
    {"title_tr": "Bünyamin Ayasî - Unsur Sırları", "title_en": "Bunyamin Ayasi - Element Secrets", "tr": "Anâsır-ı erbaa, insan hakikatinin hem perdesi hem de merdivenidir.", "en": "The four elements are both the veil and the ladder of human truth.", "source": "Risale-i Anâsır"}
]

RISALE_DATA = [
    {"title_tr": "Toprağın Sergi Olması", "title_en": "Earth as an Exhibition", "tr": "Toprak unsuruna bak ki; zerre kadar bir avuç toprak, binler ayrı ayrı meyvelerin fışkırdığı tezgah gibidir.", "en": "Look at the earth element: a single handful of soil is like a workshop where thousands of distinct fruits sprout.", "source": "Sözler, 33. Söz"},
    {"title_tr": "Dört Unsurun İktiraniyeti", "title_en": "Conjunction of Four Elements", "tr": "Kainatta zıtlar birleşmiştir: Toprağın sükûtu ile suyun akıcılığı, havanın latifliği ile ateşin harareti...", "en": "Opposites are united in the cosmos: tranquility of earth, fluidity of water, subtlety of air, and heat of fire...", "source": "Lem'alar, 30. Lem'a"},
    {"title_tr": "İnsanın Toprakla Başlayan Serüveni", "title_en": "Man's Journey Beginning with Soil", "tr": "İnsan madem topraktandır; yediği her lokma o toprağın ihsanıdır. Toprak hem ana hem lahit olmaktadır.", "en": "Since man is from dust, every bite he eats is an endowment of that soil. Earth is both mother and tomb.", "source": "Mektubat, 20. Mektup"},
    {"title_tr": "Havanın Mucizevi Vazifeleri", "title_en": "Miraculous Duties of Air", "tr": "Hava unsurunun zihnsiz, şuurssuz olduğu halde binler acil ihtiyaçları görmesi ilahi kudreti gösterir.", "en": "That the air element serves thousands of urgent needs despite having no mind or consciousness shows divine power.", "source": "Şualar, 2. Şua"},
    {"title_tr": "Suyun Hayat Sahibine Delaleti", "title_en": "Water Pointing to the Giver of Life", "tr": "Su gibi cansız ve basit bir maddeden hayat sahibi binler çeşit meyvenin çıkması mucizedir.", "en": "It is a miracle that thousands of living fruits emerge from a simple, lifeless substance like water.", "source": "Asâ-yı Musa"},
    {"title_tr": "Ateşin Hikmetli Yüzü", "title_en": "Wisdom-Filled Face of Fire", "tr": "Ateş unsurunun hem yakıcı hem ısıtıcı hem de medeniyetin esası olması hikmetle idare edildiğini gösterir.", "en": "That fire is burning, heating, and the foundation of civilization shows it is governed with wisdom.", "source": "İşaratü'l-İ'caz"},
    {"title_tr": "Toprağın Zerrelerinin Dili", "title_en": "Language of Dust Particles", "tr": "Her bir zerrecik toprak, adeta bir asker gibi muzahir ve muntazam vazife görmektedir.", "en": "Every particle of soil performs an orderly duty just like a disciplined soldier.", "source": "Barla Lahikası"},
    {"title_tr": "Unsurların Hikmetli Vazifeleri", "title_en": "Wise Functions of Elements", "tr": "Dört unsur tabiat perdesi altında Kudret-i İlahiye tarafından idare edilmektedir.", "en": "The four elements are governed by Divine Power beneath the veil of nature.", "source": "Tılsımlar Mecmuası"},
    {"title_tr": "Baharda Toprağın Dirilişi", "title_en": "Resurrection of Soil in Spring", "tr": "Baharda ölü toprağın diriltilmesi, haşrin ve kıyametin en büyük ve en muktedir delilidir.", "en": "The revival of dead earth in spring is the greatest proof of resurrection and the Day of Judgment.", "source": "Yirmi Üçüncü Söz"},
    {"title_tr": "Kainatın Büyük Fabrikası", "title_en": "Grand Factory of Universe", "tr": "Kainat fabrikasında dört unsur hammadde olarak çalıştırılmaktadır.", "en": "The four elements are employed as raw materials in the grand factory of the cosmos.", "source": "Mesnevî-i Nuriye"},
    {"title_tr": "Suyun Hakimiyeti", "title_en": "Dominion of Water", "tr": "Suyun her yere yetişmesi ve zihinsizken her ihtiyacı görmesi Rahman'ın delilidir.", "en": "Water reaching everywhere and meeting every need without possessing a mind is proof of the All-Merciful.", "source": "Kastamonu Lahikası"},
    {"title_tr": "Havanın Esrarı", "title_en": "Secret of Air", "tr": "Havanın zerreleri mahlukatın nefes borçlarını tek tek ödemektedir.", "en": "Particles of air pay off the breathing debts of all creatures one by one.", "source": "Emirdağ Lahikası"},
    {"title_tr": "Toprağın Tevazuu", "title_en": "Humility of Soil", "tr": "Toprak cömertlikte ilahi bir ahlakı yeryüzünde temsil etmektedir.", "en": "Soil represents a divine character on earth through its immense generosity.", "source": "Muhakemat"},
    {"title_tr": "Elementlerin İttifakı", "title_en": "Alliance of Elements", "tr": "Zıt unsurların ittifakla insanın imdadına koşması tesadüfen olamaz.", "en": "Opposing elements rushing in alliance to aid human beings cannot be by coincidence.", "source": "Sözler"},
    {"title_tr": "Hayatın Suyu", "title_en": "Water of Life", "tr": "Hayat su ile imtizaç etmiş, onunla latif bir nur kazanmıştır.", "en": "Life has blended with water and gained a subtle illumination through it.", "source": "Lem'alar"},
    {"title_tr": "Dağların Hikmeti", "title_en": "Wisdom of Mountains", "tr": "Dağlar yeryüzünün direkleri ve ambarları hükmündedir.", "en": "Mountains act as pillars and storehouses for the earth.", "source": "Şualar"},
    {"title_tr": "Kainatın Sütunları", "title_en": "Pillars of Cosmos", "tr": "Anâsır-ı erbaa kainat sarayının dört temel sütunudur.", "en": "The four elements are the four main pillars of the cosmic palace.", "source": "Mektubat"},
    {"title_tr": "Mevsimlerin Değişimi", "title_en": "Change of Seasons", "tr": "Unsurların harareti ve bürudeti mevsimleri, mevsimler hayatı tanzim eder.", "en": "Heat and cold of elements regulate seasons, and seasons organize life.", "source": "Yirmi Dokuzuncu Söz"},
    {"title_tr": "Yaratılıştaki Mizan", "title_en": "Balance in Creation", "tr": "Zat-ı Zülcelal hiçbir şeyi mizan ve ölçüden hariç yaratmamıştır.", "en": "The Possessor of Majesty created nothing outside of precise measure and balance.", "source": "İşaratü'l-İ'caz"},
    {"title_tr": "İnsanın Kainatla Bağlantısı", "title_en": "Man's Connection with Cosmos", "tr": "İnsan kainatın küçük bir hülasası ve özetidir.", "en": "Man is a small summary and index of the entire universe.", "source": "Asâ-yı Musa"}
]

# ==========================================
# 4. SIDEBAR & DİL SEÇİMİ / DİL SÖZLÜĞÜ
# ==========================================
with st.sidebar:
    st.header("🌌 Navigation / Navigasyon")
    st.markdown("---")
    
    # Dil Seçimi (Language Selection)
    lang_choice = st.radio(
        "🌐 Gösterim Dili / Display Language",
        ["Çift Dil (TR / EN)", "Sadece Türkçe", "English Only"],
        index=0
    )
    
    st.markdown("---")
    
    # Menü Başlıkları (Dile Göre)
    if lang_choice == "English Only":
        menu_options = [
            "General Contemplation",
            "📖 Quranic Verses (20)",
            "💬 Prophetic Hadiths (20)",
            "💡 Saints' Sayings (20)",
            "📚 Risale-i Nur Examples (20)"
        ]
    else:
        menu_options = [
            "Genel Tefekkür & Bağlantı",
            "📖 Ayet-i Kerimeler (20)",
            "💬 Hadis-i Şerifler (20)",
            "💡 Veli Kulların Görüşleri (20)",
            "📚 Risale-i Nur Örnekleri (20)"
        ]

    selected_menu = st.radio("📌 Modül Seçimi / Select Module", menu_options)
    
    st.markdown("---")
    st.info("🔒 *Telif & Koruma / Security:* Metinler kopyalamaya karşı korunmaktadır. Ticari amaçla kullanılamaz. / Content is protected against copying. Non-commercial use only.")

    # Uyku Modu Bilgi Notu ve Yönlendirmesi
    st.markdown("---")
    st.info(
        "💡 *Not / Note:* Bu web uygulaması ücretsiz sunucularda barındırılmaktadır. "
        "Uzun süre işlem yapılmadığında uygulama uyku moduna geçebilir "
        "(ekranda 'Zzzz' simgesi çıkabilir).\n\n"
        "💤 Eğer böyle bir ekranla karşılaşırsanız, ekranda beliren mavi renkli "
        "*'Yes, get this app back up!'* butonuna tıklayın ve uygulamanın "
        "yeniden uyanması için 15-30 saniye bekleyin."
    )

# ==========================================
# 5. ANA EKRAN İÇERİK YÖNETİMİ
# ==========================================

# Başlık Çevirileri
if lang_choice == "English Only":
    st.title("🌌 Anâsır-ı Erbaa: Four Elements Contemplation Portal")
else:
    st.title("🌌 Anâsır-ı Erbaa: Dört Unsur Tefekkür ve Dönüşüm Portalı")

st.markdown("---")

# 1. MODÜL: GENEL TEFEKKÜR
if selected_menu in ["Genel Tefekkür & Bağlantı", "General Contemplation"]:
    if lang_choice in ["Çift Dil (TR / EN)", "Sadece Türkçe"]:
        st.markdown("""
        > **Topraktan Gelip Toprağa Giden Büyük Çember ve İlahi Nizam**
        > 
        > Rabbimiz insanı topraktan yaratmış, yiyeceği ve içeceği her rızık unsurunu topraktan çıkararak onu besleyip büyütmüştür. 
        > İnsan çevresine baktığında yararlandığı her şeyin kökeninde toprağın ve diğer unsurların izini görür. Ancak bu serüven nihayetsiz değildir; gün gelir toprak onu yer, bağrında eritir ve büyük döngüyü tamamlar. 
        > Bu yazılım; dört unsurun (toprak, su, hava, ateş) ilahi nizamdaki uyumunu ve her modülde zenginleştirilmiş 20'şer adet hakikati tefekkür etmek amacıyla hazırlanmıştır.
        """)
    
    if lang_choice in ["Çift Dil (TR / EN)", "English Only"]:
        st.markdown("""
        > **The Grand Circle: From Dust to Dust and Divine Order**
        > 
        > Our Lord created man from dust and sustained him with provisions extracted from the earth. 
        > Looking around, everything humanity utilizes traces back to the earth and other elements. Yet, when the appointed time arrives, the earth reclaims man, absorbing him back into its womb to complete the grand cycle. 
        > This portal is designed to contemplate the harmony of the four elements (earth, water, air, fire) supported by 20 curated records per module.
        """)

# KART GÖSTERİM YARDIMCI FONKSİYONU
def render_cards(data_list, card_style="earth-card"):
    for idx, item in enumerate(data_list, 1):
        html_content = f'<div class="element-card {card_style}">'
        
        if lang_choice in ["Çift Dil (TR / EN)", "Sadece Türkçe"]:
            html_content += f'<h4>{idx}. {item["title_tr"]}</h4>'
            html_content += f'<div class="text-tr">"{item["tr"]}"</div>'
            
        if lang_choice in ["Çift Dil (TR / EN)", "English Only"]:
            if lang_choice == "English Only":
                html_content += f'<h4>{idx}. {item["title_en"]}</h4>'
            else:
                html_content += f'<h5 style="color:#555;">({item["title_en"]})</h5>'
            html_content += f'<div class="text-en">"{item["en"]}"</div>'
            
        html_content += f'<span class="source-tag">📌 Kaynak / Source: {item["source"]}</span>'
        html_content += '</div>'
        
        st.markdown(html_content, unsafe_allow_html=True)

# 2. MODÜL: AYETLER
if selected_menu in ["📖 Ayet-i Kerimeler (20)", "📖 Quranic Verses (20)"]:
    st.subheader("📖 Kur'ân-ı Kerim'den Seçilmiş 20 Ayet-i Kerime / 20 Selected Quranic Verses")
    render_cards(AYETLER_DATA, "earth-card")

# 3. MODÜL: HADİSLER
elif selected_menu in ["💬 Hadis-i Şerifler (20)", "💬 Prophetic Hadiths (20)"]:
    st.subheader("💬 Hadis-i Şerifler Kütüphanesi (20 Kayıt) / 20 Prophetic Hadiths")
    render_cards(HADISLER_DATA, "water-card")

# 4. MODÜL: VELİ KULLAR
elif selected_menu in ["💡 Veli Kulların Görüşleri (20)", "💡 Saints' Sayings (20)"]:
    st.subheader("💡 İslam Büyükleri ve Veli Kulların Görüşleri (20 Kayıt) / 20 Saints' Sayings")
    render_cards(VELI_DATA, "air-card")

# 5. MODÜL: RİSALE-İ NUR
elif selected_menu in ["📚 Risale-i Nur Örnekleri (20)", "📚 Risale-i Nur Examples (20)"]:
    st.subheader("📚 Bediüzzaman Said Nursi Hazretlerinden Örnekler (20 Kayıt) / 20 Risale-i Nur Passages")
    render_cards(RISALE_DATA, "fire-card")

# ==========================================
# 6. LEGAL DISCLAIMER & FOOTER (HUKUKİ BİLDİRİM)
# ==========================================
st.markdown("---")
st.markdown("""
<div style="background-color: #fff3cd; border: 1px solid #ffeeba; color: #856404; padding: 15px; border-radius: 5px; font-size: 0.85rem;">
    <h4>⚖️ Hukuki Bildirim, Lisans ve Şartlar / Legal Disclaimer & Terms</h4>
    <p><strong>1. Amaç ve Kapsam / Purpose & Scope:</strong> Bu yazılım ve içerisindeki derlemeler tamamen manevi gelişim, kozmolojik tefekkür ve bilgi paylaşımı amacıyla hazırlanmıştır. / This software and its compilations are prepared solely for spiritual development, cosmological contemplation, and knowledge sharing.</p>
    <p><strong>2. Ticari Kullanım Yasağı / Non-Commercial Use:</strong> Bu yazılım, kod yapısı ve içerdiği veri kütüphanesi hiçbir şekilde satılamaz, ticari bir faaliyete konu edilemez, gelir elde etmek amacıyla kullanılamaz. Ticari amaçla kullanılamaz. / This software, code architecture, and database cannot be sold, commercialized, or used for monetary gain under any circumstances.</p>
    <p><strong>3. Kopyalama ve Çoğaltma Yasağı / Copyright Protection:</strong> Yazılım içerisindeki verilerin, metinlerin ve kod yapısının izinsiz kopyalanması, seçilmesi, çoğaltılması, başka platformlara aktarılması veya dağıtılması hukuki koruma altındadır ve yasaktır. / Copying, selecting, replicating, or distributing the texts and code structure without authorization is strictly prohibited under legal protection.</p>
    <p><em>© Tüm Hakları Saklıdır / All Rights Reserved. Manevi gelişim ve bilgi paylaşımı amacıyla serbestçe görüntülenebilir.</em></p>
</div>
""", unsafe_allow_html=True)