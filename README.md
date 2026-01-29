Aqui está uma proposta de ficheiro README.md para o teu projeto, adaptada ao código fornecido.
Gerador de QR Code

Uma aplicação desktop simples desenvolvida em Python para gerar códigos QR instantaneamente através de uma Interface Gráfica de Utilizador (GUI).
📋 Descrição

Este projeto utiliza a biblioteca tkinter para criar uma janela onde o utilizador pode inserir texto ou um URL e gerar o respetivo QR Code. A aplicação trata automaticamente de links web, adicionando o protocolo https:// se este for omitido, e exibe o código gerado diretamente na janela.
🚀 Funcionalidades

    Interface Gráfica Simples: Janela fixa de 1280x720 px.

    Geração Instantânea: Criação de QR Codes a partir de qualquer texto introduzido.

    Correção de URL: Deteta se a entrada parece ser um site (ex: começa por "www." ou contém ".") e adiciona "https://" automaticamente caso falte.

    Visualização: O QR Code é redimensionado para 400x400 px para facilitar a leitura e visualização no ecrã.

🛠️ Pré-requisitos

Para executar este projeto, necessitas de ter o Python instalado e as seguintes bibliotecas:

    qrcode: Para a geração da imagem do código.

    Pillow (PIL): Para manipulação e exibição da imagem na interface tkinter.

    tkinter: Geralmente incluído na instalação padrão do Python.

📦 Instalação

    Clona este repositório ou descarrega o ficheiro QrCodeGen.py.

    Instala as dependências necessárias executando o seguinte comando no terminal:

Bash

pip install qrcode pillow

▶️ Como Utilizar

    Executa o script Python:
    Bash

    python QrCodeGen.py

    Na janela que se abre, escreve o texto ou o link que desejas converter na caixa de entrada na parte inferior.

    Clica no botão "Gerar QR Code".

    A imagem do QR Code aparecerá no centro da janela.

📄 Estrutura do Código

    QrCodeGen.py: O script principal que contém a lógica da interface e da geração do código. Utiliza Label para exibir a imagem e Entry para recolher o input do utilizador.
