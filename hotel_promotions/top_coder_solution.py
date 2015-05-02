class JanuszTheBusinessman:
  def makeGuestsReturn(self, arrivals, departures):
    n = len(arrivals)
    order = [(arrivals[i], departures[i]) for i in range(n)]
    order.sort()

    inter = lambda i, j: max(order[i][0], order[j][0]) <= min(order[i][1], order[j][1])

    dp = [[500 for i in range(n)] for j in range(n)]
    return order
    for i in range(n):
      j = 0
      while j < n and inter(i, j):
        dp[j][i] = 1
        j += 1
        
    for i in range(n):
      print(dp[i])
    print() 
    for i in range(n):
      for j in range(n):
        if dp[i][j] != 500:
          for k in range(j + 1, n):
            r = i + 1
            
            while r < n and inter(k, r):
              dp[r][k] = min(dp[r][k], dp[i][j] + 1)
              r += 1
    for i in range(n):
      print(dp[i])
    print()               
    return min(dp[n - 1])
	
z = JanuszTheBusinessman()

checkin = [154, 1, 340, 111, 92, 237, 170, 113, 241, 91, 228, 134, 191, 86, 59, 115, 277, 328, 12, 6]
checkout = [159, 4, 341, 118, 101, 244, 177, 123, 244, 96, 231, 136, 193, 95, 64, 118, 282, 330, 17, 13]

print z.makeGuestsReturn(checkin,checkout) 
