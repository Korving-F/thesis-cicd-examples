def string_reverser(text):
  if len(text) < 20:
    return text[::-1]
  return None

def is_prime(number):
  if number <= 1:
    return False
  for n in range(2, number):
    if number % n == 0:
      return False
    else:
      return True
