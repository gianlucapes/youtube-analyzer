class Neo4jService:
    def __init__(self,driver):
        self.driver = driver

    def close(self):
        self.driver.close()

    def create_entity(self, query:str,kwargs:dict):
        with self.driver.session() as session:
            session.run(
                query,
                **kwargs
            )
