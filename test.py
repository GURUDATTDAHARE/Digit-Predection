import pickle


list=[2, 3, 7, 5, 10, 17, 12, 4, 1, 13]
file='text.pkl'
fileobj=open(file,'wb')
pickle.dump(list,fileobj)
fileobj.close()