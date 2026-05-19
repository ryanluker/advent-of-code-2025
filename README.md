# Common commands

## Day 1 - 7
Use uv to consume the proper python version plus deps.
`uv run day-1.py`

## Day 8+
Use the runner helper, which cleaned up common file input code

> uv run [runner script] [puzzle day] [run mode (example|full)] [debug mode (True|False)]

`uv run runner.py day-8 example True`

## Pretty Debugging
Add the python breakpoint env to use ipdb instead
`PYTHONBREAKPOINT=ipdb.set_trace uv run day-2.py`
