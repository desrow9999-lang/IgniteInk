
import streamlit as st

# ページの基本設定（ブラウザタブのタイトルとアイコンを設定）
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

# ヘッダー部分
st.markdown('<p class="main-title">🔥 IgniteInk</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-caption">〜 思考に火を灯し、売れる言葉を紡ぎ出す 〜</p>', unsafe_allow_html=True)

# サイドバー：モード選択や設定
st.sidebar.header("⚙️ Ignition Settings")
mode = st.sidebar.selectbox(
    "壁打ちモードを選択",
    ["🔥 辛口プロデューサー（壁打ち）", "📝 売れるnote構成案・変換", "🚀 SNSポスト一括生成"]
)

# チャット履歴の初期化
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "ようこそ、IgniteInkへ。あなたの頭の中にあるモヤモヤしたアイデアを教えてください。私が鋭いツッコミを入れて、売れる形に鍛え上げます！"}
    ]

# 過去のメッセージを表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザーの入力を受け付ける
if prompt := st.chat_input("例：副業初心者に向けたプログラミング学習のnoteを書きたいけれど、何から書けばいいか迷ってます..."):
    # ユーザーのメッセージを追加
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # モードに応じた返答のシミュレーション
    if "辛口プロデューサー" in mode:
        response = f"「{prompt}」ですね。なるほど、方向性は見えてきましたが、それだと競合の海に埋もれます。**『誰の、どんな痛みを一番最初に解決するのか』**を研ぎ澄ませてください。この企画の最大の強みはどこにありますか？"
    elif "売れるnote構成案" in mode:
        response = "【IgniteInk 生成・note構成案】\n\n1. はじめに：なぜあなたの努力は今まで報われなかったのか？\n2. 第1章：多くの人が見落としている致命的な勘違い\n3. 第2章：今日から実践できる3ステップ・ロードマップ\n4. おわりに：最初の一歩を踏み出すあなたへ"
    else:
        response = f"【SNS告知ポスト案】\n「{prompt}」についてnoteを書きました！みんながハマる意外な落とし穴と、その抜け出し方とは…？詳細はこちら👇"

    # アシスタントのメッセージを追加
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
