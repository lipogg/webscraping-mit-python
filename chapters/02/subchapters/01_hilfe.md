# Hilfe!! 

Oft kommt es beim Coden zu komischen Fehlermeldungen, die mehr verwirren als helfen. Häufig steckt aber ein ganz simpler Flüchtigkeitsfehler dahinter. In diesem Fall gilt:

**1. Syntax und Rechtschreibung überprüfen.** Fehlt vielleicht nur eine Klammer? Ist die Variable wirklich richtig geschrieben? Sind wirklich alle notwendigen Pakete installiert und geladen?

**2. Fehlermeldung kopieren und googeln.** Bestimmt hatte schonmal jemand anderes dasselbe Problem und bestenfalls findet sich eine Lösung auf [https://stackoverflow.com/](https://stackoverflow.com/) oder in einem anderen Forum.

**3. ChatGPT fragen.** Das Codesnippet an ChatGPT senden und nach möglichen Fehlern fragen. 

**4. Hilfeseiten aufrufen.** In JupyterLite und JupyterLab gibt es verschiedene Möglichkeiten, Hilfe zu bekommen. Wenn ihr nicht versteht, was eine bestimmte Funktion macht, oder wenn ihr Informationen zu einer Variable abrufen wollt, könnt ihr in einer neuen Codezelle einfach den Namen der Variable oder Funktion wie folgt eingeben und ausführen: `variablenname?` bzw. `funktionsname?`. Alternativ könnt ihr in der Menüzeile oben in JupyterLite/JupyterLab auf "Help" und dann auf "Show Contextual Help" klicken. Das öffnet einen zweiten Tab neben eurem geöffneten Notebook. Wenn ihr den Cursor dann direkt neben eine Funktion oder Variable bewegt, werden in dem neuen Fenster Informationen zu dem Objekt angezeigt. Wenn ihr Fragen zum JupyterLab Interface selbst habt, schaut in die JupyterLab Dokumentation: [https://jupyterlab.readthedocs.io](https://jupyterlab.readthedocs.io) 

Manchmal macht das Skript aber auch einfach nicht das, was es soll, ohne, dass eine Fehlermeldung entsteht. In diesem Fall liegt wahrscheinlich ein logischer Fehler im Programmablauf vor. Für diesen Fall gibt es eine Strategie, die Rubber Ducking oder Quietscheentchen-Debugging genannt wird.

**5. Rubber Ducking oder Quietscheentchen-Debugging.** Wenn nichts mehr hilft, hilft nur eins: Den Code einer Person, die nichts davon versteht - oder eben einem Quietscheentchen, Zeile für Zeile erklären. Dabei fallen oft logische Fehler auf, die das Problem verursachen.

**6. Python Tutor.** Um besser zu verstehen, was eigentlich passiert, wenn (einfacher) Python-Code ausgeführt wird, könnt ihr euren Code auf [https://pythontutor.com](https://pythontutor.com/python-debugger.html) ausführen. Die Website visualisiert, was in jedem Ausführungsschritt passiert, zum Beispiel, welcher Wert auf dem Bildschirm ausgegeben wird, in welchem Programmabschnitt eine Variable sichtbar ist (Scope) und welchen Objekten wann Speicherplatz zugewiesen wird.

**7. Hilfe holen.** Falls ihr im Laufe des Seminars ein Problem habt, das ihr selbst nicht lösen könnt, könnt ihr einen Screenshot für die nächste Sitzung mitbringen oder mir eine E-Mail an l.poggel@fu-berlin.de schreiben.

Wenn ihr euren Code in JupyterLite oder JupyterLab ausführt und alles richtig aussieht, aber beim Ausführen der Zelle nichts ausgegeben wird, überprüft, ob irgendeine Codezelle im Notebook vielleicht gerade noch ausgeführt wird. Das erkennt ihr an dem Sternchen `[*]` neben der Codezelle. In diesem Fall solltet ihr abwarten, bis die Ausführung beendet ist, oder die Ausführung abbrechen, indem ihr in der Menüleiste "Kernel" und dann "Shut Down Kernel" auswählt. Ein weiterer häufiger Grund dafür, dass kein Output angezeigt wird ist, dass versehentlich als Typ der Zelle "Raw" statt "Code" ausgewählt wurde. 

Zuletzt kann es natürlich auch vorkommen, dass euch ein Inhalt aus dem Seminar nicht ganz klar ist oder ihr ein weiterführendes Interesse an einem Thema habt. 
Für Python-bezogene Fragen empfehle ich das [Lehrbuch *Learning Python* von Mark Lutz](https://www.oreilly.com/library/view/learning-python-6th/9781098171292/) (6. Aufl. 2025, aktuell als Trialversion verfügbar), die offiziellen [Python-Dokumentationsseiten](https://docs.python.org/3/), und das [Handbuch *Python 3* von Johannes Ernesti und Peter Kaiser](https://openbook.rheinwerk-verlag.de/python/) (online verfügbar in der 5. Aufl. 2017). Zwar sind diese Ressourcen detaillierter und sprachlich nicht immer so zugänglich wie diverse Blogartikel und Youtubevideos, aber die inhaltliche und sprachliche Präzision hilft enorm bei der Entwicklung eines Grundverständnisses nicht nur der Sprache selbst, sondern auch der dahinterstehenden allgemeinen Programmierkonzepte. 
Eine Übersicht über die wichtigsten Tastenkombinationen im Umgang mit JupyterLite und JupyterLab findet ihr [hier](https://gist.github.com/discdiver/9e00618756d120a8c9fa344ac1c375ac). Einen Einstieg in die Markdown-Syntax findet ihr [hier](https://www.markdownguide.org/basic-syntax/).
Für Webscraping-bezogene Fragen verweise ich auf die Literaturhinweise am Ende der entsprechenden Kapitel auf der Kurswebsite.
Eine gründliche Einführung in verschiedene Debugging-Strategien bietet [Robert Metzger, Debugging by Thinking](https://doi.org/10.1016/B978-1-55558-307-1.X5000-9). 
Für die in diesem Seminar besprochenen Hintergründe zum Aufbau und Rendering von Webseiten, der Kommunikation zwischen Client und Server und andere Themen aus der Webentwicklung empfehle ich [Philip Ackermann, Full Stack Web Development](https://books.google.com.co/books?id=8PMiEQAAQBAJ).  


