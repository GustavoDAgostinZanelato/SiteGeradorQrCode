from supabaseClient import supabase
import qrcode
import tldextract
import uuid
from io import BytesIO
from datetime import datetime
import pytz


# Gerando o QrCode
def gerarQrCode(urlRecebida):
    urlQrCode = urlRecebida
    ImagemQrCode = qrcode.make(urlQrCode)

    extracaoNome = tldextract.extract(urlQrCode)
    dominio = extracaoNome.domain.capitalize()
    qrCodeId = str(uuid.uuid4())

    # Salvando a data de criação do QrCode
    fusoBR = pytz.timezone("America/Sao_Paulo")
    dataCricao = str(datetime.now(fusoBR))

    # Gerando o QrCode na memória
    buffer = BytesIO()
    ImagemQrCode.save(buffer, format="PNG")
    buffer.seek(0)

    # Enviando para o Supabase
    salvarDadosQrCodes(qrCodeId, dataCricao, dominio, urlQrCode)
    uploadImagens(buffer, qrCodeId)


# Salvando algumas informações do QrCode no banco de dados
def salvarDadosQrCodes(qrCodeId, dataCricao, dominio, urlQrCode):
    response = supabase.table("qrCodes").insert({
        "qrCodeId": qrCodeId,
        "dataCriacao": dataCricao, 
        "dominio": dominio,
        "urlOriginal": urlQrCode
    }).execute()
    return response.data


# Salvando a imagem .png do QrCode no Storage, pasta Uploads
def uploadImagens(buffer, qrCodeId):
    imagemBytes = buffer.getvalue() # Converte o buffer para bytes, um formato que o supabse consegue reconhecer

    response = supabase.storage.from_("imagens-qrcodes").upload(
        path=f"uploads/{qrCodeId}.png",
        file=imagemBytes,
        file_options={"content-type": "image/png"}
    )
    print(f"Resposta do supabase: {response}")




