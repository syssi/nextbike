# Nextbike Sensor

![GitHub actions](https://github.com/syssi/nextbike/actions/workflows/ci.yaml/badge.svg)
![GitHub stars](https://img.shields.io/github/stars/syssi/nextbike)
![GitHub forks](https://img.shields.io/github/forks/syssi/nextbike)
![GitHub watchers](https://img.shields.io/github/watchers/syssi/nextbike)
[!["Buy Me A Coffee"](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg)](https://www.buymeacoffee.com/syssi)

The nextbike sensor platform monitors bike availability in a chosen radius of the free-floating areas. If you want to monitor a specific station please use the official citybikes sensor platform.


## Install

You can install this custom component by adding this repository ([https://github.com/syssi/nextbike](https://github.com/syssi/nextbike/)) to [HACS](https://hacs.xyz/) in the settings menu of HACS first. You will find the custom component in the integration menu afterwards, look for 'Nextbike Integration'. Alternatively, you can install it manually by copying the custom_component folder to your Home Assistant configuration folder.


## Setup

```
# configuration.yaml

sensor:
  - platform: nextbike
    name: Near bikes
    city_id: 547
    radius: 500

  - platform: nextbike
    name: Campus Poppelsdorf
    city_id: 547
    latitude: 50.7284811
    longitude: 7.0852697
    radius: 25

  - platform: nextbike
    name: Berlin
    city_id: 362
    latitude: 52.5258988
    longitude: 13.3697015
    radius: 800
```

Configuration variables:
- **city_id** (*Required*): The nextbike city ID
- **radius** (*Required*): The radius (in meters or feet, depending on the Home Assistant configuration) around the monitored location. Only bikes closer than this distance will be monitored.
- **name** (*Optional*): The name of nextbike sensor.
- **latitude** (*Optional*): Latitude of the location, around which bikes are monitored. Defaults to the latitude in your configuration.yaml file.
- **longitude** (*Optional*): Longitude of the location, around which bikes are monitored. Defaults to the longitude in your configuration.yaml file.

City IDs:

* Austria
  * nextbike Austria
  * nextbike Niederösterreich Austria
    * **57** St.Pölten (48.2058, 15.6232)
    * **64** Mödling (48.1047, 16.3202)
    * **142** Wachau (48.3188, 15.4166)
    * **143** Tulln (48.3269, 16.0569)
    * **144** Leobersdorf (47.9421, 16.1149)
    * **146** Thermenregion (47.9892, 16.2646)
    * **149** Römerland (48.0909, 16.853)
    * **156** WienerNeustadt (47.8167, 16.2426)
    * **165** Herzogenburg (48.1111, 15.8176)
    * **170** Marchfeld (48.2407, 16.9093)
    * **174** Wien Umland Nord West (48.3403, 16.279)
    * **184** Laa an der Thaya (48.7196, 16.3878)
    * **185** Südheide (48.1077, 16.3937)
    * **212** Hollabrunn (48.562, 16.0785)
    * **213** WienerWald (48.1926, 16.141)
    * **395** Groß Enzersdorf (48.1986, 16.5496)
    * **414** Amstetten (48.1218, 14.8774)
  * Stadtrad Innsbruck Austria
    * **199** Innsbruck (47.2632, 11.3961)
  * nextbike Tirol Austria
    * **286** Serfaus (47.0387, 10.6048)
  * nextbike Klagenfurt Austria
    * **396** Klagenfurt (46.6335, 14.3085)
  * nextbike Burgenland Austria
    * **23** Neusiedler See (47.839, 16.761)
  * city bike Linz
    * **692** Linz (48.3003, 14.2843)
  * WienMobil Rad
    * **748** Wien (48.2089, 16.3787)
  * VVT REGIORAD Tirol
    * **773** Kufstein (47.583, 12.1692)
    * **774** Ellmau (47.5134, 12.3025)
* Bosnia and Herzegovina
  * nextbike BIH
    * **350** Sarajevo (43.85, 18.39)
    * **805** Mostar (43.3439, 17.8018)
  * BL bike (BIH)
    * **494** Banja Luka (44.775, 17.1994)
  * Zenica (BIH)
    * **427** Zenica (44.2033, 17.9184)
* Croatia
  * nextbike Croatia
    * **220** Zagreb (45.7984, 15.9881)
    * **424** Metković (43.0654, 17.642)
    * **921** Općina Plitvička Jezera (44.7887, 15.683)
  * Grad Šibenik (Croatia)
    * **248** Šibenik (43.7294, 15.9074)
  * Grad Karlovac (Croatia)
    * **305** Karlovac (45.4905, 15.5503)
  * Grad Slavonski Brod (Croatia)
    * **308** Slavonski Brod (45.1656, 18.0183)
  * Grad Pula (Croatia)
    * **798** Pula (44.8622, 13.8541)
    * **870** Vodnjan (44.9551, 13.8572)
  * Grad Makarska (Croatia)
    * **324** Makarska (43.2992, 17.0184)
  * Grad Vukovar (Croatia)
    * **328** Vukovar (45.3575, 18.9895)
  * Hvar (Croatia)
    * **745** Stari Grad  (43.1841, 16.5886)
  * Općina Brinje (Croatia)
    * **325** Brinje (44.9977, 15.1258)
  * Grad Zadar (Croatia)
    * **327** Zadar (44.1132, 15.2356)
  * Grad Ivanić-Grad (Croatia)
    * **337** Ivanic Grad (45.7062, 16.3919)
  * Grad Sisak (Croatia)
    * **416** Sisak (45.4857, 16.3778)
  * Grad Velika Gorica (Croatia)
    * **415** Velika Gorica (45.7161, 16.0683)
  * Grad Zaprešić (Croatia)
    * **723** Zaprešić (45.8622, 15.8049)
  * Porec bike share (Croatia)
    * **429** Poreč (45.2292, 13.6035)
  * Grad Vinkovci (Croatia)
    * **739** Vinkovci (45.289, 18.8057)
  * Jastrebarsko (Croatia)
    * **425** Jastrebarsko (45.6692, 15.6541)
  * Grad Drniš (Croatia)
    * **426** Drniš (43.8425, 16.1197)
  * Općina Dugopolje (Croatia)
  * Općina Pitomača (Croatia)
    * **574** Pitomača (45.9077, 17.2622)
  * Grad Split (Croatia)
    * **445** Općina Dugopolje (43.5872, 16.5879)
    * **617** Split  (43.5162, 16.4637)
    * **740** Solin (43.5441, 16.4833)
    * **741** Općina Klis (43.5605, 16.5269)
    * **742** Općina Hrvace (43.7553, 16.6197)
    * **743** Općina Otok Dalmatinski (43.6889, 16.7361)
    * **744** Sinj (43.7031, 16.6364)
    * **766** Općina Podstrana (43.4934, 16.5598)
    * **802** Trogir (43.5234, 16.2476)
    * **804** Kaštela (43.568, 16.3847)
    * **837** Općina Dicmo (43.6297, 16.6015)
  * Grad Križevci (Croatia)
    * **714** Križevci (46.0225, 16.5482)
  * eMobi (Croatia)
    * **734** Osijek (45.5525, 18.6965)
  * Grad Šibenik (Croatia) [old]
  * Općina Brinje (Croatia) [old]
  * Grad Velika Gorica (Croatia) [old]
  * Jastrebarsko (Croatia) [old]
  * Grad Vinkovci (Croatia) [old]
  * Grad Sisak (Croatia) [old]
  * Porec bike share (Croatia) [old]
  * eMobi (Croatia) [old]
  * Grad Drniš (Croatia) [old]
  * Grad Križevci (Croatia) [old]
  * Grad Pula (Croatia) [old]
  * Grad Split (Croatia) [old]
  * nextbike Croatia [old]
  * Grad Ivanić-Grad (Croatia) [old]
  * Grad Karlovac (Croatia) [old]
  * Grad Makarska (Croatia) [old]
  * Općina Dugopolje (Croatia) [old]
  * Hvar (Croatia) [old]
  * Grad Slavonski Brod (Croatia) [old]
  * Općina Pitomača (Croatia) [old]
  * Grad Zaprešić (Croatia) [old]
  * Grad Vukovar (Croatia) [old]
  * Grad Zadar (Croatia) [old]
* Cyprus
  * nextbike Cyprus
    * **190** Limassol (34.6823, 33.0464)
    * **206** Nicosia (35.1991, 33.4535)
    * **730** Preveza (38.9551, 20.7547)
    * **889** Famagusta  (35.0204, 33.9704)
    * **940** Larnaca (34.9296, 33.6209)
* Czech Republic
  * nextbike Prostejov
    * **549** Prostejov (49.4722, 17.1055)
  * nextbike Ostrava
    * **271** Ostrava (49.8344, 18.2823)
    * **752** Hlučín (49.898, 18.1923)
    * **913** Ludgeřovice (49.8909, 18.2424)
  * nextbike Havířov
    * **637** Havířov (49.7799, 18.4328)
  * nextbike Berounsko
    * **655** Berounsko (49.9616, 14.064)
  * nextbike Brno
    * **660** Brno (49.2345, 16.7094)
    * **767** Kuřim (49.2994, 16.5368)
  * nextbike Praha
    * **661** Praha (50.0592, 14.5761)
    * **736** Říčany (49.9976, 14.6685)
  * nextbike Olomouc
    * **663** Olomouc (49.5929, 17.2459)
  * nextbike Kladno
    * **659** Kladno (50.1435, 14.1082)
  * nextbike Opava
    * **662** Opava (49.9289, 18.2634)
  * nextbike Pardubice
    * **680** Pardubice (50.0343, 15.7812)
  * nextbike Hradec Králové
    * **682** Hradec Králové (50.2079, 15.8334)
  * nextbike Mladoboleslavsko
    * **681** Mladá Boleslav (50.4278, 14.8999)
    * **704** Mnichovo Hradiště (50.5218, 14.9741)
  * nextbike Frýdek-Místek
    * **700** Frýdek-Místek (49.6832, 18.3457)
  * nextbike Uherské Hradiště
    * **702** Uherské Hradiště (49.0678, 17.4665)
  * nextbike Zlín
    * **703** Zlín (49.238, 17.6788)
  * nextbike Krnov
    * **707** Krnov (50.0703, 17.8837)
  * nextbike Rychnovsko
    * **708** Rychnovsko (50.1668, 16.2828)
  * nextbike Písek
    * **709** Písek (49.3051, 14.1463)
  * nextbike Jihlava
    * **719** Jihlava (49.4078, 15.6061)
  * nextbike Dvůr Králové
    * **768** Dvůr Králové (50.4278, 15.8162)
  * nextbike Liberec
    * **793** Liberec (50.768, 15.0565)
  * nextbike Vrchlabí
    * **769** Vrchlabí (50.6222, 15.6126)
  * nextbike Klášterec nad Ohří
    * **866** Klášterec nad Ohří (50.386, 13.1946)
  * nextbike Přerov
    * **917** Přerov (49.4574, 17.4408)
  * nextbike Třebíč
    * **863** Třebíč (49.2142, 15.878)
  * nextbike Moravská Třebová
    * **865** Moravská Třebová (49.7573, 16.6635)
  * nextbike Česká Třebová
    * **869** Česká Třebová (49.9041, 16.4428)
  * nextbike Benešov
    * **887** Benešov (49.7808, 14.6928)
  * nextbike Jablonec
    * **876** Jablonec nad Nisou (50.7225, 15.1681)
  * nextbike Hořice
    * **888** Hořice (50.3675, 15.6329)
  * nextbike Pelhřimov
    * **919** Pelhřimov (49.4351, 15.2168)
* France
  * Vélhop - Strasbourg
    * **924** Bischheim (48.6151, 7.75274)
    * **925** Entzheim (48.5328, 7.63653)
    * **926** Geispolsheim (48.5146, 7.64659)
    * **927** Hoenheim (48.6213, 7.75424)
    * **928** Illkirch-Graffenstaden (48.5288, 7.71118)
    * **929** La Wantzenau (48.6586, 7.83085)
    * **930** Lingolsheim (48.5544, 7.6823)
    * **931** Mundolsheim (48.6405, 7.71363)
    * **932** Oberhausbergen (48.6057, 7.68454)
    * **933** Schiltigheim (48.6051, 7.74534)
    * **934** Strasbourg (48.5245, 7.61476)
    * **935** Vendenheim (48.6677, 7.71326)
    * **936** Wolfisheim (48.5876, 7.66803)
* Germany
  * metropolradruhr Germany
    * **129** Dortmund (51.5141, 7.46255)
    * **130** Bochum (51.4813, 7.2133)
    * **131** Bottrop (51.5263, 6.94611)
    * **132** Duisburg (51.4487, 6.77513)
    * **133** Essen (51.4387, 7.14094)
    * **134** Gelsenkirchen (51.5404, 7.07039)
    * **135** Hamm (51.6775, 7.84836)
    * **136** Herne (51.5363, 7.21493)
    * **137** Mülheim a.d.R. (51.4308, 6.87401)
    * **138** Oberhausen (51.4936, 6.85169)
    * **859** Lünen (51.6105, 7.52776)
    * **890** Witten (51.4437, 7.35093)
  * KVV.nextbike
    * **21** Karlsruhe (49.0102, 8.41827)
    * **621** Baden-Baden (48.7365, 8.30482)
    * **627** Bruchsal (49.126, 8.5968)
    * **633** Rheinstetten (48.962, 8.29575)
    * **634** Ettlingen (48.9429, 8.39784)
    * **635** Rastatt (48.86, 8.20386)
    * **722** Gaggenau (48.8039, 8.3233)
  * VRNnextbike
    * **194** Heidelberg (49.4023, 8.67577)
    * **195** Mannheim (49.4869, 8.45638)
    * **266** Ludwigshafen (49.4741, 8.43287)
    * **278** Speyer (49.3126, 8.45295)
    * **332** Bensheim (49.6803, 8.6189)
    * **382** Worms (49.6394, 8.34618)
    * **392** Bürstadt (49.6461, 8.44917)
    * **398** Kaiserslautern (49.4413, 7.75566)
    * **448** Heppenheim (49.6431, 8.63889)
    * **469** Weinheim (49.545, 8.66027)
    * **480** Schwetzingen (49.3863, 8.5756)
    * **482** Frankenthal (Pfalz) (49.5392, 8.35164)
    * **484** Eppelheim (49.4025, 8.6331)
    * **537** Ladenburg (49.4849, 8.61491)
    * **558** Heddesheim (49.5062, 8.60446)
    * **559** Lampertheim (49.5971, 8.46857)
    * **560** Dossenheim (49.4489, 8.67158)
    * **678** Landau in der Pfalz (49.1975, 8.11693)
    * **684** Neustadt an der Weinstraße (49.3448, 8.14902)
    * **747** Limburgerhof (49.4205, 8.3922)
    * **830** Viernheim (49.5424, 8.57817)
    * **864** Walldorf (49.3058, 8.64246)
    * **911** Schriesheim (49.4737, 8.65799)
  * KVB Rad Germany
    * **14** Köln (50.9429, 6.95649)
  * nextbike business Germany
  * Heraeus Hanau
    * **301** Hanau (50.1387, 8.94429)
  * SWA Rad
    * **178** Augsburg (48.3722, 10.8929)
  * nextbike Berlin
    * **362** Berlin (52.5087, 13.3563)
  * nextbike Frankfurt
    * **8** Frankfurt (50.1219, 8.6689)
  * nextbike Kassel
    * **462** Kassel (51.3169, 9.49219)
  * nextbike Düsseldorf
    * **50** Düsseldorf (51.2243, 6.77204)
  * nextbike Erfurt
    * **493** Erfurt (50.9785, 11.0334)
  * nextbike Gießen
    * **467** Gießen (50.5943, 8.68097)
  * nextbike Leipzig
    * **1** Leipzig (51.3435, 12.3637)
  * WK-Bike (Bremen)
    * **379** Bremen (53.0781, 8.80132)
    * **937** Achim (53.009, 9.05286)
  * NEW MöBus nextbike
    * **530** Mönchengladbach (51.1817, 6.43578)
  * Bonn nextbike
    * **547** Bonn (50.7367, 7.09541)
  * nextbike Lippstadt
    * **536** Lippstadt (51.6755, 8.34394)
  * RVK
    * **648** RVK e-Bike (50.7069, 6.87607)
  * Frelo Freiburg
    * **619** Freiburg (47.9958, 7.84453)
  * wupsiRad Leverkusen
    * **607** Leverkusen (51.0341, 7.0182)
  * VAG_Rad
    * **626** Nürnberg (49.4487, 11.0794)
  * sprintRAD
    * **87** Hannover (52.3721, 9.73569)
  * Graben - ready4green
    * **647** Graben (51.1242, 10.8984)
  * nextbike Norderstedt
    * **177** Norderstedt (53.6951, 9.97627)
  * Nibelungen-Bike
    * **657** Braunschweig (52.2597, 10.5307)
  * Potsdam Rad
    * **158** Potsdam (52.3997, 13.0676)
  * meinSiggi
    * **16** Bielefeld (52.0257, 8.53286)
  * Bergisches e-Bike
    * **676** Bergisches e-Bike (51.0192, 7.18025)
  * nextbike Marburg
    * **438** Marburg (50.8019, 8.76444)
  * nextbike Gütersloh
    * **160** Gütersloh (51.9383, 8.33176)
  * nextbike Wiesbaden
    * **7** Wiesbaden (50.0739, 8.24181)
  * nextbike Rüsselsheim am Main
    * **439** Rüsselsheim am Main (49.9881, 8.42142)
  * MOBIbike
    * **685** Dresden (51.0505, 13.7446)
  * Oeynrad
    * **689** Bad Oeynhausen (52.2051, 8.80074)
  * RSVG-Bike
    * **691** RSVG (50.7669, 7.37457)
  * Eifel e-Bike
    * **706** Eifel e-Bike (50.5771, 6.64673)
  * OLi-Bike
    * **754** Oldenburg (53.1448, 8.22485)
  * Pedelec Power Usedom
  * WinsenRad
    * **794** Winsen (Luhe) (53.3547, 10.2067)
  * mobic
    * **817** REVG (50.8493, 6.6687)
  * westBike
    * **807** Erkelenz (51.0753, 6.31233)
    * **808** Geilenkirchen (50.9671, 6.11886)
    * **809** Heinsberg (51.0597, 6.11849)
    * **810** Hückelhoven (51.0529, 6.21933)
    * **811** Wegberg (51.1427, 6.2813)
  * EDEKA Grünheide
    * **819** Grünheide (Mark) (52.4247, 13.8203)
  * nextbike Erlangen
    * **829** Erlangen (49.589, 11.0065)
  * DCS Bike
    * **860** Roche - Mannheim (49.5346, 8.47004)
  * Tecklenburger Land
    * **858** Tecklenburg (52.2189, 7.8124)
  * Landkreis Nordsachsen - Deutschland
    * **867** Schkeuditz (51.3951, 12.226)
  * Unicorn Land (WL)
  * EinfachMobil
    * **155** Offenburg (48.4721, 7.94243)
    * **505** Lahr (48.3396, 7.87376)
    * **885** Achern (48.6322, 8.04194)
  * TIER Roaming
  * TIER temp Brand
    * **941** TIER temp (13, 37)
  * movemix_bike
    * **943** Halle (Saale) (51.4938, 11.9628)
* India
  * Chartered Bike (Bhopal - India)
* Ireland
  * Castletroy Bikes (Ireland)
    * **862** Limerick (52.6629, -8.62726)
  * Navan Bikes (Ireland)
    * **877** Navan (53.6544, -6.68875)
* Italy
  * nextbike Bergamo
    * **728** Bergamo (45.6986, 9.67567)
  * ARVAL
    * **746** Scandicci (43.7701, 11.1592)
  * Nomago Bikes - GO2GO Gorizia
    * **771** Gorizia (45.9469, 13.6208)
* Latvia
  * nextbike LV
    * **128** Rīga (56.9453, 24.1033)
* Mexico
  * YOY - San Luis Potosi
    * **664** San Luis Potosi (22.438, -100.514)
    * **695** Cancún (21.1675, -86.8498)
* Montenegro
  * Budva Bike Share
* Netherlands
  * nextbike Maastricht
* Poland
  * WRM nextbike Poland
    * **148** Wrocław (51.1117, 17.0357)
  * PRM Poznan Poland
  * Opole Bike Poland
  * VETURILO Poland (obsolete) 
  * Nextbike Poland 
  * BIKER Białystok Poland
    * **470** Orlen Białystok (53.1342, 23.1485)
  * KRM Konstanciński Poland
  * GRM Grodzisk Poland
    * **255** Grodzisk Mazowiecki (52.113, 20.6265)
  * Katowice Bike Poland
  * Stalowa Wola miasto rowerów Poland
  * Zgierski Rower Miejski Poland
  * System Rowerów Miejskich w Pszczynie Poland
  * Tyski Rower Miejski Poland
  * Częstochowski Rower Miejski Poland
  * Pruszkowski Rower Miejski Poland
  * Siedlecki Rower Miejski Poland
  * OK Bike Poland
  * Kołobrzeski Rower Miejski Poland
    * **422** Kołobrzeg (54.1764, 15.5759)
  * Kaliski Rower Miejski Poland
  * Rower Miejski Szamotuły Poland (RMS) Poland
    * **446** Szamotuły (52.6112, 16.5819)
  * Rower Miejski w Ostrowie Wielkopolskim Poland
  * Piaseczyński Rower Miejski Poland
    * **461** Piaseczno (52.0733, 21.0269)
  * Koszaliński Rower Miejski Poland
    * **496** Koszalin (54.2026, 16.1678)
  * Sosnowiecki Rower Miejski Poland
  * Pobiedziski Rower Gminny Poland
  * JasKółka
    * **509** Jastrzębie-Zdrój (49.9521, 18.6007)
  * Siemianowicki Rower Miejski Poland
  * Piotrkowski Rower Miejski Poland
  * Płocki Rower Miejski (PRM) Poland
  * Tychowski Rower Miejski Poland
  * Otwocki Rower Miejski Poland
  * Ciechanowski Rower Miejski Poland
  * Koniński Rower Miejski Poland
    * **545** Konin (52.2254, 18.2603)
  * Zielonogórski Rower Miejski Poland
    * **529** Zielona Góra (51.9521, 15.6003)
  * Tarnowski Rower Miejski Poland
  * Kajteroz - Chorzowski Rower Miejski Poland
  * Koło Marek Poland
    * **550** Marki (52.3256, 21.1089)
  * Żyrardowski Rower Miejski Poland
  * Rowerowe Łódzkie Poland (RL)
    * **562** Koluszki (RL) (51.7401, 19.835)
    * **563** Łask (RL) (51.5893, 19.142)
    * **564** Łowicz (RL) (52.1057, 19.9381)
    * **565** Pabianice (RL) (51.6651, 19.3548)
    * **566** Sieradz (RL) (51.5902, 18.7382)
    * **567** Skierniewice (RL) (51.9539, 20.1469)
    * **568** Zduńska Wola (RL) (51.6011, 18.938)
    * **569** Zgierz (RL) (51.8551, 19.4068)
    * **570** Kutno (RL) (52.2317, 19.3564)
    * **571** Łódź (RL) (51.7674, 19.4575)
  * System Roweru Gminnego Poland
  * Luboński Rower Miejski Poland
  * Komornicki System Rowerowy Poland
  * Oleski Rower Miejski Poland
    * **650** Olesno (50.8773, 18.4212)
  * Nextbike Polska
  * Rower Powiatowy Sokołów Podlaski
  * Chełmski Rower
    * **776** Chełm (50.939, 23.4018)
  * ŁoKeR - Łomża
  * VETURILO 3.0
    * **812** Warszawa (52.2244, 21.0196)
  * Wolsztyński Rower Miejski
    * **831** Wolsztyn (52.112, 16.1056)
* Romania
  * nextbike Romania
    * **510** Focșani (45.6947, 27.1851)
  * Drobeta Velopark
    * **693** Drobeta (44.6326, 22.6564)
  * BikeCity Campia Turzii
    * **750** Campia Turzii (46.5489, 23.8797)
  * Buzau VeloCity
    * **800** Buzău (45.145, 26.8242)
  * Topoloveni Bike
    * **832** Topoloveni (44.8105, 25.0801)
* Slovakia
  * Arriva Bike
  * BikeKIA
    * **538** Žilina (49.2205, 18.7413)
* Slovenia
  * Nomago Bikes - KOLESCE
    * **531** Celje (46.237, 15.2689)
    * **535** Laško (46.1458, 15.2312)
    * **555** Žalec (46.2529, 15.1635)
    * **556** Polzela (46.2767, 15.0753)
    * **643** Zreče (46.3751, 15.387)
    * **644** Slovenske Konjice (46.3382, 15.4244)
    * **645** Štore (46.2192, 15.3172)
    * **683** Šentjur (46.2146, 15.394)
    * **821** Vojnik (46.2914, 15.3022)
    * **822** Braslovče (46.2812, 15.0101)
  * Nomago Bikes -  LJUBLJANA
    * **717** Ljubljana (46.0577, 14.5013)
  * Nomago Bikes - GO2GO
    * **688** Nova Gorica (45.9576, 13.6406)
  * Nomago Bikes - ZANAPREJ
    * **725** Zagorje ob Savi (46.1392, 14.9785)
  * Nomago Bikes - KRANJSKA GORA
    * **780** Kranjska Gora (46.4865, 13.7903)
  * Nomago Bikes - PORTOROZ
    * **806** Portorož (45.5054, 13.5979)
  * Nomago Bikes - SLOVENIA
    * **922** Radlje ob Dravi (46.6068, 15.2188)
* Spain
  * moxsi (Las Palmas de Gran Canaria)
    * **408** Las Palmas de Gran Canaria (28.1236, -15.4366)
  * Bilbaobizi (Bilbao)
    * **532** Bilbaobizi (43.2623, -2.93747)
  * Lovesharing (Canary Islands)
    * **638** Lovesharing (Canary Islands) - Gran Canaria (27.8154, -15.5182)
    * **674** Lovesharing (Canary Islands) - Lanzarote (29.0491, -13.5729)
    * **675** Lovesharing (Canary Islands) - Fuerteventura (28.3584, -14.064)
  * ibizi
    * **629** Ibiza-City (38.9066, 1.42046)
  * nextbike León
    * **701** León (42.5672, -5.64972)
  * Getxobizi
    * **749** Getxobizi (43.3437, -3.00751)
  * BBK Klimabizi
    * **772** Urdaibai (43.395, -2.68815)
  * BiciPalma
    * **789** Palma (39.5713, 2.64689)
  * Ambici 
    * **833** AMB (41.4095, 2.17177)
    * **840** Badalona (41.3443, 2.10182)
    * **842** Cornellà de Llobregat (41.3585, 2.07081)
    * **843** Santa Coloma de Gramenet (41.4459, 2.21033)
    * **844** El Prat de Llobregat (41.3239, 2.09317)
    * **845** Castelldefels (41.2816, 1.97678)
    * **846** Viladecans (41.3165, 2.01306)
    * **847** Sant Feliu de Llobregat (41.3835, 2.03693)
    * **848** Esplugues de Llobregat (41.3771, 2.08938)
    * **849** Gavà (41.303, 2.00269)
    * **850** Sant Adrià de Besòs (41.4278, 2.22431)
    * **851** Sant Joan Despí (41.368, 2.05635)
    * **852** Molins de Rei (41.4132, 2.02037)
    * **853** Sant Just Desvern (41.3807, 2.07496)
    * **856** Sant Boi de Llobregat (41.3458, 2.03404)
  * BiciMislata
    * **835** Mislata (39.4713, -0.412331)
* Sweden
  * Styr & Ställ (Sweden, Göteborg)
    * **658** Göteborg (57.6902, 11.9881)
* Switzerland
  * nextbike Switzerland
    * **88** Sursee Plus (47.1713, 8.10877)
    * **126** Luzern (47.0472, 8.30446)
    * **323** Hergiswil (46.9905, 8.30829)
    * **383** Stans (46.9593, 8.36836)
    * **388** Stansstad (46.9801, 8.34098)
    * **391** Horw (47.0188, 8.30828)
    * **463** Sarnen (46.8963, 8.24614)
    * **464** Wolfenschiessen (46.9079, 8.39767)
    * **465** Oberdorf-Dallenwil (46.9563, 8.38867)
    * **483** Ennetmoos (46.9573, 8.3377)
    * **489** Meggen (47.0453, 8.3769)
    * **491** Kriens (47.0346, 8.27751)
    * **492** Hochdorf / Seetal (47.1667, 8.29159)
    * **624** Ebikon (47.0812, 8.33973)
    * **632** Root (47.1149, 8.39008)
    * **716** Nottwil (47.1357, 8.1357)
    * **738** Eich (47.1521, 8.16872)
    * **854** Sempach (47.1347, 8.19142)
    * **855** Neuenkirch (47.1006, 8.20147)
    * **857** Emmen (47.0743, 8.28266)
    * **861** Triengen-Büron (47.2228, 8.08645)
* Ukraine
  * nextbike (Ukraine)
    * **280** Lviv (49.8344, 24.0353)
    * **522** Kharkiv (49.9896, 36.2411)
    * **525** Ivano Frankivsk (48.9281, 24.7103)
    * **572** Odesa (46.4672, 30.7164)
    * **573** Dnipro (48.4718, 35.0491)
    * **764** Ukraine (49.2362, 31.1535)
  * nextbike Kyiv (Ukraine)
  * nextbike Ukraine Dummy Brand
  * nextbike Vinnitsa (Ukraine)
    * **546** Vinnytsia (49.2324, 28.4659)
* United Kingdom
  * nextbike Stirling
    * **243** Stirling (56.1195, -3.93495)
  * BelfastBikes
    * **238** Belfast (54.6129, -5.89269)
  * Santander Cycles - Milton Keynes
    * **320** Milton Keynes (52.0406, -0.759417)
  * Wheelchair Hospital Coventry
  * OVO Bikes Glasgow
    * **237** Glasgow (55.8589, -4.25549)
  * Dundee-Navigogo 
  * OVO Bikes Cardiff & Vale of Glamorgan
    * **476** Cardiff (51.481, -3.18003)
    * **679** Penarth (51.4365, -3.19113)
  * Santander Cycles - Brunel
    * **487** Brunel University (51.5463, -0.48048)
  * Santander Cycles - Swansea
    * **486** Swansea University (51.606, -3.9243)
  * nextbike West Midlands
  * WESTcargo powered by nextbike
    * **946** Bristol (51.4587, -2.57355)
    * **947** Bath (51.3814, -2.35519)

Extracted from https://maps.nextbike.net/maps/nextbike-official.json?list_cities=1
