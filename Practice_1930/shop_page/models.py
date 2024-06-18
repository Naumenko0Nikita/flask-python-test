from project.settings import DATABASE

class Product(DATABASE.Model):
    
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.String, nullable = False)
    
    def __repr__(self) -> str:
        
        return f"ID - {self.id}\nNAME - {self.name}"