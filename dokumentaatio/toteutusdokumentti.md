# Toteustusdokumentti

### Yleisrakenne

Tässä ristinolla pelissä pelaa vastakkain tietokone ja ihminen (sinä). Tietokone käyttää minmax algoritmia alpha-beta karsinnalla testatakseen sekä valitakseen parhaimman seuraavan siiroon. Valinnassa auttaa myös pelilaudan heuristisen arvon määrittely, joka tehdään jokaisella kierroksella. Minmax algoritmin tarkoituksena on minimoida vastustajan voittomahdollisuudet ja maximoida omat. Aplha-beta karsinnalla taas tehostetaan algoritmin toimintaa, sillä jättää tutkimatta solmut, jotka ovat varmasti huonompia kuin tämän hetkinen paras arvo.

Peli pelataan komentoriviltä. Vuorotellen laitetaan omia pelinappuloita laudalle. Se kumpi saa ensiksi 5 peräkkäin voittaa.


### Puutteet parannusehdotukset

Algoritmini menee tällä hetkellä vain syvyyteen 3. Lähtisin ihan ensimmäiseksi parantamaan algoritmia, jotta syvyydeksi saisi vähintään 5.
Työlle olisi myös hyvä tehdä parempi käyttöliittymä, jossa pystyisi esimerkiksi painamaan näytöltä ruutua johon oman nappulan haluaisi laittaa.

### Laajojen kielimallien käyttö

Käytin työssäni chatGPT:tä alla oleviin asioihin:

- Kysyin esimerkkejä minmaxista ja alpha-beta pruningista.
  - Ennen itse koodauksen aloittamista kysyin minmax algoritmista sekä alpha-beta pruningista esimerkkejä sekä selitystä niiden toiminnasta.

- Debuggaus / Virheilmoitusten ymmärtäminen
  - Kysyin tekoälyltä selityksiä saamistani error koodeista ja virheilmoituksista ja mahdollisia tilanteita mistä ne voisivat johtua.
  - Välillä myös syötin virheellisen koodin, jotta ymmärsin missä virhe on

- Koodin refektorointi 
  - Check_draw metodin (tarkastaa onko peli päättynyt tasapeliin = kaikki  otin suoraan chatGPT:n mallin mukaan sen jälkeen kun pyysin sitä refektoroimaan omaani, joka oli aika paljon pidempi sokkelo koodi.
  - Samoin kysyin apua refektoroimaan koodia check_diagonal metodissa (osa pelitilanteen heurisitisen arvon määrittelyä)


### Aikavaativuudet
Aikavaativuus on O(b^m), jossa b on mahdollisten siirtojen määrä ja m puun syvyys.
