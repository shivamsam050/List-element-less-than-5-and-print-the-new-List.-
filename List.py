list =[2,5,6,7,1,3,9,8,0]
def my_list(num):
    list1 = []
    for i in list:
        if(i<num):list1.append(i)
    print(list1)
my_list(5)
print("-----------------------------------------------------------------------------------------------------------------\n")
num = int(input("Enter the Number = "))
my_list(num)