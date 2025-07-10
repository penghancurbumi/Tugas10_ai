import random

teachers = ['Guru A', 'Guru B', 'Guru C']
subjects = ['Matematika', 'Fisika', 'Kimia']
classes = ['Kelas 1', 'Kelas 2', 'Kelas 3']
timeslots = ['Senin P1', 'Senin P2', 'Selasa P1', 'Selasa P2']

def create_individual():
    return [
        random.choice(teachers),
        random.choice(subjects),
        random.choice(classes),
        random.choice(timeslots)
    ]

def fitness(individual, schedule):
    conflicts = 0
    for entry in schedule:
        # Konflik: kelas dan waktu sama atau guru dan waktu sama
        if (individual[2] == entry[2] or individual[0] == entry[0]) and individual[3] == entry[3]:
            conflicts += 1
    return conflicts

def selection(population, schedule):
    sorted_pop = sorted(population, key=lambda x: fitness(x, schedule))
    return sorted_pop[:2]

def crossover(p1, p2):
    point = random.randint(1, 3)
    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]
    return c1, c2

def mutate(individual):
    idx = random.randint(0, 3)
    if idx == 0:
        individual[idx] = random.choice(teachers)
    elif idx == 1:
        individual[idx] = random.choice(subjects)
    elif idx == 2:
        individual[idx] = random.choice(classes)
    else:
        individual[idx] = random.choice(timeslots)

def genetic_algorithm():
    population_size = 10
    generations = 20
    population = [create_individual() for _ in range(population_size)]
    schedule = []

    for gen in range(generations):
        new_pop = []
        for _ in range(population_size // 2):
            p1, p2 = selection(population, schedule)
            c1, c2 = crossover(p1, p2)
            new_pop.extend([mutate(c1), mutate(c2)])
        population = new_pop

        best = min(population, key=lambda x: fitness(x, schedule))
        schedule.append(best)

        print(f"Gen {gen+1}: {best} | Fitness: {fitness(best, schedule)}")

    print("\nJadwal Akhir (tanpa konflik):")
    for item in schedule:
        print(f"{item[2]} - {item[1]} oleh {item[0]} pada {item[3]}")

genetic_algorithm()
