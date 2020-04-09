# AI projekt Jacob Engström ABBindustrygymnasium 180S

### Beskrivning

Movies är en fil som genererar texter baserat på disney och pixar filmer bland annat Shrek, Bee movie och Bilar. För att träna model har jag använt gpt2 och manusen har jag tagit ifrån [The Internet Movie Script Database](https://www.imsdb.com)
Filen Movies är baserad på Train a [GPT-2 Text-Generating Model w/GPU](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce) av Max Woolf.

### Användning

Jag har använt Google Colab när jag skrev programet men det går att köra programer i andra IDEer som till exempel Jupyter. öppna programet i den IDE du har valt och följ instruktionerna

## Problem

Tanken var först att efter modellen var färdigtränad skulle de genererade texterna kontrolleras av BERT, vilket är textklassificerare. Om man låter BERT analysera texterna som har genererats kan BERT avgöra om texterna är bra eller inte. BERT kontrollerar den så att texten är rimliga både grammatiskt och logiskt. med detta menar jag att texterna ska för det första inte ha stavfel, påhittade ord eller meningar som inte börjar med stor bokstav och sluta med punkt och för det anndra  Om texten är bra får man ett positivt output och tycker algoritmen att texten inte fungerar grammatiskt eller logiskt får man ett falskt output. Problemet är att det inte finns någon fördigtränar BERT för just berätelser. detta innebär att jag skulle behöva träna upp den helt från scatch. Enligt Synced tar det cirka 34 dagar och 4 separata GPUer för att träna en BERT modell 