from entities import Statistics
import numpy as np


def describe_run(outputs):
    final_results = __get_final_results(outputs)
    return str(Statistics(min=min(final_results), max=max(final_results),
                       median=np.median(final_results),
                       std=np.std(final_results), mean=np.mean(final_results)))


def __get_final_results(outputs):
    return [row[-1][1] for row in outputs]