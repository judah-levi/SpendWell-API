class ReccomendationEngine():
    
    @staticmethod
    def get_rec_list(upc):
        rec_list = []

        julia = model(upc) #returns 3 objs

        rec_list.append(julia)
        return rec_list