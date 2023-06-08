import sqlalchemy as db
 
class DBClient():
    def __init__(self, connection_str):
        engine = db.create_engine(connection_str)
        self.connection = engine.connect()
        metadata_obj = db.MetaData()
        
        self.dummy = db.Table(
            'dummy',                                        
            metadata_obj,                                    
            db.Column('name', db.String),                    
            db.Column('date_created', db.DateTime),                
            db.Column('date_modified', db.DateTime),                
        )
        
        metadata_obj.create_all(engine)

