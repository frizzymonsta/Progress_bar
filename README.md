### Simple progress bar.

Usage:
```python
import progress_bar as pg

sample_list = range(0, 999)
Bar = pg.SetBar(text='Text', total=len(sample_list), filler='#') # emojii not supported

for i in sample_list:
    Bar.update_bar()
```