def_info ="bca course information:"
with open('bca.text','w')as bca_file:
    bca_file.write('bca_info')
intro_filename='intro.text'
with open(intro_filename,'r')as intro_file:
    lines=intro_file.readlines()
a_count=b_count=c_count=o
 for line in lines:
    if line.startswith('a'):
        a_count+=1
    else if line.startswith('b'):
         b_count+=1
    
    else if line.startswith('c'):
         c_count+=1

print("total lines starting with 'a':",a_count)
print("total lines starting with 'b':",b_count)
print("total lines starting with 'c':",c_count)
