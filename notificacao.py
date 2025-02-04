from win10toast import ToastNotifier

# Cria uma instância do ToastNotifier
toaster = ToastNotifier()

# Exibe a notificação
toaster.show_toast("Título da Notificação", "Mensagem da notificação", duration=10)
