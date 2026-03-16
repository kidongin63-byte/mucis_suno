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
    
    prompt = f"""당신은 Suno AI용 전문 송라이터입니다.

다음 조건으로 노래 가사와 Suno 스타일 프롬프트를 만들어주세요:
- 주제/분위기: {', '.join(data.get('moods', [])) or '자유'}
- 장르: {', '.join(data.get('genres', [])) or 'K-Pop'}
- 보컬: {data.get('vocal', '기본')}
- 사운드: {', '.join(data.get('sounds', [])) or '기본'}
- 구조: {data.get('format', '기본')}
- 언어: {data.get('lang', '한국어')}
"""
    if data.get('hint'):
        prompt += f"\n\n참고할 가사 힌트: \"{data.get('hint')}\""

    prompt += """

아래 형식으로 JSON만 반환하세요 (마크다운 분리 문자 없이):
{
  "style_prompt": "Suno에 입력할 영문 스타일 태그 (쉼표 구분, 20단어 이내)",
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