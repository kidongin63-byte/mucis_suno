from flask import Flask, request, jsonify, send_from_directory
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static')

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/generate', methods=['POST'])
def generate_song():
    data = request.json
    
    mood_str = ', '.join(data.get('moods', []))
    if not mood_str:
        mood_str = 'AI 자동 추천 (아래 참고내용을 바탕으로 가장 잘 어울리는 주제/분위기를 스스로 판단하여 적용하세요)'
        
    genre_str = ', '.join(data.get('genres', []))
    if not genre_str:
        genre_str = 'AI 자동 추천 (아래 참고내용을 바탕으로 가장 잘 어울리는 음악 장르를 스스로 판단하여 적용하세요)'

    prompt = f"""당신은 Suno AI용 전문 송라이터입니다.

다음 조건으로 노래 가사와 Suno 스타일 프롬프트를 만들어주세요:
- 주제/분위기: {mood_str}
- 장르: {genre_str}
- 보컬: {data.get('vocal', '기본')}
- 사운드: {', '.join(data.get('sounds', [])) or '기본'}
- 구조: {data.get('format', '기본')}
- 언어: {data.get('lang', '한국어')}
"""
    if data.get('hint'):
        prompt += f"\n\n참고할 가사 힌트 및 내용: \"{data.get('hint')}\""

    prompt += """

아래 형식으로 JSON만 반환하세요 (마크다운 분리 문자 없이):
{
  "title": "이 노래에 가장 잘 어울리는 가사 제목 (한국어 또는 지정된 언어)",
  "style_prompt": "Suno에 입력할 영문 스타일 태그 (장르, 분위기, 보컬 등 종합. 쉼표 구분, 20단어 이내)",
  "lyrics": "완성된 가사 (구조 태그 포함: [Verse 1], [Chorus], [Bridge] 등)",
  "summary": "이 노래의 분위기와 특징을 한 문장으로"
}"""

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return jsonify({"result": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)