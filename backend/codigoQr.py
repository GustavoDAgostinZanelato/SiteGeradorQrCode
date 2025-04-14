import qrcode
import random
import tldextract

def gerarQrCode(urlRecebida):
    urlQrCode = urlRecebida

    extracaoNome = tldextract.extract(urlQrCode)
    dominio = extracaoNome.domain.capitalize()

    ImagemQrCode = qrcode.make(urlQrCode)
    n = int(random.randint(999,9999))
    localArquivo = (f"QrCodes/qrcode{dominio} - id{n}.png")
    ImagemQrCode.save(localArquivo)
