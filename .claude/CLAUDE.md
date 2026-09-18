# Contexto do M4 — Qualidade dos dados (PneumoVision)

## Status atual (18/09/2026) — CONCLUÍDO

- Vídeo original (`video-inalacao.mp4`): 223/312 quadros = 71,5% detecção de mãos (abaixo da meta ≥ 90% do M2), maior sequência sem detecção de mão: 53 quadros. `keypoints.json` dessa versão salvo em `keypoints_v1_backup.json`, gráfico em `deteccao_maos_video_v1_antes.png`.
- Usuário regravou o vídeo (`video-inalacao2.mp4`) ajustando iluminação/enquadramento.
- Novo `keypoints.json` extraído com `python -m pipeline.keypoints.extract --input video-inalacao2.mp4 --output keypoints.json` (venv do projeto em `.venv`, `pip install -r requirements.txt` já satisfeito lá).
- Resultado novo (`python3 M4.py`):
  - Mãos: 364/364 quadros = **100%** detecção
  - Pose: 364/364 = 100%
  - Maior sequência sem detecção de mão: **0 quadros**
  - Gráfico atualizado em `deteccao_maos_video.png`
- Veredito: **meta atingida** (100% ≥ 90%).
- Relatório de entrega já montado em `M4_relatorio.md` (taxa final, o que mudou, observação sobre qualidade dos keypoints). Falta apenas o usuário revisar e submeter no Classroom (prazo: sexta 18/09/2026).

## Entrega do M4 (Classroom, prazo: sexta 18/09/2026)

Relatório de meia página com:
- Taxa de detecção final obtida
- O que mudou após regravar (se precisou)
- Uma observação sobre a qualidade dos keypoints

Critério de aceite: relatar taxa final; se abaixo de 90%, mostrar a tentativa de melhoria (regravação). **Já satisfeito** — ver `M4_relatorio.md`.

## Arquivos relevantes no repo

- `M4.py` — script criado nesta sessão, análoga ao notebook `M4_Qualidade_dos_Dados.ipynb` do Colab, mas rodando sobre o `keypoints.json` real (não os dados simulados do notebook). Reexecutável a qualquer momento com `python3 M4.py`.
- `keypoints.json` — saída do M3, gerado do `video-inalacao.mp4`.
- `M3_explicacao.md` — explica a estrutura do `keypoints.json` e o comando de extração.
- `M2.py` — script de qualidade de captura (fps/resolução/brilho) do vídeo, mesmo estilo usado para criar `M4.py`.
- `pipeline/keypoints/extract.py` — script de extração de keypoints (MediaPipe) usado no M3.
- `deteccao_maos_video.png` — gráfico gerado pelo `M4.py` (linha do tempo de detecção de mão).

## Fontes originais do M4 (fora do repo, no Google)

- Material didático: Google Drive, PDF "Material_Didatico_18-09_M4_PneumoVision.pdf"
- Notebook do Classroom: Google Colab "M4_Qualidade_dos_Dados.ipynb" (usa dados simulados como exemplo didático; a entrega real usa o `keypoints.json` do próprio aluno)
