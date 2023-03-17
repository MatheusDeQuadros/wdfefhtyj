## Capturando um video pela webcam ##
* Maneira de escrever o código: cv2.VideoCapture(aqui vc digita o número do índice da webcam)
* Obs.: Se você tiver apenas uma câmera conectada ao sistema, digita-se 0. 
* Quando mais de uma câmera estiver conectada ao computador, podemos
digitar 1 para a segunda webcam,e assim por diante.
* Obs 2.: o OpenCV usa apenas uma câmera conectada por vez.


## Capturando um video pelo  carregamento desse vídeo ##
* cv2.VideoCapture(aqui vc digita o caminho para chegar ao vídeo)

## Podemos verificar se o vídeo foi capturado ou não ##
* Maneira de escrever o código: nome_da_variável.isOpened()
* Isto vai nos dar uma resposta em booleano,ou seja, verdadeiro ou falso, a partir disso você pode ,por exemplo, "printar" uma mensagem quando a captura pela webcam falha.

## Algumas  informações úteis sobre o vídeo ##
* Largura do quadro;
    * nome_da_variável.get(cv2.CAP_PROP_FRAME_WIDTH)
* Altura do quadro;
    * nome_da_variável.get(cv2.CAP_PROP_FRAME_HEIGHT)
* Quadros por segundo (fps);
    * nome_da_variável.get(cv2.CAP_PROP_FPS) 
* Obs.: Os resultados  virão em forma de números com vírgula,  para 
converter para número inteiro é fácil: é só colocar int() na frente

## O problema do waitKey() ##
* Você se lembra do waitKey() da última aula? O que ele faz?
* Precisamos dele para exibir o vídeo aqui também
* Aqui vai um spoiler: precisaremos que o número dentro do parenteses seja maior que 0.
* Você consegue pensar no porquê ?

## Fechando o vídeo
* Use vid.release() 

## fechar todas as janelas ##
* cv2.destroyAllWindows()