# Click: Documentation Rewrite

*Published: 22 October 2026*, *Updated: 23 October 2026*

## Click
[Click](https://github.com/pallets/click/) is a widely used (10 million download a month) Python package used to build command line utilities.

To build a utility, just decorate a function:

```Python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()

```

Then it is runnable from the the command line.

```bash
$ python hello.py --count=2
Your name: John
Hello John!
Hello John!

```
With a [few additional steps](https://click.palletsprojects.com/en/stable/entry-points/), the command line utility can be installed globally. Then it can be run by name alone.

```bash
$ hello --count=1
Your name: John
Hello John!
```

In addition to its own use, it is an integral part to other popular command line utility packages such as [Typer](https://github.com/fastapi/typer) (20 k stars).

## Intro

Click's documentation was totally rewritten starting late 2024 and finishing on May 31, 2026. Every line was considered. Nearly every line was revised. The organization was totally rethought. This was done across 60+ prs by me with help from the community (in no particular order [Kevin Deldycke](https://github.com/kdeldycke), [David Lord](https://github.com/davidism), [Andreas Backx](https://github.com/AndreasBackx), [Jaron Rosenau](https://github.com/denuoweb), and others)


## My story
Note: At various points, I will say 'this was slow' or 'PRs were not getting reviewed'. I present these as relevant facts with no judgement on maintainers. Everyone at [Pallets](https://palletsprojects.com/), myself included, are volunteers. Things get done when they get done. There are no timelines or pressure to meet deadlines as is common in the business world.

I became a contributor to Click in [June 2023](https://github.com/pallets/click/pull/2515). At that point, I had used it on some small work projects, read through the documentation multiple times, and was familiar with Click's technical and organizational issues. As contributed to the docs and experimented with the API more, I saw just how under documented Click was. At this point, I started to form the idea for a documentation rewrite. I toyed with it a bit, but wrote it off since, since my PRs being getting merged in very slowly.

After some contributions, I gain merge permissions in [October 2024](https://github.com/pallets/click/pull/2551). Then I really started to think the rewrite was possible. I could put up PR's and ask for a review, and if I did not get one, which I rarely did, I could just merge it myself. So I started.

## Goals
1. Be more precise i.e. say exactly what is meant without using esoteric jargon
2. More concise i.e. say more with less
1. More comprehensive
1. Assume the reader is proficient in python, but not the commandline
1. Organized according to [Diataxis](https://diataxis.fr/)
1. Better organization with a specific focus of being able to navigate with minimal clicks ie more skim-able
1. Written in [Myst](https://myst-parser.readthedocs.io/en/latest), Markdown + the power of [ReStructured Text](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)

## Why
Some of the goals are self explanatory, so I will skip those.

### More precise, more concise
The prior click docs were written very conversationally, which made them an easy read, but at the cost of precision and conciseness. I don't think that was a good trade. I don't intend the reference documentation to be read like a book, start to finish. I intend it to be consulted, and when consulted, for explanations to stand on their own and be very clear. Additionally extra length makes it harder to find the correct part to consult.

### Proficient in Python but not the commandline
Many people that develop in Python do so with a partial understanding of the language. They want to use it to do something rather than make a web app. The data scientist comes to [explore the data](https://blog.jetbrains.com/pycharm/2025/09/why-is-python-so-popular/#2-strength-in-data-science-and-analytics). The IT professional comes to make scripts to automate processes. They have an area of expertise, and Python is just a way to leverage that expertise. For them, a common workflow is is running scripts directly with `python -m script.py`. The next logical step to increase utility for commonly run scripts is to turn them  into command line utilities. So I want to documentation to meet them where they are. The minor downside is that we maintain some documentation that software engineers can just skim over.

### Diataxis
The essence of diataxis is to the split the documentation into major categories and to have sections of the documentation fit nicely into a single category. By deciding in advance which category a section fits into, the essential questions of audience, purpose, and writing style are also decided. Overall the documentation becomes more easy to navigate and maintain.
* Reference - for the doer trying to know how the api works
* Concepts - for the learner trying to understand why something was designed a certain way
* Guide - for the doer trying to get a specific task done
* Tutorial - for the learner to learn by doing something

A person knows what they are coming to the docs to do or learn, and once they understand the sections, they can quickly navigate to the correct quartile of the documentation.

### Written in Myst Markdown
Python documentation is traditionally written in ReStructured text, which is very powerful but not easy to write or used outside of Python. But many Python developers use Python and another language, and most other language document in Markdown. So then the best choice is one that is mostly Markdown but also extends it with power features such as arbitrary cross-linking, so [Myst](https://mystmd.org/) is the choice.



## Before and After
These examples try to give the flavor of what was achieved in the rewrite. To see for yourself poke around in the [web archive](https://web.archive.org/web/20240128021053/https://click.palletsprojects.com/en/8.1.x/) and the [current docs](https://click.palletsprojects.com/en/stable/).

The examples are provided from the web archive which can be slow so open links in a separate tab for best performance. Sections were removed so the reader can more easily compare the same text before and after
### Precise and Conciseness
* [Parameters before](https://web.archive.org/web/20240329183124/https://click.palletsprojects.com/en/8.1.x/parameters/) :

```{toggle}
Click supports two types of parameters for scripts: options and arguments.
There is generally some confusion among authors of command line scripts of
when to use which, so here is a quick overview of the differences. As
its name indicates, an option is optional. While arguments can be optional within reason, they are much more restricted in how optional they can be.

To help you decide between options and arguments, the recommendation is to use arguments exclusively for things like going to subcommands or input filenames / URLs, and have everything else be an option instead.
#### Differences

Arguments can do less than options. The following features are only available for options:
* automatic prompting for missing input
* act as flags (boolean or otherwise)
* option values can be pulled from environment variables, arguments can not
* options are fully documented in the help page, arguments are not (this is intentional as arguments might be too specific to be automatically documented)

On the other hand arguments, unlike options, can accept an arbitrary number of arguments. Options can strictly ever only accept a fixed number of arguments (defaults to 1), or they may be specified multiple times using Multiple Options.

**... Section Removed  ...**

```
* [Parameters after](https://click.palletsprojects.com/en/stable/parameters/):
````{toggle}
Click supports only two principle types of parameters for scripts (by design): options and arguments.
#### Options
* Are optional.
* Recommended to use for everything except subcommands, urls, or files.
* Can take a fixed number of arguments. The default is 1. They may be specified multiple times using Multiple Options.
* Are fully documented by the help page.
* Have automatic prompting for missing input.
* Can act as flags (boolean or otherwise).
* Can be pulled from environment variables.

#### Arguments

* Are optional within reason, but not entirely so.
* Recommended to use for subcommands, urls, or files.
* Can take an arbitrary number of arguments.
* Are not fully documented by the help page since they may be too specific to be automatically documented. For more see Documenting Arguments.
* Can be pulled from environment variables but only explicitly named ones. For more see Environment Variables.


**... Section Removed  ...**
````
* Parameters analysis: 30 percent shorter (194 words vs 137 words) with no significant loss of meaning. More comprehensible format.
* [Basic Options before](https://web.archive.org/web/20240128021053mp_/https://click.palletsprojects.com/en/8.1.x/options/#basic-value-options)
````{toggle}
The most basic option is a value option. These options accept one argument which is a value. If no type is provided, the type of the default value is used. If no default value is provided, the type is assumed to be STRING. Unless a name is explicitly specified, the name of the parameter is the first long option defined; otherwise the first short one is used. By default, options are not required, however to make an option required, simply pass in required=True as an argument to the decorator.

```{code-block} python
@click.command()
@click.option('--n', default=1)
def dots(n):
    click.echo('.' * n)

# How to make an option required
@click.command()
@click.option('--n', required=True, type=int)
def dots(n):
    click.echo('.' * n)

# How to use a Python reserved word such as `from` as a parameter
@click.command()
@click.option('--from', '-f', 'from_')
@click.option('--to', '-t')
def reserved_param_name(from_, to):
    click.echo(f"from {from_} to {to}")
```
And on the command line:
```{code-block} shell
$ dots --n=2
..
```
**... Section continues for another page...**
````
* [Basic options after](https://click.palletsprojects.com/en/stable/options/#basic-example)
````{toggle}
A simple click.Option takes one option name. By default, it’s assumed that the decorated function argument is not required and the expected type is str. If the decorated function takes a positional argument but the option is not passed with the command, then None is passed.
```{code-block} python
@click.command()
@click.option('--text')
def print_this(text):
    click.echo(text)
```
```{code-block} bash
$ print-this --text=this
this
$ print-this
```

```{code-block} bash
$ print-this --help
Usage: print-this [OPTIONS]

Options:
  --text TEXT
  --help       Show this message and exit.
```
````
* Basic example analysis: The before section does too much. The point of a basic example to show a very minimal example of what a single option does in action and on the help page. The different ideas brought up in the before section are given their own concise sections.


### Organization
* [Home page before](https://web.archive.org/web/20240328214125/https://click.palletsprojects.com/en/8.1.x/)  Just a giant overflowing list 5 + pages in length with every section and sub section
* [Home page after](https://click.palletsprojects.com/en/stable/): Nicely nested layout of about 2 pages with a scannable list of sections
* Basic Commands, Group, Context before: scattered in different sections or not written at all. The table below maps about where the sections came from.

| Stable section (8.5.x) | 8.1.7 origin | Status |
|---|---|---|
| Intro (Command / Group / Context) | `commands.rst` intro ("arbitrarily nesting… Command and Group") | Rewritten |
| Basic Command Example | `quickstart.rst`, "Basic Concepts - Creating a Command" | Moved, example changed to `--count` |
| Renaming Commands | Not in 8.1.7 docs | New |
| Deprecating Commands | Not in 8.1.7 docs (only `changes.rst`) | New |
| Basic Group Example | `quickstart.rst`, "Nesting Commands" + `commands.rst`, "Callback Invocation" | Merged, rewritten |
| Renaming Groups | Not in 8.1.7 docs | New |
| Group Invocation Without Command | `commands.rst`, same title | Moved, condensed |
| Group Separation | `commands.rst`, "Passing Parameters" | Moved, near-verbatim |
| Arbitrary Nesting | `commands.rst` intro + `quickstart.rst`, "Nesting Commands" | Partly new (`session` example origin unchecked) |
| Lazily Attaching Commands | `quickstart.rst`, "Registering Commands Later" | Moved |
| Context Object (intro) | `commands.rst`, "Nested Handling and Contexts" | Rewritten, `ctx.obj` material left behind |
| Auto Envvar Prefix | `options.rst`, "Values from Environment Variables" | Moved, near-verbatim |
| Global Context Access | `advanced.rst`, same title | Moved, near-verbatim |
| Parameter Source Priority | Not in 8.1.7 docs | New |
| Detecting the Source of a Parameter | `advanced.rst`, same title | Moved, near-verbatim |
* [Basic Commands, Group, Context after](https://click.palletsprojects.com/en/stable/commands-and-groups/): Own section with nice table of contents at the top
* [Options before](https://web.archive.org/web/20240329123600/https://click.palletsprojects.com/en/8.1.x/options/): A list so big its hard to navigate
* [Options after](https://click.palletsprojects.com/en/stable/options/#options): Added table of contents at the top. Table of contents has links to all sections. Click on the link to go to section then click on the section header to jump back to table of contents.


## Tips for repeating the process
### General
* Form goals and form consensus with the team about the goals. 7 tightly scoped goals is probably max.
* Try very hard to get reviews for the the changes. This is not always possible, but great docs are best formed by multiple people since they serve people coming from many backgrounds.
* If the project has a lot of docs, then the grind is real with a lot of the value coming when the process is totally done. So better to have a few goals and finish than have many and get halfway done.
### Diataxis
* This usually requires multiple passes.
* In the first pass, for each subsection (the smallest section that has a heading), decide whether it belongs in reference, concepts, guides, or tutorials then rewrite it to more cleanly fit in that section. Some subsections may not need rewriting. If multiple people are working on it, then you may need an issue to keep track of this.
* In the second pass do a reorg by type. Then mark the holes that appear and with issues.
* **Payoff:**  Really good, but things were a bit messy until the second pass was done.
### More skim-able
* This was mostly just adding auto generated table of contents provided by Myst and replacing paragraphs with bullets and tables.
* **Payoff:** Less words => less to maintain. Anecdotally, I have had two completely unprompted instances of users' saying that the new docs are very easy to navigate.
### Myst
