I(mport)toponymy
================

:door: Fonde due files CSV in un unico file, contenente tutte le colonne dei files sorgente, filtrate per toponimo.

Questo programma è stato scritto per importare dati territoriali da un software gestionale ad un comune applicativo GIS.

## Descrizione
Il primo CSV deve essere composto da **ID area di circolazione**, **DUG area di circolazione** e relativo **nome area di circolazione**.
Questo file proviene dal database del GIS ed in particolare dalla tavola che definisce le aree di circolazione.

Esempio input GIS:

| ID area di circolazione | DUG area di circolazione | nome area di circolazione |
|:-----------------------:|:-------------------------|:--------------------------|
| 1                       | via                      | furio giunta              |
| 2                       | via                      | melfi                     |
| 3                       | vico                     | bobby baccalieri          |
| 4                       | contrada                 | soprano                   |
| 5                       | salita                   | artie bucco               |
| ...                     | ...                      | ...                       |

Il secondo CSV deve essere composto da **DUG area di circolazione**, **nome area di circolazione**, **numero civico**, **esponente** ed eventuali altre colonne.

Esempio input SIC:

| DUG area di circolazione | nome area di circolazione | numero civico | esponente | ... |
|:-------------------------|:--------------------------|:-------------:|:---------:|-----|
| via                      | furio giunta              | 1             |           | ... |
| via                      | furio giunta              | 2             |           | ... |
| via                      | furio giunta              | 3             |           | ... |
| via                      | furio giunta              | 3             | bis       | ... |
| via                      | furio giunta              | 3             | tris      | ... |
| via                      | furio giunta              | 4             |           | ... |
| via                      | melfi                     | 1             |           | ... |
| via                      | melfi                     | 2             |           | ... |
| vico                     | b.baccalieri              | 1             |           | ... |
| vico                     | b.baccalieri              | 2             |           | ... |
| vico                     | b.baccalieri              | 3             |           | ... |
| ...                      | ...                       | ...           | ...       | ... |

Il programma unisce i due files in un unico CSV contenente **ID area di circolazione**, **DUG area di circolazione**, **nome area di circolazione**, **numero civico**, **esponente** ed eventuali altre colonne.

Esempio output:

| ID area di circolazione | DUG area di circolazione | nome area di circolazione | numero civico | esponente | ... |
|:-----------------------:|:-------------------------|:--------------------------|:-------------:|:---------:|-----|
| 1                       | via                      | furio giunta              | 1             |           | ... |
| 1                       | via                      | furio giunta              | 2             |           | ... |
| 1                       | via                      | furio giunta              | 3             |           | ... |
| 1                       | via                      | furio giunta              | 3             | bis       | ... |
| 1                       | via                      | furio giunta              | 3             | tris      | ... |
| 1                       | via                      | furio giunta              | 4             |           | ... |
| 2                       | via                      | melfi                     | 1             |           | ... |
| 2                       | via                      | melfi                     | 2             |           | ... |
| 3                       | vico                     | bobby baccalieri          | 1             |           | ... |
| 3                       | vico                     | bobby baccalieri          | 2             |           | ... |
| 3                       | vico                     | bobby baccalieri          | 3             |           | ... |
| ...                     | ...                      | ...                       | ...           | ...       | ... |

## Procedura
- Esportare dal software GIS la tavola del database contenente **ID area di circolazione**, **DUG area di circolazione** e **nome area di circolazione**;
- Esportare dal software gestionale la tavola del database contenente **DUG area di circolazione**, **nome area di circolazione**, **numero civico**, **esponente** ed eventuali altre colonne;
- Verificare la correttezza dei dati contenuti nei files, sia attraverso un foglio di calcolo, sia attraverso un text editor:
    - I CSV esportati devono utilizzare la virgola come separatore;
    - Le eventuali coordinate geografiche presenti nei files non devono utilizzare la virgola come separatore decimale ma il punto;

### Duplicati
Per far fronte ad incoerenze nei toponimi è possibile creare un file CSV contenente i vari duplicati:
Nella prima colonna si riporta il nome dell'area di circolazione del CSV generato dal software GIS, nella seconda colonna si riporta il nome dell'area di circolazione del CSV generato dal gestionale SIC/SIT.

Esempio input:

| DUG nome area di circolazione GIS | DUG nome area di circolazione SIC |
|:----------------------------------|:----------------------------------|
| vico bobby baccalieri             | vico b.baccalieri                 |
| salita artie bucco                | salita a.bucco                    |
| ...                               | ...                               |

## Sviluppo
Questo applicativo è stato sviluppato per un caso molto specifico ma allo stesso tempo è stato pensato per potersi adattare a circostanze simili. Si invita a contribuire allo sviluppo ed a segnalare eventuali bugs.

### TODO
- Opzione colonne match;
- Opzione colonna merge;
- Opzione separatore (colonne e numeri decimali);
- GUI.

### Eseguibile
Utilizzare le opzioni `--onefile` e `--icon=main.ico`.

## License

[MIT]

___

*Non men che saver, dubbiar m'aggrata.*

[MIT]:https://opensource.org/licenses/MIT
