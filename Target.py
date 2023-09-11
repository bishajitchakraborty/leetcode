n = int(input("Total Number:"))
array = [];
for i in range(0, n):
    ele = int(input())
    array.append(ele);

target_value =  int(input("Target Value:"))
sum=0;
for i in range(0,n):
    sum=sum+array[i];
    if sum == target_value:
        break;
    

print("Total Addistin:", sum);

