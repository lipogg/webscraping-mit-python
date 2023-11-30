# Installation und Setup

### Die richtige Python-Version

Generell wird empfohlen, nicht mit der allerneusten Python-Version zu arbeiten, sondern mit der vorletzten Python-Release. 
Die aktuelle Python-Release ist 3.11, in der Version 3, also 3.11.3. 
Das heißt die Release, mit der wir arbeiten sollten, ist idealerweise 3.10. 

Je nachdem, wie alt euer Computer ist und welche Version euer Betriebssystem hat, werden bei euch verschiedene Python-Versionen vorinstalliert sein.
Wenn ihr Windows verwendet, ist Python generell nicht vorinstalliert. 
Da wir also in einer Gruppe arbeiten, in der die Startvoraussetzungen sehr verschieden sind, werden wir zur Installation der richtigen 
Python-Version und für das Setup von JupyterLab Anaconda verwenden. 

### Was ist Anaconda? 

Anaconda vereint verschiedene Komponeneten: Python selbst, sowie einen sogenannten Paketmanager, der die Verwaltung verschiedener Pakete ermöglicht, eine Entwicklungsumgebung und ein graphisches User-Interface. 
Die verschiedenen Funktionalitäten, die Anaconda bereitstellt, können auch über das Terminal / die Kommandozeile verwendet werden.
Wir werden Anaconda nur herunterladen und anschließend die Kommandozeile verwenden, um JupyterLab zu installieren. 


### Anaconda installieren

1. Öffnet die Anaconda-Website: https://www.anaconda.com/download/ und ladet die Installationsdatei herunter.\
**Falls ihr einen Mac habt**, müsst ihr neben dem Download-Button auf den Pfeil klicken und zwischen der Installationsdatei für Intel und M1/M2 Macs auswählen. Wenn ihr nicht wisst, welchen Prozessor euer Mac hat, schaut unter Apple-Menü -> "Über diesen Mac" nach.  
2. Führt die Installationsdatei aus und folgt den Anweisungen. \
**Achtung**: Falls eine Option angezeigt wird, Anaconda zum Pfad hinzuzufügen ("Add Anaconda to PATH"), diese Option NICHT auswählen. 
Falls eine Option angezeigt wird, Anaconda als default Python-Version zu registreiern (Register Anaconda as my default Python), diese Option ebenfalls nicht auswählen, wenn bei euch bereits Python vorinstalliert ist. Wenn Python nicht vorinstalliert ist, könnt ihr diese Option auswählen.
3. Wenn die Installation abgeschlossen ist, öffnet das Terminal (Mac) bzw. die Kommandozeile (Windows). Mit Kommandozeile ist ab jetzt immer Anaconda Prompt gemeint.
Gebt `conda list` ein und drückt auf Enter. Wenn eine Liste mit verschiedenen Paketnamen und Versionen erscheint, ist alles richtig. 
In dem Fall lest bei "Was sind virtuelle Umgebungen?" weiter. Wenn ihr Windows verwendet und den Befehl in Anaconda Prompt eingegeben habt, sollte es hier kein Problem geben. 


Wenn auf dem Mac eine Meldung **"command not found: conda"** erscheint, führt die folgenden Schritte aus: 
1. Sucht in Spotlight nach "anaconda3". Es sollte ein Ordner mit dem Namen "anaconda3" angezeigt werden.
Kopiert den Pfad zu dem Ordner in die Zwischenablage. Wenn ihr nicht wisst, wie das geht, schaut in [diese Anleitung](https://www.youtube.com/watch?v=J3octfsPH1s).
2. Wechselt wieder in das Terminal. Gebt ein `source EUER_PFAD/bin/activate` und drückt auf Enter. Also zum Beispiel: `source /Users/admin/anaconda3/bin/activate` auf einem Mac mit dem Usernamen admin.
3. Wenn in der oberen Leiste von eurem Terminalfenster ein "zsh" steht, gebt ein: `conda init zsh` und drückt auf Enter. Falls dort "bash" steht, gebt ein `conda init` und drückt auf Enter.
4. Gebt nochmal `conda list` ein und drückt auf Enter. Wenn jetzt KEINE Meldung "command not found: conda" mehr angezeigt wird, hat alles geklappt. Lest in dem Fall bei "Was sind virtuelle Umgebungen?" weiter. 
Falls die Meldung immer noch erscheint, kommt in meine Installationssprechstunde. 


### Was sind virtuelle Umgebungen? 

Mithilfe von Anaconda kann man über das Terminal / die Kommandozeile für jedes Coding-Projekt, für das man Python verwendet, eine spezielle "virtuelle Umgebung" erstellen. 
Virtuelle Umgebungen sind reproduzierbare, übertragbare und isolierte Umgebungen für Python-Projekte. 
In einer virtuellen Umgebung kann man die gewünschte Python-Version und alle zusätzlichen Python-Pakete, die man für das Projekt braucht, installieren. 
Mithilfe von virtuellen Umgebungen können so verschiedene Python-Versionen mit ganz verschiedenen Paketen nebeneinander auf demselben Rechner verwendet werden.
JupyterLab können wir ebenfalls direkt in der virtuellen Umgebung installieren.

Theoretisch kann man verschiedene Python-Versionen, JupyterLab und alle Python-Pakete, die man braucht, auch installieren, ohne dazu eine virtuelle Umgebung einzurichten. 
Das erscheint im ersten Moment weniger kompliziert, allerdings entstehen so auf lange Sicht große Probleme, 
denn alle Pakete liegen dann am selben Ort. Es kann vorkommen, dass man für ein Coding-Projekt ein Python-Paket in einer bestimmten Version verwendet hat. 
Ein bisschen später will man dasselbe Paket für ein anderes Projekt verwendet. In der Zwischenzeit haben die Entwickler:innen des Pakets allerdings ein paar Änderungen vorgenommen und eine neue Version des Pakets veröffentlicht. 
Man updated deswegen das Paket und verwendet die neue Version für das neue Coding-Projekt. 
Die Änderungen haben aber dazu geführt, dass irgendwo im Code im alten Coding-Projekt eine Fehlermeldung entsteht. 
Ein anderes Problem entsteht zum Beispiel, wenn eine andere Person unseren Code nachnutzen will und diese Person auf ihrem Rechner bereits andere Pakete als wir vorinstalliert hat und es zu Konflikten zwischen den installierten Paketen kommt. Vielleicht verwendet die Person zudem noch ein anderes Betriebssystem.
Python ohne virtuelle Umgebungen zu verwenden, kann also die Reproduzierbarkeit unserer Daten einschränken und sogar zu Fehlermeldungen führen.

Professionelle Programmierer:innen verwenden deswegen für Python-Projekte eigentlich immer virtuelle Umgebungen. 



### Virtuelle Umgebung erstellen

1. Zunächst solltet ihr einen Ordner auf eurem Computer erstellen, in dem ihr die Jupyter Notebooks, die wir im Laufe der nächsten Stunden erstellen werden, ablegt. 
Das ist unser Projektordner. Auch, wenn ihr bereits einen Ordner für diesen Kurs angelegt habt, solltet ihr für die Notebooks einen extra Ordner erstellen. 
Benennt den Ordner simpel, ohne Sonderzeichen oder Leerzeichen. 
Der Ordner sollte außerdem nicht ein Unter-Unter-Unterordner von irgendeinem Ordner sein, sondern direkt auf eurem Desktop oder im Home-Verzeichnis liegen.
2. Jetzt müsst ihr den Ordnerpfad in die Zwischenablage kopieren. 
Wenn ihr nicht wisst, wie das geht, schaut in [diese Anleitung für Windows](https://www.youtube.com/watch?v=Xm4HEfZdzbY) oder [diese Anleitung für Mac](https://www.youtube.com/watch?v=J3octfsPH1s).
2. Öffnet anschließend wieder euer Terminal / Kommandozeile. Gebt den Befehl `cd` ein, gefolgt von einem Leerzeichen und dem Pfad zu eurem Ordner. 
Also z.B.: `cd /Users/admin/LV_Webscraping`.
Führt den Befehl anschließend mit Enter aus.
Ihr seht jetzt, dass sich die Eingabeaufforderung in eurem Terminal / Kommandozeile geändert hat: Dort steht jetzt der Name des Ordners. 
Das bedeutet, dass ihr mithilfe des Terminals / der Kommandozeile in euren Ordner navigiert seid. 
Ordner nennt man auch Verzeichnis, oder auf Englisch Directory, und der Befehl cd steht einfach für "change directory".
3. Gebt jetzt in eurem Terminal / Kommandozeile ein `conda create --name ws-env python=3.10` und drückt Enter.
Durch diesen Befehl habt ihr eine virtuelle Umgebung mit dem Name ws-env erstellt. 
Diesen Namen habe ich mir überlegt, er steht für "Webscraping Environment". 
Mit dem Zusatz "python=3.10" habt ihr dem Computer mitgeteilt, dass ihr in der Umgebung "ws-env" Python 3.10 verwenden wollt. \
**Achtung**: Falls eine Meldung erscheint "The following NEW packages will be INSTALLED. Proceed \[y\]/n?", dann gebt ein y und drückt wieder auf Enter.
5. Wenn die Einrichtung der virtuellen Umgebung abgeschlossen ist, seht ihr den Hinweis: "# To activate this environment, use \$ conda activate ws-env To deactivate an active environment, use \$ conda deactivate"
6. Gebt ein `conda activate ws-env` und drückt Enter. 
Jetzt hat sich die Eingabeaufforderung wieder geändert. Dort steht jetzt zusätzlich der Name der aktuell aktivierten Umgebung.
Lasst die Umgebung "ws-env" aktiviert und macht direkt weiter mit den Schritten im nächsten Abschnitt "JupyterLab installieren".

### JupyterLab installieren

7. Gebt ein `conda install -c conda-forge jupyterlab` und drückt auf Enter. 
Mit diesem Befehl habt ihr JupyterLab installiert. \
**Achtung**: Falls wieder eine Meldung der Art "The following packages will be UPDATED" kommt, bestätigt wieder, indem ihr y eingebt und Enter drückt.

8. Gebt ein `python -m ipykernel install --user --name ws-env --display-name="Python 3.10 (Webscraping)"` und drückt Enter. 
Dieser Befehl erstellt einen neuen "Kernel". 
Der Kernel ist das Herzstück von JuypterLab, er übernimmt die eigentliche Berechnung und Ausführung von Code und stellt die Verbindung zwischen dem JupyterLab-Benutzerinterface und Python her. 
Wir installieren mit diesem Befehl also einen neuen Kernel, der Python in der Version 3.10 verwendet, um die Berechnungen auszuführen.

9. Jetzt könnt ihr Jupyter Lab starten, indem ihr `jupyter lab` eingebt und auf Enter drückt.\
Jetzt sollte automatisch ein neuer Tab in eurem Browser geöffnet werden. 
Euer Terminal / Kommandozeile ist jetzt die ganze Zeit "aktiv", bis JupyterLab wieder geschlossen wird. Das heißt, ihr müsst JupyterLab nach jeder Benutzung immer beenden.

10. Wechselt jetzt in das Browserfenster, in dem JupyterLab geöffnet wurde. Klickt auf unseren Kernel "Python 3.10 (Webscraping)". 
Es öffnet sich ein neues Jupyter Notebook. In die erste Zelle schreibt ihr `import sys` und führt die Zelle aus.
In die zweite Zelle schreibt ihr `sys.version` und führt sie aus. Jetzt sollte als Output '3.10.xx' angezeigt werden. 
Wenn das nicht der Fall ist, kommt in meine Installationssprechstunde.

11. Schließt jetzt JupyterLab, indem ihr im Menü oben auf File -> Shut Down klickt. Bestätigt das Fenster "Shutdown Confirmation".
Das Browserfenster schließt sich jetzt automatisch.

12. Zuletzt müssen wir auch die virtuelle Umgebung wieder deaktivieren. Wechselt dazu wieder in euer Terminal / Kommandozeile, gebt den Befehl `conda deactivate` ein und drückt auf Enter.

Jetzt könnt ihr Terminal / Kommandozeile wieder schließen. Super! Mit diesem Setup können wir nächste Woche starten. 
