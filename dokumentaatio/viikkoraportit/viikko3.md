# Viikko3

##### Voitontarkitus
Tällä viikolla teim funktion voiton tarkistukseen, joka toimii juuri niinkuin pitääkin. Funktio ottaa parametrikseen viimeisimmän siirron speksit (rivi,sarake) ja symbolin eli X tai O riippuen kumman vuoro edellisellä kierroksella on ollut. Voiton tarkistus tehdään jokaisen uuden siirron jälkeen. Tällä hetkellä vieläkin ihmispelaaja pelaa symbolilla X ja AI symbolilla O. Jos voitto havaitaan julkistaa se voittajaksi sen pelaajan kenen vuoro on ollut viimeisimmällä siirolla.

##### Algoritmi
Käytin aika paljon aikaa lukemalla vielä tietoa minimax algoritmista ja kesti yllättävän kauan, että ymmärsin täysin sen toiminnan (jos vieläkään). Tällä hetkellä koen olevani kuitenkin ihan ok kärryillä, pitäisi vielä saada algoritmi toimimaan oikein omaan ohjelmaan. Tällä hetkellä se tutkii ruudut, jotka ovat korkeintaan 2 siirron päässä edellisestä siirrosta. Koska monet ruudut ovat samanarvoisia (eli ei voittoa itselle eikä voittoa toiselle) niin aika usein se menee ensimmäiseen tutkittavaan ruutuun eli AI on todella ennalta-arvattava, tyhmä liikkeistään sekä helposti voitettava tällä hetkellä. 

##### Testit
Olen hieman laiminlyönyt testien tekemimstä, kun jostain syystä aikaa uppoaa muihin asioihin usein enemmän kuin olin suunnitellut. Olen yrittänyt luoda Boardille testejä varten BoardStubb luokkaa, joka loisi board.py testejä varten ihan oman pelilautansa, koetko tämän olevan hyvä lähestymistapa?

##### Ensi viikko
Ensi viikolla pyrin saamaan algoritmin toimimaan viisaammin jottei sitä voittaisi niin helposti. 

##### Kysymksiä
- Aiheen määrittelyssä sanotaan, että edelliset siirrot pitäisi säilöä jossain ja lähimpiä pitäisi priorisoida (niitä jotka ovat nyt ainoat tutkittavat minulla, eikä algoritmi niistäkään tee ehkä parhaimpia valintoja) niin miten tämä on järkevin totetuttaa? Olisko esim. sanakirja niin, että key olisi esimerkiksi tietyn ruudun koordinaatti ja value sen siirron hyvyys ja sieltä valitaan ruutu parhaimmalla hyvyydellä. Kannattaako minun kuitenkin pitää tuo lista viereisistä ruuduista vielä osana koodia vai koetko ,että se saattaa käydä turhaksi kun parannan algoa?

##### Työaika
Käytin tällä viikolla työhön varmaan n. 15-20h
