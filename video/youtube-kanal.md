# Der Kanal, gemessen — nicht geschätzt

**Kanal:** `UC5r4pxlAtt2alIOIGjdn4Qw` · `@yannick-noah` · Yannick N. Bernard  
**Gemessen:** Mo 19.10.2026, gegen 14:45 Kapstadt · **ohne API-Schlüssel**, direkt von der öffentlichen Kanalseite.

## Was dasteht

| | Stück | davon mit Zahl | Aufrufe (nur gezählte) | Median | Bestes | Schwächstes |
|---|---:|---:|---:|---:|---:|---:|
| **Lange Videos** | 37 | 29 | 30.091 | **331** | 12.000 | 28 |
| **Shorts** | 38 | 38 | 27.512 | **757** | 2.700 | 24 |
| **Summe** | 75 | 67 | 57.603 | — | — | — |

**Bei 8 langen Videos liefert die öffentliche Seite keine Zahl** — das sind *nicht gemessene* Werte,
**keine Nullen**. Sie fehlen in Summe und Median. Welche es sind, steht unten.

**Der Median eines Shorts liegt 2,3× über dem eines langen Videos** (757 gegen 331).

**Die Einschränkung gehört dazu:** Short-Aufrufe und Video-Aufrufe sind nicht dasselbe. Shorts laufen
im Feed mit Autoplay, ein Aufruf zählt nach wenigen Sekunden; ein langes Video wird geklickt.
Der Faktor misst **Sichtbarkeit, nicht Aufmerksamkeit** — wie viele Dich sehen, nicht wie lange sie
bleiben. Verweildauer, Klickrate und Zuschauerquellen stehen öffentlich nicht da; dafür bräuchte es
YouTube Analytics über OAuth.

## Die zehn stärksten langen Videos

| Aufrufe | Länge | Titel |
|---:|---:|---|
| 12.000 | 70:39 | Queer Actor: "Homosexuality is NOT unnormal" – About Masculinity, Tant |
| 2.400 | 16:35 | The Last Year Of My Life |
| 2.200 | 20:02 | 10 Life Lessons I Learned at AfrikaBurn |
| 1.800 | 7:50 | The Video Alex Hormozi Doesn't Want You to See |
| 1.300 | 14:10 | Why Kids Should Be Allowed Trans Surgery – Dr. Curtis Crane |
| 1.300 | 109:53 | America's #1 Transgender Doctor: Burning Man, Bobby Kennedy & Black Ho |
| 1.300 | 13:10 | Living My Dream Life in Cape Town at 26 y/o |
| 1.100 | 27:25 | Football-Star REVEALS The Dark Truth About The NFL |
| 1.000 | 9:01 | When America’s #1 Transgender Doctor goes to Burning Man… |
| 795 | 102:28 | Ex-NFL Star: Football Broke Me. Then God Saved Me. (Eben Britton) |

## Die zehn stärksten Shorts

| Aufrufe | Titel |
|---:|---|
| 2.700 | The Biggest Scandal in the German School System |
| 1.600 | Why Are We So Afraid of Stillness? |
| 1.500 | NFL Star: My Dream Turned Into A Nightmare |
| 1.300 | What Makes Life Meaningful? (Francis Michael) |
| 1.200 | Why I Quit Gilmore Girls, Friends & Hollywood |
| 1.100 | The Secret Of Becoming A Great Podcaster |
| 1.100 | Millionaire: You Need to Get MARRIED |
| 1.100 | Gurus DO NOT Exist |
| 1.100 | What’s a real man? |
| 1.100 | the pursuit of happiness is a lie #selfactualization #growthmindset #m |

## Ohne Zahl auf der öffentlichen Seite

- `frNOUgxE0IM` — The Hollywood Star Who Quit Everything To Heal Men: Feminism, Manosphe
- `6lz48mI8xJw` — 'I Didn’t Believe In Past Lives – Until THIS Happened'
- `23NNT7aMgL4` — Podcast Star turned Hypnotherapist: I quit everything to follow God‘s 
- `zlLwIupitJI` — Into The Wild: What Chris McCandless Really Died For
- `FF-eRPgZI2k` — The SHOCKING Truth About The Crisis in South Africa: Segregation, Whit
- `Kj8XjhrauiI` — Why Feminism Is A BIG Mistake
- `6U_fhkqFq60` — Iboga Taught Me To Love Hitler
- `cv-I2lkMebE` — A Radically Honest Conversation about Feminism, Vipassana and Crystal 

## Wie ich das hole

```python
import yt_dlp
opts={'quiet':True,'skip_download':True,'extract_flat':'in_playlist'}
for tab in ['videos','shorts']:
    url=f'https://www.youtube.com/channel/UC5r4pxlAtt2alIOIGjdn4Qw/{tab}'
    with yt_dlp.YoutubeDL(opts) as y: info=y.extract_info(url, download=False)
```

**Kein API-Schlüssel, kein Google-Cloud-Projekt, kein OAuth.** Möglich geworden durch die
Netzwerk-Freigabe vom 19.10. Vorher war `youtube.com` im Container nicht auflösbar, und ich
konnte Reichweite überhaupt nicht messen — das war mein blinder Fleck vom 17./18.10.
