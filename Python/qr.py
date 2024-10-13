import qrcode
import os

def generate_qrcode(text, filename):
    """Gera um QR code a partir de um texto e salva na pasta atual como um arquivo PNG."""
    try:
        # Obtém o caminho da pasta atual onde o script está sendo executado
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        # Define o caminho completo do arquivo
        filepath = os.path.join(current_directory, f"QrCodes/{filename}.png")
        
        # Gera e salva o QR code
        img = qrcode.make(text)
        img.save(filepath)

        print(f"QR code gerado e salvo com sucesso em: {filepath}")
    except Exception as e:
        print(f"Erro ao gerar o QR code: {e}")

def main():
    # Solicita o texto ou URL para gerar o QR code
    textQR = input("Digite um texto ou URL para o QR code: ").strip()
    
    if not textQR:
        print("Erro: O texto ou URL não pode estar vazio.")
        return

    # Solicita o nome do arquivo para salvar
    save = input("Digite o nome do arquivo (sem a extensão .PNG): ").strip()

    if not save:
        print("Erro: O nome do arquivo não pode estar vazio.")
        return
    
    # Garante que o nome do arquivo não tenha caracteres inválidos
    save = "".join([c for c in save if c.isalnum() or c in (' ', '.', '_')]).rstrip()

    # Chama a função para gerar o QR code
    generate_qrcode(textQR, save)

if __name__ == "__main__":
    main()
