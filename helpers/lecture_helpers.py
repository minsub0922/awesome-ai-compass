"""
lecture_helpers.py - 강의 공통 유틸리티 함수
AI 특강 실습 자료 - 공통 헬퍼

각 노트북에서 import해서 사용하거나,
Colab에서 독립 실행 시 해당 코드를 직접 셀에 붙여넣기 가능.
"""

import json
import os
import time
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple


# ============================================================
# .env 자동 로드 (python-dotenv 가 설치되어 있으면)
# ============================================================

def _load_dotenv_once() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    # helpers/ 또는 그 상위 디렉토리에서 .env 탐색
    here = Path(__file__).resolve().parent
    for candidate in [here, here.parent, Path.cwd(), Path.cwd().parent]:
        env_file = candidate / ".env"
        if env_file.exists():
            load_dotenv(env_file, override=False)
            return


_load_dotenv_once()


# ============================================================
# 모드 설정
# ============================================================

def setup_mode(api_key: Optional[str] = None) -> Tuple[str, Any]:
    """
    실행 모드를 설정합니다.

    Args:
        api_key: OpenAI API 키 (없으면 환경변수 또는 로컬 모드)

    Returns:
        (mode, client) 튜플
        mode: "api" 또는 "local"
        client: OpenAI 클라이언트 (api 모드) 또는 None (local 모드)
    """
    key = api_key or os.environ.get("OPENAI_API_KEY", "")

    if key and key not in ("your-api-key-here", ""):
        try:
            from openai import OpenAI
            client = OpenAI(api_key=key)
            # 간단한 연결 테스트
            print("✅ API 모드: OpenAI 연결 성공")
            return "api", client
        except Exception as e:
            print(f"⚠️ OpenAI 초기화 실패: {e}")
            print("🔄 로컬 모드로 전환합니다.")
            return "local", None
    else:
        print("💡 로컬 모드: API 키 없이 실행합니다.")
        print("   (sentence-transformers + mock LLM 응답 사용)")
        return "local", None


def check_environment():
    """현재 환경을 체크하고 요약을 출력합니다."""
    import sys
    import platform

    print("=" * 55)
    print("  환경 체크")
    print("=" * 55)
    print(f"Python: {sys.version.split()[0]}")
    print(f"OS: {platform.system()} {platform.release()}")

    # GPU 체크
    try:
        import torch
        gpu = torch.cuda.is_available()
        print(f"GPU (CUDA): {'✅ 사용 가능' if gpu else '❌ 없음 (CPU 모드)'}")
    except ImportError:
        print("GPU (PyTorch): 미설치")

    # 주요 패키지 체크
    packages = {
        "openai": "OpenAI SDK",
        "sentence_transformers": "로컬 임베딩",
        "rank_bm25": "BM25 검색",
        "networkx": "그래프 처리",
        "pandas": "데이터 처리",
        "numpy": "수치 계산",
        "sklearn": "ML 유틸",
    }
    print("\n패키지 상태:")
    for pkg, desc in packages.items():
        try:
            __import__(pkg)
            print(f"  ✅ {desc} ({pkg})")
        except ImportError:
            print(f"  ❌ {desc} ({pkg}) - 미설치")

    # API 키 체크
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if api_key and api_key not in ("your-api-key-here", ""):
        print(f"\nAPI 키: ✅ 설정됨 (sk-...{api_key[-4:]})")
    else:
        print("\nAPI 키: ❌ 없음 (로컬 모드 사용)")
    print("=" * 55)


# ============================================================
# 출력 포맷팅
# ============================================================

def print_section(title: str, emoji: str = "▶", width: int = 55):
    """섹션 구분선을 출력합니다."""
    print(f"\n{'─' * width}")
    print(f"  {emoji}  {title}")
    print(f"{'─' * width}\n")


def print_box(title: str, content: str, color: str = "default", width: int = 60):
    """텍스트를 박스 형태로 출력합니다."""
    borders = {
        "default": ("┌", "┐", "│", "└", "┘", "─"),
        "success": ("╔", "╗", "║", "╚", "╝", "═"),
        "warning": ("┌", "┐", "│", "└", "┘", "╌"),
    }
    tl, tr, v, bl, br, h = borders.get(color, borders["default"])

    print(f"\n{tl}{h * width}{tr}")
    print(f"{v} {title:<{width - 1}}{v}")
    print(f"{'├' if color == 'default' else v}{h * width}{'┤' if color == 'default' else v}")
    for line in content.strip().split('\n'):
        # 긴 줄 처리
        while len(line) > width - 2:
            print(f"{v} {line[:width - 2]} {v}")
            line = line[width - 2:]
        print(f"{v} {line:<{width - 1}}{v}")
    print(f"{bl}{h * width}{br}\n")


def display_comparison(
    query: str,
    left_title: str, left_content: str,
    right_title: str, right_content: str,
    footer: str = None
):
    """두 결과를 나란히 비교해서 출력합니다."""
    from IPython.display import display, HTML

    left_html = left_content.replace('\n', '<br>').replace(' ', '&nbsp;')
    right_html = right_content.replace('\n', '<br>').replace(' ', '&nbsp;')
    footer_html = f'<div style="margin-top:15px;padding:10px;background:#f8f9fa;border-radius:5px;font-size:13px;">{footer}</div>' if footer else ''

    html = f"""
    <div style="font-family:'Noto Sans KR',Arial,sans-serif;max-width:920px;margin:10px auto;">
      <div style="background:#2c3e50;color:white;padding:12px 16px;border-radius:8px 8px 0 0;">
        <strong>🔍 질문:</strong> {query}
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:0;border:1px solid #ddd;border-top:none;">
        <div style="padding:15px;background:#fdf2f2;border-right:1px solid #ddd;">
          <div style="font-weight:bold;color:#c0392b;margin-bottom:10px;font-size:14px;">{left_title}</div>
          <div style="color:#555;font-size:13px;line-height:1.7;">{left_html}</div>
        </div>
        <div style="padding:15px;background:#f0fdf4;">
          <div style="font-weight:bold;color:#27ae60;margin-bottom:10px;font-size:14px;">{right_title}</div>
          <div style="color:#333;font-size:13px;line-height:1.7;">{right_html}</div>
        </div>
      </div>
      {footer_html}
    </div>
    """
    display(HTML(html))


def display_search_results(results: List[Dict], query: str, title: str = "검색 결과"):
    """검색 결과를 표 형태로 시각화합니다."""
    import pandas as pd
    from IPython.display import display, HTML

    rows = []
    for i, r in enumerate(results, 1):
        score = r.get('score', r.get('similarity', 0))
        rows.append({
            "순위": f"#{i}",
            "점수": f"{score:.4f}",
            "문서 ID": r.get('doc_id', '-'),
            "내용 미리보기": r.get('content', '')[:90] + "…",
        })

    df = pd.DataFrame(rows)
    print(f"\n🔍 [{title}] 쿼리: '{query}'")
    display(df.style.set_properties(**{
        'font-size': '12px',
        'text-align': 'left',
    }).background_gradient(subset=['점수'], cmap='Blues'))
    return df


# ============================================================
# 임베딩
# ============================================================

_local_embedding_model = None  # 싱글톤 캐싱


def get_local_embedding_model(model_name: str = "all-MiniLM-L6-v2"):
    """sentence-transformers 모델을 로드합니다 (캐싱)."""
    global _local_embedding_model
    if _local_embedding_model is None:
        print(f"📥 임베딩 모델 로딩 중: {model_name} ...")
        from sentence_transformers import SentenceTransformer
        _local_embedding_model = SentenceTransformer(model_name)
        print("✅ 모델 로드 완료")
    return _local_embedding_model


def embed_texts(
    texts: List[str],
    mode: str = "local",
    client=None,
    api_model: str = "text-embedding-3-small",
    local_model: str = "all-MiniLM-L6-v2",
    show_progress: bool = False,
) -> np.ndarray:
    """
    텍스트 리스트를 임베딩합니다.

    Returns:
        shape (N, D) numpy array
    """
    if mode == "api" and client is not None:
        try:
            vecs = []
            batch_size = 50
            for i in range(0, len(texts), batch_size):
                batch = texts[i:i + batch_size]
                resp = client.embeddings.create(input=batch, model=api_model)
                batch_vecs = [r.embedding for r in resp.data]
                vecs.extend(batch_vecs)
                if show_progress:
                    print(f"  임베딩 진행: {min(i + batch_size, len(texts))}/{len(texts)}")
            return np.array(vecs, dtype=np.float32)
        except Exception as e:
            print(f"⚠️ API 임베딩 실패: {e} → 로컬 모드로 전환")

    # 로컬 모드
    model = get_local_embedding_model(local_model)
    vecs = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=show_progress,
        batch_size=32,
    )
    return vecs.astype(np.float32)


def cosine_similarity_batch(query_vec: np.ndarray, doc_vecs: np.ndarray) -> np.ndarray:
    """쿼리 벡터와 문서 벡터 배열의 코사인 유사도를 일괄 계산합니다."""
    q = np.array(query_vec, dtype=np.float32).flatten()
    D = np.array(doc_vecs, dtype=np.float32)

    q_norm = np.linalg.norm(q)
    d_norms = np.linalg.norm(D, axis=1)

    if q_norm < 1e-9:
        return np.zeros(len(D))

    scores = D @ q
    d_norms = np.where(d_norms < 1e-9, 1e-9, d_norms)
    return scores / (d_norms * q_norm)


# ============================================================
# 벡터 검색
# ============================================================

class SimpleVectorStore:
    """
    강의용 초경량 인메모리 벡터 스토어.
    실제 서비스에서는 Pinecone / Weaviate / pgvector 등을 사용합니다.
    """

    def __init__(self):
        self.doc_ids: List[str] = []
        self.contents: List[str] = []
        self.embeddings: Optional[np.ndarray] = None
        self.metadata: List[Dict] = []

    def add_documents(
        self,
        documents: List[Dict],
        mode: str = "local",
        client=None,
        show_progress: bool = True,
    ):
        """문서 리스트를 인덱싱합니다."""
        self.doc_ids = [d["doc_id"] for d in documents]
        self.contents = [d["content"] for d in documents]
        self.metadata = [{k: v for k, v in d.items() if k != "content"} for d in documents]

        if show_progress:
            print(f"📊 {len(documents)}개 문서 임베딩 중...")

        self.embeddings = embed_texts(
            self.contents,
            mode=mode,
            client=client,
            show_progress=show_progress,
        )

        if show_progress:
            print(f"✅ 인덱싱 완료 (벡터 차원: {self.embeddings.shape[1]})")

    def search(self, query: str, top_k: int = 5, mode: str = "local", client=None) -> List[Dict]:
        """유사 문서를 검색합니다."""
        if self.embeddings is None:
            raise RuntimeError("문서를 먼저 add_documents()로 인덱싱하세요.")

        query_vec = embed_texts([query], mode=mode, client=client)[0]
        scores = cosine_similarity_batch(query_vec, self.embeddings)

        top_indices = np.argsort(scores)[::-1][:top_k]

        results = []
        for idx in top_indices:
            results.append({
                "doc_id": self.doc_ids[idx],
                "content": self.contents[idx],
                "score": float(scores[idx]),
                "metadata": self.metadata[idx],
            })
        return results

    def __len__(self):
        return len(self.doc_ids)


# ============================================================
# LLM 호출
# ============================================================

def call_llm(
    prompt: str,
    client=None,
    mode: str = "api",
    model: str = "gpt-4o-mini",
    system: str = "당신은 테크코어 주식회사의 내부 지식 어시스턴트입니다. 친절하고 정확하게 답변해주세요.",
    temperature: float = 0.7,
    max_tokens: int = 800,
    mock_response: str = None,
) -> str:
    """
    LLM을 호출합니다.

    mode='api': OpenAI API 사용
    mode='local': mock_response 반환 (또는 기본 안내 메시지)
    """
    if mode == "api" and client is not None:
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt},
                ],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            print(f"⚠️ LLM API 호출 실패: {e}")
            if mock_response:
                print("🔄 사전 준비된 mock 응답을 사용합니다.")
                return f"[Mock 응답]\n{mock_response}"
            return "[API 오류 - 로컬 모드로 전환하거나 API 키를 확인하세요]"

    # 로컬 모드
    if mock_response:
        return f"[📋 Mock 응답 (로컬 모드)]\n{mock_response}"
    return (
        "[로컬 모드: LLM 없이 실행 중]\n"
        "실제 강의 데모에서는 OpenAI API 또는 다른 LLM API를 사용합니다.\n"
        "API 키를 설정하면 실제 LLM 응답을 받을 수 있습니다."
    )


def call_llm_json(
    prompt: str,
    client=None,
    mode: str = "api",
    model: str = "gpt-4o-mini",
    system: str = "JSON 형식으로만 응답하세요. 코드 블록 없이 순수 JSON만 출력하세요.",
    mock_response: dict = None,
) -> dict:
    """JSON 출력을 요구하는 LLM 호출입니다."""
    if mode == "api" and client is not None:
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt},
                ],
                response_format={"type": "json_object"},
                temperature=0.2,
                max_tokens=1000,
            )
            return json.loads(resp.choices[0].message.content)
        except Exception as e:
            print(f"⚠️ JSON LLM 호출 실패: {e}")
            if mock_response:
                return mock_response
            return {"error": str(e)}

    if mock_response:
        return mock_response
    return {"mode": "local", "message": "LLM API 없이 실행 중"}


# ============================================================
# RAG 유틸리티
# ============================================================

def build_rag_prompt(
    query: str,
    retrieved_docs: List[Dict],
    max_context_chars: int = 3000,
) -> str:
    """RAG 프롬프트를 구성합니다."""
    context_parts = []
    total = 0

    for i, doc in enumerate(retrieved_docs, 1):
        content = doc.get("content", "")
        doc_id = doc.get("doc_id", f"문서{i}")
        chunk = f"[출처: {doc_id}]\n{content}"

        if total + len(chunk) > max_context_chars:
            break

        context_parts.append(chunk)
        total += len(chunk)

    context = "\n\n---\n\n".join(context_parts)

    return f"""아래 참고 문서를 기반으로 질문에 답변해주세요.

참고 문서에 없는 내용은 "해당 정보를 찾을 수 없습니다"라고 솔직하게 말하세요.
답변 마지막에는 어떤 문서를 참고했는지 "[참고: 문서ID]" 형식으로 명시하세요.

=== 참고 문서 ===
{context}

=== 질문 ===
{query}

=== 답변 ==="""


# ============================================================
# BM25 검색
# ============================================================

def build_bm25_index(documents: List[Dict]):
    """BM25 인덱스를 생성합니다."""
    from rank_bm25 import BM25Okapi

    # 한국어 간단 토크나이저 (공백 + 일부 특수문자 분리)
    def tokenize(text: str) -> List[str]:
        import re
        tokens = re.sub(r'[^\w\s]', ' ', text).split()
        return [t.lower() for t in tokens if len(t) > 1]

    contents = [d["content"] for d in documents]
    tokenized = [tokenize(c) for c in contents]
    bm25 = BM25Okapi(tokenized)

    return bm25, tokenize


def bm25_search(
    query: str,
    documents: List[Dict],
    bm25,
    tokenize_fn,
    top_k: int = 5,
) -> List[Dict]:
    """BM25로 문서를 검색합니다."""
    tokens = tokenize_fn(query)
    scores = bm25.get_scores(tokens)

    top_indices = np.argsort(scores)[::-1][:top_k]
    results = []
    for idx in top_indices:
        results.append({
            "doc_id": documents[idx]["doc_id"],
            "content": documents[idx]["content"],
            "score": float(scores[idx]),
        })
    return results


def hybrid_search(
    query: str,
    documents: List[Dict],
    vector_store: SimpleVectorStore,
    bm25,
    tokenize_fn,
    top_k: int = 5,
    mode: str = "local",
    client=None,
    alpha: float = 0.5,  # alpha=1이면 vector only, alpha=0이면 BM25 only
) -> List[Dict]:
    """
    하이브리드 검색: BM25 + 벡터 검색 결합

    최종 점수 = alpha * normalized_vector_score + (1-alpha) * normalized_bm25_score
    """
    # 벡터 검색
    vec_results = vector_store.search(query, top_k=len(documents), mode=mode, client=client)
    vec_scores = {r["doc_id"]: r["score"] for r in vec_results}

    # BM25 검색
    bm25_results = bm25_search(query, documents, bm25, tokenize_fn, top_k=len(documents))
    bm25_scores = {r["doc_id"]: r["score"] for r in bm25_results}

    # 정규화 (min-max)
    def normalize(scores_dict: dict) -> dict:
        vals = list(scores_dict.values())
        min_v, max_v = min(vals), max(vals)
        if max_v - min_v < 1e-9:
            return {k: 0.5 for k in scores_dict}
        return {k: (v - min_v) / (max_v - min_v) for k, v in scores_dict.items()}

    vec_norm = normalize(vec_scores)
    bm25_norm = normalize(bm25_scores)

    # 결합
    all_ids = set(vec_scores.keys()) | set(bm25_scores.keys())
    combined = {}
    for doc_id in all_ids:
        v = vec_norm.get(doc_id, 0.0)
        b = bm25_norm.get(doc_id, 0.0)
        combined[doc_id] = alpha * v + (1 - alpha) * b

    # 정렬
    sorted_ids = sorted(combined.keys(), key=lambda x: combined[x], reverse=True)[:top_k]

    doc_map = {d["doc_id"]: d for d in documents}
    results = []
    for doc_id in sorted_ids:
        doc = doc_map.get(doc_id, {})
        results.append({
            "doc_id": doc_id,
            "content": doc.get("content", ""),
            "score": combined[doc_id],
            "vec_score": vec_norm.get(doc_id, 0.0),
            "bm25_score": bm25_norm.get(doc_id, 0.0),
        })
    return results


# ============================================================
# 강의용 요약 출력
# ============================================================

LECTURE_TIPS = {
    "01": "💡 LLM은 '말 잘하기'가 아니라 '구조화'가 핵심입니다. 같은 입력도 프롬프트 구조에 따라 완전히 다른 결과가 나옵니다.",
    "02": "💡 멀티모달은 이미지를 '보는' 게 아니라, 현실 세계의 다양한 입력을 AI 시스템이 처리할 수 있게 됐다는 의미입니다.",
    "03": "💡 벡터 DB는 신비한 것이 아닙니다. 의미 기반 검색 인프라입니다. LLM이 내 문서를 모르기 때문에 필요합니다.",
    "04": "💡 RAG는 모델 재학습이 아니라, 답변 직전에 지식을 붙여주는 패턴입니다. 학습 비용 없이 지식을 업데이트할 수 있습니다.",
    "05": "💡 2026년 관점에서 중요한 것은 vector DB 자체가 아니라 retrieval quality입니다. 검색 실패 = 답변 실패.",
    "06": "💡 현실의 AI 시스템은 단발성 RAG보다 agentic retrieval 쪽으로 진화하고 있습니다. LLM이 도구를 반복 사용합니다.",
    "07": "💡 GraphRAG가 정답이 아닙니다. 관계가 중요한 문제에서 구조화된 context가 도움이 된다는 것이 핵심 메시지입니다.",
}


def print_lecture_tip(notebook_id: str):
    """강의자 팁을 출력합니다."""
    from IPython.display import display, HTML
    tip = LECTURE_TIPS.get(notebook_id, "")
    if tip:
        display(HTML(f"""
        <div style="background:#fff9c4;border-left:4px solid #f39c12;
                    padding:12px 16px;border-radius:5px;margin:10px 0;
                    font-family:Arial,sans-serif;font-size:13px;">
          <strong>🎤 강의자 멘트 포인트</strong><br>
          {tip}
        </div>
        """))


def print_audience_question(questions: List[str]):
    """청중 질문 유도 포인트를 출력합니다."""
    from IPython.display import display, HTML
    items = "".join(f"<li>{q}</li>" for q in questions)
    display(HTML(f"""
    <div style="background:#e8f4fd;border-left:4px solid #3498db;
                padding:12px 16px;border-radius:5px;margin:10px 0;
                font-family:Arial,sans-serif;font-size:13px;">
      <strong>🙋 청중 질문 유도</strong>
      <ul style="margin:8px 0 0 0;padding-left:18px;line-height:1.8;">{items}</ul>
    </div>
    """))


def print_production_notes(notes: List[str]):
    """실무 확장 포인트를 출력합니다."""
    from IPython.display import display, HTML
    items = "".join(f"<li>{n}</li>" for n in notes)
    display(HTML(f"""
    <div style="background:#f0f4ff;border-left:4px solid #6c5ce7;
                padding:12px 16px;border-radius:5px;margin:10px 0;
                font-family:Arial,sans-serif;font-size:13px;">
      <strong>🏗️ 실무 확장 포인트</strong>
      <ul style="margin:8px 0 0 0;padding-left:18px;line-height:1.8;">{items}</ul>
    </div>
    """))


if __name__ == "__main__":
    check_environment()
