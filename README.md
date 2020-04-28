# AI projekt Jacob Engström ABBindustrygymnasium 180S

### Beskrivning

Movies är en fil som genererar texter baserat på Disney och Pixar filmer bland annat Shrek, Bee movie och Bilar. För att träna model har jag använt gpt2 och manusen har jag tagit ifrån [The Internet Movie Script Database](https://www.imsdb.com)
Filen Movies är baserad på Train a [GPT-2 Text-Generating Model w/GPU](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce) av Max Woolf. I filen Movies.ipynd kan man träna och generare texter och i MoviesV2.ipynd kan man även produsera en MP3 fil där man får berättelsen uppläst


### Användning och återskapning

Jag har använt Google Colab när jag skrev programmet men det går att köra programmet i andra IDEer som till exempel Jupyter. Öppna programmet i den IDE du har valt och följ instruktionerna i filen. Om du vill ändra de texter som programet ska träna på ändrar du innehållet i filen scripts.txt annars kan du lägga till en ny fil men då måste du ändra sökvägen i programmet. Tänk på att filen med text måste vara i .txt format. Om texten eller texterna hu har valt är kortade än min rekommenderar jag att man ökar antalet epoker som den tränar. Eftersom det blir mindre träningsdata behöver man träna flera gånger

### Movies V2
i movies V2 använder jag mig av Google Text To Speech för att kunna generara MP3 filer där en berättaröst berättar berättelsen som programet har skapat

### Problem

Tanken var först att efter modellen var färdigtränad skulle de genererade texterna kontrolleras av BERT, vilket är textklassificerare. Om man låter BERT analysera texterna som har genererats kan BERT avgöra om texterna är logiska och grammatiskt korrekta. Detta betyder att texterna ska för det första inte ha stavfel, påhittade ord eller meningar som inte börjar med stor bokstav och sluta med punkt och för det andra vara logiska det vill säga en karaktär inte kan ha flera namn och befinna sig på olika platser samtidigt bland annat. Om texten är bra enligt BERT får man ett positivt output och tycker algoritmen att texten inte fungerar grammatiskt eller logiskt får man ett falskt output.  
Problemet jag har haft under i stort sett hela tiden är att det inte finns någon färdigtränad BERT för just berättelser, filmer eller sagor. Detta innebär att jag skulle behöva träna upp en egen BERT helt från scratch. Enligt Synced tar det cirka 34 dagar och 4 separata GPUer för att träna en BERT modell. på grund av detta så när företag har gjort en modell vill de gärna behålla den för sig själva eller ta betalt för att låta någon annan använda den


### Slutsats

Hadde jag haft mera tid och en dator men möjligheten för att konstuera en BERT modell skulle jag såsklart ha gjort det men med den tidsramen vi hadde samt att jag inte har tillgång till en dator med fyra grafikkort så var det inte möljigt
