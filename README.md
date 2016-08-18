Merge CSV
=========

Ho scritto questo programma per importare dei dati dal gestionale del territorio ad un comune software GIS senza rimuovere i dati già inseriti.
Poiché l'inserimento dei dati non avviene in maniera parallela e sincronizzata nel software gestionale e nell'applicativo GIS, gli ID delle aree di circolazione inserite, nei rispettivi databases, non coincidono.

## Descrizione
Considerato un CSV composto da **ID area di circolazione** e relativo **nome area di circolazione**

Es.

| ID area di circolazione | nome area di circolazione |
|:-----------------------:|:--------------------------|
| 1                       | via furio giunta          |
| 2                       | via melfi                 |
| 3                       | vico bobby baccalieri     |
| 4                       | contrada soprano          |
| 5                       | salita artie bucco        |

Considerato un secondo CSV composto da **nome area di circolazione**, **numero civico**, **esponente** ed eventuali altre colonne:

Es.

| nome area di circolazione | numero civico | esponente | ... |
|:--------------------------|:-------------:|:---------:|-----|
| via furio giunta          | 1             |           | ... |
| via furio giunta          | 2             |           | ... |
| via furio giunta          | 3             |           | ... |
| via furio giunta          | 3             | bis       | ... |
| via furio giunta          | 3             | tris      | ... |
| via furio giunta          | 4             |           | ... |
| via melfi                 | 1             |           | ... |
| via melfi                 | 2             |           | ... |

Il seguente programma unisce i due files CSV in un unico CSV contenente **ID area di circolazione**, **nome area di circolazione**, **numero civico** ed **esponente**

Es.

| ID area di circolazione | nome area di circolazione | numero civico | esponente | ... |
|:-----------------------:|:--------------------------|:-------------:|:---------:|-----|
| 1                       | via furio giunta          | 1             |           | ... |
| 1                       | via furio giunta          | 2             |           | ... |
| 1                       | via furio giunta          | 3             |           | ... |
| 1                       | via furio giunta          | 3             | bis       | ... |
| 1                       | via furio giunta          | 3             | tris      | ... |
| 1                       | via furio giunta          | 4             |           | ... |
| 2                       | via melfi                 | 1             |           | ... |
| 2                       | via melfi                 | 2             |           | ... |

## Procedura
- esportare dal software GIS la tavola del database che contiene **ID area di circolazione** e **nome area di circolazione**;

- esportare dal software gestionale la tavola del database che contiene **nome area di circolazione**, **numero civico**, **esponente**, **coordinata x**, **coordinata y** (se non si ha accesso al database contattare l'assistenza);

- Verificare la correttezza dei dati contenuti nei files, sia attraverso un foglio di calcolo, sia attraverso un text editor:
    - I CSV esportati devono utilizzare la virgola come separatore delle colonne;
    - Le eventuali coordinate presenti nei files non devono utilizzare la virgola come separatore decimale ma il punto;
    - Il CSV esportato dal GIS deve contenere:
        - **ID area di circolazione** nella prima colonna;
        - **nome area di circolazione** nella seconda colonna;
        - ulteriori colonne sono ininfluenti.
    - Il CSV esportato dal gestionale deve contenere:
        - **nome area di circolazione** nella prima colonna;
        - **numero civico** nella seconda colonna;
        - **esponente** nella terza colonna;
        - ulteriori colonne sono ininfluenti.


### Attenzione
- Nel caso di un **nome area di circolazione** abbreviato come *s. maria* questo viene assegnato all'**ID area di circolazione** di *santa maria*.

Per far fronte ad incoerenze nei toponimi è possibile creare un CSV contenente le varie associazioni:
Nella prima colonna si riporta il **nome area di circolazione** del CSV generato dal GIS, nella seconda colonna si riporta il **nome area di circolazione** del CSV generato dal SIC/SIT.

Es.

| nome area di circolazione | nome area di circolazione |
|:-------------------------:|:--------------------------|
| vico bobby baccalieri     | vico b. baccalieri        |
| salita artie bucco        | salita a. bucco           |

### Sviluppo
Questo applicativo è stato sviluppato per un caso molto specifico ma allo stesso tempo è stato pensato per potersi adattare a circostanze simili. Si invita a segnalare eventuali bugs.

### License

[MIT]

___

*Non men che saver, dubbiar m'aggrata.*

[MIT]:https://opensource.org/licenses/MIT
