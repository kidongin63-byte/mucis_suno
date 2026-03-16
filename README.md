# 새로운시작 - Anti-Gravity Song Creator

AI 기술을 활용하여 나만의 노래 가사와 Suno AI용 스타일 프롬프트를 자동으로 생성해주는 어플리케이션입니다.

## 🚀 주요 기능
- **주제 및 분위기 선택:** 사랑, 이별, 희망, 파티 등 다양한 감성 테마별 가사 생성
- **다양한 음악 장르:** K-Pop, 발라드, R&B, EDM, 인디 팝 등 여러 장르 복수 선택 지원
- **보컬 스타일 지정:** 여성/남성, 파워풀/소프트, 듀엣, 코러스, 랩 등 맞춤형 보컬 설정
- **세부 사운드 튜닝:** 신스 웨이브, 어쿠스틱 기타, 오케스트라, 리버브 등 디테일한 악기 및 사운드 구성
- **노래 구조 (Format) 설정:** 표준형(Verse-Chorus-Bridge), 숏폼, 앤섬 등 노래 전개 방식 결정
- **Suno 스타일 프롬프트 자동 최적화:** 위 선택 항목들을 조합하여 Suno AI에 바로 복사하여 붙여넣을 수 있는 최적화된 영문 스타일 프롬프트 자동 생성

## 🛠️ 기술 스택
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript (Vanilla)
- **AI Model:** Google Gemini (gemini-2.5-flash)

## 💻 로컬에서 실행하는 방법
1. 저장소를 클론합니다.
   ```bash
   git clone https://github.com/kidongin63-byte/mucis_suno.git
   ```
2. 프로젝트 폴더로 이동합니다.
   ```bash
   cd mucis_suno
   ```
3. 가상환경을 생성하고 패키지를 설치합니다.
   ```bash
   python -m venv venv
   # Windows의 경우: .\venv\Scripts\activate
   # Mac/Linux의 경우: source venv/bin/activate
   pip install -r requirements.txt
   ```
4. 최상위 경로에 `.env` 파일을 만들고 아래와 같이 Gemini API 키를 입력합니다.
   ```env
   GEMINI_API_KEY=당신의_제미나이_API_키를_입력하세요
   ```
5. 서버를 실행합니다.
   ```bash
   python app.py
   ```
6. 웹 브라우저에서 `http://localhost:5000` 으로 접속합니다.
