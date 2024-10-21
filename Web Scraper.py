import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup


def scrape():
    url = url_entrada.get() 
    if not url:
        messagebox.showerror("Error", "Por favor, ingresa una URL válida.")
        return

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            price = soup.find_all("div", class_="ui-search-result__wrapper")
            
            if price:
                resultado_texto = "información encontrada:\n"
                for price in price:
                    resultado_texto += price.get_text() + "\n"  
                resultado_label.config(text=resultado_texto)
            else:
                resultado_label.config(text="No se encontró información en la página.")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"No se pudo obtener la página: {e}")


ventana = tk.Tk()
ventana.title("Web Scraper")

url_label = tk.Label(ventana, text="Ingresa la URL:")
url_label.pack(pady=10)

frame = tk.Frame(ventana)
frame.pack(pady=5)

url_entrada = tk.Entry(frame, width=50)
url_entrada.pack(side="left")

scrape_button = tk.Button(frame, text="Iniciar Scraping", command=scrape)
scrape_button.pack(side="left", padx=20) 

resultado_label = tk.Label(ventana, text="")
resultado_label.pack(pady=10)

ventana.mainloop()