# MyFirst Crew

Vytvoril som jednoduchý chatbot, ktorý bude hľadať zaujímavé fakty na základe zadaného topiku. Využil som dvoch agentov a dva zodpovedné nástroje – pre každého agenta jeden. Jeden agent slúži na vyhľadávanie zaujímavých informácií o topiku a druhý ďalej spracuje získané informácie, zhrnie ich a vytvorí 5 faktov o topiku na ich základe.


## Installation

git clone https://github.com/valeriikucenko55555-lang/wrl3.git

## Running the Project

Pred spusteniem potrebujeme zadat AZURE_API_KEY v my_first/.env
cd wrl3\my_first\src
python -m my_first.main gradio
