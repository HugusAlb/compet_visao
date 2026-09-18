import cv2
import numpy as np
import matplotlib.pyplot as plt

CAMINHO_VIDEO = "video-inalacao.mp4"

cap = cv2.VideoCapture(CAMINHO_VIDEO)
assert cap.isOpened(), "Não consegui abrir o vídeo"

fps_v = cap.get(cv2.CAP_PROP_FPS)
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
duracao = total / fps_v if fps_v else 0
print(f"fps={fps_v} | quadros={total} | resolução={w}x{h} | duração={duracao:.1f}s")

indices = [int(total * f) for f in (0.1, 0.5, 0.9)]
for idx in indices:
    cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
    ok, q = cap.read()
    if ok:
        cv2.imwrite(f"amostra_quadro_{idx}.jpg", q)

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
brilhos = []
while True:
    ok, q = cap.read()
    if not ok:
        break
    cinza = cv2.cvtColor(q, cv2.COLOR_BGR2GRAY)
    brilhos.append(float(np.mean(cinza)))
cap.release()

brilho_medio = float(np.mean(brilhos))
print(f"brilho médio: {brilho_medio:.1f} (ideal: entre ~60 e ~200)")

plt.plot(brilhos)
plt.xlabel("quadro")
plt.ylabel("brilho (0-255)")
plt.title("Iluminação ao longo do vídeo")
plt.savefig("brilho_video.png")


def check(nome, condicao):
    print(("✓ " if condicao else "✗ ATENÇÃO: ") + nome)


check("Duração entre 10 e 20 s", 10 <= duracao <= 20)
check("Resolução mínima 480p (altura >= 480)", h >= 480)
check("Iluminação adequada (brilho 60-200)", 60 <= brilho_medio <= 200)
print("\nSe algum item deu ATENÇÃO, regrave ajustando o ponto indicado.")
