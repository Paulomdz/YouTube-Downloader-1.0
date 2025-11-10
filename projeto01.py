from pytubefix import YouTube
import os 

def download_video():
    print("Descarrega um video do youtube.")
    url = input(f"Insira a URL do video do YTB:")
    rota_salvar = input(f"\nInsira a rota onde deseja salvar o video: ").strip() or "."

    if not os.path.exists(rota_salvar):
        os.makedirs(rota_salvar)
        print(f"Pasta criada: {rota_salvar}")

    try: 
        ytb = YouTube(url)

        print(f"\nTitulo: {ytb.title}--")
        
        stream = ytb.streams.get_highest_resolution()

        if stream: 
            print(f"Descarregando...{ytb.title}")
            print(f"Qualidade: {stream.resolution}")

            stream.download(output_path=rota_salvar)   
          
            print(f"Download concluido, video salvo em: {os.path.abspath(os.path.join(rota_salvar, stream.default_filename))}")
              
    except Exception as e: 
        print(f"Ocorreu um erro: {e}")
        print(f"URL pode ser invalida ou problema de conexao.\n Tente mais tarde.")

if __name__=="__main__": 
    download_video()