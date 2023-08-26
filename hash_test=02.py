import time
start=time.time()
int_val=4
str_val="GeekOfGeek"
flt_val=12.33
print("The integer hash value is : " + str(hash(int_val)))
print("The string hash value is : " + str(hash(str_val)))
print("The float hash value is : " + str(hash(flt_val)))
end = time.time()
print(f"Runtime of the program is {end - start}")
