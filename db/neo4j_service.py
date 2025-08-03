class Neo4jService:
    def __init__(self,driver):
        self.driver = driver

    def close(self):
        self.driver.close()

    def run_query(self, query:str,kwargs:dict=None,list_of_entities:list=None):
        with self.driver.session() as session:
            if not kwargs and not list_of_entities:
                session.run(
                    query
                )
                
            elif kwargs:
                session.run(
                    query,
                    **kwargs
                )
            elif list_of_entities:
                session.run(
                    query,
                    {"list_of_entities": list_of_entities}
                )
    
