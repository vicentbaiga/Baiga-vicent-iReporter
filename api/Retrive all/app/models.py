from datetime import datetime
redflag = []


class Red_flag:
    
    def __init__(self, created_by, location, status, comment):

        self.created_on = datetime.now().replace(second=0, microsecond=0)
        self.created_by = created_by  
        self.location = location  
        self.comment = comment
        self.id = len(redflag) + 1

    
    

