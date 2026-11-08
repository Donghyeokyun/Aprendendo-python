import os
#os.system("cls") deu problema : ele apagava o terminal, mas o problem a foi ele apagar o print seguinte junto
#Tive que trocar por outro codigo a função #def finalizar_app()

restaurantes = [{"nome":"Praça", "categoria":"Japonesa", "ativo":False},
                {"nome":"Pizzaria", "categoria":"Massas", "ativo":True},
                {"nome":"Feijoada", "categoria":"Brasileira", "ativo":False},                
]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def limpar_tela():
    print("\033[2J\033[3J\033[H", end="", flush=True)
    #flush = obriga o Python a enviar o comando ao terminal na hora
    #\033[J2 Apaga o terminal
    #\033[J3 Apaga a rolagem do terminal

def retorno():
    print("\nEscolha novamente uma opção valida")
    input("Digite qualquer tecla para retornar as opções validas: ")
    main()

def exibir_subtitulo(texto):
    limpar_tela()
    print(texto)
    print()

def finalizar_app():
    exibir_subtitulo("Finalizando o app ")

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de restaurantes novos")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: " )
    categoria = input(f"Digite a categoria do {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"\nSeu restaurante {nome_do_restaurante} foi registrado com sucesso\n")
    input("Digite qualquer tecla para retornar ao principal ")
    main()

def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes")
    print("Os restaurantes cadastrados são os seguintes:\n")
    for lista in restaurantes:
        nome_restaurante = lista["nome"]
        categoria = lista["categoria"]
        status = lista["ativo"]
        print(f"- {nome_restaurante} | {categoria} | {status}")
    input("\nDigite qualquer tecla para retornar ao menu principal: ")
    main()

def trocar_status_restaurante():
    exibir_subtitulo("Alterar estado do restaurante")
    usuario_restaurante = input("Digite o nome do seu restaurante para alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if usuario_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {usuario_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {usuario_restaurante} foi desativado com sucesso"
            # o nome é ternario que aconteceu aqui
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")
    input("\nDigite qualquer tecla para retornar ao menu principal: ")
    main()
 
    

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            trocar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            retorno()
    except:
        retorno()
    

def main():
    limpar_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()