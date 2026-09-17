import streamlit as st

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
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🔥 IgniteInk</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-caption">〜 思考に火を灯し、売れる言葉を紡ぎ出す 〜</p>', unsafe_allow_html=True)

# サイドバー：モード選択とツール情報
st.sidebar.header("⚙️ Ignition Settings")
st.sidebar.info("💡 デモモード稼働中：入力したアイデアを瞬時にビジネス・発信の形へ変換します。")

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
        {"role": "assistant", "content": "ようこそ、IgniteInkへ。あなたの頭の中にあるモヤモヤしたアイデアを教えてください。私が鋭いツッコミを入れて、売れる形に鍛え上げます！"}
    ]

# 過去のメッセージを表示
for idx, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        # アシスタントの返答に対して「コピーしやすい工夫（簡易表示）」などを追加可能にする場所

# ユーザーの入力を受け付ける
if prompt := st.chat_input("例：副業初心者に向けたプログラミング学習のnoteを書きたいけれど..."):
    # ユーザーのメッセージを追加
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # モードに応じた超リアルな自動生成レスポンス
    if "辛口プロデューサー" in mode:
        ai_response = f"🔥 **【辛口プロデューサーからの指摘】**\n\n「{prompt}」ですね。率直に言って、その切り口のままでは競合の海に埋もれます。\n\n1. **ターゲットが広すぎます：** 「初心者向け」ではなく、「30代でプログラミング未経験の文系会社員」くらいまで絞り込んでください。\n2. **独自のベネフィットは？：** あなた自身がその壁をどうやって突破したのかの『生々しい失敗談』が最大の価値になります。\n\nまずは、あなたが一番苦労したエピソードを一つ教えてください。それを軸に再構築しましょう。"
    elif "売れるnote構成案" in mode:
        ai_response = f"📝 **【IgniteInk 生成・売れるnote構成案】**\n\nテーマ：「{prompt}」\n\n- **タイトル案：** 【完全ロードマップ】スキルゼロから始めた私が最初にやった3つのこと\n- **第1章：** なぜ9割の初心者が最初の1ヶ月で挫折してしまうのか？\n- **第2章：** 今日から迷わない、最短ルートの具体的手順\n- **第3章：** 【有料部分】実際に収益を生んだ裏側のテンプレート\n\nこの構成で執筆を進めると、読者の離脱を防ぎ、自然に有料部分への導線が作れます。どの章から肉付けしていきますか？"
    else:
        ai_response = f"🚀 **【SNS告知ポスト案】**\n\n「{prompt}」についてnoteにまとめました🔥\n\n正直、みんなここを勘違いしていて損をしています…。元・未経験の人が、遠回りして気づいた『たった一つの真実』を暴露します👇\n\n#副業 #プログラミング #note \nhttps://note.com/your_account"

    # アシスタントのメッセージを追加
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    with st.chat_message("assistant"):
        st.markdown(ai_response)
        
        # スマホで便利：生成されたテキストをテキストエリアに表示してコピーしやすくする
        with st.expander("📋 この出力をコピーする"):
            st.text_area("長押しして全選択・コピーしてください", ai_response, height=150, key=f"copy_{len(st.session_state.messages)}")
