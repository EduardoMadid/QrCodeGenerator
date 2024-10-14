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

Assim o código em python gera o QrCode baseado no seu texto, salvando o QrCode na pasta de QrCodes!

### 1. Estrutura do QrCode
Um QR code é uma grade de módulos (pequenos quadrados) que representam dados. Esses módulos formam um padrão específico, que é organizado em diferentes regiões, cada uma com uma função própria. A estrutura básica inclui:
- ``Posicionamento``: Existem três grandes quadrados em três cantos do QR code (exceto o canto inferior direito), chamados "marcadores de posição". Eles ajudam os leitores de QR code a identificar a orientação e os limites do código.
- ``Alinhamento``: Há pequenos quadrados espalhados dentro do QR code para garantir que a leitura seja precisa, mesmo que o código esteja distorcido ou inclinado.
- ``Dados``: A maior parte do QR code é composta por blocos de dados, onde a informação real é armazenada em forma de padrões binários (zeros e uns).
- ``Correção de erros``: QR codes possuem redundância embutida. Isso significa que, mesmo que partes do código sejam danificadas ou ocultas, ele ainda pode ser lido corretamente, graças a algoritmos de correção de erros (como Reed-Solomon).

### 2. Codificação dos Dados
Os dados armazenados em um QR code podem variar de texto simples, URLs, informações de contato (vCards), números de telefone, links para aplicativos ou até mesmo transações financeiras. Esses dados são convertidos em um padrão binário que é compactado e codificado de acordo com o padrão do QR code. O processo envolve:
- ``Entrada de dados``: O conteúdo (como uma URL) é convertido para um formato binário.
- ``Divisão em blocos``: Os dados binários são divididos em blocos, que são dispostos na grade do QR code.
- ``Nível de correção de erros``: Dependendo do nível de tolerância ao erro escolhido (existem quatro níveis: L, M, Q, H), mais ou menos blocos de redundância são incluídos para permitir a leitura mesmo com partes danificadas.

### 3. Leitura e Decodificação
Quando um QR code é escaneado por um dispositivo, o processo de leitura envolve várias etapas:
- ``Detecção``: A câmera detecta o código por meio dos padrões de posicionamento. Como esses marcadores são sempre em locais fixos, o software do scanner pode determinar a orientação e o tamanho do código rapidamente.
- ``Digitalização``: O software do leitor de QR code transforma a imagem capturada em uma grade de módulos preto-e-branco, comparando-os com o padrão binário (0 para módulos brancos e 1 para módulos pretos).
- ``Decodificação``: Com a estrutura da matriz de dados identificada, o leitor começa a decodificar os blocos binários. Isso envolve a conversão do padrão binário de volta ao formato original (por exemplo, um URL ou texto), levando em consideração o nível de correção de erros.
- ``Correção de erros``: Se alguma parte do QR code estiver corrompida ou suja, o leitor usa a redundância para corrigir os dados danificados e completar a leitura.

### 4. Níveis de Correção de Erros
Os QR codes incorporam diferentes níveis de correção de erros. Estes níveis permitem que uma parte do código seja danificada ou obscurecida e ainda assim possa ser lida corretamente:
- ``L (Baixo)``: Pode corrigir até 7% dos erros. Ideal para códigos que precisam ser compactos, mas que não enfrentam muita interferência.
- ``M (Médio)``: Corrige até 15% dos erros. Este é o nível padrão e balanceia bem entre a quantidade de dados e a resistência a danos.
- ``Q (Alta)``: Corrige até 25% dos erros. Usado quando a leitura é crítica e a redundância é necessária.
- ``H (Muito Alta)``: Corrige até 30% dos erros. Usado em ambientes onde há alta probabilidade de o código ser danificado, como em outdoors ou produtos que podem ser arranhados.

### 5. Capacidade de Armazenamento
A quantidade de dados que um QR code pode armazenar varia dependendo do nível de correção de erros e do tipo de dado que está sendo codificado:
- Números: Até 7.089 caracteres numéricos.
- Texto alfanumérico: Até 4.296 caracteres (letras e números).
- Bytes (dados binários): Até 2.953 bytes.
- Kanji/Kana (caracteres japoneses): Até 1.817 caracteres.

Quanto mais informação for armazenada, maior será o QR code, pois mais módulos são necessários para representar os dados.

### 6. Aplicações Práticas
- ``URLs``: QR codes frequentemente codificam URLs que levam a sites, aplicativos ou landing pages.
- ``Pagamentos``: Em aplicativos como Alipay e PayPal, QR codes são usados para transações de pagamento.
- ``Marketing``: Campanhas publicitárias utilizam QR codes para conectar o público a mais conteúdo.
- ``Logística``: QR codes são usados para rastrear pacotes e gerenciar inventários.
- ``VCard``: Um QR code pode armazenar informações de contato que, ao serem lidas, automaticamente criam um novo contato no dispositivo do usuário.

### 7. Vantagens dos QR Codes
- ``Capacidade de armazenamento``: Eles podem armazenar mais dados do que códigos de barras tradicionais.
- ``Leitura rápida``: Leitores de QR code são rápidos e eficazes, reconhecendo o código em frações de segundo.
- ``Tolerância a danos``: Graças à correção de erros, QR codes podem ser lidos mesmo quando parcialmente danificados.
- ``Versatilidade``: Podem ser usados para armazenar diferentes tipos de dados (URLs, textos, informações de contato, etc.)

### 8. Segurança e QR Codes
Apesar de serem simples de usar, QR codes também podem apresentar riscos de segurança, como redirecionamento para sites maliciosos. Por isso, é recomendável que os usuários verifiquem a origem dos QR codes antes de escaneá-los.

Em resumo, QR codes funcionam convertendo dados em um formato binário que é organizado em uma matriz de módulos. Eles são projetados para serem robustos e lidos de forma rápida e eficiente por dispositivos com câmeras, oferecendo uma ampla gama de aplicações, desde o marketing até a logística.
