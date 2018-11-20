# import dependencies
import random
import math
from matplotlib import pyplot as plt
from collections import Counter

# we are looking for the probability that "both children are girls" conditional on the event "the older child is a girl"

def random_kid():
    return random.choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)
for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

print("P(both | older):", both_girls / older_girl)
print("P(both | either):", both_girls / either_girl)

# normal distribution

def normal_pdf(x, mu = 0, sigma = 1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma = 1) for x in xs], '-', label = "mu = 0, sigma = 1")
plt.plot(xs, [normal_pdf(x, sigma = 2) for x in xs], '-', label = "mu = 0, sigma = 2")
plt.plot(xs, [normal_pdf(x, sigma = 0.5) for x in xs], '-', label = "mu = 0, sigma = 0.5")
plt.plot(xs, [normal_pdf(x, mu = -1) for x in xs], '-', label = "mu = -1, sigma = 1")
plt.legend()
plt.title("Various normal pdfs")
plt.show()

def normal_cdf(x, mu = 0, sigma = 1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# central limit theorem
def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]

    # use a bar chart to show the actual binomial samples
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
    [v / num_points for v in histogram.values()],
    0.8, 
    color = "0.75")

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # use a line chart to show the normal approximation
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
    for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial distribution vs normal approximation")
    plt.show()

make_hist(0.75, 100, 10000)