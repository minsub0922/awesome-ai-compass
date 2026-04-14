# AI 특강 실습 가이드
## "LLM은 단순 챗봇이 아니다 - AI 시스템 설계의 실제"
### 2시간 30분 | AI/SW 연수생 대상

---

## 📁 파일 구조

```
ai_special_course/
├── LECTURE_GUIDE.md          ← 이 파일 (강의자 가이드)
├── requirements.txt          ← 설치 패키지 목록
├── helpers/
│   ├── lecture_helpers.py    ← 공통 유틸리티 함수
│   └── demo_data.py          ← 샘플 문서 데이터
└── notebooks/
    ├── 00_overview_and_setup.ipynb
    ├── 01_llm_as_interface.ipynb
    ├── 02_multimodal_demo.ipynb
    ├── 03_embeddings_and_vector_search.ipynb
    ├── 04_basic_rag_demo.ipynb
    ├── 05_better_rag_hybrid_and_rerank.ipynb
    ├── 06_agentic_search_or_tool_use.ipynb
    └── 07_graphrag_concept_demo.ipynb
```

---

## ⏱️ 시간 배분 추천 (2시간 30분)

| 시간 | 노트북 | 내용 | 형태 |
|------|--------|------|------|
| 0:00-0:10 | 없음 | 강의 소개, 핵심 메시지 | 슬라이드 |
| 0:10-0:20 | 00 | 환경 설정, 데이터 소개 | 셋업 |
| 0:20-0:35 | 01 | LLM as Interface | **핵심 시연** |
| 0:35-0:50 | 02 | 멀티모달 데모 | 시연 |
| 0:50-1:05 | 03 | Embeddings & Vector Search | **핵심 시연** |
| 1:05-1:15 | - | 휴식 + Q&A | - |
| 1:15-1:35 | 04 | Basic RAG (Before/After) | **핵심 시연** |
| 1:35-1:55 | 05 | Hybrid Search & Rerank | 시연 |
| 1:55-2:15 | 06 | Agentic Search | **핵심 시연** |
| 2:15-2:25 | 07 | GraphRAG 개념 (선택) | 개념 시연 |
| 2:25-2:30 | - | 마무리 & 핵심 메시지 | 슬라이드 |

### 빠른 시연 버전 (90분)
- 00 + 01 + 03 + 04 + 06 (각 10-15분)
- 02, 05, 07은 생략 또는 설명으로 대체

---

## 🎯 노트북-메시지 매핑

| 노트북 | 핵심 메시지 | 드라마틱한 포인트 |
|--------|------------|-----------------|
| 01 | LLM은 구조화 인터페이스다 | 회의 메모 → JSON TODO 변환 |
| 02 | 현실 입력을 AI가 처리한다 | 영수증 사진 → 경비처리 JSON |
| 03 | Vector DB = 의미 기반 검색 인프라 | BM25 vs Vector 비교 |
| 04 | 검색+LLM = 내부 지식 연결 | LLM 단독 vs RAG 전/후 비교 |
| 05 | Retrieval quality가 전부다 | 하이브리드로 coverage 향상 |
| 06 | 도구 반복 사용 = Agentic | 복잡한 질문 → 다단계 해결 |
| 07 | 관계 중요한 문제 = 구조화 필요 | 영향 체인 추적 시연 |

---

## 🔑 API 키 안내

### API 키가 있는 경우 (권장)
- OpenAI API 키 사용 (gpt-4o-mini, text-embedding-3-small)
- 각 노트북 상단 `OPENAI_API_KEY = "sk-..."` 에 입력
- 예상 비용: 강의 1회 약 $0.5~2.0 (절약 팁: temperature=0, max_tokens 제한)

### API 키가 없는 경우 (완전 작동)
- 임베딩: sentence-transformers all-MiniLM-L6-v2 (로컬, 무료)
- LLM: 사전 준비된 Mock 응답 (실제 API 응답과 동일한 내용)
- 01번 노트북의 구조화 출력은 로컬 모드에서 mock으로 시연 가능

---

## 🚨 라이브 데모 실패 대비

### 플랜 A: API 모드 (정상)
- 실제 LLM 응답 표시
- 실시간 API 호출

### 플랜 B: 네트워크 실패
- 각 노트북의 `mock_response` 변수로 즉시 전환
- 노트북 상단 `MODE = "local"` 강제 설정

### 플랜 C: 완전 오프라인
- 모든 mock 응답 사전 실행 후 결과 캡처
- Colab 출력 결과 이미지 준비

### 사전 점검 체크리스트
```
□ Colab에서 00번 노트북 미리 실행 → 패키지 설치 완료 확인
□ API 키 유효성 확인 (잔액 확인)
□ 각 노트북 1회 사전 실행 → 출력 결과 저장
□ 백업 이미지 파일 준비 (스크린샷)
□ 로컬 모드에서도 임베딩 모델 다운로드 완료 확인
```

---

## 💡 강의자 체크포인트

### 01번 (LLM as Interface)
- "같은 입력, 다른 프롬프트 → 완전히 다른 출력" 강조
- JSON 출력을 보여주면서 "이게 Jira에 바로 올라갈 수 있다" 언급

### 03번 (Embeddings)
- "의미가 비슷하면 벡터가 가깝다" - 유사도 막대 그래프 강조
- "벡터 DB는 결국 이걸 빠르게 하는 인프라"

### 04번 (RAG) ← 가장 중요
- LLM 단독 vs RAG 비교에서 잠시 멈추고 청중 반응 확인
- "이게 모델 재학습 없이 일어났다" 강조

### 05번 (Hybrid)
- BM25가 잘 되는 케이스, Vector가 잘 되는 케이스 각각 보여주기
- "2026년 기준 Vector DB 자체보다 retrieval quality가 중요"

### 06번 (Agentic)
- 도구 호출 로그가 출력되면서 "모델이 스스로 계획한다"는 느낌 강조
- "이것이 LLM이 Agent로 진화하는 방향"

---

## 🙋 예상 질문 & 모범 답변

**Q: Fine-tuning vs RAG, 언제 뭘 써야 하나요?**
A: Fine-tuning은 모델의 말투/형식/전문 어휘를 바꿀 때. RAG는 최신 정보/내부 지식을 제공할 때. 대부분의 기업 use case는 RAG가 먼저입니다.

**Q: Vector DB는 어떤 제품을 선택해야 하나요?**
A: 스타트업/MVP: Chroma, PostgreSQL+pgvector / 중규모: Weaviate, Qdrant / 대규모: Pinecone. 하지만 제품 선택보다 검색 전략이 더 중요합니다.

**Q: GraphRAG는 언제 필요한가요?**
A: 관계 추적이 핵심인 도메인 (법률 조항 계층, 조직도, 의존성 분석). 대부분의 경우 Agentic RAG로 충분합니다.

**Q: 한국어 임베딩은 어떤 모델이 좋나요?**
A: paraphrase-multilingual-MiniLM-L12-v2 (다국어), jhgan/ko-sroberta-multitask (한국어 특화), OpenAI text-embedding-3-small (API).
