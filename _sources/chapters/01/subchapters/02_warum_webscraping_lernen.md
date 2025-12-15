# Motivation


> "Writing code is not programming. Programming has more to do with **_problem-solving_** than writing code. With the current ways of doing things, we are still stuck in _writing code_ as a way to _instruct_ computers — just like the people who use to code in machine language were struck in 0s and 1s. You might poke fun at those binary coders and wonder why they went through all those troubles to instruct the computers. Future generations will feel the same way. **Programming is the process of solving problems using a computer. Writing code is just one aspect of this process.** It’s a necessary part, but it’s not the whole picture. If all you can do is write code, you are not a programmer, you are a coder and you are bound to get replaced."


Quelle: [Somnath Singh, Coding Won't Exist in 5 Years. This is Why, 20.01.2023, Medium.com](https://javascript.plainenglish.io/coding-wont-exist-in-5-years-this-is-why-6da748ba676c)


Wenn man dieser Prognose aus einem Blogbeitrag von Somnath Singh und vielen ähnlichen Beiträgen aus den vergangenen Jahren glauben möchte, dann wird das Coden, also das Schreiben von Code und das Erlernen der Syntax einer Programmiersprache, eine zunehmend ersetzbare Fähigkeit. 
Viel wichtiger ist und bleibt es dagegen zu verstehen und zu lernen, wie Fragestellungen und Lösungsstrategien so formuliert werden können, dass sie mithilfe eines Computers möglichst effizient umgesetzt werden können. 
Dabei muss die Entscheidung für die ein oder andere Strategie besonders in der Wissenschaft auch rechtliche, forschungsethische und forschungspraktische Aspekte berücksichtigen.
Damit Forschung reproduziert und verstanden werden kann, muss auch der Prozess der Datenbeschaffung transparent und kritisch erfolgen. 
Auch, wenn wir in diesem Seminar ganz praktisch lernen werden, Code in Python zu schreiben, steht deswegen die konzeptionelle Ebene im Mittelpunkt des Seminars.
Bevor überhaupt Code geschrieben werden kann, der Inhalte von Webseiten extrahiert, braucht es ein Verständnis davon, wie Inhalte überhaupt im Web dargestellt werden, und wie die manuelle Arbeit automatisiert und in die Logik einer Programmiersprache übertragen werden kann (z.B. das Anklicken eines "Herunterladen"-Buttons, das Herauskopieren von Kommentaren aus Kommentarspalten). 
Denn nicht zuletzt können ohne ein Verständnis von Webscraping-Strategien auch die vielen Tools und Anleitungen, die versprechen, Webscraper mithilfe von GPT oder einem anderen Sprachmodell zu schreiben, oder Web Scraping komplett ohne technisches Wissen zu ermöglichen, in den meisten Fällen nicht sinnvoll und sicher eingesetzt werden.

Warum nicht? Ein paar Beispiele: 

- Eine naive Anfrage mit GPT 3.5:  [https://chat.openai.com](https://chat.openai.com/share/e2962221-50e9-49fa-b63e-c431186705d2)

Warum funktioniert der Web Scraper nicht? ChatGPT in der Version 3.5 kann sich die Website nicht "ansehen" und die Struktur der Webseite nicht analysieren.
Damit ChatGPT dabei helfen kann, einen Web Scraper zu schreiben, reicht es nicht, eine ganz allgemeine Anfrage zu stellen. 
Es muss ganz genau beschrieben werden, welche Elemente extrahiert werden sollen, wie sie heißen und wie und in welcher Form sie heruntergeladen werden sollen. 
Um das zu machen, muss man aber bereits einiges verstehen:

1. Wie ist die Website aufgebaut? 
2. Welche Daten können und dürfen überhaupt extrahiert werden?
3. Was ist der beste Weg, um an diese Daten zu gelangen bzw. welche Python Bibliothek kann dazu verwendet werden?  
4. Wo genau befinden sich die Daten? 
5. In welcher Form sollen die Daten abgespeichert werden (-> Forschungsdesign!)
6. Und, nicht zuletzt: Ist es überhaupt notwendig, die Daten zu scrapen? Gibt es vielleicht eine öffentliche API, die den Zugriff auf die Daten bereitstellt (was das ist, lernen wir noch)?

Mit ein bisschen sogenanntem "prompt engineering" und GPT 4o lässt sich auch ein funktionierendes Skript für das Beispiel generieren: [https://chatgpt.com/](https://chatgpt.com/share/67fcdafb-8964-800f-8f6f-e035747377a9). 
Aber ob ein funktionierendes Skript generiert wird oder nicht hängt von vielen Faktoren ab. Wenn die Anfrage scheitert und eine Webseite nicht sehr kompliziert aufgebaut ist, kann alternativ der Seitenquelltext kopiert werden und an ChatGPT 3.5 geschickt werden. 
Dateien können auf diese Weise natürlich nicht heruntergeladen werden. Aber Daten, zum Beispiel eine Liste aller Zitate von einer Unterseite der Seite [quotes.toscrape.com](https://quotes.toscrape.com/page/3/) können so durchaus erfolgreich extrahiert werden: 

- Eine erfolgreiche Anfrage mit GPT 3.5: [https://chat.openai.com](https://chat.openai.com/share/aa9245e4-afbd-4290-91d3-ac94b624d2c8)

Allerdings muss der Vorgang für jede Unterseite wiederholt werden, und der Quelltext der meisten Webseiten ist so lang, dass er die maximale von ChatGPT erlaubte Zeichenanzahl überschreitet.
Seit GPT 4 ist es zwar auch möglich, eine Webseite als HTML-Datei hochzuladen, sodass auch sehr langer Seitenquelltext von ChatGPT verarbeitet werden kann, allerdings ist diese Strategie oft trotzdem nicht erfolgreich.
Denn diese Strategie funktioniert nur für bestimmte Webseiten und Inhalte, für andere dagegen nicht: 

- Eine gescheiterte Anfrage mit GPT 4: [https://chat.openai.com](https://chat.openai.com/share/b6c36130-3446-455a-b51c-f2a2ccc08aad)

Die Antwort von ChatGPT deutet bereits darauf hin, dass etwas Hintergrundwissen zu "dynamischen Inhalten" erforderlich ist, um zu verstehen, warum die Anfrage nicht erfolgreich war. 

Die Fähigkeiten der Modelle entwickeln sich natürlich fortwährend weiter und bereits im nächsten Semester werden diese Beispiele nicht mehr aktuell sein und es wird bereits andere Schwierigkeiten und Möglichkeiten geben. 
Einige Bedenken bei der Verwendung von LLMs zum Webscraping, insbesondere ohne das nötige Hintergrundwissen, werden aber auf absehbare Zeit bestehen bleiben, und diese sind für uns als Forscher:innen ganz besonders relevant: 

- Personenbezogene Daten dürfen laut DSGVO nicht einfach über Server außerhalb der EU geschickt werden. Ist die Verwendung dieser Tools zur Verarbeitung dieser Daten überhaupt legal? 
- Der Quellcode proprietärer Anwendungen ist meist nicht öffentlich einsehbar. Macht die Verwendung solcher Tools Forschung intransparent und ggf. nicht reproduzierbar?
- Kann ein:e Forscher:in ohne Grundkenntnisse im Webscraping überhaupt glaubhaft die Vollständigkeit und Richtigkeit der auf diese Weise extrahierten Daten versichern?  
- Code, den ChatGPT oder eine andere LLM-Anwendung generiert hat zu kopieren und auf dem eigenen Rechner auszuführen, ohne zu verstehen, was der Code macht, birgt nicht zuletzt auch erhebliche Sicherheitsrisiken, besonders dann, wenn aus dem Code heraus Webseiten aufgerufen werden. Dazu zählt nicht nur die Tatsache, dass Code, der aus Internetforen kopiert oder von LLMs generiert wird, [oft sicherheitsrelevante Schwachstellen aufweist]( 	
https://doi.org/10.48550/arXiv.2403.15600), sondern auch Risiken durch neuere Angriffsstrategien wie das sogenannte [AI Slopsquatting](https://hackernoon.com/ai-slopsquatting-how-llm-hallucinations-poison-your-code), [data-, model- und tool poisoning](https://www.ibm.com/think/topics/data-poisoning) sowie [indirect prompt injections](https://www.ibm.com/de-de/topics/prompt-injection). Solche Angriffe zählen zu "Supply Chain Attacks", die in den letzten Jahren massiv angestiegen sind und insbesondere Open Source Projekte im Python- und JavaScript Ökosystem betreffen (siehe dazu z.B. [diesen Blogbeitrag](https://medium.com/@ronityadav234/supply-chain-malware-targets-popular-npm-pypi-packages-in-gluestack-attack-5cec43cf2a6a))
- Für das Webscraping gelten in verschiedenen Staaten verschiedene rechtliche Regelungen. Wenn ihr Code ausführt, der sich nicht rechtskonform verhält, macht ihr euch ggf. strafbar.
- Wie aus den obigen Beispielen vielleicht bereits deutlich wurde, gibt es viele technische Details, die die Qualität und Zugänglichkeit der Daten beeinflussen. Ohne Kenntnisse der zugrundeliegenden Mechanismen und Strategien bleibt die Art der Daten, die ein:e Forscher:in extrahieren kann, am Ende begrenzt. 
- ChatGPT und andere kommerzielle Anwendungen kosten Geld. 

Das soll nicht bedeuten, dass ChatGPT und die GPT-Modelle (oder andere LLMs) überhaupt nicht verwendet werden sollten. Die Modelle können helfen, Code zu verbessern oder zu verstehen, und sie können erfahrenere Programmierer:innen auch beim Schreiben von Code unterstützen, aber ohne ein Grundverständnis in Webscraping-Strategien und Programmierung kann dieser Code nicht sinnvoll verwendet werden. 
Am Ende des Semesters könnt ihr hoffentlich die aufgeworfenen Fragen selbst beantworten und habt euch das notwendige Grundlagenwissen erarbeitet, um effizienter Forschungsdaten zu beschaffen als in den hier vorgestellten Beispielen mit ChatGPT.
Beim Umgang mit fremdem Code könnt ihr euch allerdings bereits jetzt merken: "Any code that can be copied and pasted from an outside source, AI-generated or human-created, cannot be blindly trusted" ([Hamer, d'Amorim und Williams 2024, S. 6](https://doi.org/10.48550/arXiv.2403.15600)).
