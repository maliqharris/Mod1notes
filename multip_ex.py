import multiprocessing

def compute_square(x):
    return x * x
if __name__ == "__main__":
    with multiprocessing.Pool(processes=2) as pool:
        results = pool.map(compute_square, [1, 2, 3, 4])
        print(results)