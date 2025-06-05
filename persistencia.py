import pickle
import os

def salvar_tarefas(tarefas, nome_arquivo="teste.pkl"):
    with open(nome_arquivo, "wb") as arquivo:
        pickle.dump(tarefas, arquivo)
    print(f"Tarefas salvas em '{nome_arquivo}' com sucesso!")

def carregar_tarefas(nome_arquivo="teste.pkl"):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "rb") as arquivo:
            tarefas = pickle.load(arquivo)
        print(f"Tarefas carregadas de '{nome_arquivo}' com sucesso!")
        return tarefas
    else:
        return []
