# Viikko5

Anteeksi myöhäisestä palautuksesta. En eilen illala ehtinyt saada kaikkia erroreita pois niin en viitsinyt pushata tänne ihan rikkinäisenä.

Yritin viime viikolla ja tällä viikolla aloittaa heuristiikan luomista ja parantaa algoritmia paikan valinnassa. Sain jotenkin sotkettua koodin hetkeksi ihan kokonaan, mutta nyt hieman parempi jo taas. 
En kyllä oikein vieläkään saanut tuota algoa paremmaksi ja heuristiikkaakin pitäisi vielä parantaa.

Muokkasin lähinnä Board luokan check_win funktiota (heuristiikan lisäys) ja Opponent luokan ai_create_move ja minmax funktioita. Yritin tehdä ohjeidesi mukaan listan jota käydään takaperin ja tutkitaan siirtoja sekä luoda heuristiikkaa. 

Olisiko antaa vinkkiä noiden edellä mainittujen funktioiden osalta, että mihin suuntaan kannattaa lähteä muokkaamaan. Tuntuu että olen vähän jumissa ja kaikki mitä kokeilen ei toimi ainakaan sen paremmin kuin miten tähän mennessä on toiminut, monesti jopa huonommin ja joudun palaamaan taaksepäin.

( Tällä hetkellä muuten listan self.investigated_moves = [] sijainti on väärä ai_create_moves funktiossa, koska se tyhjentyy aina kun funktiota kutsutaan uudestaan, mutta jos pidin sitä konstruktorissa niin jostain syystä lauta näytti vain kaksi siirtoa kerrallaan laudalla eli poisti aikaisemmat siirrot näkyvistä.)

Tällä viikolla käytin työhön n 15h
