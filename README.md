# QrCode Generator📱

A ideia principal desse projeto é entender ``como funcionam os QrCodes``!

***Lembrando que existem diversas maneiras de realizar o que foi feito e eu estou trzendo apenas duas soluções!***

### Breve Explicação

Um ``QR Code (Quick Response Code)`` é um tipo de código de ``barras bidimensional`` que armazena informações de maneira rápida e acessível. Ele pode ser lido por dispositivos como smartphones, que utilizam a câmera para decodificar os dados. O QR Code é composto por uma matriz de quadrados pretos e brancos, organizados em um padrão específico.

Quando um dispositivo escaneia o código, o software de leitura ``converte os padrões em uma sequência de dados``, que pode ser um texto, URL, número de telefone, ou qualquer outro tipo de informação. Esses códigos são amplamente utilizados por sua capacidade de armazenar grandes volumes de dados em um pequeno espaço e sua facilidade de leitura em múltiplas direções (360º).


## Site 🖥️

A primeira forma de criar seu código QR é por meio de um simples site e pela API de QrCodes!

- ``1.`` Primeiramente abra seu editor de código e crie o ``index.html`` e o ``script.js``.
  - ``1.1.`` Como eu utilizei TailwindCSS não existe um ``style.css``.
  - ``1.2.`` ***DICA: no seu arquivo HTML ao digitar ``!`` e pressionar a tecla ``Enter`` a estrutura HTML já é auto completada!.***
    <details>
      <summary>Assim:</summary>
        <img <img width="428" alt="image" src="https://github.com/user-attachments/assets/75084dd9-8fce-40f9-a462-3ba82d8c9fdd">
    </details>

### HTML
Agora que o básico foi feito e explicado vamos comecar pelo código HTML!

- ``1.`` Altere o título para QrCode Generator que está dentro da tag ``<head``.
  
  ```html
  <title>QrCode Generator</title>
  ```

- ``2.`` Importe o TailwindCSS dentro da tag ``<head>``.

    ```html
  <script src="https://cdn.tailwindcss.com"></script>
  ```

- ``3.``





















































## Python 🐍

Podemos também criar o QrCode em ``PYTHON``.
```py
import qrcode
import os
```

- ``import qrcode``:  Importa o módulo ``qrcode``, que facilita a geração de QR codes.
- ``import os``: Importa o módulo ``os``, que oferece funções para interagir com o sistema operacional, como obter e manipular caminhos de diretórios.

# 

```py
def generate_qrcode(text, filename):
    """Gera um QR code a partir de um texto e salva na pasta atual como um arquivo PNG."""
```
- ``def generate_qrcode(text, filename):``: Define a função ``generate_qrcode`` que recebe dois parâmetros: ``text`` (o conteúdo que será transformado em QR code) e ``filename`` (o nome do arquivo onde o QR code será salvo).
- ``""" Gera um QR code a partir de um texto e salva na pasta atual como um arquivo PNG. """``: Um comentário (docstring) que descreve o que a função faz.

#

```py
 try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
```

- ``try:``: Inicia um bloco ``try`` para capturar possíveis exceções (erros) durante a execução.
- ``current_directory = os.path.dirname(os.path.abspath(__file__))``: Obtém o diretório onde o script Python está sendo executado e o armazena na variável ``current_directory. __file__`` é o nome do arquivo atual, e ``os.path.abspath`` obtém o caminho absoluto desse arquivo.

#

```py
        filepath = os.path.join(current_directory, f"QrCodes/{filename}.png")
```

- ``filepath = os.path.join(current_directory, f"QrCodes/{filename}.png")``: Constrói o caminho completo do arquivo onde o QR code será salvo. A função ``os.path.join`` combina o diretório atual com o subdiretório "QrCodes" e o nome do arquivo (passado como argumento). O arquivo será salvo com a extensão ``.png``.

#

```py
        img = qrcode.make(text)
        img.save(filepath)
```

- ``img = qrcode.make(text)``: Cria um QR code com o conteúdo fornecido no parâmetro ``text``. A função ``qrcode.make`` converte o texto ou URL em uma imagem de QR code e armazena essa imagem na variável ``img``.

- ``img.save(filepath)``: Salva a imagem gerada do QR code no caminho especificado por ``filepath``.

#

```py
        print(f"QR code gerado e salvo com sucesso em: {filepath}")
```
- ``print(f"QR code gerado e salvo com sucesso em: {filepath}")``: Exibe uma mensagem no console informando que o QR code foi gerado e salvo com sucesso, mostrando o caminho onde ele foi armazenado.

# 

```py
    except Exception as e:
        print(f"Erro ao gerar o QR code: {e}")
```
- ``except Exception as e:``: Captura qualquer exceção que possa ocorrer no bloco try e armazena o erro na variável ``e``.
- ``print(f"Erro ao gerar o QR code: {e}")``: Exibe uma mensagem de erro no console se algo der errado, mostrando detalhes do erro (``e``).

#

```py
def main():
    textQR = input("Digite um texto ou URL para o QR code: ").strip()
```
- ``def main():``: Define a função principal ``main``, que será executada quando o programa for iniciado.
- ``textQR = input("Digite um texto ou URL para o QR code: ").strip()``: Solicita ao usuário que insira o texto ou URL que será convertido em QR code. O método ``.strip()`` remove espaços em branco no início e no final do texto.

#

```py
    if not textQR:
        print("Erro: O texto ou URL não pode estar vazio.")
        return
```
- ``if not textQR:``: Verifica se o usuário não inseriu nenhum texto. Se o campo estiver vazio, a condição é verdadeira.
- ``print("Erro: O texto ou URL não pode estar vazio.")``: Exibe uma mensagem de erro caso o campo de texto esteja vazio.
- ``return``: Termina a execução da função ``main`` se o texto estiver vazio.

#

```py
    save = input("Digite o nome do arquivo (sem a extensão .PNG): ").strip()
```
- ``save = input("Digite o nome do arquivo (sem a extensão .PNG): ").strip()``: Solicita ao usuário o nome do arquivo para salvar o QR code, sem a extensão ``.png``. O método ``.strip()`` remove espaços desnecessários no início e no fim.

#

```py
    if not save:
        print("Erro: O nome do arquivo não pode estar vazio.")
        return
```
- ``if not save:``: Verifica se o usuário não inseriu um nome de arquivo. Se estiver vazio, exibe uma mensagem de erro.
- ``return``: Termina a função ``main`` se o nome do arquivo estiver vazio.

#

```py
    save = "".join([c for c in save if c.isalnum() or c in (' ', '.', '_')]).rstrip()
```
- ``save = "".join([c for c in save if c.isalnum() or c in (' ', '.', '_')]).rstrip()``: Remove quaisquer caracteres inválidos no nome do arquivo, permitindo apenas letras, números, espaços, pontos e underscores. ``rstrip()`` remove espaços em branco à direita.

#

```py
    generate_qrcode(textQR, save)
```
- ``generate_qrcode(textQR, save)``: Chama a função ``generate_qrcode`` com o texto fornecido e o nome do arquivo para gerar o QR code.

#

```py
if __name__ == "__main__":
    main()
```
- ``if __name__ == "__main__":``: Verifica se o script está sendo executado diretamente (não importado como módulo). Se for o caso, chama a função ``main`` para iniciar o programa.

#

Assim o código em python gera o QrCode baseado no seu texto, salvando o QrCode na pasta de 
