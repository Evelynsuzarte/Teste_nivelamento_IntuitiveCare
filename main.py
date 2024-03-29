import requests
import zipfile
import tabula
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
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
                zip_file.write(nome,os.path.basename(nome))
                print(f"Arquivo '{nome}' adicionado ao ZIP.")
            else:
                print(f"Arquivo '{nome}' não encontrado. Ignorando.")
    print(f"Arquivo ZIP '{nome_zip}' criado com sucesso.")


def transformar_csv(nome_arquivo):
    lista_df = tabula.read_pdf("Teste1/"+nome_arquivo, pages="all", encoding="utf-8")
    df = pd.concat(lista_df)
    df.to_csv("Teste2/"+nome_arquivo[:-4]+".csv", index=False)


def alterar_palavra(arquivo, palavras_antigas, palavras_novas):
    df = pd.read_csv("Teste2/"+arquivo)
    
    for antiga, nova in zip(palavras_antigas,palavras_novas):
        df.replace(antiga, nova, inplace=True)
    
    df.to_csv("Teste2/corrigido_"+arquivo[:-4]+'.csv', index=False, encoding='utf-8')




    


url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
nomes_arquivos = ["Anexo_I_Rol_2021RN_465.2021_RN599_RN600.pdf","Anexo_II_DUT_2021_RN_465.2021_RN599.pdf"]
nome_zip_teste1 = "Anexos.zip"
nome_zip_teste2 = "Teste2/Teste_EvelynSuzarteFernandes.zip"
palavras_antigas = ["OD","AMB"]
palavras_novas = ["Seg. Odontológica","Seg. Ambulatorial"]

#baixar_arquivosPDF(url,nomes_arquivos)
#transformar_zip("Teste1/"+nomes_arquivos, nome_zip_teste1)
transformar_csv(nomes_arquivos[0])
alterar_palavra("Anexo_I_Rol_2021RN_465.2021_RN599_RN600.csv",palavras_antigas, palavras_novas)
#transformar_zip(["Teste2/corrigido_"+nomes_arquivos[0][:-4]+".csv"], nome_zip_teste2)

