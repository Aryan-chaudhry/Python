# unordered unique and immutable
st = {1,2,3,4,5}

# methos
st.add(10);
print(st);

# remove
st.remove(3)
print(st);

# pop --> rmeove random element
st.pop();
print(st);

# clear --> clear the set
st.clear();
print(st);

s1 = {1,2,3,4,5}
s2 = {2,3,4,5,6,7};

# union
s3 = s1.union(s2);
print(s3);

# intersection
s4 = s1.intersection(s2);
print(s4)