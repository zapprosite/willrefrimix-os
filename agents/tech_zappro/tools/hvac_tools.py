import os
from langchain.tools import tool

class HVACTools:
    @tool("query_qdrant_manuals")
    def query_qdrant_manuals(query: str):
        """Consulta o Vector DB Qdrant para encontrar soluções em manuais técnicos Daikin/Elgin."""
        # Integração futura com qdrant-client
        return f"Resultado da busca semântica para: {query} (Simulado)"

    @tool("capture_pocophone_data")
    def capture_pocophone_data(instruction: str):
        """Aciona o ADB no Pocophone para capturar dados do app Facilita Técnico."""
        try:
            os.system("adb shell screencap -p /sdcard/screen.png")
            os.system("adb pull /sdcard/screen.png /srv-2/willrefrimix-os/memory/raw_images/")
            return "✅ Captura de tela do Pocophone realizada e enviada para análise Vision."
        except Exception as e:
            return f"❌ Erro ao acessar ADB: {str(e)}"
