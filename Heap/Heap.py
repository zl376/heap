class Heap:
    '''
    Customized implementation of Heap (minimum)
    Suitable for:
        item that can be hashed (has unique key <-> item mapping)
    '''
    def __init__(self, 
                 map_item2key=None):
        '''
        ------
        Input:
            map_item2key    function(item: *) -> key: int
        '''
        self.data_ = [None]
        if not map_item2key is None:
            self.map_item2key_ = map_item2key
            self.map_item2key_store_ = None
        else:
            # Use step stamp as key
            self.map_item2key_store_ = dict()
            self.step_ = 0
            self.map_item2key_ = self._map_item2key_def
        self.map_key2ind_ = dict()
        
    
    def push(self, item, weight):
        '''
        ------
        Input:
            item,       *  
            weight,     float,      priority of item
        '''
        # append to tail
        self.data_.append([weight, item])
        ind = self.size
        key = self.map_item2key_(item)
        self.map_key2ind_[key] = ind
        # perc up
        self._perc_up(ind)
        
    
    def pop(self, item=None):
        '''
        ------
        Input:
            item,       *,       if None, pop the top item
        -------
        Output:
                        *,       poped item
        '''
        if item is None:
            item = self.data_[1][1]
        # swap {item} and tail
        key = self.map_item2key_(item)
        ind = self.map_key2ind_[key]
        self._swap(ind, self.size)
        # remove {item}
        self.data_.pop()
        self.map_key2ind_.pop(key)
        if not self.map_item2key_store_ is None:
            self.map_item2key_store_.pop(item)
        # perc down original tail
        self._perc_down(ind)
        return item
    
    
    def top(self):
        '''
        -------
        Output:
                        *,       head item
        '''        
        return self.data_[1][1]
    
    
    def update(self, item, weight):
        '''
        ------
        Input:
            item,       *  
            weight,     float,      priority of item
        '''
        # update item
        key = self.map_item2key_(item)
        ind = self.map_key2ind_[key]
        weight_old = self.data_[ind][0]
        self.data_[ind][0] = weight
        if weight > weight_old:
            # perc down
            self._perc_down(ind)
        else:
            # perc up
            self._perc_up(ind)
    
    
    def _perc_up(self, ind):
        '''
        Percolate up from index {ind}
        '''
        while ind > 1:
            ind_p = ind >> 1
            if self.data_[ind][0] >= self.data_[ind_p][0]:
                break
            # swap
            self._swap(ind, ind_p)
            # move up
            ind = ind_p
    
    
    def _perc_down(self, ind):
        '''
        Percolate down from index {ind}
        '''
        while (ind << 1) <= self.size:
            ind_lc = ind << 1
            ind_rc = ind_lc + 1
            ind_c = ind_rc if ind_rc <= self.size and self.data_[ind_rc][0] < self.data_[ind_lc][0] else ind_lc
            if self.data_[ind][0] <= self.data_[ind_c][0]:
                break
            # swap
            self._swap(ind, ind_c)
            # move down
            ind = ind_c
            
            
    def _swap(self, ind_a, ind_b):
        '''
        Swap items at indice {ind_a} and {ind_b}
        '''
        pair_a, pair_b = self.data_[ind_a], self.data_[ind_b]
        item_a, item_b = pair_a[1], pair_b[1]
        key_a, key_b = self.map_item2key_(item_a), self.map_item2key_(item_b)
        self.data_[ind_a], self.data_[ind_b] = pair_b, pair_a
        self.map_key2ind_[key_a], self.map_key2ind_[key_b] = ind_b, ind_a       
    
    
    def _map_item2key_def(self, item):
        '''
        Default function to map {item} to its key, the step stamp
        '''
        if not item in self.map_item2key_store_:
            self.map_item2key_store_[item] = self.step_
            self.step_ += 1
        return self.map_item2key_store_[item]
            
    
    @property
    def size(self):
        return len(self.data_) - 1
