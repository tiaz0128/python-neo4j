import dotenv
import os
from neo4j import GraphDatabase

load_status = dotenv.load_dotenv()
if load_status is False:
    raise RuntimeError("Environment variables not loaded.")

URI = os.getenv("NEO4J_URI")
AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
    print("Connection established.")
    query = """CREATE (:Person {name: $name, age: $age, email: $email})"""

    summary = driver.execute_query(
        query,
        name="Alice",
        age=33,
        database_="neo4j",
    ).summary

    print(
        "Created {nodes_created} nodes in {time} ms.".format(
            nodes_created=summary.counters.nodes_created,
            time=summary.result_available_after,
        )
    )
