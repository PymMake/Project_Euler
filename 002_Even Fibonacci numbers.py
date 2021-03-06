'''Even Fibonacci numbers
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

偶斐波那契数
斐波那契数列中的每一项都是前两项的和。由1和2开始生成的斐波那契数列前10项为：
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …
考虑该斐波那契数列中不超过四百万的项，求其中为偶数的项之和。'''

a,b,y =1,1,0
while a <= 4000000:
    a,b = b,a+b
    if a%2 == 0:
        y += a

print(y)
