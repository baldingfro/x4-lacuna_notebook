# Intro

All content shown in Lacuna Notebook is pulled from the Markdown files in docs/md_files.  
Everytime a change is made inside that folder, the converter script is run to write
a new t/0001.xml file.

There are several advantages to using Markdown files for this task:

* Editing 0001.xml directly, especially for large amounts of text is a nightmare
* Markdown is designed for plain-text formatting
* Content can be broken up into several files
* Content can easily viewed outside the game

## Important Notes

### Markdown Style & Formatting Guidelines

#### Markdown Style References

* [Markdown Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
* [Markdown lint tool](https://github.com/DavidAnson/markdownlint/)
  + VS Code extension available
    - Enable sublist style for unordered lists in settings.json

```json
    "markdownlint.config": {
        "MD004": {
            "style": "sublist"
        }
    },
```

#### Formatting Guidelines

* Keep lines to 80-characters or less
  + X4 does support word wrap but the display of the text lookers clean with an 80
    character limit

##### Lists Format

* Use two spaces for nested list items
* When text in a list spans multiple lines, indent additional lines under the first
  letter of the first line

### In-Game Display of Text vs in the Markdown Document

* Heading 1 (#) are used as the Category Title
* Heading 2 (##) are used as the Entry Title
* Heading 3 (###) and above are shown two levels higher in the Description Text
  + So ### becomes #, #### becomes ##, etc...
  + This change was made for cosmetic reasons so that headings start at # as expected
    instead of ### when viewing the Description Text in-game
* Markdown tables **will not** line up because to my knowledge, there is no fixed-width
  font available to use in X4.  There is the font "Zekton Fixed", but it was
  proportional instead of fixed-width and tables looked messed up in my testing.

### Handling of Escaped Characters by the Converter Script

* All XML reserved characters that need to be escaped such as &, <, >
* X4 text files (t-files) need to have ()'s and \'s escaped with a "\"
