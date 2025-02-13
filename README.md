[![made Language {generic badge}](https://img.shields.io/badge/Made%20with-Python-8A2BE2)](https://github.com/alanmugiwara)
[![Created Badge](https://badges.pufler.dev/created/alanmugiwara/metedanca-tube-downloader?color=blueviolet)](https://github.com/alanmugiwara)
[![last update date](https://badges.pufler.dev/Updated/alanmugiwara/metedanca-tube-downloader/?color=blueviolet)](https://github.com/alanmugiwara)
[![Commits Badge](https://img.shields.io/github/commit-activity/m/alanmugiwara/metedanca-tube-downloader.svg?color=blueviolet)](https://github.com/alanmugiwara)

[![contributors](https://img.shields.io/github/contributors/alanmugiwara/metedanca-tube-downloader?color=8A2BE2)](https://github.com/alanmugiwara)
[![issues counter](https://img.shields.io/github/issues/alanmugiwara/metedanca-tube-downloader?color=8A2BE2)](https://github.com/alanmugiwara)
[![repo size](https://img.shields.io/github/repo-size/alanmugiwara/metedanca-tube-downloader?color=8A2BE2)](https://github.com/alanmugiwara)
[![directory files](https://img.shields.io/github/directory-file-count/alanmugiwara/metedanca-tube-downloader?color=8A2BE2)](https://github.com/alanmugiwara)

## MeteDança Tube Downloader: Ferramenta gráfica para baixar vídeos do Youtube

MeteDança Tube Downloader é uma aplicação gráfica desenvolvida em Python para facilitar o download de vídeos do YouTube. Basta colar o link do vídeo, clicar em baixar e escolher onde salvar!

## Funcionalidades

- **Download de vídeos do YouTube:** Baixe vídeos do YouTube colando o link na interface;
- **Interface gráfica:** Interface amigável e intuitiva com PyQt6;
- **Seleção do local de salvamento:** Escolha o diretório onde o vídeo será salvo;
- **Feedback sonoro:** Emite um som ao iniciar o download.

## Tecnologias Utilizadas

- **Python 3.13.2:** Linguagem de programação utilizada;
- **PyQt6:** Biblioteca para criação da interface gráfica;
- **pytubefix:** Biblioteca para interagir com o YouTube;
- **playsound:** Biblioteca para reproduzir sons;
- **sys:** Biblioteca usada para integrar o interpretador Python e o ambiente de execução.

# Demonstração
![Demonsraoção](https://github.com/alanmugiwara/alanmugiwara.github.io/blob/main/img/demo.gif?raw=true)

## Como Utilizar

1. **Clone este repositório usando comando abaixo:**

   ```bash
   git clone https://github.com/alanmugiwara/metedanca-tube-downloader
   ```

2.  **Navegue até o diretório /source:**
   ```bash
   cd metedanca-tube-downloader/source
   ```

3. **Instale todas as dependências necessárias:**
     ```bash
     pip install -r requirements.txt
     ```
     
4. **Execute o Programa:**
     ```bash
     app.py
     ```
     
5. **Baixe um vídeo:**
     - Na janlea da aplicação, cole o link do vídeo do YouTube no campo de texto;
     - Clique em "Baixar vídeo do youtube;
     - Uma janela será aberta para você escolher onde salvar o vídeo;
     - O download será iniciado e o vídeo será salvo no local escolhido.

## Estrutura do Código
>
> O QUE FOI UTILIZADO?
>
> 1: Bibliotecas (pytubefix, PyQt6, playsound, sys)
> 
> 2: Classes (QApplication, QWidget, QPushButton, QLineEdit, QLabel, QFileDialog)
>
> 3: Funções
>
> ALGORITIMO:
> 
> Passo 01: Criar a janela principal da aplicação (home_screen);
> 
> Passo 02: Adicionar um campo de entrada de texto (QLineEdit) para o link do vídeo;
> 
> Passo 03: Adicionar um botão (QPushButton) para iniciar o download;
> 
> Passo 04: Adicionar uma imagem (QLabel) para o visual da aplicação;
> 
> Passo 05: Adicionar um rodapé (QLabel) com créditos;
> 
> Passo 06: Implementar a função de download que:
>
> Passo 07: Abre um diálogo para escolher o local de salvamento;
>
> Passo 08: Toca um som de clique;
>
> Passo 09: Extrai o link do vídeo do campo de texto;
>
> Passo 10: Utiliza pytubefix para baixar o vídeo na maior resolução que possua áudio atrelado ao vídeo;
>
> Passo 11: Conectar o clique do botão à função de download;
>
> Passo 12: Exibir a janela principal;

Para dúvidas, sugestões ou problemas, entre em contato. Álan Cruz:

<div>
<a href="https://instagram.com/alancruz_tec" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"></a>
<a href="mailto:contato@alancruz.tec.br"><img loading="lazy" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail"></a>
<a href="https://linkedin.com/in/alansilvadacruz" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin"></a>
<a href="https://alancruz.tec.br" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-My%20Website-%230077B5?style=for-the-badge&logo=wordpress&logoColor=white" alt="Website"></a>
</div>
