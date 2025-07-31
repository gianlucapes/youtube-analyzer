from neo4j import GraphDatabase
from config import settings
from db.neo4j_service import Neo4jService

# Connessione al database Neo4j
uri = "bolt://localhost:7687"
username = "neo4j"

driver = GraphDatabase.driver(uri, auth=(username, settings.NEO4J_PASSWORD))

neo4jService=Neo4jService(driver=driver)