# %%
import os
from pinecone import Pinecone
from llama_index.llms.gemini import Gemini
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import StorageContext, VectorStoreIndex, download_loader

from llama_index.core import Settings


# %%
GOOGLE_API_KEY = "AIzaSyDe5fdajCq6xOANQ7bKZzLDf5q70SDmfsU"
PINECONE_API_KEY = "6d7761a8-f0c4-4e1f-bbd6-7a711b393bf9"

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


llm = Gemini()


# %%
pinecone_client = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
pinecone_index = pinecone_client.Index('rutgersdemo')

# %%
BeautifulSoupWebReader = download_loader("BeautifulSoupWebReader")

loader = BeautifulSoupWebReader()
URLS = [
"https://newbrunswick.rutgers.edu/academics/schools-colleges/school-of-arts-and-sciences",
"https://bloustein.rutgers.edu/",
 "https://gsapp.rutgers.edu/",
"https://gse.rutgers.edu/",
"https://www.masongross.rutgers.edu/",
"https://www.business.rutgers.edu/","https://sas.rutgers.edu/",
"https://comminfo.rutgers.edu/",
"https://soe.rutgers.edu/apply",
"https://sebs.rutgers.edu/",
"https://grad.rutgers.edu/",
"https://smlr.rutgers.edu/",
"https://socialwork.rutgers.edu/",
"https://pharmacy.rutgers.edu/",
"https://njms.rutgers.edu/",
"https://rwjms.rutgers.edu/",
"https://sdm.rutgers.edu/",
"https://shp.rutgers.edu/",
"https://nursing.rutgers.edu/",
"https://sph.rutgers.edu/"
]
documents = loader.load_data(urls=URLS)

# %%
embed_model = GeminiEmbedding(model_name="models/embedding-001")

Settings.llm = llm
Settings.embed_model = embed_model
Settings.chunk_size = 512

# %%
# Create a PineconeVectorStore using the specified pinecone_index
vector_store = PineconeVectorStore(pinecone_index=pinecone_index)

# Create a StorageContext using the created PineconeVectorStore
storage_context = StorageContext.from_defaults(
    vector_store=vector_store
)

# Use the chunks of documents and the storage_context to create the index
index = VectorStoreIndex.from_documents(
    documents, 
    storage_context=storage_context
)

# %%
query_engine = index.as_query_engine()

# Query the index, send the context to Gemini, and wait for the response
# Ask for a query from the user
query = input("Enter your query: ")

# Query the index with the user's query, send the context to Gemini, and wait for the response
gemini_response = query_engine.query(query)


# %%
print(gemini_response)


