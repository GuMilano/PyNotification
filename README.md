# Notificação no Windows com Python

Este projeto demonstra como exibir notificações no Windows usando a biblioteca `win10toast`.

## 📌 Requisitos

Antes de executar o código, certifique-se de ter o Python instalado e a biblioteca `win10toast` instalada.

## 📦 Instalação

Abra o terminal (cmd, PowerShell ou terminal do VS Code) e execute:

```
pip install win10toast
```

## 🚀 Como Executar

Crie um arquivo `notificacao.py` e copie o seguinte código:

```
from win10toast import ToastNotifier

# Cria uma instância do ToastNotifier
toaster = ToastNotifier()

# Exibe a notificação
toaster.show_toast("Título da Notificação", "Mensagem da notificação", duration=10)
```

Agora, execute o script com:

```
python notificacao.py
```

## ⚙️ Personalização

Você pode alterar o título, a mensagem e a duração da notificação modificando os valores da função `show_toast()`.

Exemplo:

```
toaster.show_toast("Alerta!", "Este é um aviso importante!", duration=5)
```

## 🎯 Compatibilidade

Este código funciona apenas no **Windows**. Para notificações em outros sistemas operacionais, use bibliotecas como `plyer`.

## 📜 Licença

Este projeto está disponível sob a licença MIT.

---
💻 **Desenvolvido com Python** 🐍
