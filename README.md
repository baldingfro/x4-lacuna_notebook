# Lacuna Notebook

Lacuna Notebook is an expansion of the in-game Encyclopedia that includes guides and
documentation on many of the game systems and mechanics.  It is designed to provide
information to help players get the most out of their playthrough.  Research has shown
it reduces alt-tabbing to lookup information by 69.67% (Nice!).

The information provided in the Notebook entries tries to fill the gaps of in-game
documentation but it will also include spoilers.  If the entry has spoiler information,
it will have a [Spolier] tag at the beginning of the title.  A best-effort will be made
to note if any entry has spoilers but sometimes it could be matter of opinion.  

All documentation in the Lacuna Notebook comes from Markdown files that be viewed
n'here:

[LNB Markdown Files](https://github.com/baldingfro/lacuna_nb/tree/main/docs/md_files)

Currently, LNB is a heavy work-in-progress and is missing a lot of planned content.

## Features

* Includes all the content and features of the in-game Encyclopedia
* Examples of topics covered by Lacuna Notebook:
  + New Player Guide/Walkthrough
  + Information for players returning to X4
  + [Spoiler] How to obtain all the unique ships in the game
  + How to trigger all the quests/plotlines
  + And more!

## Installation

* Clone the repo into $X4_INSTALL_DIR/extensions/lacuna_notebook
* Download the repo as a zip and extract into $X4_INSTALL_DIR/extensions/lacuna_notebook

Publishing the mod to Nexus Mods is planned.

## Usage

After the mod is installed, a new button with the letters "LNB" will appear in the
same top-level bar used to open the Encyclopedia.

* Pressing this button leads to joy

![Press here](docs/images/lnb_button_small.png)

* A new category "Lacuna Notebook" will appear at the bottom that can be expanded for
  wonderful topics that contain much sensation!

![LNB Expanded](docs/images/lnb_expanded.png)

## Known Issues

* When Lacuna Notebook is opened, the Encyclopedia icon in the top bar displays as
  active instead

## Technical Information About Lacuna Notebook

* It is a copy of the Encyclopedia Menu with custom code bolted on
* No dependencies
* Uses page range 698008001 - 698008999
* No AI/logic scripts in this mod and nothing runs when it's closed
* Content is populated using a script to convert the Markdown files to text in 0001.xml

## Contributing

Got stuff to change or add, submit an issue or a pull request.  This is my first public
repo so it's all new to me.  You can also find me in the Egosoft Discord if you have
questions before submitting anything.

## Contact

Got questions, problems, or feedback, open an issue or find me on the Egosoft Discord in
the #x4_modding channel.

## Changelog

Need to make changes first.

## License

[MIT License](https://opensource.org/license/mit)
