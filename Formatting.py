message1 = '{0} is easier than {1}'. format('Python', 'Java')

message2 = '{1} is easier than {0}'. format('Python', 'Java')

message3 = '{:10.2f} and {:d}'. format(1.234234234, 12)

message4 = '{}'. format(1.234234234)

print(message1)
#You'll get 'Python is easier than Java'

print(message2)
#You'll get 'Java is easier than Python'

print(message3)

print(message4)
