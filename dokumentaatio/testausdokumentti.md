# Testausdokumentti

Tein projektiini yksikkötestejä UnitTestien avulla. Yksikkötesteillä testataan yksittäisten metodien toimintaa ja myös reaktiota vääränlaisiin syötteisiin. Testikattavuus voisi ja pitäisikin olla korkeampi kuin minulla tällä hetkellä.

![image](https://github.com/henniseppis/algoritmit-harjoitustyo/blob/main/dokumentaatio/Screenshot%20from%202024-05-14%2020-27-15.png)

##### Mitä yksikkötesteillä testataan:

- ui.py
  - lauta tulostetaan oikein
  - ihmispelaajan syöttämä liike on validi (ei liian lyhyt, väärässä muodossa tai varattu)
  - voittajan julistukseen käytettävä metodi julistaa oikean voittajan

- board.py
  - Voitontsekkaus metodi tunnistaa voitot vaaka- ja pystysuuntiin sekä diagonaalisesti. Myös testit, joissa voittoa ei havaita. Esimerkiksi 5 samalla rivillä, mutta ei peräkkäin.
  - Pelilaudalle liikkeen syöttävä metodi toimii oikein
  - Tasapelin tunnistava metodi toimii. Myös False testi
  - Heuristisen arvon määritteleville metodeille muutama testi

- opponent.py
  - Metodi, joka etsii edellisen siirron läheltä tutkittavia liikkeitä löytää oikeat koordinaatit.
  - Testi myös samaiselle metodille, ettei se lisää listaan jo varattujen ruutujen koordinaatteja
  - Testi, jossa katsotaan että minmax osaa torjua vastakkaisen pelaajan toisesta päästä suljetun 4 suoran.

## Käyttöliittymätestaus
Alla tapauksia, jotka väkisinkin tulee testattua peliä kokeiltaessa. Osaan näistä on myös yksikkötestit

1. Pelaaja syöttää halutun liikkeen väärin  
    - Liian lyhyt käsky
      - syöte : 6
        - reaktio: "Virhe. Syötäthän siirtosi esim. C5 or F15" ja kysytään uutta siirtoa
    - Vääränlainen käsy
      - syöte: 2B
      - reaktio: "Virhe. Syötäthän siirtosi esim. C5 or F15" ja kysytään uutta siirtoa

2. Pelaaja syöttää koordinaatit ruutuun, jossa on jo nappula
   
    Aloitetaan peli ja laitetaan ensimmäinen liike vaikkapa C6. Tämän jälkeen jos yritämme myöhemmin lisätä nappulan ruutun C6 se ei luonnollisesti onnistu. Kun näin tapahtuu ohjelma reagoi siihen ilmoittamalla: "Ruudussa on jo nappula. Valitse toinen ruutu" ja kysymällä uutta.

3. Peli kulkee niinkuin pitää
   Peli kulkee koodissa While True-loopin sisällä. Vuorotellen ihmispelaaja ja AI laittavat nappuloitaan. Peliä pelatessa voidaan huomata, että loop toimii moitteettomasti eteenpäin.


## Testien ajaminen

voit ajaa testit virtuaaliympäristöss komennolla ```invoke test```

virtuaaliympäristöön pääset komennolla ```poetry shell```
