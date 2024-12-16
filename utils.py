# Code by https://kioku-space.com/en/jupyter-skip-execution/
# as an alternative to using cell tags to suppress cell execution

from IPython.core.magic import register_cell_magic

@register_cell_magic
def skip(line, cell):
    return


