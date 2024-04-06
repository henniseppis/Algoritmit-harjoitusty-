# Viikko3

##### Voitontarkitus
Tällä viikolla aloitin tekemällä funktion voiton tarkistukseen. Funktio ottaa parametrikseen viimeisimmän siirron speksit (rivi,sarake) ja symbolin eli X tai O riippuen kumman vuoro edellisellä kierroksella on ollut. Voiton tarkistus tehdään jokaisen uuden siirron jälkeen. Tällä hetkellä vieläkin ihmispelaaja pelaa symbolilla X ja AI symbolilla O.

##### Algoritmi
Käytin aika paljon aikaa lukemalla tietoa minimax algoritmista ja kesti yllättävän kauan, että ymmärsin täysin sen toiminnan. Tällä hetkellä koen olevani ihan hyvin kärryillä, pitäisi vielä saada algoritmi toimimaan oikein omaan ohjelmaan. Tällä hetkellä se tutkii ruudut, jotka ovat korkeintaan 2 siirron päässä edellisestä siirrosta. Koska monet ruudut ovat samanarvoisia (eli ei voittoa itselle eikä voittoa toiselle) niin aika usein se menee ensimmäiseen tutkittavaan ruutuun eli AI on todella ennalta-arvattava ja tyhmä liikkeistään tällä hetkellä. 

##### Testit
Olen hieman laiminlyönyt testien tekemimstä, kun jostain syystä aikaa uppoaa muihin asioihin usein enemmän kuin olin suunnitellut, mutta muutaman sain tehtyä lisää.

##### Ensi viikko
Ensi viikolla pyrin saamaan algoritmin toimimaan viisaammin. 

##### Kysymksiä
-Aiheen määrityksessä sanotaan, että edelliset siirrot pitäisi säilöä jossain ja  lähimpiä pitäisi priorisoida (niitä jotka ovat nyt ainoat tutkittavat minulla) niin miten tämä on järkevin totetuttaa. Ja onko tämän hetkinen lista viimeisimmän siirron läheisimmistä ruuduista turha/saisiko sen tehtyä järkevämmin? Löytyy koodista opponent.py luokasta Opponent ja funktio def find_nearest_free_cells  
- Vakuuttavaan testaukseen tarvittiin myös muitakin kuin yksikkötestejä. Mikä saattaisi olla paras vaihtoehto tähän?
- Pylint tarkastuksen mukaan koodissani on parannettavaa (jonka toki allekirjoitan), mutta useimmat pylint huomatuokset koskevat tyhjiä rivejä. Mielestäni se ettei kaikki ole ihan peräkanaa niin auttaa myös ehkä hahmottamaan koodia tarkemmin. Olisiko mielestäsi parempi ottaa kaikki rivivälit pois ihan joka kohdasta?
