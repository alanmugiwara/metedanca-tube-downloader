from pytubefix import YouTube
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QFileDialog  
# GUI: Aplicação (QApplication), Janelas (QWidget), Botões (QPushButton), Caixa de Texto (QLineEdit), Rótulo (QLabel), Saída de arquivo (QFileDialog)

from PyQt6.QtGui import QPixmap # Importa a classe QPixmap do módulo PyQt6.QtGui, usada para trabalhar com imagem.
from PyQt6.QtCore import Qt # Importa o módulo Qt do PyQt6.QtCore, que contém flags de alinhamento e modos de redimensionamento
from playsound import playsound 
import sys

def home_screen():
    """ Janela principal da aplicação """
    home_screen = QWidget()  # Cria a janela principal tipo QWidget.
    home_screen.setWindowTitle("MeteDança Tube Downloader")  # Título da janela.
    home_screen.resize(350, 350)  # tamanho da janela (largura / altura).
    
    """ Caixa de input de texto """
    barra_de_input = QLineEdit(home_screen)  # Caixa de input de texto (QLineEdit) dentro da janela principal.
    barra_de_input.setPlaceholderText("Cole o link do video...")  # Define o texto de dica.
    barra_de_input.text()  # Chama o texto de dica
    barra_de_input.resize(200, 30)  # Tamanho do campo de entrada.
    barra_de_input.move(80, 50)  # Posição do campo de entrada.

    """ Botão de Download """
    download_button = QPushButton('Baixar vídeo do youtube', home_screen)  # Botão com o texto "Baixar vídeo do youtube" dentro da janela principal.
    download_button.setGeometry(0, 0, 150, 50)  # Posição (x:horizontal / y:vertical | (largura / altura).
    download_button.setStyleSheet('background-color:grey')  # Cor de fundo do botão.
    download_button.move(108, 100)
    
    """ Imagem acima do rodapé """
    robissao = QLabel(home_screen)  # Cria um QLabel para exibir a imagem.
    pixmap = QPixmap("img.png")  # Carrega a imagem do arquivo "img.png".
    robissao.setPixmap(pixmap)  # Define o QPixmap no QLabel, exibindo a imagem.
    scaled_pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)  # Largura / altura matendo a proporção
    robissao.setPixmap(scaled_pixmap) # Define o QPixmap redimensionado no QLabel, exibindo a imagem redimensionada
    robissao.move(135, 200)  # Define a posição absoluta da imagem dentro da janela.
    
    """ Rodapé """
    rodape_credits = QLabel(home_screen)  # Cria um QLabel (rótulo de texto)
    rodape_credits.setText('<a href="https://github.com/alanmugiwara">github.com/alanmugiwara</a>')  # Define o texto do rótulo como um link HTML.
    rodape_credits.setOpenExternalLinks(True)  # Habilita a abertura de link externo.
    rodape_credits.move(110, 300)  # Define a posição absoluta da Label dentro da janela.
    
    """ Função que faz o download """
    def download():
        save_path = QFileDialog.getExistingDirectory(home_screen, "Escolha onde salvar o vídeo") # Solicita a saída dentro da janela inicial
        playsound('click.mp3') # Toca o mp3
        video_url = barra_de_input.text()  # Puxa a URL do vídeo
        video_downloader = YouTube(video_url)  # Cria um objeto YouTube com a URL do vídeo.
        stream = video_downloader.streams.get_highest_resolution() # Obtém o stream de vídeo na maior resolução disponível que inclua áudio.
        stream.download(saida=save_path)  # Inicia o download.
        
        
    download_button.clicked.connect(download)  # Conecta o sinal 'clicked' do botão à função 'download', para que ela seja chamada quando o botão for clicado.

    home_screen.show()  # Exibe a janela principal.
    return home_screen  # Retorna a janela principal.

""" Chamada de execução da aplicação"""
app = QApplication(sys.argv)  # Cria uma instância da aplicação PyQt6. O sys.argv permite que o app receba argumentos da linha de comando do sistema.
home_screen_call = home_screen()  # Chama a função home_screen() para criar e exibir a janela principal. Importante para que a janela não seja coletada pelo garbage collector.
sys.exit(app.exec())  # Inicia o loop de eventos da aplicação, que aguarda interações. Quando o app é fechado, app.exec() retorna uma saída, que é passado pro sys.exit() que encerra a execução.