# MyFirst Crew

Vytvoril som jednoduchý chatbot, ktorý bude hľadať zaujímavé fakty na základe zadaného topiku. Využil som dvoch agentov a dva zodpovedné nástroje – pre každého agenta jeden. Jeden agent slúži na vyhľadávanie zaujímavých informácií o topiku a druhý ďalej spracuje získané informácie, zhrnie ich a vytvorí 5 faktov o topiku na ich základe.


## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the my_first Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

