print("Olá, eu sou sua assistente, Pythrina. O que você quer fazer hoje?")

comando = input("Digite um comando: ")

match comando:
    case "oi" | "ola":
        print("Oi, como vai você?")
    case "tchau" | "sair" | "xau":
        print("Tchau, foi bom conversar com você!")
    case "piada":
        print("Sabe qual é o padroeiro das pessoas que trabalham com TI? O São Login")
    case "clima" | "previsão do tempo":
        print("Tá muuuuuuuuito quente!! Deve ter passado de 40°C! 🥵")    
    case _:
        print("Desculpe, não entendi o comando.")    