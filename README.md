# Detector de Objetos e Faces

Sistema de reconhecimento em tempo real que utiliza YOLOv8 e Haar Cascade para detectar objetos e rostos através da webcam.

## Funcionalidades

- Detecção de objetos em tempo real (80 classes: pessoa, carro, celular, etc.)
- Detecção específica de rostos humanos
- Interface visual com caixas delimitadoras e rótulos
- Execução leve e rápida com YOLOv8 Nano

## Tecnologias Utilizadas

- **Python 3**
- **OpenCV** - Captura de vídeo e processamento de imagens
- **Ultralytics YOLOv8** - Detecção de objetos
- **Haar Cascade** - Detecção de rostos

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Flaviodev1206/detector-de-objetos-face.git
cd detector-de-objetos-face
```

2. Instale as dependências:
```bash
pip install opencv-python ultralytics
```

## Uso

Execute o script principal:
```bash
python detector.py
```

- O sistema abrirá a webcam e iniciará a detecção
- Pressione **'q'** para sair

## Como Funciona

1. O YOLOv8n detecta objetos comuns no frame da webcam
2. O classificador Haar Cascade identifica especificamente rostos humanos
3. Os resultados são sobrepostos no vídeo com caixas coloridas e rótulos

## Screenshot

![Reconhecimento em Tempo Real](Reconhecimento%20em%20Tempo%20Real_screenshot_02.05.2026.png)

## Requisitos

- Webcam
- Python 3.x
- OpenCV
- Ultralytics (YOLOv8)
