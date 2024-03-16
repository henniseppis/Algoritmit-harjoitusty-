# Määrittelydokumentti 

#### Opinto-ohjelma:
- Tietojenkäsittelytieteen kandidaatti

#### Projektin ohjelmointikieli ja muiden kielien osaaminen
- Teen projektini Pythonilla
- Dokumentointi on suomeksi, mutta koodi englanniksi
- Pystyn vertaisarvioimaan tarvittaessa myös JavaScriptillä tehtyjä töitä, mieluiten python.

#### Projektin aihe

Päädyin aiheessani klassiseen ristinolla peliin. Mielenkiintoinen aihe, jossa pääsee haastaamaan itseään ja oppimaan uutta.

Ristinolla tulee olemaan 20x20 lauta. Algoritmina käytössä minimax aplha-beta karsinnalla. 

Tarkoituksena algoritmin avulla löytää viimeisimmän siirron perusteella, siihen tilanteeseen parhain siirto. Löytääksemme parhaimman siirron nopeiten, tutkitaan vain aikaisempien siirtojen lähialueet.

Voitto selvitetään tarkastelemalla vain viimeiseen siirtoon liittyviä ruutuja, viimesimmän siirron tehnyt julistetaan voittajaksi jos voiton ehdot täyttyvät.

#### Pelin kulku
- Peliä voi pelata komentoriviltä
- Käyttäjä pelaa tietokonetta vastaan. Toisella nappulana ristit, toisella nollat.
- Nappuloita laitetaan laudalle vuorotellen
- Se kumpi saa ensiksi 5 omaa nappulaa peräkkäin pelilaudalle, voittaa. (Pysty, vaaka tai diagonaali)
- Pelissä tehdään siirtoja syöttämällä paikan koordinaatti johon oman nappulan haluaa (esim. B3, jolloin oma nappula laitetaan toisen rivin kolmannelle sarakkeelle)
- Teen (ehkä) niin, että käyttäjä on aina risti ja tietokone nolla. Toki saatan myös tehdä niin että käyttäjä voi valita kumpi haluaa olla.

#### Minimax-algoritmi alpha-beta-karsinnalla

Minimax-algoritmia käytetään esimerkiksi pelien luonnissa minimoimaan häviö huonoimmassa mahdollisessa tilanteessa. Minimax-algoritmi pyrkii minimoimaan häviön joko itse voittamalla, tai tekemällä siiroon joka ei johda toisen pelaajan voittoon seuraavalla kierroksella.

  
