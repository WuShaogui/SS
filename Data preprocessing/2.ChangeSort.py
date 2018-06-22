
# coding: utf-8

# **二级排序氨基酸列表难在程序中实现,因此外部实现后,相应的氨基酸信息也跟着改变**

# In[5]:


cb513_flist2=list(map(lambda line:line.replace('\n',''),open('0.Featrue/aminslist_cb513_Q3').readlines()))
cullpdb_flist2=list(map(lambda line:line.replace('\n',''),open('0.Featrue/aminslist_cullpdb_Q3').readlines()))

cb513_amni=list(map(lambda line:line.replace('\n',''),open('0.Featrue/aminsinfo_cb513_Q3').readlines()))
cullpdb_amni=list(map(lambda line:line.replace('\n',''),open('0.Featrue/aminsinfo_cullpdb_Q3').readlines()))

cb513_flist3=list(map(lambda line:line.replace('\n',''),open('1.change/aminslist_cb513_Q3.sort').readlines()))
cullpdb_flist3=list(map(lambda line:line.replace('\n',''),open('1.change/aminslist_cullpdb_Q3.sort').readlines()))

print(len(cb513_flist2),len(cullpdb_flist2),len(cb513_amni),len(cullpdb_amni),len(cb513_flist3),len(cullpdb_flist3))


# In[6]:


fw_cb513=open('1.change/aminsinfo_cb513_Q3.sort','w')
for filename in cb513_flist3:
    content=cb513_flist2.index(filename)
    fw_cb513.write(cb513_amni[content]+'\n')
fw_cb513.close()


# In[ ]:


fw_cullpdb=open('1.change/aminsinfo_cullpdb_Q3.sort','w')
for filename in cullpdb_flist3:
    content=cullpdb_flist2.index(filename)
    fw_cullpdb.write(cullpdb_amni[content]+'\n')
fw_cullpdb.close()

