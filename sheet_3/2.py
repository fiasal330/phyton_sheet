fl_num = 1234.5678
bef_int_num = 2
aft_int_num = 3

fl_str = str(fl_num)

bef_part, aft_part = fl_str.split(".")


result = bef_part[-bef_int_num:] + "." + aft_part[:aft_int_num]

print(result)