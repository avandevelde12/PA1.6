from numpy.random import default_rng

class RNG:
    def __init__(self, seed: int):
        self.rng = default_rng(seed)

    def gauss(self, mu: float, sigma: float) -> float:
        sample = self.rng.normal(mu, sigma)
        return float(sample)

    def uniform(self, a: float, b: float) -> float:
        sample = self.rng.uniform(a, b)
        return float(sample)

    def bernoulli(self, p: float) -> bool:
        sample = self.rng.binomial(1, p)
        return bool(sample)
