# a = input()
# s =[]
# f = 0
# c = 0
# for i in a:
#     if(i in '{[('):
#         s.append(i)
#     elif(not s):
#         if(i == '}' and s[-1] == '{' or i == ']' and s[-1] == '[' or i == '(' and s[-1] == ')'):
#             s.pop()
#         else:
#             print(c)
#             f = 1
#             break






# def paranthesis_check(self):
#         b=list()
#         t=self.head
#         c=1
#         flag=1
#         while t.next:
#             if t.data in ']})':
#                 flag=0
#                 break
#             if t.data in '({[':
#                 b.append(t.data)
#             elif t.data == ')' and '(' == b[-1]:
#                 b.pop()
#             elif t.data == ']' and '[' == b[-1]:
#                 b.pop()
#             elif t.data == '}' and '{' == b[-1]:
#                 b.pop()
#             elif t.data !=b[-1]:
#                 break
#             t=t.next
#             c+=1
#         return -1 if len(b)==0 and flag==1 else c