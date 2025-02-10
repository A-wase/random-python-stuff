# In general, use for loops when you already know the number of iterations
# and while loops when there is a condition that needs to be met.
import time
seats = 10
while seats > 0:
  print("Sell ticket")
  seats = seats - 1
  time.sleep(1)