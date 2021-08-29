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
    * **417** Salzburg  (47.8014, 13.0458)
  * nextbike Niederösterreich Austria
    * **57** St.Pölten (48.2058, 15.6232)
    * **64** Mödling (48.1047, 16.3202)
    * **142** Wachau (48.3188, 15.4166)
    * **143** Tulln (48.3269, 16.0569)
    * **144** Triestingtal (47.9421, 16.1149)
    * **146** Thermenregion (47.9892, 16.2646)
    * **156** WienerNeustadt (47.8167, 16.2426)
    * **170** Marchfeld (48.2407, 16.9093)
    * **174** Zehn vor Wien (48.3403, 16.279)
    * **395** Groß Enzersdorf (48.1986, 16.5496)
  * Stadtrad Innsbruck Austria
    * **199** Innsbruck (47.2632, 11.3961)
  * nextbike Tirol Austria
    * **286** Serfaus (47.0387, 10.6048)
  * nextbike Klagenfurt Austria
    * **396** Klagenfurt (46.6335, 14.3085)
  * nextbike Burgenland Austria
    * **23** Neusiedler See (47.839, 16.761)
* Bosnia and Herzegovina
  * Sarajevo Bosnia and Herzegovina
    * **350** Sarajevo (43.85, 18.39)
  * BL bike
    * **494** Banja Luka (44.775, 17.1994)
  * Zenica
    * **427** Zenica (44.2033, 17.9184)
* Croatia
  * nextbike Croatia
    * **220** Zagreb (45.7984, 15.9789)
  * Grad Šibenik (Croatia)
    * **248** Šibenik (43.7294, 15.9074)
  * Grad Karlovac (Croatia)
    * **305** Karlovac (45.4905, 15.5503)
  * Grad Slavonski Brod (Croatia)
    * **308** Slavonski Brod (45.1656, 18.0183)
  * Grad Gospić (Croatia)
    * **291** Gospić (44.5469, 15.375)
  * Grad Makarska (Croatia)
    * **324** Makarska (43.2992, 17.0184)
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
  * Grad Metković (Croatia)
    * **424** Metković (43.0654, 17.642)
  * Jastrebarsko (Croatia)
    * **425** Jastrebarsko (45.6692, 15.6541)
  * Grad Drniš (Croatia)
    * **426** Drniš (43.8425, 16.1197)
  * Općina Dugopolje (Croatia)
    * **445** Dugopolje (43.5943, 16.5986)
  * Općina Pitomača (Croatia)
    * **574** Pitomača (45.9077, 17.2622)
  * Grad Split (Croatia)
    * **617** Split (43.5162, 16.4637)
* Cyprus
  * nextbike Cyprus
    * **190** Limassol (34.6823, 33.0464)
    * **206** Nicosia (35.1991, 33.4535)
    * **696** Larnaca (34.9187, 33.6331)
* Czech Republic
  * nextbike Prostejov
    * **549** Prostejov (49.4722, 17.1055)
  * nextbike Ostrava
    * **271** Ostrava (49.8344, 18.2823)
  * nextbike Havířov
    * **637** Havířov (49.7799, 18.4328)
  * nextbike Berounsko
    * **655** Berounsko (49.9616, 14.064)
  * nextbike Brno
    * **660** Brno (49.1911, 16.6148)
  * nextbike Praha
    * **661** Praha (50.0827, 14.4244)
  * nextbike Olomouc
    * **663** Olomouc (49.5929, 17.2459)
  * nextbike Kladno
    * **659** Kladno (50.1435, 14.1082)
  * nextbike Opava
    * **662** Opava (49.9393, 17.8955)
  * nextbike Pardubice
    * **680** Pardubice (50.0343, 15.7812)
  * nextbike Hradec Králové
    * **682** Hradec Králové (50.2079, 15.8334)
  * nextbike Mladá Boleslav
    * **681** Mladá Boleslav (50.4278, 14.8999)
* Finland
  * Oulu Poland
    * **595** Oulu (65.0049, 25.4539)
* Germany
  * UsedomRad Germany
    * **176** Usedom (53.9779, 13.9925)
  * metropolradruhr Germany
    * **129** Dortmund (51.5141, 7.46255)
    * **131** Bottrop (51.5263, 6.94611)
    * **132** Duisburg (51.4487, 6.77513)
    * **133** Essen (51.4425, 7.02301)
    * **134** Gelsenkirchen (51.5404, 7.07039)
    * **135** Hamm (51.6775, 7.84836)
    * **136** Herne (51.5363, 7.21493)
    * **137** Mülheim a.d.R. (51.4308, 6.87401)
    * **138** Oberhausen (51.4936, 6.85169)
  * KVV.nextbike
    * **21** Karlsruhe (49.0102, 8.41827)
    * **621** Baden-Baden (48.7653, 8.23985)
    * **627** Bruchsal (49.126, 8.5968)
    * **633** Rheinstetten (48.962, 8.29575)
    * **634** Ettlingen (48.9429, 8.39784)
    * **635** Rastatt (48.86, 8.20386)
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
    * **477** Hockenheim (49.3227, 8.54258)
    * **480** Schwetzingen (49.3863, 8.5756)
    * **482** Frankenthal (Pfalz) (49.5392, 8.35164)
    * **484** Eppelheim (49.4025, 8.6331)
    * **537** Ladenburg (49.4849, 8.61491)
    * **558** Heddesheim (49.5062, 8.60446)
    * **559** Lampertheim (49.5971, 8.46857)
    * **560** Dossenheim (49.4489, 8.67158)
    * **678** Landau in der Pfalz (49.1975, 8.11693)
    * **684** Neustadt an der Weinstraße (49.3448, 8.14902)
  * KVB Rad Germany
    * **14** Köln (50.9429, 6.95649)
  * SWA Rad
    * **178** Augsburg (48.3676, 10.8646)
  * nextbike Berlin
    * **362** Berlin (52.5087, 13.3563)
  * nextbike Frankfurt
    * **8** Frankfurt (50.1219, 8.6689)
  * nextbike Kassel
    * **462** Kassel (51.3127, 9.47975)
  * nextbike Düsseldorf
    * **50** Düsseldorf (51.2243, 6.77204)
  * nextbike Erfurt
    * **493** Erfurt (50.9785, 11.0334)
  * nextbike Gießen
    * **467** Gießen (50.5943, 8.68097)
  * nextbike Lahr (Pedelecs)
    * **505** Lahr (48.3396, 7.87376)
  * nextbike Leipzig
    * **1** Leipzig (51.3435, 12.3637)
  * WK-Bike (Bremen)
    * **379** Bremen (53.0781, 8.80132)
  * Berlin-Buch Campus
    * **508** Berlin-Buch (52.6364, 13.5029)
  * Santander nextbike Mönchengladbach
    * **530** Mönchengladbach (51.1817, 6.43578)
  * Bonn nextbike
    * **547** Bonn (50.7367, 7.09541)
  * nextbike Lippstadt
    * **536** Lippstadt (51.6755, 8.34394)
  * SAP Walldorf
    * **592** Walldorf (49.2945, 8.62324)
  * RVK
    * **648** RVK-Gesamt (50.7069, 6.87607)
  * Frelo Freiburg
    * **619** Freiburg (47.9958, 7.84453)
  * wupsiRad Leverkusen
    * **607** Leverkusen (51.0699, 6.97632)
  * VAG_Rad
    * **626** Nürnberg (49.4487, 11.0794)
  * Sprottenflotte
    * **613** KielRegion (54.3242, 10.1515)
  * nextbike Hannover
    * **87** Hannover (52.3721, 9.73569)
  * Graben - ready4green
    * **647** Graben (48.1893, 10.8254)
  * nextbike Norderstedt
    * **177** Norderstedt (53.6969, 10.002)
  * Airbus
    * **654** Hamburg Finkenwerder (53.5383, 9.83019)
  * Nibelungen-Bike
    * **657** Braunschweig (52.2598, 10.5318)
  * Potsdam Rad
    * **158** Potsdam (52.3997, 13.0676)
  * flowBie Siggi
    * **16** Bielefeld (52.0257, 8.53286)
  * Bergisches e-Bike
    * **676** Bergisches e-Bike (51.0192, 7.18025)
  * nextbike Marburg
    * **438** Marburg (50.8019, 8.76444)
  * nextbike Gütersloh
    * **160** Gütersloh (51.9383, 8.33176)
  * nextbike Quickborn
    * **256** Quickborn (53.7333, 9.90272)
  * nextbike Wiesbaden
    * **7** Wiesbaden (50.0709, 8.24322)
  * nextbike Offenburg
    * **155** Offenburg (48.4721, 7.94243)
  * nextbike Rüsselsheim am Main
    * **439** Rüsselsheim am Main (49.9881, 8.42142)
  * nextbike Würzburg
    * **281** Würzburg (49.8, 9.93333)
  * MOBIbike
    * **685** Dresden (51.0505, 13.7446)
  * metropolradruhr Bochum
    * **130** Bochum (51.4813, 7.2133)
  * Oeynrad
    * **689** Bad Oeynhausen (52.2051, 8.80074)
  * RSVG-Bike
    * **691** RSVG (50.7669, 7.37457)
* India
  * Chartered Bike (Bhopal - India)
    * **376** Bhopal (23.2467, 77.411)
  * Smartbike (Vijayawada - India)
    * **402** Vijayawada (16.5109, 80.6313)
  * Smartbike (Hyderabad - India)
    * **367** Hyderabad (17.38, 78.4725)
  * Smartbike (New Delhi - India)
    * **511** Delhi (28.6228, 77.2084)
  * Chartered Bike (Ranchi - India)
    * **609** Ranchi (23.341, 85.3075)
  * Smartbike (Chennai - India)
    * **594** Chennai (13.09, 80.27)
* Latvia
  * nextbike LV
    * **128** Rīga (56.9453, 24.1033)
    * **140** Jūrmala (56.9732, 23.8225)
* Lebanon
  * bike4all
    * **375** Byblos (34.1236, 35.6511)
* Malta
  * nextbike Malta
    * **302** Malta (35.9192, 14.4889)
* Mexico
  * YOY - San Luis Potosi
    * **664** San Luis Potosi (22.1577, -100.979)
* Netherlands
  * nextbike Dordrecht
    * **447** Dordrecht (51.7833, 4.69391)
* New Zealand
  * nextbike New Zealand
    * **193** Christchurch (-43.5341, 172.621)
    * **361** Auckland Central (-36.8493, 174.765)
* Poland
  * WRM nextbike Poland
    * **148** Wrocław (51.1115, 17.0257)
    * **618** Wrocław-Wawa (52.2265, 21.0127)
  * PRM Poznan Poland
    * **192** Poznań (52.3669, 17.1599)
    * **394** Stacje Sponsorskie Nextbike PRM (52.4077, 16.9323)
    * **615** Poznań - TEST  (52.232, 20.9956)
  * VETURILO Poland
    * **210** Warszawa (52.2305, 21.0017)
    * **372** Stacje Sponsorskie Nextbike Veturilo (52.2299, 20.9942)
    * **475** Orlen Warszawa (52.2317, 21.0052)
  * BIKER Białystok Poland
    * **245** Białystok (53.1262, 23.1427)
    * **686** Białystok-wawa (52.2811, 21.0148)
  * KRM Konstanciński Poland
    * **247** Konstancin Jeziorna (52.0759, 21.1161)
  * GRM Grodzisk Poland
    * **255** Grodzisk Mazowiecki (52.113, 20.6265)
  * Katowice Bike Poland
    * **342** Katowice (50.2594, 19.0215)
  * Bike_S SRM Poland
    * **346** Szczecin (53.4301, 14.5498)
  * System Legnicki Rower Miejski (SLRM) Poland
    * **363** Legnica (51.2059, 16.1667)
  * Tyski Rower Miejski Poland
    * **413** Tychy (50.1124, 18.9972)
  * Kołobrzeski Rower Miejski Poland
    * **422** Kołobrzeg (54.1762, 15.5761)
  * Kaliski Rower Miejski Poland
    * **431** Kalisz (51.7525, 18.0341)
  * Rower Miejski w Ostrowie Wielkopolskim Poland
    * **452** Ostrów Wielkopolski (51.65, 17.8253)
  * Piaseczyński Rower Miejski Poland
    * **461** Piaseczno (52.0733, 21.0269)
  * Koszaliński Rower Miejski Poland
    * **496** Koszalin (54.2026, 16.1678)
  * Sosnowiecki Rower Miejski Poland
    * **497** Sosnowiec (50.278, 19.1345)
  * Pobiedziski Rower Gminny Poland
    * **504** Pobiedziska (52.4765, 17.2866)
  * Siemianowicki Rower Miejski Poland
    * **519** Siemianowice Śląskie (50.3031, 19.0222)
  * Piotrkowski Rower Miejski Poland
    * **518** Piotrków Trybunalski (51.3975, 19.6779)
  * Płocki Rower Miejski (PRM) Poland
    * **521** Płock (52.5445, 19.7017)
    * **639** Orlen Płock (52.5466, 19.7047)
  * Tychowski Rower Miejski Poland
    * **528** Tychowo (53.9395, 16.2306)
    * **534** Tychowo - Atrakcje turystyczne  (53.9294, 16.2467)
  * Ciechanowski Rower Miejski Poland
    * **523** Ciechanów (52.8763, 20.6102)
  * Koniński Rower Miejski Poland
    * **545** Konin (52.2284, 18.2553)
  * Zielonogórski Rower Miejski Poland
    * **529** Zielona Góra (51.9381, 15.5048)
  * Tarnowski Rower Miejski Poland
    * **548** Tarnów (50.0113, 20.9728)
  * Kajteroz - Chorzowski Rower Miejski Poland
    * **557** Chorzów (50.2925, 18.9635)
  * Koło Marek Poland
    * **550** Marki (52.3256, 21.1089)
  * Żyrardowski Rower Miejski Poland
    * **551** Żyrardów (52.0503, 20.4464)
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
    * **593** Pielgrzymka (51.1185, 15.8153)
  * Luboński Rower Miejski Poland
    * **620** Luboń (52.3461, 16.8765)
  * Komornicki System Rowerowy Poland
    * **630** Komorniki (52.3347, 16.8094)
  * Oleski Rower Miejski Poland
    * **650** Olesno (50.8773, 18.4212)
* Romania
  * nextbike Romania
    * **510** Focșani (45.6947, 27.1851)
  * Drobeta Velopark
    * **693** Drobeta (44.6326, 22.6564)
* Saudi Arabia
  * iBike ( Saudi Arabia )
    * **264** King Abdullah Economic City (22.4053, 39.0815)
* Slovakia
  * Arriva Nitra Slovakia
    * **430** Nitra (48.3088, 18.0783)
  * BikeKIA
    * **538** Žilina (49.2205, 18.7413)
* Slovenia
  * NomagoBikes (Slovenia)
    * **531** Celje (46.252, 15.296)
    * **535** Laško (46.1458, 15.2312)
    * **555** Žalec (46.2529, 15.1635)
    * **643** Zreče (46.3751, 15.387)
    * **644** Slovenske Konjice (46.3382, 15.4244)
    * **645** Štore (46.2192, 15.3172)
    * **683** Šentjur (46.2146, 15.394)
* Spain
  * Sitycleta (Las Palmas)
    * **408** Las Palmas de Gran Canaria (28.1236, -15.4366)
  * Bilbaobizi (Bilbao)
    * **532** Bilbao (43.2623, -2.93747)
  * Lovesharing (Canary Islands)
    * **638** Lovesharing (Canary Islands) - Gran Canaria (27.8154, -15.5182)
    * **674** Lovesharing (Canary Islands) - Lanzarote (29.0491, -13.5729)
    * **675** Lovesharing (Canary Islands) - Fuerteventura (28.3584, -14.064)
  * ibizi
    * **629** Ibiza-City (38.9066, 1.42046)
* Sweden
  * Styr & Ställ (Sweden, Göteborg)
    * **658** Göteborg (57.7038, 11.9648)
* Switzerland
  * nextbike Switzerland
    * **88** Sursee (47.1713, 8.10877)
    * **126** Luzern (47.0472, 8.30446)
    * **323** Hergiswil (46.9905, 8.30829)
    * **383** Stans (46.9593, 8.36836)
    * **388** Stansstad (46.9801, 8.34098)
    * **391** Horw (47.0188, 8.30828)
    * **463** Sarnen (46.8963, 8.24614)
    * **464** Wolfenschiessen (46.9079, 8.39767)
    * **465** Oberdorf (46.9563, 8.38867)
    * **483** Ennetmoos (46.9573, 8.3377)
    * **489** Meggen (47.0453, 8.3769)
    * **490** Küssnacht SZ (47.0856, 8.44145)
    * **492** Hochdorf / Seetal (47.1667, 8.29159)
    * **624** Ebikon (47.0812, 8.33973)
    * **636** Stadt Zug (47.1663, 8.51587)
* Ukraine
  * nextbike (Ukraine)
    * **280** Lviv (49.8344, 24.0353)
    * **522** Kharkiv (49.9896, 36.2411)
    * **525** Ivano Frankivsk (48.9281, 24.7103)
    * **572** Odesa (46.4672, 30.7164)
  * nextbike Vinnitsa (Ukraine)
    * **546** Vinnytsia (49.2324, 28.4659)
* United Kingdom
  * nextbike UK
    * **243** Stirling (56.1195, -3.93495)
  * BelfastBikes
    * **238** Belfast (54.5969, -5.92918)
  * Santander Cycles - Milton Keynes
    * **320** Milton Keynes (52.0406, -0.759417)
  * Co-bikes
    * **354** Exeter (50.7272, -3.53605)
  * nextbike Glasgow
    * **237** Glasgow (55.8589, -4.25549)
  * nextbike Cardiff
    * **476** Cardiff (51.481, -3.18003)
    * **679** Penarth (51.4365, -3.19113)
  * Santander Cycles - Brunel
    * **487** Brunel University (51.5463, -0.48048)
  * University of Surrey
    * **485** University of Surrey (51.2422, -0.590594)
  * Santander Cycles - Swansea
    * **486** Swansea University (51.6106, -3.9764)
  * nextbike Warwick
    * **272** University of Warwick (52.3815, -1.56159)
* United States
  * Healthy Ride Pittsburgh
    * **254** Pittsburgh (40.4349, -79.9794)

Extracted from https://maps.nextbike.net/maps/nextbike-official.json?list_cities=1

