import streamlit as st

# ページの基本設定
st.set_page_config(
    page_title="IgniteInk（イグニットインク）",
    page_icon="🔥",
    layout="centered"
)

# 洗練されたダークモード風カスタムCSS
st.markdown("""
    <style>
    /* 全体の背景とフォントの調整 */
    .stApp {
        background-color: #0e1117;
        color: #e6edf3;
    }
    /* メインタイトル */
    .brand-container {
        padding: 1.5rem 0;
        border-bottom: 1px solid #21262d;
        margin-bottom: 2rem;
    }
    .main-title {
        font-size: 2.8rem;
        font-weight: 900;
        letter-spacing: -0.03em;
        background: linear-gradient(135deg, #ff4b4b, #ff8f00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .brand-ruby {
        font-size: 0.9rem;
        color: #8b949e;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-top: 4px;
    }
    .sub-caption {
        color: #8b949e;
        font-size: 1.05rem;
        margin-top: 0.5rem;
    }
    /* チャットボックスやボタンの洗練 */
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

# ブランディングヘッダー（読み方を明記）
st.markdown("""
    <div class="brand-container">
        <div class="main-title">🔥 IgniteInk</div>
        <div class="brand-ruby">イグニットインク ｜ 思考を火花に変える壁打ちAI</div>
        <p class="sub-caption">頭の中のモヤモヤを、売れる言葉と戦略へ焼き付ける。</p>
    </div>
""", unsafe_allow_html=True)

# サイドバー：モード選択とプロ仕様の演出
st.sidebar.header("⚙️ System Control")
st.sidebar.markdown("---")
st.sidebar.success("⚡ Status: Online\n\n🧠 Model: Ignite-Pro v2.1")

mode = st.sidebar.selectbox(
    "壁打ちモードを選択",
    [
        "🔥 辛口プロデューサー（壁打ち）", 
        "📝 売れるnote構成案・変換", 
        "🚀 SNSポスト一括生成"
    ]
)

# チャット履歴の初期化
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "ようこそ、**IgniteInk（イグニットインク）**へ。あなたの頭の中にあるアイデアを聞かせてください。容赦ないツッコミとプロのマーケティング視点で、売れる形に昇華させます。"}
    ]

# 過去のメッセージを表示
for idx, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザーの入力を受け付ける
if prompt := st.chat_input("例：副業初心者に向けたプログラミング学習のnoteを書きたい..."):
    # ユーザーのメッセージを追加
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # モードに応じた超リアルな自動生成レスポンス
    if "辛口プロデューサー" in mode:
        ai_response = f"🔥 **【辛口プロデューサーからの指摘】**\n\n「{prompt}」ですね。率直に言って、その切り口のままでは市場の海に埋もれます。\n\n1. **ターゲットの解像度：** 「初心者向け」ではなく、「30代・未経験の文系会社員」など痛みを特定してください。\n2. **独自のフック：** あなた自身の生々しい失敗談こそが最大の差別化になります。\n\nまずは、あなたが一番苦労したエピソードを教えてください。"
    elif "売れるnote構成案" in mode:
        ai_response = f"📝 **【IgniteInk 生成・売れるnote構成案】**\n\nテーマ：「{prompt}」\n\n- **タイトル案：** 【完全ロードマップ】スキルゼロから月5万稼ぐまでの全記録\n- **第1章：** 9割の初心者が最初の1ヶ月で挫折する本当の理由\n- **第2章：** 今日から迷わない、最短ルートの具体的手順\n- **第3章：** 【有料部分】実際に収益を生んだテンプレート\n\nこの構成で読者の離脱を防ぎ、自然な購買導線を引きます。"
    else:
        ai_response = f"🚀 **【SNS告知ポスト案】**\n\n「{prompt}」についてnoteを公開しました🔥\n\n正直、みんなここを勘違いして損をしています…。元未経験の私が遠回りして気づいた『たった一つの真実』を暴露します👇\n\n#副業 #プログラミング #note"

    # アシスタントのメッセージを追加
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    with st.chat_message("assistant"):
        st.markdown(ai_response)
        
        # コピーしやすいエリア
        with st.expander("📋 この出力をコピーする"):
            st.text_area("長押しして全選択・コピーしてください", ai_response, height=150, key=f"copy_{len(st.session_state.messages)}")
