def strip_str(str):

    if len(str) <= 2:
        i_str.append(str)
    else:
        str = str[:2]
        i_str.append(str)
    return i_str
a= True
i_str = []
while a:
    us_str = input("请输入字符：")
    if 'end' in us_str:
        a= False
    end_list = strip_str(us_str)

#input_str = input("请输入字符：")
end_list.pop()
print(end_list)
