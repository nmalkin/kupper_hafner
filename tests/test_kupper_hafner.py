from __future__ import division
import unittest


from kupper_hafner import *


class ConcordanceProportionTest(unittest.TestCase):
    def test_concordance(self):
        # As a simple example, let K={P, Q, R, S} so that Card(K)=4.
        k = 4
        # Suppose that rater A chooses A_i={P}
        A_codes = ['P']
        # and rater B chooses B_i={P, R} to describe the i-th unit.
        B_codes = ['P', 'R']
        # Thus, the two raters agree on one attribute and pi_hat_i=1/2.
        self.assertEqual(
            0.5, observed_proportion_of_concordance(A_codes, B_codes))


class KHStatisticTest(unittest.TestCase):
    def test_statistic(self):
        A_ratings = [[10], [20, 30], [40]]
        B_ratings = [[10, 20], [30], [40]]

        pi_hat = (0.5+0.5+1)/3
        pi_0 = 3/(3*4)
        self.assertEqual(kupper_hafner(A_ratings, B_ratings),
                         (pi_hat-pi_0)/(1-pi_0))


if __name__ == '__main__':
    unittest.main()
