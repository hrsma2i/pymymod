class SpaceUnits(object):
    def __init__(self, max_n_layer, max_n_unit):
        self.max_n_layer = max_n_layer
        self.max_n_unit = max_n_unit
        self.length = sum([max_n_unit**nl for nl in range(1,max_n_layer+1)])
        
        itr = chain(*(
                product(*(
                    range(1, max_n_unit+1) 
                    for l in range(1, n_layer+1)
                ))
                for n_layer in range(1, max_n_layer+1)
        ))
        self.itr = itr
        
    def __iter__(self):
        return self.itr
    
    def __getitem__(self, i):
        itr = deepcopy(self.itr)
        return next(islice(itr, int(i), None))
    
    def __len__(self):
        return self.length
    

if __name__=='__main__':
    max_n_layer = 10
    max_n_unit  = 10
    su = SpaceUnits(max_n_layer, max_n_unit)
    print(len(su))
    print(su[70704])
