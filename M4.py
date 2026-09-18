import json
import matplotlib.pyplot as plt

CAMINHO_KEYPOINTS = "keypoints.json"
META = 0.90  # meta do projeto (M2): detecção válida em >= 90% dos quadros

with open(CAMINHO_KEYPOINTS, encoding="utf-8") as f:
    kp = json.load(f)

frames = kp["frames"]
total = len(frames)

com_mao = sum(1 for f in frames if f["hands"])
com_pose = sum(1 for f in frames if f["pose"])
taxa_mao = com_mao / total
taxa_pose = com_pose / total
print(f"quadros: {total}")
print(f"mãos: {com_mao}/{total} = {100*taxa_mao:.1f}%")
print(f"pose: {com_pose}/{total} = {100*taxa_pose:.1f}%")

linha = [1 if f["hands"] else 0 for f in frames]
plt.figure(figsize=(9, 1.6))
plt.plot(linha, drawstyle="steps-post")
plt.yticks([0, 1], ["sem mão", "com mão"])
plt.xlabel("quadro")
plt.title("Detecção de mão ao longo do vídeo")
plt.savefig("deteccao_maos_video.png")

maior = atual = 0
for v in linha:
    if v == 0:
        atual += 1
        maior = max(maior, atual)
    else:
        atual = 0
print("maior sequência sem detecção:", maior, "quadros")

if taxa_mao >= META:
    print(f"✔ OK: detecção de mãos {100*taxa_mao:.1f}% (>= 90%). Dados prontos para modelar.")
else:
    print(f"✗ ABAIXO da meta: {100*taxa_mao:.1f}% (< 90%). Sugestões para regravar:")
    print(" - Melhore a iluminação (luz de frente, sem contraluz).")
    print(" - Mantenha as mãos totalmente no enquadramento.")
    print(" - Evite movimento muito rápido e fundo confuso.")
    print(" - Aumente a resolução/estabilidade (apoie o celular).")
