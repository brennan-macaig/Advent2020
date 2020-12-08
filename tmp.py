from collections import defaultdict
from re import match

def fit(d):
  required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
  return len(required.intersection(d.keys())) == len(required)

def fit2(d):
  if not 1920 <= int(d['byr']) <= 2002:
    return False

  if not 2010 <= int(d['iyr']) <= 2020:
    return False

  if not 2020 <= int(d['eyr']) <= 2030:
    return False

  hgt = d['hgt']
  hgt_match = match('^(\d{2,3})(cm|in)$', hgt)
  if not hgt_match:
    return False
  hgt_qty = int(hgt_match.group(1))
  if hgt.endswith('cm') and not 150 <= hgt_qty <= 193:
    return False
  elif hgt.endswith('in') and not 59 <= hgt_qty <= 76:
    return False

  if not match('^#[0-9a-f]{6}$', d['hcl']):
    return False

  if d['ecl'] not in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
    return False

  if not match('^\d{9}$', d['pid']):
    return False

  return True

with open('input/day4.txt') as f:
  # Split passport by multiple newline
  # Combine multiple passport lines into one
  passport_lines = [line.replace('\n', ' ').rstrip() for line in ''.join(f.readlines()).split('\n\n')]

  # Make key value pairs for passport
  ds = []
  for passport in passport_lines:
    d = defaultdict(str)
    for pair in passport.split(' '):
      k, v = pair.split(':')
      d[k] = v
    ds.append(d)

  print(len([d for d in ds if fit(d) and fit2(d)]))
