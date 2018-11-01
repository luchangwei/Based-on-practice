def input_test(i_str):
    test_s = {}
    for i in set(i_str):
        num = i_str.count(i)
        test_s[i] = num
    print(test_s)
r= input("请输入字符：")
input_test(r)
