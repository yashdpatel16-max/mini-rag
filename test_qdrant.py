# from qdrant_service import create_collection, insert_sample, search_test

# create_collection()
# insert_sample()

# results = search_test()
# print(results)

from app.retrieval.qdrant_service import create_collection, insert_sample, search_test

create_collection()
insert_sample()

results = search_test()
print(results)