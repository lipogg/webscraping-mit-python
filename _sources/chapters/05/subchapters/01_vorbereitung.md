# Vorbereitung

Während der Installation von Python und JupyterLab verwenden wir immer mal wieder die Kommandozeile (Windows) bzw. das Terminal (Mac).

### Kommandozeile aufrufen 

Mac: 

a) Spotlight-Suche nach "Terminal" \
b) Launchpad -> Andere -> Terminal

Windows: 

a) Suche nach "cmd" oder "Eingabeaufforderung" \
b) Start-Menü -> Alle Programme -> Zubehör -> Eingabeaufforderung \
c) Start-Menü -> Windows System -> Eingabeaufforderung

**Wenn ihr Windows verwendet, werdet ihr allerdings gleich auf eine andere Kommandozeile umsteigen, die heißt "Anaconda Prompt".**
Anaconda Prompt ist jetzt noch nicht auf eurem Computer installiert. Sobald ihr im Kapitel "Installation und Setup" Miniconda installiert habt, könnt ihr über die Suche auch Anaconda Prompt finden.   

Nachdem ihr Miniconda installiert habt: 

a) Suche nach "Anaconda Command Prompt" oder einfach "Anaconda Prompt"

**Wenn immer im Kapitel "Installation und Setup" die Kommandozeile erwähnt wird, ist damit Anaconda Prompt gemeint!**
**Nur in diesem Kapitel ist damit die vorinstallierte Eingabeaufforderung gemeint.**

### Kommandozeile kennenlernen 

Wenn ihr Mac verwendet, sieht euer Terminal ungefähr so aus: 

:::{figure-md} markdown-fig
<img src="mac_zsh.png" alt="Mac zsh" class="bg-transparent" width="50%">

Mac Terminal mit Z-Shell. Bild: https://catalins.tech/improve-mac-terminal/
:::

Wenn ihr macOS älter als Catalina installiert habt, sieht das Terminal vielleicht etwas anders aus. 
Das ist aber nicht weiter schlimm, die Befehle sind dieselben. 

Die Windows-Eingabeaufforderung (auf Englisch: Command Prompt) sieht ungefähr so aus: 

:::{figure-md} markdown-fig
<img src="windows_cmd.png" alt="Windows cmd" class="bg-transparent" width="50%">

Windows Eingabeaufforderung cmd.exe. Bild: https://www.giga.de/downloads/windows-10/tipps/windows-10-eingabeaufforderung-oeffnen/
:::

Anaconda Prompt sieht ungefähr so aus: 

:::{figure-md} markdown-fig
<img src="windows_anaconda_prompt.png" alt="Anaconda prompt" class="bg-transparent" width="50%">

Anaconda Prompt. Bild: https://www.youtube.com/watch?v=UAUO_K-bRMs
:::


### Python vorinstalliert? 

Bevor ihr Python installiert, solltet ihr überprüfen, ob Python auf eurem Computer vielleicht schon vorinstalliert ist.
Dazu gebt ihr den folgenden Befehl im Terminal / Kommandozeile ein und drückt Enter. Mit Kommandozeile ist nur in diesem Fall die Windows-Eingabeaufforderung gemeint.

`python --version` 

Falls eine Meldung "command not found: python" angezeigt wird, gebt ihr ein: \
`python3 --version`

Wenn bei einem der beiden Befehle irgendeine Antwort der Art "Python 3.9.6" (oder irgendeine andere Zahl) kommt, dann habt ihr Python bereits installiert. 
Ihr seid trotzdem noch nicht fertig, denn wir werden im Kurs mit einer bestimmten Python-Version arbeiten. Lest deswegen jetzt den Abschnitt "Installation und Setup" und folgt den Anweisungen, auch, wenn bei euch Python bereits vorinstalliert ist.



