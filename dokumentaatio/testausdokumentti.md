# Testausdokumentti

Tein projektiini yksikkötestejä UnitTestien avulla. Yksikkötesteillä testataan yksittäisten metodien toimintaa ja myös reaktiota vääränlaisiin syötteisiin.


## Käyttöliittymätestaus
Alla testitapauksia, joilla olen manuaalisesti testannut projektia

1. Pelaaja syöttää halutun liikkeen väärin  
    - Liian lyhyt käsky
      - syöte : 6
        - reaktio: "Virhe. Syötäthän siirtosi esim. C5 or F15" ja kysytään uutta siirtoa
    - Vääränlainen käsy
      - syöte: 2B
      - reaktio: "Virhe. Syötäthän siirtosi esim. C5 or F15" ja kysytään uutta siirtoa

2. Pelaaja syöttää koordinaatit ruutuun, jossa on jo nappula
   
    Aloitetaan peli ja laitetaan jokin ensimmäinen liike C6. Tämän jälkeen jos yritämme myöhemmin lisätä nappulan ruutun C6 se ei luonnollisesti onnistu. Kun näin tapahtuu ohjelma reagoi siihen ilmoittamalla: "Ruudussa on jo nappula. Valitse toinen ruutu" ja kysymällä uutta.

