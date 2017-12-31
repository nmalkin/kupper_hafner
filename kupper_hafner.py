import unittest

def observed_proportion_of_concordance(A_codes, B_codes):
    # Let the variables a_i, and b_i, denote the numbers of attributes for the i-th unit chosen by raters A and B, respectively
    a_i = len(A_codes)
    b_i = len(B_codes)

    # Let the random variable Xi denote the number of elements common to the sets A_i and B_i
    x_i = len(set(A_codes).intersection(set(B_codes)))

    # The observed proportion of concordance is pi_hat_i = x_i / max(a_i, b_i)
    pi_hat_i = x_i / max(a_i, b_i)

    return pi_hat_i


class ConcordanceProportionTest(unittest.TestCase):
    def test_concordance(self):
        # As a simple example, let K={P, Q, R, S} so that Card(K)=4.
        k = 4
        # Suppose that rater A chooses A_i={P}
        A_codes = ['P']
        # and rater B chooses B_i={P, R} to describe the i-th unit.
        B_codes = ['P', 'R']
        # Thus, the two raters agree on one attribute and pi_hat_i=1/2.
        self.assertEqual(0.5, observed_proportion_of_concordance(A_codes, B_codes))


def kupper_hafner(data1, data2, codebook=None):
    # Consider a study in which two equally trained raters, rater A and rater B, independently examine each of n units.
    if len(data1) != len(data2):
        raise Exception('The size of the datasets is different.')
    n = len(data1)


    # Following examination of the ith unit, each rater must decide which subset, from a prespecified set of k>=2 nominal attributes, best describes the i-th unit.
    # k = len(codebook), but we will compute it later, when we know the codebook has been populated.

    pi_hat = []
    min_codes = []
    observed_codebook = set()
    for A_codes, B_codes in zip(data1, data2):
        # Find the observed proportion of concordance
        pi_hat_i = observed_proportion_of_concordance(A_codes, B_codes)
        pi_hat.append(pi_hat_i)

        # Also store the minimum number of codes, in order to compute the chance correction (explained below)
        min_codes.append(min(len(A_codes), len(B_codes)))

        # Keep track of the codes we've seen
        observed_codebook.update(A_codes)
        observed_codebook.update(B_codes)

    # Establish k, the size of the codebook
    if codebook is None:
        codebook = observed_codebook
    k = len(codebook)

    # The overall observed concordance between raters A and B can be computed as the average of the pi_hat_i's
    pi_hat = sum(pi_hat) / len(pi_hat)

    # However, since some of this observed agreement will be due purely to chance, the quantity should be adjusted in an appropriate manner
    # […]
    # pi_0 = Sum_i{min(a_i, b_i)} / (nk)
    pi_0 = sum(min_codes) / (n * k)

    # The overall measure of chance-corrected concordance between rater A and rater B is
    # C_AB = (pi_hat - pi_0) / (1 - pi_0)
    C_AB = (pi_hat - pi_0) / (1 - pi_0)

    return C_AB
