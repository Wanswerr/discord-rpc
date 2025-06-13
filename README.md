# 🎮 Discord RPC Personalizado

Um aplicativo em Python com interface gráfica (`customtkinter`) que permite personalizar seu Rich Presence no Discord — incluindo **status, emojis, imagens e humores**.

---

## 📦 Requisitos

- Python 3.10+ instalado
- Conta de desenvolvedor no Discord com um app criado: https://discord.com/developers/applications
- Chave de cliente (client ID) do seu app do Discord
- Biblioteca `pypresence` e `customtkinter`

---

## 🔧 Instalação

1. Clone este repositório:
```bash
git clone https://github.com/Wanswerr/discord-rpc.git
cd discord-rpc
```

2. Instale os pacotes necessários:
```bash
pip install -r requirements.txt
```

---

## 🚀 Como usar

1. Crie um aplicativo no [Discord Developer Portal](https://discord.com/developers/applications) e copie o `Client ID`.

2. No portal do Discord, vá em **Rich Presence > Art Assets** e **adicione imagens** com os mesmos nomes usados pelos humores predefinidos no aplicativo.

3. Execute o aplicativo:

```bash
python app.py
```

4. A interface gráfica abrirá:
   - Selecione um **humor pré-definido** ou digite um personalizado
   - O aplicativo usará o nome do humor como referência para buscar a imagem no app do Discord
   - Clique em **“Ativar RPC”**

> O Discord deve estar **aberto** para o RPC funcionar!

---

## 📁 Estrutura do Projeto

```
discord-rpc/
├── app.py
├── discord_connection.py
└── README.md
```

---

## 🛠 Funcionalidades

- Interface clean com `customtkinter`
- Dropdown de humores com imagem vinculada via nome
- Mensagens e status personalizados
- Integração em tempo real com o Discord

---

## 🧠 To-Do (Futuras Features)

- Suporte a múltiplos perfis salvos
- Auto start com Windows
- Sincronização via webhook / API

---

## 👨‍💻 Autor

[GitHub: Wanswerr](https://github.com/Wanswerr)  
Tecnologia usada: Python + pypresence + customtkinter

---

## ⚠️ Observações

- O RPC **não funciona em dispositivos móveis**.
- Certifique-se de que o Discord está **aberto e logado**.
- Os nomes dos humores devem corresponder exatamente às imagens cadastradas no Developer Portal.

## 🆘 Precisa de ajuda?

- Caso não esteja conseguindo utilizar, me envie uma mensagem no Discord, irei te auxiliar da melhor forma possível!
- Discord: Gabryeh