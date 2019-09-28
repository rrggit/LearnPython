a = 10
b = 20

# Arithmetic

'''
+
-
*
/
%
**
'''

res = a * b

# Assignment 
'''
=
'''

a = 100
b = a

# Compound assignment
'''
+=
-=
*=
/=
%=
**=
'''

res **= a    # res = res ** a
'''
Not available
    ++  --> a += 1
    --  --> a -= 1
'''

# Comparision
'''
<
>
<=
>=
==
!=
'''

res = a == b

# Logical
'''
and
or
not
p   q   and     or  not(p)
0   0   0       0   1
0   1   0       1   1
1   0   0       1   0
1   1   1       1   0
'''

res = not((a < b) and (b == 100))
print('Result:', res)