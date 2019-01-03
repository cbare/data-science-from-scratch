# Data Science from Scratch

Examples and hacks inspired by Joel Grus' [Data Science from Scratch][1].

* [Joel's github repo][2]


## Chapters

01. Introduction
02. A Crash Course in Python
03. Visualizing Data
04. Linear Algebra
05. Statistics
06. Probability
07. Hypothesis and Inference
08. Gradient Descent
09. Getting Data
10. Working with Data
11. Machine Learning
12. k-Nearest Neighbors
13. Naive Bayes
14. Simple Linear Regression
15. Multiple Regression
16. Logistic Regression
17. Decision Trees
18. Neural Networks
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
