class Neo4jService:
    def __init__(self,driver):
        self.driver = driver

    def close(self):
        self.driver.close()

    def run_query(self, query:str,kwargs:dict=None):
        with self.driver.session() as session:
            if kwargs:
                session.run(
                    query,
                    **kwargs
                )
            else:
                session.run(
                    query
                )
