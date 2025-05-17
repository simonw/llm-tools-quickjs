# llm-tools-quickjs

[![PyPI](https://img.shields.io/pypi/v/llm-tools-quickjs.svg)](https://pypi.org/project/llm-tools-quickjs/)
[![Changelog](https://img.shields.io/github/v/release/simonw/llm-tools-quickjs?include_prereleases&label=changelog)](https://github.com/simonw/llm-tools-quickjs/releases)
[![Tests](https://github.com/simonw/llm-tools-quickjs/actions/workflows/test.yml/badge.svg)](https://github.com/simonw/llm-tools-quickjs/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/llm-tools-quickjs/blob/main/LICENSE)

JavaScript execution as a tool for LLM

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
llm install llm-tools-quickjs
```
## Usage

To use this with the [LLM command-line tool](https://llm.datasette.io/en/stable/usage.html):

```bash
llm '43424 * 234234' -T quickjs -m gpt-4.1-mini --tools-debug
```
Example output:
```
Tool call: quickjs({'javascript': 'function execute() {\n  return 43424 * 234234;\n}'})
  10171377216.0
The result of multiplying 43424 by 234234 is 10,171,377,216.
```

With the [LLM Python API](https://llm.datasette.io/en/stable/python-api.html):

```python
import llm
from llm_tools_quickjs import quickjs

model = llm.get_model("gpt-4.1-mini")

chain = model.chain(
    "Draw a 40 character wide mandelbrot with JavaScript",
    tools=[quickjs]
)
print(chain.text())
```
I got:
````
Here is a 40 character wide Mandelbrot set rendered in ASCII using JavaScript. The
characters represent iteration counts for points in the Mandelbrot set, creating a
visual pattern that resembles the fractal:

```
...........................::...........
...........................::...........
..........................*  ...........
.........................:   :..........
......................: -      :::......
.....................:+          .......
..............:......:           :......
...............*:-:.:            :......
..............:-    :             ......
.............::     =            *......
......                          :.......
.............::     =            *......
..............:-    :             ......
...............*:-:.:            :......
..............:......:           :......
.....................:+          .......
......................: -      :::......
.........................:   :..........
..........................*  ...........
...........................::...........
```

If you'd like a different size or more detail, just let me know!
````

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-tools-quickjs
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
