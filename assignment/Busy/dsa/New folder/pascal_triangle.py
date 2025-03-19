class pascal_triangle:
    def __init__(self,number):
        self.number = number
        self.list = []

        for count in range(1,self.number+1):
            for counter in range(1,[count+1]):
                print(counter,end=" ")
                print([count])

# [
#     [1],
#     [1,1],
#     [1,2,1],
#     [1,3,3,1],
#     [1,4,6,4,1],
#     [1,5,10,10,5,1],
#     [1,6,15,20,15,6,1],
#     [1,7,21,35,35,21,7,1],
#     [1,8,28,56,70,56,28,8,1],
#     [1,9,36,84,126,126,84,36,9,1],
#
# ]