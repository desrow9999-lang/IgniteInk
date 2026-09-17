import streamlit as st
from openai import OpenAI

# ページの基本設定
st.set_page_config(
    page_title="IgniteInk（イグニットインク）",
    page_icon="🔥",
    layout="centered"
)

# 洗練されたダークモード風カスタムCSS
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #f0f6fc;
    }
    .brand-container {
        padding: 1.2rem 0;
        border-bottom: 1px solid #30363d;
        margin-bottom: 1.5rem;
    }
    .main-title {
        font-size: 2.6rem;
        font-weight: 900;
        letter-spacing: -0.03em;
        background: linear-gradient(135deg, #ff4b4b, #ff8f00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .brand-ruby {
        font-size: 0.85rem;
        color: #8b949e;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-top: 4px;
    }
    .sub-caption {
        color: #c9d1d9;
        font-size: 1rem;
        margin-top: 0.5rem;
    }
    .stChatMessage p, .stChatMessage span, .stChatMessage div, .stChatMessage li {
        color: #f0f6fc !important;
    }
    .stButton>button {
        background: linear-gradient(135deg, #ff4b4b, #ff8f00);
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: bold;
    }
    .stButton>button:hover {
        opacity: 0.9;
    }
    </style>
""", unsafe_allow_html=True)

# ブランディングヘッダー
st.markdown("""
    <div class="brand-container">
        <div class="main-title">🔥 IgniteInk</div>
        <div class="brand-ruby">イグニットインク ｜ 思考を火花に変える壁打ちAI</div>
        <div class="sub-caption">頭の中のモヤモヤを、売れる言葉と戦略へ焼き付ける。</div>
    </div>
""", unsafe_allow_html=True)

# サイドバー：APIキー設定とモード選択
st.sidebar.header("⚙️ API Configuration")
api_key = st.sidebar.text_input("OpenAI APIキーを入力", type="password", help="sk-... から始まるOpenAIのAPIキーを入力してください。")

st.sidebar.markdown("---")
st.sidebar.header("🎯 Ignition Mode")
mode = st.sidebar.selectbox(
    "壁打ちモードを選択",
    [
        "🔥 辛口プロデューサー（壁打ち）", 
        "📝 売れるnote構成案・変換", 
        "🚀 SNSポスト一括生成"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **使い方**\n1. サイドバーにOpenAIのAPIキーを入力\n2. モードを選んで下にアイデアを入力！")

# チャット履歴の初期化
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "ようこそ、IgniteInk（イグニットインク）へ！サイドバーにAPIキーを設定し、あなたの頭の中にあるアイデアを聞かせてください。プロのマーケティング視点で売れる形に昇華させます。"}
    ]

# 過去のメッセージを表示
for idx, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# モードに応じたシステムプロンプトの定義
system_prompts = {
    "🔥 辛口プロデューサー（壁打ち）": "あなたは超一流の辛口ビジネスプロデューサーです。ユーザーのアイデアの論理の穴やターゲットの甘さを容赦なく突いた上で、どうすれば市場で勝てるか、愛ある具体的な改善案を提示してください。",
    "📝 売れるnote構成案・変換": "あなたは売れっ子Webライター・編集者です。ユーザーの入力したテーマをもとに、読者の離脱を防ぎ、自然に有料部分やコンバージョンへの導線が作れる「売れるnoteの構成案（タイトル・目次・各章の要点）」を出力してください。",
    "🚀 SNSポスト一括生成": "あなたはSNSマーケターです。ユーザーのアイデアやnoteのテーマをもとに、タイムラインで思わずスクロールの手を止めてクリックしたくなる、X（旧Twitter）用の魅力的な告知ポスト文面を生成してください。"
}

# ユーザーの入力を受け付ける
if prompt := st.chat_input("例：副業初心者に向けたプログラミング学習のnoteを書きたい..."):
    # APIキーのチェック
    if not api_key:
        st.error("⚠️ サイドバーにOpenAIのAPIキーが入力されていません。キーを入力してから再度送信してください。")
    else:
        # ユーザーのメッセージを追加
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AIからの応答生成
        with st.chat_message("assistant"):
            with st.status("🔥 IgniteInkが思考を燃やしています...", expanded=False):
                try:
                    client = OpenAI(api_key=api_key)
                    
                    # 過去の会話履歴をOpenAIのフォーマットに変換
                    messages_payload = [{"role": "system", "content": system_prompts[mode]}]
                    for msg in st.session_state.messages:
                        messages_payload.append({"role": msg["role"], "content": msg["content"]})

                    response = client.chat.completions.create(
                        model="gpt-4o-mini",  # 高速かつコストパフォーマンスに優れた最新モデルを使用
                        messages=messages_payload,
                        temperature=0.7
                    )
                    ai_response = response.choices[0].message.content
                except Exception as e:
                    ai_response = f"❌ エラーが発生しました。APIキーが正しいか確認してください。\n\n詳細: `{str(e)}`"

            st.markdown(ai_response)
            
            # コピーしやすいエリア
            with st.expander("📋 この出力をコピーする"):
                st.text_area("長押しして全選択・コピーしてください", ai_response, height=150, key=f"copy_{len(st.session_state.messages)}")

        # アシスタントのメッセージを追加
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
