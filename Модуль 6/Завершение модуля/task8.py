print(('Можно' if any(s == tuple(reversed(s))
                      for s in __import__('itertools').permutations(input())) else 'Нельзя')
      + ' сделать палиндромом')
