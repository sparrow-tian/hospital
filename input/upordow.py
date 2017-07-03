# rf = open('phmid.txt','r')
#
# #line_list=html.split('\r\n')
# new_list = []
# for line in rf:
#     if line.find('----->')!=-1:
#         new_list.append('\r\n'+line.strip())
#     else:
#         new_list.append(' '+line.strip())
#
#
#     #index=index+1
#
# #print ''.join(new_list)
# #print new_list

with open('phfmt.txt','r') as rf:
    for line in rf:
        if len(line.split('--->'))==3:
            print line
