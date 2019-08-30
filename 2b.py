def f1(s):
    st1=st.split(" ")
    st1.reverse()
    return st1

def f2(s):
    st=s[::-1]
    return st

st=input("Enter the string:")
print("Original string:\n",st)
print("\nWords in reverse order:\n",f1(st))
print("\nCharacters in reverse order:\n",f2(st))

    



