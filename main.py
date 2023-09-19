import random

def genetic_algorithm(items, max_weight, population_size, mutation_rate, number_of_generations):
    # Losowa inicjalizacja populacji
    population = []
    for i in range(population_size):
        chromosome = [random.randint(0, 1) for _ in items]
        population.append(chromosome)

    # Funkcja fitness - liczy wartość i wagę plecaka
    def fitness(chromosome):
        value = weight = 0
        for i, item in enumerate(items):
            if chromosome[i] == 1:
                value += item[0]
                weight += item[1]
        if weight > max_weight:
            value = 0
        return value, weight

    # Krzyżowanie dwóch rodziców - operator jednopunktowy
    def one_point_crossover(parent1, parent2):
        crossover_point = random.randint(0, len(parent1) - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        return child

    # Krzyżowanie dwóch rodziców - operator dwupunktowy
    def two_point_crossover(parent1, parent2):
        crossover_point1 = random.randint(0, len(parent1) - 1)
        crossover_point2 = random.randint(crossover_point1, len(parent1) - 1)
        child = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
        return child

    # Mutacja chromosomu - losowa zamiana bitów z zadanym prawdopodobieństwem
    def mutate(chromosome):
        for i in range(len(chromosome)):
            if random.random() < mutation_rate:
                if chromosome[i] == 1:
                    chromosome[i] = 0
                else:
                    chromosome[i] = 1
        return chromosome

    # Główna pętla algorytmu
    for generation in range(number_of_generations):
        # Ocena populacji
        population_with_values = [
            (chromosome, fitness(chromosome)) for chromosome in population
        ]

        # Sortowanie populacji w oparciu o wartość (malejąco)
        population_with_values = sorted(
            population_with_values, key=lambda x: x[1][0], reverse=True
        )

        # Selekcja - wybór najlepszych chromosomów z posortowanej populacji
        population = [
            chromosome for chromosome, _ in population_with_values[:population_size//2]
        ]

        # Krzyżowanie i mutacja
        while len(population) < population_size:
            parent1 = random.choice(population)
            parent2 = random.choice(population)

        # Losowy wybór typu krzyżowania
            if random.random() < 0.5:
                child = one_point_crossover(parent1, parent2)
            else:
                child = two_point_crossover(parent1, parent2)

            # Mutowanie dzieci po krzyżowaniu
            child = mutate(child)
            # Dodawanie nowych dzieci do populacji
            population.append(child)

    # Zwracanie najlepszego rozwiązania
    best_result = population_with_values[0][1]
    best_value = best_result[0]
    best_weight = best_result[1]
    return population_with_values[0][0], best_value, best_weight

# item (wartość, waga)

def test_genetic_algorithm():
    items = [(2, 3), (3, 4), (1, 6), (4, 5)]
    max_weight = 8
    population_size = 100
    mutation_rate = 0.05
    number_of_generations = 100
    result, value, weight = genetic_algorithm(items, max_weight, population_size, mutation_rate, number_of_generations)
    expected_result = [1, 0, 0, 1]
    print(f'Do plecaka chcemy włożyć przedmioty: (wartość, waga) \n{items}\nMaksymalna waga: {max_weight}')
    print(f'Oczekiwano {expected_result}, otrzymano {result}')
    print(f'Maksymalna wartość {value} z użyciem wagi {weight}\n')

    items = [(10, 1), (20, 3), (30, 6), (40, 8)]
    max_weight = 10
    population_size = 100
    mutation_rate = 0.05
    number_of_generations = 100
    result, value, weight = genetic_algorithm(items, max_weight, population_size, mutation_rate, number_of_generations)
    expected_result = [1, 1, 1, 0]
    print(f'Do plecaka chcemy włożyć przedmioty: (wartość, waga) \n{items}\nMaksymalna waga: {max_weight}')
    print(f'Oczekiwano {expected_result}, otrzymano {result}')
    print(f'Maksymalna wartość {value} z użyciem wagi {weight}\n')

    items = [(40, 2), (160, 2), (70, 3), (300, 15), (70, 1), (25, 4), (25, 5), (180, 6)]
    max_weight = 15
    population_size = 100
    mutation_rate = 0.15
    number_of_generations = 100
    result, value, weight = genetic_algorithm(items, max_weight, population_size, mutation_rate, number_of_generations)
    expected_result = [1, 1, 1, 0, 1, 0, 0, 1]
    print(f'Do plecaka chcemy włożyć przedmioty: (wartość, waga) \n{items}\nMaksymalna waga: {max_weight}')
    print(f'Oczekiwano {expected_result}, otrzymano {result}')
    print(f'Maksymalna wartość {value} z użyciem wagi {weight}\n')

    items = [(40, 2), (160, 1), (70, 3), (200, 15), (130, 6), (70, 1), (25, 4), (35, 5), (120, 7)]
    max_weight = 20
    population_size = 100
    mutation_rate = 0.15
    number_of_generations = 100
    result, value, weight = genetic_algorithm(items, max_weight, population_size, mutation_rate, number_of_generations)
    expected_result = [1, 1, 1, 0, 1, 1, 0, 0, 1]
    print(f'Do plecaka chcemy włożyć przedmioty: (wartość, waga) \n{items}\nMaksymalna waga: {max_weight}')
    print(f'Oczekiwano {expected_result}, otrzymano {result}')
    print(f'Maksymalna wartość {value} z użyciem wagi {weight}\n')

test_genetic_algorithm()