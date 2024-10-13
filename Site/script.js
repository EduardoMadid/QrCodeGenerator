function GenerateQR() {
    const qrText = document.getElementById("qrText");
    const qrImage = document.getElementById("qrImage");
    const imgBox = document.getElementById("imgBox");

    // Remove shake class if it's already present
    qrText.classList.remove("animate-shake");

    if (qrText.value) {
        const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?data=${encodeURIComponent(qrText.value)}&size=200x200`;
        qrImage.src = qrUrl;

        // Exibe a imagem
        imgBox.classList.add("max-h-60");
    } else {
        // Adiciona a classe de animação de shake
        qrText.classList.add("animate-shake");

        // Remove a classe após a animação para que possa ser usada novamente
        setTimeout(() => {
            qrText.classList.remove("animate-shake");
        }, 500); // Duração do shake em milissegundos
    }
}
