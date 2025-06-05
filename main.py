import argparse
from ast import main
import os
from gerenciador import GerenciadorDeTarefas

# Apaga o arquivo .pkl se existir
#if os.path.exists("teste.pkl"):
  #  os.remove("teste.pkl")
   # print("Arquivo 'teste.pkl' apagado com sucesso!\n")

# Cria gerenciador e adiciona nova tarefa
#gerenciador = GerenciadorDeTarefas("teste.pkl")
#gerenciador.adicionar_tarefa("Estudar Python", "Revisar manipulação de arquivos", "27/05/2025")
#gerenciador.adicionar_tarefa("Estudar Python", "Revisar manipulação de arquivos", "28/05/2025")
#gerenciador.adicionar_tarefa("Estudar back and", "python", "29/05/2025")
#Editar tarefa
#input_do_usoario = 1
#gerenciador.editar_tarefa(input_do_usoario - 1, "Editado","Nova descricao","06/06/1995")

#Excluir tarefas

#gerenciador.remover_tarefa(1)

#marca concluida status

#gerenciador.marcar_concluida(1)
#gerenciador.marcar_concluida(0)
#gerenciador.marcar_concluida(2)

# Lista todas as tarefas
#gerenciador.listar_tarefa()


def main():
    parser = argparse.ArgumentParser(description="Gerenciador de tarefa CLI em Python!")

    subparsers = parser.add_subparsers(dest="comando", help="Comando disponível")

    # Adicionar tarefa
    parser_adicionar = subparsers.add_parser("adicionar", help="Adicionar nova tarefa")
    parser_adicionar.add_argument("titulo", type=str, help="Título da tarefa")
    parser_adicionar.add_argument("descricao", type=str, help="Descrição da tarefa")
    parser_adicionar.add_argument("data_vencimento", type=str, help="Data de vencimento (DD/MM/AAAA)")

    # Listar tarefas
    parser_listar = subparsers.add_parser("listar", help="Listar todas as tarefas")
    parser_listar.add_argument("--status", choices=["Pendente", "Concluida"], help="Filtrar por status")

    # Editar tarefa
    parser_editar = subparsers.add_parser("editar", help="Editar uma tarefa")
    parser_editar.add_argument("indice", type=int, help="Índice da tarefa a ser atualizada")
    parser_editar.add_argument("--titulo", type=str, help="Novo título da tarefa")
    parser_editar.add_argument("--descricao", type=str, help="Nova descrição da tarefa")
    parser_editar.add_argument("--data_vencimento", type=str, help="Nova data de vencimento (DD/MM/AAAA)")

    # Remover tarefa
    parser_remover = subparsers.add_parser("remover", help="Remover uma tarefa")
    parser_remover.add_argument("indice", type=int, help="Índice da tarefa a ser removida")

    # Marcar tarefa como concluída
    parser_marcar_concluida = subparsers.add_parser("concluir", help="Concluir uma tarefa")
    parser_marcar_concluida.add_argument("indice", type=int, help="Índice da tarefa concluída")

    # Processar argumentos
    args = parser.parse_args()
    gerenciador = GerenciadorDeTarefas()

    if args.comando == "adicionar":
        gerenciador.adicionar_tarefa(args.titulo, args.descricao, args.data_vencimento)

    elif args.comando == "listar":
        gerenciador.listar_tarefa(status=args.status)

    elif args.comando == "editar":
        gerenciador.editar_tarefa(args.indice - 1,
                                  titulo=args.titulo,
                                  descricao=args.descricao,
                                  data_vencimento=args.data_vencimento)

    elif args.comando == "remover":
        gerenciador.remover_tarefa(args.indice - 1)

    elif args.comando == "concluir":
        gerenciador.marcar_concluida(args.indice - 1)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
