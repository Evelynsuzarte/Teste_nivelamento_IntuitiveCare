import requests
import zipfile
from bs4 import BeautifulSoup
import os


def baixar_arquivosPDF(url, nomes_arquivos):
    result = requests.get(url)

    if result.status_code == 200:
        soup = BeautifulSoup(result.content,"html.parser")
        links = soup.find_all("a")

        for link in links:
            for nome in nomes_arquivos:
                href = link.get("href")
                href.endswith(".pdf")
                filename = os.path.basename(href)
                if filename == nome:
                    pdf_result = requests.get(href)
                    with open("Teste1/"+filename, "wb") as file:
                        file.write(pdf_result.content)
                    print(f"Arquivo '{filename}' baixado com sucesso.")

    else:
        print("Falha ao acessar o site.")

    
def transformar_zip(nomes_arquivos, nome_zip):
    with zipfile.ZipFile(nome_zip,'w') as zip_file:
        for nome in nomes_arquivos:
            if os.path.exists(nome):
                zip_file.write("Teste1/"+ nome,os.path.basename(nome))
                print(f"Arquivo '{nome}' adicionado ao ZIP.")
            else:
                print(f"Arquivo '{nome}' não encontrado. Ignorando.")
    print(f"Arquivo ZIP '{nome_zip}' criado com sucesso.")


url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
nomes_arquivos = ["Anexo_I_Rol_2021RN_465.2021_RN599_RN600.pdf","Anexo_II_DUT_2021_RN_465.2021_RN599.pdf"]
nome_zip = "Anexos.zip"

#baixar_arquivosPDF(url,nomes_arquivos)
transformar_zip(nomes_arquivos, nome_zip)

