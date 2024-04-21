# Was ist Web Scraping? 

Wenn ihr für ein Forschungsprojekt ein großes Korpus von Texten, Bildern, anderen Dateien oder auch Metadaten zusammenstellen müsst, kann das ohne die richtigen Werkzeuge sehr lange dauern. Wenn ihr beispielsweise 200 Plaintext-Dateien von [wikisource.org](https://de.wikisource.org) manuell herunterladen wollt, müsstet ihr jeden Text erst suchen, dann jedes Mal auf den "Herunterladen"-Button klicken und hier die Parameter für den Download jedes Mal erneut auswählen. Oder ihr wollt vielleicht eine interaktive Karte aller Publikationsjahre und -orte von mehreren Hundert Publikationen erstellen und müsstet diese Informationen manuell aus einem Online-Bibliothekskatalog kopieren.

Vielleicht habt ihr aber auch eine Fragestellung, für deren Beantwortung ihr Daten braucht, auf die ihr ohne Web Scraping gar keinen oder nur sehr eingeschränkten Zugriff habt. Beispielsweise, wenn euch interessiert, ob einige wenige Leser:innen einer Online-Publikation die Kommentarspalten dominieren, oder ob Artikel von vielen verschiedenen Leser:innen kommentiert werden. Wenn diese Fragestellung manuell beantwortet werden soll, muss jede Seite Kommentare durchgeklickt und Usernamen, kommentierte Artikel und Anzahl der Kommentare in eine Exceltabelle kopiert werden. Dieser Arbeitsaufwand schränkt die Anzahl der Artikel, die auf diese Weise analysiert werden können, sehr ein. 

Es gibt jedoch verschiedene Methoden, um solche Arbeiten zu erleichtern: 

1. **API** der Website abrufen: Vielleicht verfügt die Website über eine Schnittstelle, eine sogenannte API, die ihr anzapfen könnt, um direkt die Dateien herunterzuladen. API steht für **A**pplication **P**rogramming **I**nterface und wird verwendet, um anderen den Zugriff auf Daten oder Funktionalitäten einer Anwendung zu ermöglichen, ohne dabei den Quellcode zu offenbaren. Die Inhalte können mit einer simplen Abfrage ("GET-Request") über das Internet-Protokoll HTTP abgerufen werden. 
     + Beispiele: [dracor.org](https://dracor.org/doc/api), [Chronicling America Archive](https://chroniclingamerica.loc.gov/about/api/) 

2. **Web Scraping**: Wenn es keine API gibt, bleiben euch mehrere mögliche Strategien. Um euch für eine Strategie zu entscheiden, müsst ihr euch zunächst mit dem Quellcode der Website vertraut machen. 
     + **Beautiful Soup**: Ist die Website sehr einfach strukturiert, findet ihr den Inhalt der Seite meist auf den ersten Blick direkt zwischen verschiedenen HTML-Tags. In diesem Fall könnt ihr den HTML-Baum parsen und den Inhalt der Elemente mithilfe der Python Bibliothek BeautifulSoup extrahieren.
Beispiele: [quotes.toscrape.com](https://quotes.toscrape.com/), [projekt-gutenberg.org](https://www.projekt-gutenberg.org), [fanfiction.net](https://www.fanfiction.net)
     + **Selenium**: Viele Webseiten sind jedoch nicht so simpel aufgebaut. Hier werden Inhalte "dynamisch" geladen, das heißt, erst dann, wenn ein:e Nutzer:in die Seite besucht, auf ein Element klickt oder weiterscrollt, werden Inhalte geladen. Hier kommen komplexe Web Scraping Strategien zum Einsatz, die wir nur oberflächlich behandeln können. Zum Scrapen solcher Inhalte verwenden wir Python Selenium.  
Beispiele:[quotes.toscrape.com/js](https://quotes.toscrape.com/js), [twitter.com](https://twitter.com/), [youtube.com](https://www.youtube.com/)

Da viele Webscraping-Tutorials im Web die Begriffe "statische und dynamische Webseiten" verwenden, um zwischen verschiedenen Webscraping-Strategien zu unterscheiden, dienen uns diese Begriffe zu Beginn als Orientierung. Wir werden aber im Laufe des Semesters sehen, dass diese Unterscheidung zwischen "statischen" und "dynamischen" Webseiten eigentlich nicht ganz korrekt ist. 
In diesem Seminar werden wir uns mit allen drei Methoden auseinandersetzen. Der Schwerpunkt liegt dabei auf dem "Scrapen" statischer Webseiten und API-Abfragen, es werden aber auch Strategien zum Scrapen dynamischer Webseiten vorgestellt. 

```{note}
Je nach **Definition** kann argumentiert werden, dass Datenextraktion mithilfe von  API-Abfragen auch eine Form des Web Scraping ist, genauso wie das manuelle Kopieren von Websiteinhalten. Im engeren und gängigeren Sinne beschreibt Web Scraping nur das unter Punkt 2 beschriebene Parsen und Extrahieren von Inhalten aus Webseiten. Trotzdem werdet ihr in diesem Seminar lernen, wie mithilfe von einfachen Python-Skripten API-Abfragen gestellt werden können, weil das eine deutlich sauberere und einfachere Methode ist. 
```


