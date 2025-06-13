import customtkinter as ctk
import threading
from discord_connection import conectar_discord, atualizar_status, atualizar_presenca

app = ctk.CTk()
app.title("Status do Humor")
app.geometry("400x400")

status_label = ctk.CTkLabel(app, text="Conectando ao Discord...")
status_label.pack(pady=10)

def manter_rpc():
    try:
        conectar_discord()
        atualizar_status(status_label, "conectado")
    except Exception as e:
        atualizar_status(status_label, "erro", str(e))

threading.Thread(target=manter_rpc, daemon=True).start()

# mapping id = status
humores = {
    1: ("to feliz", "😄"),
    2: ("to triste", "😢"),
    3: ("to pensativo", "🤔"),
    4: ("to bravo", "😡"),
    5: ("to chateado", "😒"),
    6: ("sla pô kk", "😒"),
    7: ("to com mto sono", "😒"),
    8: ("to confuso", "😒"),
    9: ("vendo pazpeaceful", "😒"),
    10: ("vendo 202", "😒"),
    11: ("eu ainda amo ela", "😒"),
    12: ("to dormindo", "😒"),
}

# id p definir a imagem
def enviar_humor_por_id(humor_id):
    humor_texto, _ = humores[humor_id]
    atualizar_presenca(humor_texto, status_label, imagem_id=str(humor_id))

# botões
for humor_id, (humor, emoji) in humores.items():
    ctk.CTkButton(app, text=f"{humor} {emoji}", width=200,
                  command=lambda h_id=humor_id: enviar_humor_por_id(h_id)).pack(pady=5)

# campo input
ctk.CTkLabel(app, text="Ou digite seu humor:").pack(pady=(20, 5))
input_humor = ctk.CTkEntry(app, width=250)
input_humor.pack(pady=5)

def enviar_humor_personalizado():
    humor = input_humor.get()
    if humor.strip():
        atualizar_presenca(humor.strip(), status_label, imagem_id="1d", small_image="2d")

ctk.CTkButton(app, text="Enviar Humor Personalizado", width=200, command=enviar_humor_personalizado).pack(pady=10)

app.mainloop()