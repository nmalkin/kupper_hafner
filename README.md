Kupper-Hafner inter-rater agreement calculation
================================================

This repository contains code to calculate inter-rater agreement for multiple attribute responses, as described by Lawrence L. Kupper and Kerry B. Hafner in [their article](https://dx.doi.org/10.2307/2531695):

    On Assessing Interrater Agreement for Multiple Attribute Responses 
    ------------------------------------------------------------------
    Authors: Lawrence L. Kupper and Kerry B. Hafner
    Source: Biometrics, Vol. 45, No. 3 (Sep., 1989), pp. 957-967
    Published by: International Biometric Society
    Stable URL: https://www.jstor.org/stable/2531695


Why Kupper-Hafner agreement?
----------------------------
A common technique in scientific studies is for two or more raters to independently assign attributes to each item in a dataset (such as a response or specimen).
Inter-rater agreement, or [inter-rater reliability](https://en.wikipedia.org/wiki/Inter-rater_reliability), is used to measure the degree to which these raters end up agreeing with each other. Commonly used statistics for this include Cohen's kappa and Fleiss' kappa.

One assumption of these statistics, however, is that items are assigned to only one of several mutually exclusive categories. But, in certain coding situations, we want to be able to assign multiple codes to the same item. If we do that, the assumptions in the kappa statistics no longer hold.

The paper by Hupper and Hafner provides a statistic that allows the calculation of inter-rater agreement in these situations as well.

Installation
------------
This code implements Kupper-Hafner agreement in Python. It was written and tested in Python 3.
You can install it using pip:

    pip install git+https://github.com/nmalkin/kupper_hafner.git


Usage
-----
Let's say we have three items, and two raters (A and B) assigned them the following categories:

- Item 0: A rated it 10; B rated it 10, 20
- Item 1: A rated it 20, 30; B rated it 30
- Item 2: A rated it 40; B rated it 40

We would calculate Kupper-Hafner agreement as follows:
```python
from kupper_hafner import kupper_hafner

A_ratings = [[10], [20, 30], [40]]
B_ratings = [[10, 20], [30], [40]]
kupper_hafner(A_ratings, B_ratings)
```

If the codebook included categories that were not used by either rater, it can be provided as follows:

```python
codebook = [10, 20, 30, 40, 50]
kupper_hafner(A_ratings, B_ratings, codebook)
```