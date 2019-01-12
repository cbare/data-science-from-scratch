# Data Science from Scratch

Examples and hacks inspired by Joel Grus' [Data Science from Scratch][1].

* [Joel's github repo][2]


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
19. Clustering
20. Natural Language Processing
21. Network Analysis
22. Recommender Systems
23. Databases and SQL
24. MapReduce


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
