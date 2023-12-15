# APIs


### Was sind APIs?

Kurze Erklärung im Videoformat: [https://youtu.be/KLe2lCEy-Xw?t=76](https://youtu.be/KLe2lCEy-Xw?t=76)

API steht für Application Programming Interface, auf Deutsch als "Anwendungsprogrammierschnittstelle" übersetzt. 
APIs ermöglichen die Kommunikation zwischen Softwaresystemen bzw. Programmen, also die "Maschine-zu-Maschine"-Kommunikation. 
Entwickler:innen können APIs nutzen, um auf Daten oder Dienste anderer Softwaresysteme zuzugreifen und in ihren eigenen Code einzubinden. 
Das Konzept kennen wir im Grunde bereits: Auch beim Aufruf von Funktionen aus verschiedenen Bibliotheken oder Modulen in Python haben wir bereits Schnittstellen verwendet, um auf vordefinierte Funktionen zuzugreifen, ohne die Implementierungsdetails zu kennen.

Man kann sich eine API also vielleicht abstrakt wie eine Tür vorstellen, durch die Programme Informationen anfordern oder teilen können. 
Sie definiert, welche Anfragen gestellt werden können, wie die Antworten aussehen und wie man auf die gewünschten Informationen zugreifen kann. 

Wenn wir in diesem Abschnitt von APIs sprechen, dann meinen wir aber eine ganz bestimmte Art von API: Web-APIs, und genauer gesagt APIs, die von verschiedenen Websitebetreiber:innen gezielt für den Zugriff auf Daten bereitgestellt werden.  

### Web-APIs

Web-APIs ermöglichen verschiedenen (Web-)Anwendungen, und konkret Client und Server, miteinander zu kommunizieren und Daten auszutauschen. 

Beim Aufruf der Seite [https://quotes.toscrape.com/js/](https://quotes.toscrape.com/js/) haben wir beispielsweise mithilfe der Browser-Entwicklertools beobachtet, dass unter dem Tab "Netzwerk" mehrere HTTP-Anfragen gestellt wurden.
Es wurde zum Beispiel eine Javascript-Datei mithilfe einer HTTP-Anfrage vom Webserver angefragt. 
Diese Anfrage hat der Browser "automatisch" gestellt, ohne, dass wir dafür etwas tun mussten. Dabei hat der Browser unter der Moterhaube auf eine Web-API zugegriffen, genauer gesagt auf eine Browser-API, die im Browser "vorinstalliert" ist.

APIs können aber auch von Websitebetreiber:innen selbst bereitgestellt werden, um Nutzer:innen und anderen Anwendungen einen direkten Zugang zu Daten auf dem Server zu ermöglichen.
Genau diese APIs können wir als Forscher:innen anzapfen, um Forschungsdaten direkt herunterzuladen, zum Beispiel Metadaten zum Bestand eines Archivs, Statistiken, oder sogar Volltexte, Musik- oder Bildateien. 

Bei der Entwicklung von Web-APIs greifen Entwickler:innen auf vordefinierte "Architekturstile" zurück, also auf Ansätze, wie die Gesamtstruktur einer API entworfen wird. 
Die meist verwendete Ansatz zum Entwerfen von dieser Art von Web-API nennt sich REST (Representational State Transfer, dt. "Repräsentationsstatustransfer").
APIs, die nach diesem Ansatz implementiert sind, nennt man auch RESTful APIs.
RESTful APIs nutzen zur Kommunikation zwischen Client und Server das HTTP-Protokoll.
Da REST APIs HTTP verwenden, können bei der Abfrage von Ressourcen über RESTful APIs ebenfalls die HTTP-Methode GET verwendet werden. 

:::{figure-md} 
<img src="rest_api.png" alt="RESTful API Schaubild" class="bg-transparent" width="80%">

Schaubild RESTful API. Bild: https://www.youtube.com/watch?v=-mN3VyJuCjM
:::

### Welche Daten können über APIs abgerufen werden? 

Standardmäßig ist der Body einer HTTP-Antwort auf eine Anfrage über eine REST API ein JSON-String.  
JSON ist ein Datenformat in menschenlesbarer Textform zum Zweck des Datensaustauschs zwischen Anwendungen.
Die Syntax einer JSON-Datei sieht in etwa so aus wie ein Python-Dictionary. 

RESTful APIs können aber auch so konfiguriert werden, dass sie Daten direkt in anderen Formaten zurückgeben, zum Beispiel als Plaintext oder Bilddateien. 
Die genaue Konfiguration und das unterstützte Spektrum an Antwortformaten hängen von der konkreten Implementierung der API ab.

Zur Abfrage einer Ressource wird dabei in der HTTP-Anfrage eine URI (= Uniform Resource Identifier), also in dem Fall ein Pfad zu einer konkreten Ressource auf einem Server, angegeben.
Diese URIs nennen sich dann auch Endpunkte oder "Endpoints".  

Ein Unternehmen kann zum Beispiel über eine öffentliche API mithilfe verschiedener URIs verschiedene Arten von Daten bereitstellen.
Im Beispiel unten wird eine Auflistung aller alle Nutzer:innen eines sozialen Netzwerks im JSON-Format als Antwort auf die HTTP-Anfrage zurückgegeben, aber es sind auch zwei weitere Endpunkte abgebildet: Eine Auflistung aller Posts der Nutzer:innen sowie Daten zu deren Follower:innen.

:::{figure-md} 
<img src="rest_api_3.png" alt="RESTful API Schaubild" class="bg-transparent" width="80%">

Schaubild Beispielabfrage über eine RESTful API. Bild: [Alexander Barge](https://mediathek.htw-berlin.de/video/VL-6-2D-Prog2E-mobiler-Anwendungen3A-APIs-26amp3B-Schnittstellen2DEntwicklung/b748cb18680d2f27a66b05c6a788c7fc)
:::

### Wer kann APIs benutzen?

Manche APIs sind öffentlich zugänglich (Public APIs), andere sind öffentlich zugänglich, aber erfordern eine Authentifizierung via API Key. 
Der Key kann normalerweise recht unbürokratisch und kostenlos über die Dokumentationsseiten zu der Schnittstelle beantragt werden. 
Ein Beispiel hierfür ist die API des Guardian: https://open-platform.theguardian.com/documentation/. 
Aber es gibt auch APIs, die nur über einen proprietären Key angezapft werden dürfen. 
Die vormals kostenlose Twitter API wurde beispielsweise mit Elon Musks Übernahme des Unternehmens zu einer Bezahl-API. 

### Beispiele

Misc
- Free Open APIs (ohne Authentifizierung) Liste: https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/

Unternehmen 
- Spotify: https://developer.spotify.com/documentation/web-api
- Twitter: https://developer.twitter.com/en/docs/twitter-api
- OpenAI: https://openai.com/blog/openai-api

Institutionen 
- API-Portal des Bundes: https://bund.dev/ 
(inklusive DWD-API, Autobahn API, NINA Api,..)
- Vorlesungsverzeichnis TU Chemnitz: https://www.tu-chemnitz.de/verwaltung/vlvz/api/doc/index.html

Medien 
- The Guardian: https://open-platform.theguardian.com/documentation/
Tutorial: How to Use the Guardian's API: https://gist.github.com/dannguyen/c9cb220093ee4c12b840
- The New York Times: https://developer.nytimes.com/
- Überblick: https://upload-magazin.de/6778-offene-medien-ein-uberblick-uber-apis-bei-verlagen-und-co/

Forschungsprojekte, spezialisierte Forschungsdatenbanken: 
- Dracor: https://dracor.org/doc/api
https://github.com/dracor-org/dracor-api
https://exist-db.org/exist/apps/doc/devguide_rest
https://stackoverflow.com/questions/48123867/open-api-vs-rest-api-difference

Bibliotheken: 
- Münchener DigitalisierungsZentrum: https://digitale-sammlungen.de/de/schnittstellen
- Staatsbibliothek Berlin: https://lab.sbb.berlin/dc/ 
https://gist.github.com/cneud/ba595b0d70413c952d64154646f560cf 
- HathiTrust: https://www.hathitrust.org/data 
https://www.hathitrust.org/data_api
- Deutsche Digitale Bibliothek: https://pro.deutsche-digitale-bibliothek.de/daten-nutzen/schnittstellen

Archive
- Internet Archive: https://archive.org/developers/index-apis.html
https://blog.archive.org/2013/07/04/metadata-api/
- Archives Portal Europe: https://deprecated.archivesportaleurope.net/information-api
- LOC (s.u.)

LOC APIs
- https://www.loc.gov/apis/
- https://www.loc.gov/apis/additional-apis/
- https://guides.loc.gov/digital-scholarship/accessing-digital-materials#s-lib-ctab-26648178-2
- Chronicling America API: https://chroniclingamerica.loc.gov/about/api/
- Microservices: https://www.loc.gov/apis/micro-services/
Darunter Text Services: https://www.loc.gov/apis/micro-services/text-services/
Und Streaming Services: https://www.loc.gov/apis/micro-services/streaming-services/


LOC Collections
- American Archive of Public Broadcasting APIhttps://github.com/WGBH-MLA/AAPB2#api
- Digital Collections: Audio Recordings: https://www.loc.gov/collections/?fa=original-format:sound+recording
- American English Dialect Recordings: https://www.loc.gov/collections/american-english-dialect-recordings-from-the-center-for-applied-linguistics/


LOC Tutorials 
- LOC for robots: https://labs.loc.gov/lc-for-robots
- images: https://github.com/LibraryOfCongress/data-exploration/blob/master/loc.gov%20JSON%20API/Accessing%20images%20for%20analysis.ipynb
- Chronicling America API Tutorial: https://github.com/LibraryOfCongress/data-exploration/blob/master/Chronicling%20America%20API/ChronAm%20API%20Samples.ipynb
- working with sound files: https://github.com/LibraryOfCongress/data-exploration/blob/master/Data%20Sets/Web%20Archives/loc_goes_lofi.ipynb

Before you scrape...
- Beschränkungen für die Nutzung der LOC-API: https://www.loc.gov/apis/json-and-yaml/working-within-limits


Manchmal gibt es auch Institutionen, die keine API bereitstellen, sondern direkt ganze Korpora zum Donwload bereitstellen, zum Beispiel: 
- Deutsches Textarchiv: https://www.deutschestextarchiv.de/download
- European Literary Text Collection (ELTeC): https://github.com/COST-ELTeC/ELTeC
Download über Github, z.B. für die deutschen Texte: https://github.com/COST-ELTeC/ELTeC-deu
Assoziiertes Projekt: https://www.distant-reading.net/

### Praxis

In der heutigen Stunde und in der Stunde nächste Woche werden wir uns zwei APIs genauer ansehen. 
Und ihr werdet lernen, wie ihr mithilfe von Python Abfragen an die APIs stellt, um bestimmte Daten zu erhalten. 
Zunächst schauen wir uns die DraCor-API an, und danach die API der Library of Congress. 


### Quellen 

```{bibliography}
   :list: enumerated
   :filter: keywords % "apis" or keywords % "dop_07"
```
