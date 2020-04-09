# AI projekt Jacob Engström ABBindustrygymnasium 180S

### Beskrivning

Movies är en fil som genererar texter baserat på disney och pixar filmer bland annat Shrek, Bee movie och Bilar. För att träna model har jag använt gpt2 och manusen har jag tagit ifrån [The Internet Movie Script Database](https://www.imsdb.com)
Filen Movies är baserad på Train a [GPT-2 Text-Generating Model w/GPU](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce) av Max Woolf.


### Användning

Jag har använt Google Colab när jag skrev programet men det går att köra programer i andra IDEer som till exempel Jupyter. öppna programet i den IDE du har valt och följ instruktionerna


### Problem

Tanken var först att efter modellen var färdigtränad skulle de genererade texterna kontrolleras av BERT, vilket är textklassificerare. Om man låter BERT analysera texterna som har genererats kan BERT avgöra om texterna är logiska och gramatiskt korekta. Detta betyder att texterna ska för det första inte ha stavfel, påhittade ord eller meningar som inte börjar med stor bokstav och sluta med punkt och för det andra att en karaktär kan inte ha flera namn och befinna sig på olika platser sammtidit. Om texten är bra enligt BERT får man ett positivt output och tycker algoritmen att texten inte fungerar grammatiskt eller logiskt får man ett falskt output.

Problemet jag har hafft under istortsätt hela tiden är att det inte finns någon fördigtränar BERT för just berätelser, filmer eller sagor. Detta innebär att jag skulle behöva träna upp en egen bert helt från scatch. Enligt Synced tar det cirka 34 dagar och 4 separata GPUer för att träna en BERT modell. pågrund avv detta så när företag har gjort en modell vill de gärna behålla den för sig själva eller ta betalt för att låta någon annan använda den


### Slutsats

Hadde jag haft mera tid och en dator men möjligheten för att konstuera en BER>T modell skulle jag såsklart ha gjort det men med den tidsramen vi hadde samt att jag inte har tillgåg till en dator med fyra grafik kort så var det inte möljigt