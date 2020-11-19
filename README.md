#  HTML Generator
## Qgis Plugin per processing

<!-- TOC -->

- [HTML Generator](#html-generator)
  - [Qgis Plugin per processing](#qgis-plugin-per-processing)
    - [1. - Finestra processing](#1---finestra-processing)
    - [2. - Opzioni](#2---opzioni)
    - [3. CSS - Esempio Standard.css](#3-css---esempio-standardcss)
- [4. Dati di esempio](#4-dati-di-esempio)
- [5. Videotutorial](#5-videotutorial)
- [6. Ringraziamenti](#6-ringraziamenti)

<!-- /TOC -->

### 1. - Finestra processing
Il plugin, una volta caricato, compare negli script di processing nella cartella HTML

![uno](images/HTML.png)

Il plugin permette la composizione di una pagina HTML con i dati da una fonte tra quelle compatibili.

![uno](images/Finestra_processing_annotata.png)

1. sorgente dati, eventualmente anche filtrati e/o solo selezionati se da mappa;
2. selettore campi dati da inserire nell'html;
3. [opzionale] espressione filtro;
4. [opzionale] titolo in testa alla pagina html;
5. [opzionale] icona o immagine in alto a sinistra;
6. [opzionale] css da includere nell'html;
7. dimensioni icona e foto;
8. scelta tra link con percorso assoluto (default) o relativo;
9. file in uscita.

Il plugin riconosce i campi data e quelli in cui è memorizzata l'immagine o le immagini purchè con estensione di file immagine (gif; jpeg; jpg; png; svg).

I campi selezionati possono essere riordinati a piacimento.

Le dimensioni dell'icona e delle immagini possono essere espresse in tutte le unità di misura previste dall'html.

Il file css determina tutte le caratteristiche estetiche del file prodotto, riferendosi sempre all'elemento 'Table', alt tag **'b'** per il titolo ed al tag **'div'** per l'immagine o l'icona in intestazione.

I file prodotti, se temporanei, avranno sempre percorsi assoluti, altrimenti non sarebbero funzionanti, se salvati possono avere sia percorsi assoluti sia relativi.

Per poter eventualmente traferire il progetto con i file html relativi, tutti i file devono risiedere in sottocartelle della cartella di progetto.

Lo script effettua una serie di controlli sulla congruenza dei percorsi dei file origine (sorgente, css, icona/immagine) e avverte se
c'è la possibilità che il file html prodotto possa non funzionare correttamente.

Per default il percorso di progetto viene considerato per primo, in seconda scelta il percorso del file sorgente.

_NOTA BENE: 
Con i file temporanei, se i campi contengono percorsi relativi, l'html prodotto non avrà le immagini correttamente visualizzate._

↑[torna su](#HTML-and-CSS )↑

### 2. - Opzioni

1. Espressione filtro: un filtro componibile nativo di QGIS;
2. Titolo: una qualsiasi combinazione alfanumerica nella casella di testo, senza apici, il sistema la mette in rosso, ma funziona perfettamente; altrimenti una qualsiasi composizione entro il solito calcolatore, ovviamente si tratta di una scritta non dinamica;
3. Icona o immagine: una qualsiasi immagine tra quelle compatibili:
4. CSS: questa è la parte più interessante dato che permette una personalizzazione accurata della pagina html prodotta. Come anzidetto i tag utilizzati sono **'Table'**, **'b'** e **'div'**, per generare comodamente il css vi sono diversi tools gratuiti online tra cui **https://divtable.com/table-styler/** che permette con pochi passaggi di ottenere risultati veramente notevoli e la cui unica limitazione è la fantasia dell'autore. Il sito da anche la possibilità di definire ogni singolo aspetto dell'impaginazione.

↑[torna su](#HTML-and-CSS )↑

### 3. CSS - Esempio Standard.css
Assieme al plugin è presente un CSS denominato Standard.css che trovate dentro la cartella del plugin o anche nello zip, và copiato nella cartella del vostro progetto.

E' possibile avere quanti file css si vuole e lo potete modificare in base alle vostre esigenze.

E' interamente commentato in maniera da poter intervenire su tutti gli aspetti della pagina HTML.
```
/* GF 15.11.2020*/
/* qualsiasi proprietà dei singoli elementi è da qui personalizzabile */
/* quanto presente non è esaustivo di tutte le proprietà possibili    */

/* proprietà titolo */
b{
	font-family: "Comic Sans MS", cursive, sans-serif;
	font-size: 19px;
	font-weight: bold;
	color: red;
}
/* proprietà titolo tabella */
caption {
	font-family: "Comic Sans MS", cursive, sans-serif;
	font-size: 19px;
	font-weight: bold;
	color: red;
}

/* proprietà div contenente logo/icona */
div .links {
	font-size: 19px;
}
/* proprietà immagini */
img {
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 3px;
  width: auto;
  height: 10%;
  background: #FFFFFF;
}
/* proprietà immagine/icona */
#logoimg {
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 3px;
  width: auto;
  height: 5%;
  background: #FFFFFF;  
  /* transform: scale(1.5);
  background: #000000;*/
}
/* beta zoom ma solo se html in browser */
.zoom {
  padding: 3px;
  background-color: white;
  transition: transform .2s; /* Animation */
  width: auto;
  height: 10%;
  margin: 0 auto;
}
/* beta zoom puntatore sull'immagine ma solo se html in browser */
.zoom:hover {
  transform: scale(4); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
}
/* proprietà generali tabella */
table.Table {
  font-family: "Comic Sans MS", cursive, sans-serif;
  border: 2px solid #4F7849;
  background-color: #EEEEEE;
  width: 100%;
  text-align: center;
  border-collapse: collapse;
}
/* proprietà dati td e header th*/
table.Table td, table.Table th {
  border: 2px solid #4F7849;
  padding: 3px 2px;
}
/* proprietà dati corpo tabella */
table.Table tbody td {
  border: 2px solid #4F7849;
  font-size: 19px;
  font-weight: bold;
  color: #4F7849;
}
/* proprietà riga */
table.Table tr:nth-child(even) {
  background: #CEE0CC;
}
/* proprietà piè di pagina */
table.Table tfoot, table.Table thdr {
  font-size: 13px;
  font-weight: bold;
  color: #000000;
  background: #4F7849;
  background: -moz-linear-gradient(top, #CEE0CC 0%,#CEE0CC 66%,#CEE0CC 100%);
  background: -webkit-linear-gradient(top,#CEE0CC 0%, #CEE0CC 66%, #CEE0CC 100%);
  background: linear-gradient(to bottom, #CEE0CC 0%,#CEE0CC66%, #CEE0CC 100%);
  border-top: 2px solid #444444;
}
/* proprietà dati piè di pagina */
table.Table tfoot td{
  font-size: 13px;
}
/* proprietà link in piè di pagina */
table.Table tfoot .links{
  text-align: center;
}
/* proprietà contenuti links piè di pagina */
table.Table tfoot .links a{
  display: inline-block;
  background: #EEEEEE;
  color: #000000;
  padding: 2px 8px;
  border-radius: 5px;
}
/* proprietà links ripetuti in intestazione */
#h {
  font-size: 13px;
  font-weight: bold;
  color: #000000;
  background: #4F7849;
  background: -moz-linear-gradient(top, #CEE0CC 0%,#CEE0CC 66%,#CEE0CC 100%);
  background: -webkit-linear-gradient(top,#CEE0CC 0%, #CEE0CC 66%, #CEE0CC 100%);
  background: linear-gradient(to bottom, #CEE0CC 0%,#CEE0CC66%, #CEE0CC 100%);
  border-top: 2px solid #444444;
  border-bottom: 2px solid #444444;
}
#h td{
  font-size: 13px;
}
#h .links{
  text-align: center;
}
#h .links a{
  display: inline-block;
  background: #EEEEEE;
  color: #000000;
  padding: 2px 8px;
  border-radius: 5px;
}
```
E' possibile impostare come unità di misura nei parametri **width** e **height** i mm cosa che consente impaginazioni precise.

↑[torna su](#HTML-and-CSS )↑

# 4. Dati di esempio
* [Arial fixed (mm)](./script-css/css/Arial%20fixed.css)
* [Black](./script-css/css/Black.css)
* [Comicgreen](./script-css/css/Comicgreen.css)
* [Grey](./script-css/css/Grey.css)

↑[torna su](#HTML-and-CSS )↑
# 5. Videotutorial
[![](https://img.youtube.com/vi/reoXJ7Pmk-I/0.jpg)](https://youtu.be/reoXJ7Pmk-I "HTML with CSS generator")

↑[torna su](#HTML-and-CSS )↑

# 6. Ringraziamenti
[QGIS.org](https://www.qgis.org/it/site/) - [divtable.com](https://divtable.com/table-styler/) - [Totò Fiandaca](https://pigrecoinfinito.com/) - A. Cusano


↑[torna su](#HTML-and-CSS )↑