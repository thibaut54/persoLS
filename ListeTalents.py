listeTalents = [
"Acrobatie équestre      (+10% equitation)", #0
"Acuité auditive      (+20% perception auditive)", #1
"Acuité visuelle      (+10% perception visuelle / lecture sur les lèvres)", #2
"Adresse au tir      (20% CT si visée)", #3
"Ambidextre      (pas de malus CC si l'arme change de main)", #4
"Armes naturelles      (à mains nues, BF en dégat)", #5
"Calcul mental      (+10% jeu / orientation | +20% perception estimation)", #6
"Camouflage rural      (+10% déplacement silencieux / dissimulation en milieu rural)", #7
"Camouflage souterrain      (+10% déplacement silencieux / dissimulation en milieu souterrain)", #8
"Camouflage urbain      (+10% déplacement silencieux / dissimulation en milieu urbain)", #9
"Chance      (inclus dans profil secondaire)", #10
"Chirurgie      (+10% soins, +2PV si blessé gravement au lieu de 1 si soins réussis)", #11
"Code de la rue      (+10% charisme / commerage avec le milieu du crime)", #12
"Combat de rue      (+10% CC et +1 dégat à mains nues)", #13
"Combattant virevoltant      (désengagement gratuit et possible coups accrobatiques au CAC)", #14
"Connaissance des pièges      (+10% crochetage / perception des pièges)", #15
"Contorsionniste      (+20% Ag pour se libérer de liens, passage par petites ouvertures, etc.)", #16
"Coups assommants      (possibilité d'assomer pour 1D10 round)", #17
"Coups précis      (+1 aux coups critiques)", #18
"Coups puissants      (+1 dégat avec armes au CAC)", #19
"Course à pied      (inclus dans profil secondaire)", #20
"Désarmement      (possibilité de désarmer au CAC, si CC passe --> jet Ag opposé)", #21
"Dur à cuire      (inclus dans profil principal)", #22
"Dur en affaires      (+10% évaluation / marchandage)", #23
"Effrayant      (vous provoquez la peur)", #24
"Éloquence      (nombre de personnes affectées par charisme x 10)", #25
"Étiquette (+10% charisme / commerage avec noblesse et 10% déguisement / imitation noble)", #26
"Force accrue      (inclus dans profil principal)", #27
"Frénésie      (jusque fin de combat, obligation d'attaque brutale ou charge sur ennemi le plus proche avec +10% F et FM, -10% CC et Int, fuite impossible)", #28
"Fuite      (+1 de mouvement si fuite pendant 1D10 round)", #29
"Fureur vengeresse      (+5% CC si orque, gobelin, hobgobelin)", #30
"Grand voyageur      (+10% connaissance générale et langue)", #31
"Guerrier né      (inclus dans profil principal)", #32
"Harmonie aethyrique      (+10% focalisation / sens de la magie)", #33
"Imitation      (+10% déguisement / expression artistique)", #34
"Incantation de bataille      (malus d'armure sur magie réduit de 3)", #35
"Inspiration divine : Grungni      (liste de sorts)", #36
"Intelligent      (inclus dans profil principal)", #37
"Intrigant      (+10% charisme pour intriguer / +10% FM contre charisme)", #38
"Lévitation      (possibilité de voler sur courte distance)", #39
"Linguistique      (+10% lire/écrire / langue)", #40
"Lutte      (+10% CC et F pour prise au CAC)", #41
"Magie commune : occulte      (liste de sorts)", #42
"Magie mineure      (liste de sorts)", #43
"Magie noire      (1D10 supplémentaire sur lancement sorts de Sombre savoir, retirez le plus petit D10)", #44
"Magie commune : vulgaire      (liste de sorts)", #45
"Mains agiles      (+20% CC si sort de contact)", #46
"Maître artilleur      (-1 demi-action pour recharger arme à poudre, cumulable avec rechargement rapide)", #47
"Maîtrise : arbalètes", #48 
"Maîtrise : arcs longs", #49 
"Maîtrise : armes à feu", #50 
"Maîtrise : armes de cavalerie", #51 
"Maîtrise : armes de jet", #52
"Maîtrise : armes de parade", #53
"Maîtrise : armes d’escrime", #54
"Maîtrise : armes lourdes", #55
"Maîtrise : armes mécaniques", #56
"Maîtrise : armes paralysantes", #57
"Maîtrise : fléaux", #58
"Maîtrise : lance-pierres", #59
"Méditation      (bonus égale à la valeur de magie si rituel)", #60
"Menaçant      (+10% intimidation / torture)", #61
"Mort-vivant      (immunisé contre peur, coup assommants, poison, maladie, sorts d'esprit)", #62
"Orateur né      (nombre de personnes affectées par charisme x 100)", #63
"Parade éclair      (possibilité d'échanger 1 attaque contre 1 parade gratuite, 1 parade max par round)", #64
"Projectile puissant      (+1 dégat avec projectiles magiques)", #65
"Rechargement rapide      (-1 demi-action rechargement arme de tir)", #66
"Réflexes éclair      (inclus dans profil principal)", #67
"Résistance accrue      (inclus dans profil principal)", #68
"Résistance à la magie      (+10% FM pour résister aux sorts)", #69
"Résistance au Chaos      (+10% FM pour résister aux sorts du Chaos, immunisé mutation du Chaos)", #70
"Résistance aux maladies      (+10% FM pour résister aux maladies)", #71
"Résistance aux poisons      (+10% Endu pour résister aux poisons)", #72
"Robuste      (pas de malus de mouvement si armure lourde)", #73
"Sain d’esprit      (pas de test de folie avant 8PF)", #74
"Sang-froid      (inclus dans profil principal)", #75
"Sans peur      (immunisé contre peur / intimidation / troublant, terreur devient peur)", #76
"Savoir-faire nain      (+10% métiers typiques des nains)", #77
"Science de la magie      (liste de sorts)", #78
"Sens aiguisés      (+20% perception)", #79
"Sens de l’orientation      (+10% orientation)", #80
"Sixième sens      (si danger proche, MJ test de FM secret et peut vous avertir)", #81
"Sociable      (inclus dans profil principal)", #82
"Sombre savoir : domaine du Chaos      (liste sorts)", #83
"Sur ses gardes      (dégainez gratuitement 1 fois par round)", #84
"Talent artistique      (+20% métier artiste / évaluation objet d'art)", #85
"Terrifiant      (provoquez la terreur)", #86
"Tir de précision      (ignorez 1 point d'armure en tir à distance)", #87
"Tir en puissance      (+1 dégat avec armes de tir)", #88
"Tireur d’élite      (inclus dans profil principal)", #89
"Troublant      (à votre vue, les ennemis doivent réussir FM sinon -10% CC / CT, tentative possible chaque round)", #90
"Valeureux      (+10% FM si peur / terreur / intimidation)", #91
"Vision nocturne      (pas de malus perception jusque 30m si obscurité naturelle)", #92
"Vol      (moi, je vole)", #93
"Magie commune : divine      (liste de sorts)", #94
"Inspiration divine : Manann      (liste de sorts)", #95
"Inspiration divine : Morr      (liste de sorts)", #96
"Inspiration divine : Myrmidia      (liste de sorts)", #97
"Inspiration divine : Ranald      (liste de sorts)", #98
"Inspiration divine : Sigmar      (liste de sorts)", #99
"Inspiration divine : Shallya      (liste de sorts)", #100
"Inspiration divine : Taal/Rhya      (liste de sorts)", #101
"Inspiration divine : Ulric      (liste de sorts)", #102
"Inspiration divine : Verena      (liste de sorts)", #103
"Sombre savoir : nécromancie      (liste de sorts)", #104
"Sombre savoir : domaine de Nurgle      (liste de sorts)", #105
"Sombre savoir : domaine de Slaanesh      (liste de sorts)", #106
"Sombre savoir : domaine de Tzeentch      (liste de sorts)", #107
"Rompu au Chaos      (liste de sorts)", #108
"Magie vulgaire      (ajoutez 1D10 aux incantations seulement pour maledction de Tzeentc)h", #109
"Magie des Nains du Chaos      (boule de feu, cautérisation, coeur ardent, conflagration fatale, couronne de feu, explosion flamboyante, faveur du Chaos, main de la destruction, souffle de feu et vision d’horreur.)"] #110

listeTalentsRandom = [
"Acuité auditive     (+20% perception auditive)", #0	 		01–05 	01–04
"Acuité visuelle     (+10% perception visuelle / lecture sur les lèvres)", #1	 		06–10 	05–09
"Ambidextre     (pas de malus CC si l'arme change de main)", #2		 		11–15 	10–14
"Calcul mental     (+10% jeu / orientation | +20% perception estimation)", #3		 		16–20 	15–18
"Chance     (inclus dans profil secondaire)", #4			  		21–25 	19–22
"Course à pied     (inclus dans profil secondaire)", #5		  		26–30 	23–26
"Sociable     (inclus dans profil principal)", #6			  		31–35 	27–30
"Dur à cuire     (inclus dans profil secondaire)", #7		  		36–39 	31–35
"Force accrue     (inclus dans profil principal)", #8		  		40–43 	36–39
"Guerrier né     (inclus dans profil principal)", #9  		 	 	44–48 	40–44
"Imitation     (+10% déguisement / expression artistique)", #10		  		49–53 	45–48
"Intelligent     (inclus dans profil principal)", #11		  		54–58 	49–53
"Réflexes éclair     (inclus dans profil principal)", #12	  		59–62 	54–57
"Résistance à la magie     (+10% déguisement / expression artistique)", #13  	63–64 	58–61
"Résistance accrue     (inclus dans profil principal)", #14  		65–68 	62–65
"Résistance aux maladies     (+10% FM pour resister aux maladies)", #15  69–72 	66–69
"Résistance aux poisons     (+10% Endu pour resister aux poisons)", #16  	73–76 	70–73
"Robuste     (pas de malus de mouvement si armure lourde)", #17  				77–81 	74–77
"Sain d'esprit     (pas de test de folie avant 8PF)", #18  			82–86 	78–81
"Sang froid     (inclus dans profil principal)", #19  				87–91 	82–85
"Sixième sens     (si danger proche, MJ test de FM secret et peut vous avertir)", #20  			92–96 	86–90
"Tireur d'élite     (inclus dans profil principal)", #21  			97–00 	91–95
"Vision nocturne     (pas de malus perception jusque 30m si obscurité naturelle)"] #22  			– 	96–00