from pybaht import bahttext
from typing import List, Any
import json
import time

all_test_cases: List[Any]

# load test cases from json file
with open('tests/testcases.json') as d:
    all_test_cases = json.load(d)

n_test_cases = len(all_test_cases)
test_cases = all_test_cases[0:n_test_cases]
n_iterations = 10000


def process():
    global n_iterations

    start_time = time.time()
    for _ in range(n_iterations):
        run_test_cases()

    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")


def run_test_cases():
    global test_cases

    for test_case in test_cases:
        input_number = float(test_case["number"])
        expected_string = test_case["text"]
        actual_string = bahttext(input_number)


process()
