"""
tsp_ga.py
Genetic Algorithm solver for the 10-city TSP (start & end at A).
Usage: python tsp_ga.py
Produces console output and a route plot (requires matplotlib).
"""

import math
import random
import copy
import matplotlib.pyplot as plt

# === City coordinates ===
CITIES = {
    'A': (100, 300),
    'B': (200, 130),
    'C': (300, 500),
    'D': (500, 390),
    'E': (700, 300),
    'F': (900, 600),
    'G': (800, 950),
    'H': (600, 560),
    'I': (350, 550),
    'J': (270, 350)
}

# For consistent ordering
CITY_NAMES = list(CITIES.keys())

# Starting city fixed as 'A'
START = 'A'

# === Utilities ===
def euclidean(a, b):
    (x1, y1), (x2, y2) = a, b
    return math.hypot(x2 - x1, y2 - y1)

# Precompute distance matrix
DIST = {}
for i in CITY_NAMES:
    DIST[i] = {}
    for j in CITY_NAMES:
        DIST[i][j] = euclidean(CITIES[i], CITIES[j])

def route_distance(route):
    """route: list of city names starting and ending implicitly at START.
       route must contain every city exactly once, including START only once in list (we'll add start at ends)"""
    # route is expected to be a permutation of all cities with START included or excluded.
    # We'll treat route as sequence visiting all cities in order; ensure start at START.
    tour = [START] + route + [START]
    total = 0.0
    for i in range(len(tour)-1):
        total += DIST[tour[i]][tour[i+1]]
    return total

# === GA operators ===

def create_individual(all_cities_except_start):
    """Create random individual (list of city names without START)."""
    indiv = all_cities_except_start[:]
    random.shuffle(indiv)
    return indiv

def initial_population(pop_size, all_cities_except_start):
    return [create_individual(all_cities_except_start) for _ in range(pop_size)]

def tournament_selection(population, fitnesses, k=3):
    selected = random.sample(list(range(len(population))), k)
    selected.sort(key=lambda i: fitnesses[i])
    return copy.deepcopy(population[selected[0]])

def ordered_crossover(parent1, parent2):
    """Ordered crossover (OX) for permutations."""
    size = len(parent1)
    a, b = sorted(random.sample(range(size), 2))
    child = [None]*size
    # copy a..b from parent1
    child[a:b+1] = parent1[a:b+1]
    # fill remaining from parent2 in order
    p2_idx = 0
    for i in range(size):
        if child[i] is None:
            while parent2[p2_idx] in child:
                p2_idx += 1
            child[i] = parent2[p2_idx]
    return child

def swap_mutation(indiv, mutation_rate=0.02):
    indiv = indiv[:]
    for i in range(len(indiv)):
        if random.random() < mutation_rate:
            j = random.randrange(len(indiv))
            indiv[i], indiv[j] = indiv[j], indiv[i]
    return indiv

def evolve(population, pop_size, elite_size, mutation_rate, tournament_k):
    # compute fitnesses (lower is better)
    fitnesses = [route_distance(ind) for ind in population]
    # sort by fitness
    ranked = sorted(zip(population, fitnesses), key=lambda x: x[1])
    new_pop = [copy.deepcopy(ind) for ind, _ in ranked[:elite_size]]  # elitism

    # fill rest
    while len(new_pop) < pop_size:
        p1 = tournament_selection(population, fitnesses, k=tournament_k)
        p2 = tournament_selection(population, fitnesses, k=tournament_k)
        child = ordered_crossover(p1, p2)
        child = swap_mutation(child, mutation_rate)
        new_pop.append(child)
    return new_pop, [route_distance(ind) for ind in new_pop]

# === Main GA flow ===
def run_ga(
    generations=500,
    pop_size=200,
    elite_size=5,
    mutation_rate=0.02,
    tournament_k=5,
    seed=None,
    verbose=True
):
    if seed is not None:
        random.seed(seed)

    # Define genes: all cities excluding START (A)
    all_cities_except_start = [c for c in CITY_NAMES if c != START]

    pop = initial_population(pop_size, all_cities_except_start)
    best_distance = float('inf')
    best_route = None
    history = []

    for gen in range(1, generations+1):
        pop, fitnesses = evolve(pop, pop_size, elite_size, mutation_rate, tournament_k)
        gen_best_idx = min(range(len(pop)), key=lambda i: fitnesses[i])
        gen_best = pop[gen_best_idx]
        gen_best_dist = fitnesses[gen_best_idx]
        history.append(gen_best_dist)

        if gen_best_dist < best_distance:
            best_distance = gen_best_dist
            best_route = gen_best[:]

        if verbose and (gen % max(1, generations//10) == 0 or gen==1 or gen==generations):
            print(f"Gen {gen:4d} Best distance: {gen_best_dist:.2f} (overall best: {best_distance:.2f})")

    return {
        'best_route': [START] + best_route + [START],
        'best_distance': best_distance,
        'history': history
    }

# === Plotting ===
def plot_solution(solution):
    route = solution['best_route']
    xs = [CITIES[c][0] for c in route]
    ys = [CITIES[c][1] for c in route]

    plt.figure(figsize=(8,8))
    plt.plot(xs, ys, marker='o')
    for c in set(route):
        x,y = CITIES[c]
        plt.text(x+5, y+5, c, fontsize=12)
    plt.title(f"TSP route (distance {solution['best_distance']:.2f})")
    plt.grid(True)
    plt.show()

# === If run as script ===
if __name__ == '__main__':
    sol = run_ga(
        generations=800,
        pop_size=300,
        elite_size=8,
        mutation_rate=0.03,
        tournament_k=7,
        seed=42,
        verbose=True
    )
    print("\nBest route found:")
    print(" -> ".join(sol['best_route']))
    print(f"Total distance: {sol['best_distance']:.2f}")
    # plot
    plot_solution(sol)
