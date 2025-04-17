import qrcode
import random
import tldextract
from supabaseClient import supabase


# Gerando o QrCode
def gerarQrCode(urlRecebida):
    urlQrCode = urlRecebida

    extracaoNome = tldextract.extract(urlQrCode)
    dominio = extracaoNome.domain.capitalize()

    ImagemQrCode = qrcode.make(urlQrCode)
    qrCodeId = int(random.randint(9999,99999))
    nome_arquivo = f"qrcode{dominio} - id{qrCodeId}.png"
    localArquivo = f"QrCodes/{nome_arquivo}"

    # Salvar localmente
    ImagemQrCode.save(localArquivo)
    
    salvarQrCodeSupabase(qrCodeId, dominio, urlQrCode)



def salvarQrCodeSupabase(qrCodeId, dominio, urlQrCode):
    response = supabase.table("qrCodes").insert({
        "qrCodeId": qrCodeId,
        "dominio": dominio,
        "urlOriginal": urlQrCode
    }).execute()

    return response.data
