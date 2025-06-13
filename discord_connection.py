from pypresence import Presence
import time

rpc = None

def conectar_discord():
    global rpc
    try:
        rpc = Presence("1371011397454139392")
        rpc.connect()
    except Exception as e:
        raise ConnectionError(f"Erro ao conectar com o Discord: {e}")

def atualizar_status(status_label, status, erro=None):
    if status == "conectado":
        status_label.configure(text="Conectado ao Discord", text_color="green")
    elif status == "erro":
        status_label.configure(text=f"Erro na Conexão: {erro}", text_color="red")
    else:
        status_label.configure(text="Conectando ao Discord...", text_color="gray")

def atualizar_presenca(humor, status_label=None, imagem_id="default", small_image=None):
    global rpc
    try:
        #trocar status
        rpc.update(
            state=humor,
            large_image=imagem_id,  
            large_text=humor,      
            small_image=small_image,  
            small_text=humor,       
            start=time.time()
        )
        if status_label:
            atualizar_status(status_label, "conectado")
    except Exception as e:
        #reconectar
        print(f"Erro ao atualizar presença: {e}")
        if "pipe was closed" in str(e).lower():
            try:
                print("Tentando reconectar com o Discord...")
                rpc.connect()
                print("Reconectado com sucesso.")
                atualizar_presenca(humor, status_label, imagem_id, small_image)
            except Exception as reconect_erro:
                print(f"Falha ao reconectar: {reconect_erro}")
                if status_label:
                    atualizar_status(status_label, "erro", str(reconect_erro))
        else:
            if status_label:
                atualizar_status(status_label, "erro", str(e))
