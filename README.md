# ENews
### 모델 선택
```sh
1. M1 Pro에서 실행하기 좋은 무료 LLM
M1 Pro에서 실행하려면 Metal (MPS) 지원이 있는 모델 사용
(7B 이하, 로컬 실행 가능)
Mistral 7B → 가볍고 빠름, 16GB 메모리에서 실행 가능
Llama 2 7B (Meta) → GPT-3.5 수준, Ollama 지원

Ollama는 M1/M2 Mac에서 LLM을 쉽게 실행할 수 있는 툴.
✅ 장점: GPU 최적화 지원, 간편한 설치
✅ Mac에 최적화된 Metal 지원
✅ 기본적으로 필요한 모델을 자동 다운로드
```
### Ollama 설치
- Ollama 설치
```sh
brew install ollama # 
```
- 모델 다운로드
```sh
ollama pull mistral  # 또는 ollama pull llama2
```
📌 Mistral이 빠르고 적은 메모리를 사용하므로 추천

- 모델 실행
  - 터미널에서 실행 
    ```sh
    ollama run llama2 # Llama 2 실행
    ollama run mistral # Mistral 실행
    ```
  - Python에서 실행 : `subprocess로 실행 가능.`