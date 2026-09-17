import streamlit as st
from openai import OpenAI

# ページの基本設定
st.set_page_config(
    page_title="IgniteInk 〜思考を火花に変える壁打ちAI〜",
    page_icon="🔥",
    layout="centered"
)

# スタイリッシュなカスタムCSS
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        letter-spacing: -0.05em;
        margin-bottom: 0px;
    }
    .sub-caption {
        color: #888888;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🔥 IgniteInk</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-caption">〜 思考に火を灯し、売れる言葉を紡ぎ出す 〜</p>', unsafe_allow_html=True)

# サイドバー：APIキーとモード設定
st.sidebar.header("⚙️ Ignition Settings")
api_key = st.sidebar.text_input("OpenAI APIキーを入力", type="password")

mode = st.sidebar.selectbox(
    "壁打ちモードを選択",
    [
        "🔥 辛口プロデューサー（壁打ち）", 
        "📝 売れるnote構成案・変換", 
        "🚀 SNSポスト一括生成"
    ]
)

# モードに応じたシステムプロンプト（AIへの指示書）の切り替え
if "辛口プロデューサー" in mode:
    system_prompt = "あなたは超一流のマーケター兼辛口プロデューサーです。ユーザーのアイデアの論理の穴、ターゲットの甘さ、競合との違いを鋭く突いてください。ただし、最終的には読者に売れるコンテンツへと昇華させるための愛ある具体的な改善案を提示してください。"
elif "売れるnote構成案" in mode:
    system_prompt = "あなたは売れるnoteの構成作家です。ユーザーから提供されたテーマや壁打ちの内容に基づき、読者の離脱を防ぎ、購買意欲を高めるための魅力的なnoteの目次・構成案を自動作成してください。"
else:
    system_prompt = "あなたはSNSマーケティングの専門家です。ユーザーのアイデアや記事の魅力を一瞬で伝え、タイムラインで思わずクリックしたくなるようなX（旧Twitter）の告知ポスト文面を作成してください。"

# チャット履歴の初期化
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "ようこそ、IgniteInkへ。左側のメニューにAPIキーを入力し、あなたの頭の中にあるモヤモヤしたアイデアを教えてください。私が鋭いツッコミを入れて、売れる形に鍛え上げます！"}
    ]

# 過去のメッセージを表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザーの入力を受け付ける
if prompt := st.chat_input("例：副業初心者に向けたプログラミング学習のnoteを書きたいけれど..."):
    if not api_key:
        st.error("⚠️ サイドバーにOpenAIのAPIキーを入力してください。")
    else:
        # ユーザーのメッセージを追加
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # OpenAI APIの呼び出し
        try:
            client = OpenAI(api_key=api_key)
            
            # メッセージの構築（システムプロンプト ＋ 過去の会話）
            messages_for_api = [{"role": "system", "content": system_prompt}]
            for m in st.session_state.messages:
                messages_for_api.append({"role": m["role"], "content": m["content"]})

            with st.spinner("🔥 思考の火花を散らし中..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",  # 高速かつ高品質なモデル
                    messages=messages_for_api
                )
                ai_response = response.choices[0].message.content

        except Exception as e:
            ai_response = f"⚠️ エラーが発生しました: {e}"

        # アシスタントのメッセージを追加
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        with st.chat_message("assistant"):
            st.markdown(ai_response)
