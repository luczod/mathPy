# 1: Using Venn Diagrams to Visualize Relationships Between Sets

import csv
import pathlib
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet

current_dir = pathlib.Path(__file__).parent.resolve()

def read_csv(filename: str) -> tuple[list[int], list[int]]:
  football = []
  others = []

  with open(filename, "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
      if row[1] == '1':
        football.append(row[0])
      if row[2] == '1':
        others.append(row[0])

    return football, others

def draw_venn(sets: tuple[FiniteSet, FiniteSet]):
  venn2(subsets=sets, set_labels=('Football', 'Other')) # type: ignore
  plt.show()

if __name__ == '__main__':
  football, others = read_csv(f'{current_dir}/sports.csv')
  setFootball = FiniteSet(*football)
  setOthers = FiniteSet(*others)

  draw_venn((setFootball, setOthers))