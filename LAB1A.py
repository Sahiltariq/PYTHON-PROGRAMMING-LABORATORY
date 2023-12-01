m1=int(input("enter marks of the test one"))
m2=int(input("enter the marks of test 2nd"))
m3=int(input("enter the marks of test 3rd"))
if m1<=m2 and m1<=m3:
      avgmarks=(m2+m3)/2
elif m2<=m1 and m2<=m3:
      avgmarks=(m1+m3)/2
elif m3<=m1 and m3<=m2:
      avgmarks=(m1+m2)/2
print("evgmarks of best of two marks out of three test marks are",avgmarks)
