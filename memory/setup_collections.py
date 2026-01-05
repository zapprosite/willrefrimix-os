import qdrant_client
from qdrant_client.http import models

client = qdrant_client.QdrantClient(host="localhost", port=6333)

def create_hvac_collections():
    # Coleção para Manuais Técnicos (Alta Precisão)
    client.recreate_collection(
        collection_name="manuais_tecnicos",
        vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE),
    )
    # Coleção para Histórico de Obras (Experiência Will Refrimix)
    client.recreate_collection(
        collection_name="historico_obras",
        vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE),
    )
    print("✅ Coleções 'manuais_tecnicos' e 'historico_obras' criadas no Qdrant.")

if __name__ == "__main__":
    create_hvac_collections()
