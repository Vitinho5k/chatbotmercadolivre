import pyautogui
import time

pyautogui.PAUSE = 0.8

TOTAL_DE_PRODUTOS = 12
PRODUTOS_POR_LINHA = 4

# Coordenadas dos 4 produtos da linha
posicoes_produtos = [
    (365, 735),    # produto 1
    (766, 735),    # produto 2
    (1126, 735),    # produto 3
    (1500, 735)    # produto 4
]

# Vai para o Mercado Livre
pyautogui.hotkey('alt', 'tab')
time.sleep(2)

# Posiciona a página
pyautogui.click(x=1777, y=535)
pyautogui.scroll(-700)
time.sleep(2)


for linha in range(TOTAL_DE_PRODUTOS // PRODUTOS_POR_LINHA):

    print(f"Processando linha {linha + 1}")

    # Processa os 4 produtos da linha
    for posicao in posicoes_produtos:

        # MERCADO LIVRE
        
        # Clica no produto
        pyautogui.click(
            x=posicao[0],
            y=posicao[1]
        )

        time.sleep(2)

        # Copia o link
        pyautogui.click(x=783, y=587)

        time.sleep(1)

        # WHATSAPP
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(2)

        # Campo de mensagem
        pyautogui.click(x=914, y=975)

        # Cola o link
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(10)

        # Envia
        pyautogui.press('enter')

        time.sleep(2)

        # VOLTA PARA O MERCADO LIVRE

        pyautogui.hotkey('ctrl', 'shift', 'tab')
        time.sleep(2)
        

        # Fecha/desativa o campo de copiar link
        pyautogui.click(x=1777, y=535)
        time.sleep(1)

    # PRÓXIMA LINHA
    if linha < (TOTAL_DE_PRODUTOS // PRODUTOS_POR_LINHA) - 1:

        print("Descendo para a próxima linha...")

        #rever o scroll
        pyautogui.scroll(-600) 

        time.sleep(2)

print("Todos os produtos foram enviados!")