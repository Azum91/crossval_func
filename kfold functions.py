from sklearn.model_selection import train_test_split, KFold
import glob
import random
import shutil
import os


def kfold_data_split(k = None,path = None):
    
    data_class_path = glob.glob(path)
    
    list_all = []
    
    for i in data_class_path:
    
        class_idx = i.split('\\')[-1]
        
        images = glob.glob(i+'/*.jpg')
        
        for a in images:
        
            list_all.append([str(a),int(class_idx)])
    
    random.shuffle(list_all)
    
    train_data = np.array(list_all)
    
    x_train = train_data[:,0]
    
    y_train = train_data[:,1]
    
    folds = list(KFold(n_splits=k, shuffle=True, random_state=1).split(x_train, y_train))
    
    return folds, x_train, y_train

def kfold_folders(folds=None,x_train=None,y_train=None,save_folds_path=None):
    
    for j, (train_idx, val_idx) in enumerate(folds):
    
        print('\nFold ',j)
        
        x_train_cv = x_train[train_idx]
        
        y_train_cv = y_train[train_idx]
        
        x_valid_cv = x_train[val_idx]
        
        y_valid_cv= y_train[val_idx]
    #LOOPED TO CREATED TRAIN FILES OF EACH FOLD
        for i in range(len(x_train_cv)):
        
            desti_path = base_path + str(j) + '/train/' + y_train_cv[i] +'/'
            
            if not os.path.exists(desti_path):
            
                os.makedirs(desti_path)
            
            shutil.copy(x_train_cv[i],desti_path)
    #LOOPED TO CREATED VALIDATION FILES OF EACH FOLD
        for i in range(len(x_valid_cv)):
        
            desti_path = base_path + str(j) + '/val/' + y_valid_cv[i] +'/'
            
            if not os.path.exists(desti_path):
            
                os.makedirs(desti_path)
            
            shutil.copy(x_valid_cv[i],desti_path)
    
    return 'Process completed'