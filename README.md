# Data Science from Scratch

Examples and hacks inspired by Joel Grus' [Data Science from Scratch][1].

* [Joel's github repo][2]

I divided things up by chapter, which makes imports difficult. You'll have
to do some ridiculous thing like this:

```
export PYTHONPATH=./chapter_01:./chapter_03:./chapter_04:./chapter_05:./chapter_06:./chapter_07
```

or this:

```
import os.path
import sys
book_dir = '/Users/CBare/Documents/projects/data-science-from-scratch'
sys.path.extend(os.path.join(book_dir, 'chapter_{:02d}'.format(i)) for i in [3,4,5,6,7])
```


[1]: http://shop.oreilly.com/product/0636920033400.do
[2]: https://github.com/joelgrus/data-science-from-scratch
