# Data Science from Scratch

Examples from the book and a few other hacks inspired by [Joel Grus][3]' [Data Science from Scratch][1].

* [Joel's github repo][2]


## Mini book review

I had a lot of fun with this book. Data science lends itself to the hacker's approach of diving in and getting your hands dirty with a breadth of topics.

That said, the book gives a fly-over view of some fairly deep subjects, leaving the reader with a good lay of the land but also an  intimidating sense of how much there is left to learn.

I had little problem using Python 3 to work through the book even though it's done in Python 2. You'll have to add some parentheses here and there and be aware that map is a generator in Python 3. The 2nd Edition is fully Python 3 and in the works now.


## Chapters

01. [Introduction](chapter_01)
02. A Crash Course in Python
03. [Visualizing Data](chapter_03)
04. [Linear Algebra](chapter_04)
05. [Statistics](chapter_05)
06. [Probability](chapter_06)
07. [Hypothesis and Inference](chapter_07)
08. [Gradient Descent](chapter_08)
09. [Getting Data](chapter_09)
10. [Working with Data](chapter_10)
11. [Machine Learning](chapter_11)
12. [k-Nearest Neighbors](chapter_12)
13. [Naive Bayes](chapter_13)
14. [Simple Linear Regression](chapter_14)
15. [Multiple Regression](chapter_15)
16. [Logistic Regression](chapter_16)
17. [Decision Trees](chapter_17)
18. [Neural Networks](chapter_18)
19. [Clustering](chapter_19)
20. [Natural Language Processing](chapter_20)
21. [Network Analysis](chapter_21)
22. [Recommender Systems](chapter_22)
23. Databases and SQL
24. [MapReduce](chapter_24)


## Links

* Joel's Jupyter-con talk [I don't like notebooks](http://preview.pyvideo.org/jupytercon-2018/i-dont-like-notebooks-joel-grus-allen-institute-for-artificial-intelligence.html) and [slides](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/edit#slide=id.g3b600ce1e2_0_0).

* [Building a deep learning library](https://www.youtube.com/watch?v=o64FV-ez6Gw)

* [100+ Interesting Data Sets for Statistics](http://rs.io/100-interesting-data-sets-for-statistics/) by Robb Seaton


## Note:

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
[3]: http://joelgrus.com/
