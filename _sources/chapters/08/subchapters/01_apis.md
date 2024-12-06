# APIs


### Was sind APIs?

Kurze Erklärung im Videoformat: [https://youtu.be/KLe2lCEy-Xw?t=76](https://youtu.be/KLe2lCEy-Xw?t=76)

API steht für Application Programming Interface, auf Deutsch als "Anwendungsprogrammierschnittstelle" übersetzt. 
APIs ermöglichen die Kommunikation zwischen Softwaresystemen bzw. Programmen, also die "Maschine-zu-Maschine"-Kommunikation. 
Entwickler:innen können APIs nutzen, um auf Daten oder Dienste anderer Softwaresysteme zuzugreifen und in ihren eigenen Code einzubinden. 
Das Konzept kennen wir im Grunde bereits: Auch beim Aufruf von Funktionen aus verschiedenen Bibliotheken oder Modulen in Python haben wir bereits Schnittstellen verwendet, um auf vordefinierte Funktionen zuzugreifen, ohne die Implementierungsdetails zu kennen.

Man kann sich eine API also vielleicht abstrakt wie eine Tür vorstellen, durch die Programme Informationen anfordern oder teilen können. 
Sie definiert, welche Anfragen gestellt werden können, wie die Antworten aussehen und wie man auf die gewünschten Informationen zugreifen kann. 

Wenn wir in diesem Abschnitt von APIs sprechen, dann meinen wir aber eine ganz bestimmte Art von API: Web-APIs, und genauer gesagt Web-APIs, die von verschiedenen Websitebetreiber:innen gezielt für den Zugriff auf Daten bereitgestellt werden.  

### Web-APIs

:::{figure-md} 
<img src="web_api.png" alt="REST API Schaubild" class="bg-transparent" width="80%">

Schaubild Web-API. Quelle: [Frank Dopatka (2024)](https://www.youtube.com/watch?v=FfR9B5rPBuw)
:::

Web-APIs ermöglichen verschiedenen (Web-)Anwendungen, und konkret Client und Server, miteinander zu kommunizieren, Daten auszutauschen und die Funktionalitäten der jeweiligen Anwendung zu nutzen. 

Beim Aufruf der Seite [https://quotes.toscrape.com/js/](https://quotes.toscrape.com/js/) haben wir beispielsweise mithilfe der Browser-Entwicklertools beobachtet, dass unter dem Tab "Netzwerk" mehrere HTTP-Anfragen gestellt wurden.
Es wurde zum Beispiel eine Javascript-Datei mithilfe einer HTTP-Anfrage vom Webserver angefragt. 
Diese Anfrage hat der Browser "automatisch" gestellt, ohne, dass wir dafür etwas tun mussten. Dabei hat der Browser unter der Motorhaube auf eine Web-API zugegriffen, genauer gesagt auf eine Browser-API, die in den Browser integriert ist.

APIs können aber auch von Websitebetreiber:innen selbst bereitgestellt werden, um Nutzer:innen und anderen Anwendungen einen direkten Zugang zu Daten auf dem Server zu ermöglichen.
Genau diese APIs können wir als Forscher:innen anzapfen, um Forschungsdaten direkt herunterzuladen, zum Beispiel Metadaten zum Bestand eines Archivs, Statistiken, oder sogar Volltexte, Musik- oder Bildateien. 

Bei der Entwicklung von Web-APIs greifen Entwickler:innen auf vordefinierte Paradigmen zurück, also auf Ansätze, wie die Gesamtstruktur einer API entworfen wird. 
Die meist verwendete Ansatz zum Entwerfen von dieser Art von Web-API nennt sich REST (Representational State Transfer, dt. "Repräsentationsstatustransfer").
APIs, die nach diesem Ansatz implementiert sind, nennt man auch REST APIs (oder manchmal RESTful API).
REST APIs nutzen zur Kommunikation zwischen Client und Server das HTTP-Protokoll.
Da REST APIs HTTP verwenden, können bei der Abfrage von Ressourcen über REST APIs ebenfalls die HTTP-Methode GET verwendet werden. 

:::{figure-md} 
<img src="rest_api.png" alt="REST API Schaubild" class="bg-transparent" width="80%">

Schaubild REST API. Quelle: [Alex Xu und Sahn Lam (2022)](https://www.youtube.com/watch?v=-mN3VyJuCjM)
:::

### Welche Daten können über APIs abgerufen werden? 

Bei der Anfrage einer Website war der Body einer erfolgreichen HTTP-Antwort ein HTML-Dokument, das in Python als String repräsentiert wird. 
Standardmäßig ist der Body einer HTTP-Antwort auf eine Anfrage über eine REST API dagegen ein JSON-String. JSON ist ein Datenformat in menschenlesbarer Textform zum Zweck des Datensaustauschs zwischen Anwendungen.
Die Syntax einer JSON-Datei sieht in etwa so aus wie ein Python-Dictionary. 
Während HTML-Strings zur Weiterverarbeitung in BeautifulSoup-Objekte umgewandelt werden können, können JSON-Strings deswegen zur Weiterverarbeitung einfach in Python Dictionaries umgewandelt werden. 

REST APIs können aber auch so konfiguriert werden, dass sie Daten direkt in anderen Formaten zurückgeben, zum Beispiel als Plaintext oder Bilddateien. 
Die genaue Konfiguration und das unterstützte Spektrum an Antwortformaten hängen von der konkreten Implementierung der API ab.

Zur Abfrage einer Ressource wird dabei in der HTTP-Anfrage eine **URI (= Uniform Resource Identifier)**, also in dem Fall ein Pfad zu einer konkreten Ressource auf einem Server, angegeben.
Diese URIs nennen sich dann auch **Endpunkte oder "Endpoints".  

Ein Unternehmen kann zum Beispiel über eine öffentliche API mithilfe verschiedener URIs verschiedene Arten von Daten bereitstellen.
Im Beispiel unten wird eine Auflistung aller alle Nutzer:innen eines sozialen Netzwerks im JSON-Format als Antwort auf die HTTP-Anfrage zurückgegeben, aber es sind auch zwei weitere Endpunkte abgebildet: Eine Auflistung aller Posts der Nutzer:innen sowie Daten zu deren Follower:innen.

:::{figure-md} 
<img src="rest_api_3.png" alt="REST API Schaubild" class="bg-transparent" width="80%">

Schaubild Beispielabfrage über eine REST API. Quelle: [Alexander Barge](https://mediathek.htw-berlin.de/video/VL-6-2D-Prog2E-mobiler-Anwendungen3A-APIs-26amp3B-Schnittstellen2DEntwicklung/b748cb18680d2f27a66b05c6a788c7fc)
:::

### Wer kann APIs benutzen?

Manche APIs sind öffentlich zugänglich (Public APIs), andere sind öffentlich zugänglich, aber erfordern eine Authentifizierung via API Key. 
Der Key kann normalerweise recht unbürokratisch und kostenlos über die Dokumentationsseiten zu der Schnittstelle beantragt werden. 
Ein Beispiel hierfür ist die API des Guardian: https://open-platform.theguardian.com/documentation/. 
Aber es gibt auch APIs, die nur über einen proprietären Key oder nur nach einer Anmeldung angezapft werden dürfen. 
Die vormals kostenlose Twitter API wurde beispielsweise mit Elon Musks Übernahme des Unternehmens zu einer Bezahl-API, und zur Verwendung der TikTok Research API ist eine Bewerbung mit einer Vorstellung des eigenen Forschungsprojekts notwendig. 

### Beispiele

Zur Inspiration: [Cool stuff made with cultural heritage APIs](http://museum-api.pbworks.com/w/page/21933412/Cool%20stuff%20made%20with%20cultural%20heritage%20APIs)

Überblick
- Free Open APIs (ohne Authentifizierung) Liste: https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/
- ProgrammableWeb API Directory (via Wayback Machine): https://web.archive.org/web/20220131204631/https://www.programmableweb.com/apis/directory?page=1

Unternehmen 
- Spotify: https://developer.spotify.com/documentation/web-api
- Twitter: https://developer.twitter.com/en/docs/twitter-api
- OpenAI: https://openai.com/blog/openai-api
- Reddit: https://www.reddit.com/dev/api
- TikTok: https://developers.tiktok.com/products/research-api/
- Springer Verlag: https://support.springer.com/en/support/solutions/articles/6000195668-springerlink-api-details

Institutionen
- API-Portal des Bundes: https://bund.dev/ 
(inklusive DWD-API, Autobahn API, NINA Api,..)
- Gemeinsame Normdatei (GND): https://lobid.org/gnd/api ([über die GND](https://www.dnb.de/DE/Professionell/Standardisierung/GND/gnd_node.html))
- Wikimedia Foundation (Wikipedia, Wikidata): https://developer.wikimedia.org/de/build-tools/apis/
- World Bank: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589
- Vorlesungsverzeichnis TU Chemnitz: https://www.tu-chemnitz.de/verwaltung/vlvz/api/doc/index.html

Medien 
- The Guardian: https://open-platform.theguardian.com/documentation/
Tutorial: How to Use the Guardian's API: https://gist.github.com/dannguyen/c9cb220093ee4c12b840
- The New York Times: https://developer.nytimes.com/
- Überblick: https://upload-magazin.de/6778-offene-medien-ein-uberblick-uber-apis-bei-verlagen-und-co/

Forschungsprojekte, spezialisierte Forschungsdatenbanken: 
- Dracor: https://dracor.org/doc/api
- CorrespSearch: https://correspsearch.net/en/api.html
- World Historical Gazetteer (historische Ortsnamen): https://whgazetteer.org/usingapi/

Weitere Datenbanken: 
- GeoNames: https://www.geonames.org/export/web-services.html
- Pantheon World: https://pantheon.world/data/api
- OpenCitations: https://opencitations.net/querying

Archive und Museen:
- Internet Archive: https://archive.org/developers/index-apis.html
https://blog.archive.org/2013/07/04/metadata-api/
- Archives Portal Europe: https://deprecated.archivesportaleurope.net/information-api
- E-Manuscripta: https://www.e-manuscripta.ch/wiki/apiinfo
- Europeana: https://pro.europeana.eu/page/apis
- The Museum of Modern Art: https://api.moma.org/

Bibliotheken: 
- Münchener DigitalisierungsZentrum: https://digitale-sammlungen.de/de/schnittstellen
- Staatsbibliothek Berlin: https://lab.sbb.berlin/dc/ 
https://gist.github.com/cneud/ba595b0d70413c952d64154646f560cf 
- HathiTrust: https://www.hathitrust.org/data 
https://www.hathitrust.org/data_api
- Deutsche Digitale Bibliothek: https://pro.deutsche-digitale-bibliothek.de/daten-nutzen/schnittstellen
- Digital Public Library of America: https://dp.la/guides/for-developers
- National Library of France: https://api.bnf.fr/api-document-de-gallica
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
- American Archive of Public Broadcasting: https://github.com/WGBH-MLA/AAPB2#api
- Digital Collections – Audio Recordings: https://www.loc.gov/collections/?fa=original-format:sound+recording
- American English Dialect Recordings: https://www.loc.gov/collections/american-english-dialect-recordings-from-the-center-for-applied-linguistics/


LOC Tutorials 
- LOC for robots: https://labs.loc.gov/lc-for-robots
- Accessing images: https://github.com/LibraryOfCongress/data-exploration/blob/master/loc.gov%20JSON%20API/Accessing%20images%20for%20analysis.ipynb
- Chronicling America API Tutorial: https://github.com/LibraryOfCongress/data-exploration/blob/master/Chronicling%20America%20API/ChronAm%20API%20Samples.ipynb
- Working with sound files: https://github.com/LibraryOfCongress/data-exploration/blob/master/Data%20Sets/Web%20Archives/loc_goes_lofi.ipynb

Before you scrape...
- Beschränkungen für die Nutzung der LOC-API: https://www.loc.gov/apis/json-and-yaml/working-within-limits


Manchmal stellen Institutionen keine API bereit, sondern bieten direkt ganze Korpora zum Download als "Data Dump", zum Beispiel: 
- Deutsches Textarchiv: https://www.deutschestextarchiv.de/download
- European Literary Text Collection (ELTeC): https://github.com/COST-ELTeC/ELTeC
Download über Github, z.B. für die deutschen Texte: https://github.com/COST-ELTeC/ELTeC-deu
Assoziiertes Projekt: https://www.distant-reading.net/
- SlaveVoyages Datenbank: https://www.slavevoyages.org/american/downloads#intra-american-database-downloads/0/en/
- Digitale Sammlung Deutscher Kolonialismus: https://www.deutschestextarchiv.de/dsdk/
- Journal of Open Humanities Data: https://openhumanitiesdata.metajnl.com/articles
- HathiTrust derived datasets: https://analytics.hathitrust.org/deriveddatasets; https://htrc.atlassian.net/wiki/spaces/COM/pages/43287791/HTRC+Derived+Datasets
- Somar Social Media Archive: https://socialmediaarchive.org/
- Digitale Sammlungen der Österreichischen Nationalbibliothek: https://labs.onb.ac.at/de/datasets/

In diesem Fall sind natürlich weder Web Scraping noch eine API notwendig, um an die Daten zu gelangen, aber es muss beachtet werden, dass diese Daten nicht unbedingt tagesaktuell sind. 
Bevor ihr anfangt, ein Skript zum Scrapen einer Seite zu schreiben, solltet ihr immer überprüfen, ob die gesuchten Daten nicht vielleicht auch über eine API oder als Data Dump verfügbar sind.

### Praxis

In der heutigen Stunde und in der Stunde nächste Woche werden wir uns zwei APIs genauer ansehen. 
Und ihr werdet lernen, wie ihr mithilfe von Python Daten über die APIs abfragen könnt. 
Zunächst schauen wir uns die DraCor-API an, und danach die API der Library of Congress. 
Am Ende des Semesters kommen wir noch einmal auf das Thema zurück und betrachten Authentifizierungs- und Autorisierungsmechanismen am Beispiel der TikTok Research API.  


### Quellen 

```{bibliography}
   :list: enumerated
   :filter: keywords % "apis" or keywords % "dop_07" or keywords % "dop_08"
```
