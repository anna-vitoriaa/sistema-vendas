import customtkinter as ctk

class Tela_principal():
    def __init__(self):
        super().__init__()
        self.app = ctk.CTk()
        self.app.title("Sistema de vendas")
        self.app.geometry('900x600')

        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('dark-blue')

        self.frame_menu = ctk.CTkFrame(self.app, width=800, height=100, corner_radius=15, fg_color= '#0034a5')
        self.frame_menu.pack(pady=20, padx=20, expand=True, anchor='n', fill='x')

        self.btt_dashboard = ctk.CTkButton(self.frame_menu, corner_radius=20, text= '📊 Dashboard', font=("Segoe UI", 16), fg_color='#0034a5', anchor='n')
        self.btt_dashboard.pack(expand=True, fill='both', side='left')

        self.btt_vendas = ctk.CTkButton(self.frame_menu, corner_radius=20, text= '🛒 Vendas', font=("Segoe UI", 16), fg_color='#0034a5', anchor='n')
        self.btt_vendas.pack(expand=True, fill='both', side='left')

        self.btt_prod = ctk.CTkButton(self.frame_menu, corner_radius=20, text= '📦 Produtos', font=("Segoe UI", 16), fg_color='#0034a5', anchor='n')
        self.btt_prod.pack(expand=True, fill='both', side='left')

        self.btt_relat = ctk.CTkButton(self.frame_menu, corner_radius=20, text= '📈 Relatórios', font=("Segoe UI", 16), fg_color='#0034a5', anchor='n')
        self.btt_relat.pack(expand=True, fill='both', side='left')

        