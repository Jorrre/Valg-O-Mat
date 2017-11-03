## Valg-O-Mat

### Struktur

<pre>
    .
    ├── .idea
    │   ├── encodings.xml
    │   ├── FlaskApp2.iml
    │   ├── misc.xml
    │   ├── modules.xml
    │   └── workspace.xml
    ├── __pychache__
    │   └── methods.cpython-35
    ├── static
    │   ├── data.json
    │   └── style.css
    ├── templates
    │   ├── done.html
    │   ├── index.html
    │   └── slides.html
    ├── app.py
    ├── methods.py
    └── README.md
</pre>

- Under *templates* ligger HTML filene som kjører i løpet av programmet. Alle HTML filer som skal brukes må ligge i *templates* mappen.
- Under *static* ligger alle filer som ikke endres mens programmet kjører, blant annes .css og .json.

### Spørsmål og `data.json`

Alle spørsmål som lastes gjennom programmet ligger i `data.json`. JSON filen er strukturert med et array som holder spørsmålene, og vektingene til forskjellige spørsmålene. For å legge til et nytt spørsmål, legg til blokken under på slutten av "spm" arrayet på starten av `data.json`.

**Viktig:** For at .json filen skal fungere etter blokken er lagt inn, legg til et komma rett etter den siste krøllparantesen før blokken blir limt inn.

```json
	{ 	
		"id": 1,
		"q": "Spørsmål 1",
		"vekt": [
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0]
		]
	}
```

For å vekte spørsmålene, bruk de 3 nested arrayene under "vekt" under hvert av spørsmålene. Fra topp til bunn representerer arrayene "Ja", "Vet ikke" og "Nei".
