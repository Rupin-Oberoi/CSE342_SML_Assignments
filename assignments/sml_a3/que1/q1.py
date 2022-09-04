import pickle
import matplotlib

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

dict1 = unpickle("./cifar-10-batches-py/data_batch_1")


dict2 = {"name":"amul", "age":"2 months"}
print(dict2['name'])