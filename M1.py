import cv2

CAMINHO_VIDEO = "video_exemplo.mp4"
SAIDA_FRAME_MEIO = "frame_meio.jpg"

cap = cv2.VideoCapture(CAMINHO_VIDEO)
print("Vídeo aberto?", cap.isOpened())

fps_lido = cap.get(cv2.CAP_PROP_FPS)
total = cap.get(cv2.CAP_PROP_FRAME_COUNT)
larg = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
alt = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"fps={fps_lido} | total de quadros={total} | tamanho={larg}x{alt}")

quadros = []
while True:
    ret, quadro = cap.read()
    if not ret:
        break
    quadros.append(quadro)
cap.release()

total_lidos = len(quadros)
print("Quadros lidos:", total_lidos)

indice_meio = total_lidos // 2
cv2.imwrite(SAIDA_FRAME_MEIO, quadros[indice_meio])
print("Salvo", SAIDA_FRAME_MEIO, "(quadro", indice_meio, "de", total_lidos, ")")

# O vídeo é uma sequência de quadros; cada quadro é uma matriz de pixels
# com 3 canais de cor (BGR) e é exibido numa taxa de "fps" quadros por segundo.
