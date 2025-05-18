# 1: How Does the Temperature Vary During the Day?

import matplotlib.pyplot  as plt

hours = ['06:00 AM','07:00 AM','08:00 AM','09:00 AM','10:00 AM','11:00 AM','12:00 PM','13:00 PM','14:00 PM','15:00 PM','16:00 PM','17:00 PM','18:00 PM']
london_temp = [10,10,11,12,13,14,15,16,17,18,18,18,18]

plt.figure().set_figwidth(14)
# plt.figure(figsize=(10,6))
plt.plot(hours, london_temp, marker='o')

plt.title('London Temperature During the Day')
plt.xlabel('Hours')
plt.ylabel('Temperature')

plt.show()