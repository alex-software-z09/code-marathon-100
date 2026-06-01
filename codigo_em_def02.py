import os

def encapsular_em_funcoes():
    pasta_origem = r'C:\Users\alex61551966\Downloads\questoes_resolvidas_guanabara (1)\questoes_resolvidas_guanabara'
    pasta_destino = r'C:\Users\alex61551966\Downloads\questoes_nomeadas'
    
    
    os.makedirs(pasta_destino, exist_ok=True)   
    
    for i in range(1, 101):
        nome_arquivo = f'questao_{i}.py'
        caminho_origem = os.path.join(pasta_origem, nome_arquivo)
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)
        
        if os.path.exists(caminho_origem):
            
            with open(caminho_origem, 'r', encoding='utf-8') as f_entrada:
                linhas = f_entrada.readlines()
            
            
            with open(caminho_destino, 'w', encoding='utf-8') as f_saida:
                f_saida.write(f'def q_{i}():')
                
                if linhas:
                    for texto in linhas:
                        f_saida.write(f"    {texto}")
                


encapsular_em_funcoes()