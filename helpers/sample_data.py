"""
sample_data.py - 강의 실습용 샘플 데이터 통합 모듈

AI 특강 실습 노트북 00~07에서 사용하는 샘플 데이터를 한 곳에 모아 둡니다.
각 노트북에서는 `from helpers.sample_data import <이름>` 형식으로 import 합니다.

노트북별 섹션:
  00: SAMPLE_DOCS_OVERVIEW_00  - 개요 노트북용 15개 문서 (원문 유지)
  01: MEETING_MEMO / SUPPORT_TICKET_TEXT / USER_SEARCH_REQUEST
  02: MOCK_RECEIPT_OCR / MOCK_WHITEBOARD_OCR / UI_DESCRIPTION / mock_ux
  03: SAMPLE_DOCS_MINI_03 / TEST_TEXTS_03
  04: SAMPLE_DOCS_MINI_04 / MOCK_LLM_ONLY / MOCK_RAG_RESPONSE
  05: SAMPLE_DOCS_05 / TEST_CASES_05
  06: RELEASE_NOTES / POLICIES / SAMPLE_DOCS_06 / MOCK_AGENTIC_ANSWER_1
  07: ENTITIES / RELATIONS

참고:
  - helpers/demo_data.py 의 full-text SAMPLE_DOCS 도 여기서 재노출 합니다.
    `from helpers.sample_data import SAMPLE_DOCS` 로 바로 쓸 수 있습니다.
"""

# ------------------------------------------------------------------
# 00_overview_and_setup 의 full-text SAMPLE_DOCS 는 demo_data.py 에 마스터가 있으며
# 편의를 위해 여기서도 재노출 합니다.
# ------------------------------------------------------------------
try:
    from helpers.demo_data import (  # noqa: F401
        SAMPLE_DOCS,
        SAMPLE_QUERIES,
        MOCK_IMAGE_DESCRIPTIONS,
        get_sample_docs,
        get_docs_by_category,
        get_doc_by_id,
        get_all_contents_with_ids,
    )
except ImportError:  # Colab 등 패키지 경로가 다를 때
    from demo_data import (  # type: ignore  # noqa: F401
        SAMPLE_DOCS,
        SAMPLE_QUERIES,
        MOCK_IMAGE_DESCRIPTIONS,
        get_sample_docs,
        get_docs_by_category,
        get_doc_by_id,
        get_all_contents_with_ids,
    )

# ========================================================================
# 00_overview_and_setup - 개요 노트북 전용 SAMPLE_DOCS (compact 버전)
# ========================================================================
# 00번 노트북에는 demo_data.SAMPLE_DOCS 와는 content 포맷이 다른
# compact 형식의 15개 문서가 정의되어 있었습니다. 원문을 그대로 보존합니다.
SAMPLE_DOCS_OVERVIEW_00 = [
    {
        "doc_id": "SEC-POL-003",
        "title": "API 키 및 시크릿 관리 정책 v3.1 [현행]",
        "category": "보안정책",
        "date": "2024-11-01",
        "content": """[최신 정책 - v3.1 시행: 2024-11-01]
API 키 생명주기:
  - 개발용 키: 90일 자동 만료
  - 운영용 키: 365일 자동 만료, 60일 전 갱신 알림
  - 긴급 키: 발급 후 24시간 내 폐기
저장 규칙:
  - 코드베이스 하드코딩 금지
  - 반드시 환경변수 또는 AWS Secrets Manager 사용
  - .env 파일은 .gitignore에 포함 필수
  - CI/CD는 GitHub Actions Secrets 또는 Vault 사용
접근 권한:
  - 최소 권한 원칙 적용
  - 팀 리드 이상만 운영 키 발급 권한
  - 보안팀 승인 필요 (SLA: 2 영업일)
유출 시 대응:
  - 즉시 Slack #security-alert 보고
  - 10분 이내 키 폐기 의무
  - 7일 이내 보안 감사 보고서 제출
담당: 보안팀 이민준 / 승인: CISO 박지수"""
    },
    {
        "doc_id": "SEC-POL-002",
        "title": "API 키 관리 정책 v2.8 [구버전 - 비효력]",
        "category": "보안정책",
        "date": "2024-03-15",
        "content": """[구버전 v2.8 - 현재 비효력, 참고용]
API 키 유효기간:
  - 모든 키: 180일 자동 만료 (신버전과 다름!)
  - 만료 30일 전 이메일 알림
저장 방법:
  - 환경변수 사용 권장
  - 팀 공유 키는 팀 리드가 관리
분실/유출 시 대응:
  - 팀 리드에게 보고
  - IT헬프데스크 티켓 생성
※ 주의: 이 문서는 구버전입니다. 현행 정책은 SEC-POL-003 참조."""
    },
    {
        "doc_id": "REL-CLOUDSYNC-023",
        "title": "CloudSync v2.3 릴리즈 노트",
        "category": "릴리즈노트",
        "date": "2024-10-20",
        "content": """CloudSync v2.3 (출시: 2024-10-20)
새 기능:
  - 실시간 파일 동기화 속도 40% 향상
  - Apple Silicon (M3) 네이티브 지원
  - 파일 버전 히스토리 90일로 연장 (기존 30일)
Breaking Changes (업그레이드 필수 확인):
  - Python SDK 최소 버전: 3.8 → 3.10
  - REST API v1 엔드포인트 완전 제거 (v2로 마이그레이션)
  - 설정 파일 경로: ~/.cloudsync/config → ~/.config/cloudsync/config.yaml
  - 인증 방식: JWT → OAuth 2.0 Bearer Token
버그 수정:
  - 대용량 파일(>4GB) 업로드 연결 끊김 수정
  - Windows 11 특수문자 파일명 오류 수정
마이그레이션 가이드: docs.techcore.kr/cloudsync/migration/v2.3
담당: 클라우드플랫폼팀 김도현"""
    },
    {
        "doc_id": "REL-CLOUDSYNC-022",
        "title": "CloudSync v2.2 릴리즈 노트 [이전 버전]",
        "category": "릴리즈노트",
        "date": "2024-07-15",
        "content": """CloudSync v2.2 (출시: 2024-07-15)
새 기능:
  - 선택적 동기화 폴더 설정
  - 모바일 앱 오프라인 모드
  - 파일 버전 히스토리 30일 제공
Breaking Changes:
  - API v1 일부 엔드포인트 deprecated 예고 (v2.3에서 제거)
버그 수정: macOS Ventura 호환성 수정
담당: 클라우드플랫폼팀"""
    },
    {
        "doc_id": "REL-DATAPULSE-011",
        "title": "DataPulse v1.1 릴리즈 노트",
        "category": "릴리즈노트",
        "date": "2024-09-05",
        "content": """DataPulse v1.1 (출시: 2024-09-05)
DataPulse: 실시간 데이터 파이프라인 모니터링 도구
새 기능:
  - Kafka 0.11+ 네이티브 커넥터
  - Slack 웹훅 알림 연동
  - 커스텀 알림 규칙 설정
Breaking Changes:
  - 설정 파일: JSON → YAML (자동 변환 도구 제공)
  - 최소 메모리: 512MB → 1GB
주의: v1.0 업그레이드 시 config.yaml 변환 도구 먼저 실행 필요
담당: 데이터인프라팀 최서연"""
    },
    {
        "doc_id": "WFH-POL-001",
        "title": "원격 근무 정책 v2.0",
        "category": "HR정책",
        "date": "2024-09-01",
        "content": """원격 근무 정책 v2.0 (시행: 2024-09-01)
기본 원칙: 주 3일 사무실 / 2일 재택 (하이브리드)
수요일: 전사 오피스데이 (출근 권장)
재택 환경 요건:
  - 인터넷 최소 50Mbps
  - 화상회의 가능 환경
  - VPN 사용 필수
해외 원격 근무: 연 30일 한도, HR팀 사전 승인 필수
장비 지원:
  - 노트북 1대 지급 (신규)
  - 주변기기: 연 50만원 한도
  - 인터넷 요금: 월 3만원 지원
코어타임: 오전 10시~오후 4시 (온라인 필수)
담당: HR팀 강하늘"""
    },
    {
        "doc_id": "ONBOARD-ENG-001",
        "title": "개발자 온보딩 체크리스트",
        "category": "프로세스",
        "date": "2024-08-01",
        "content": """개발자 온보딩 체크리스트
1주차:
  - 노트북 수령 및 개발 환경 세팅 (Homebrew, pyenv, Docker)
  - GitHub 조직 초대, Slack 참여
  - 필수 계정: Jira, Confluence, AWS SSO, 1Password
  - 보안 교육 수료 (온라인 2시간, 필수)
2주차:
  - 코드베이스 개요 세션 (기술 리드와 1시간)
  - 첫 PR: Good first issue 1개 해결
  - 페어 프로그래밍 세션
3~4주차:
  - 독립 기능 구현 1개
  - 코드 리뷰 리뷰어로 참여
  - 30일 체크인 미팅 (직속 매니저)
온보딩 버디: 팀내 시니어 엔지니어 (랜덤 배정)"""
    },
    {
        "doc_id": "MTG-2024Q3-STRATEGY",
        "title": "2024년 3분기 전략 회의록",
        "category": "회의록",
        "date": "2024-07-02",
        "content": """3분기 전략 기획 회의 (2024-07-02)
참석: CTO 송재원, PM 장유진, 클라우드팀 김도현, 데이터팀 최서연, 보안팀 이민준
주요 결정:
  1. CloudSync v2.3 출시 목표: 2024년 10월 (확정)
  2. DataPulse v1.1 출시 목표: 2024년 9월 (확정)
  3. 보안 정책 v3.1 개정: 2024년 11월 시행 (확정)
  4. 채용: 시니어 백엔드 3명, ML 엔지니어 2명
액션 아이템:
  - 김도현: v2.3 마일스톤 Jira 업데이트 (7/10)
  - 최서연: DataPulse 마이그레이션 가이드 초안 (7/20)
  - 이민준: 보안 정책 v3.1 초안 (8월 말)
  - 강하늘: ML엔지니어 JD 초안 (7/15)
다음 회의: 2024-08-06"""
    },
    {
        "doc_id": "MTG-2024-SEC-REVIEW",
        "title": "보안 정책 개정 검토 회의록",
        "category": "회의록",
        "date": "2024-09-15",
        "content": """보안 정책 개정 검토 회의 (2024-09-15)
참석: 보안팀 이민준, CTO 송재원, 클라우드팀 김도현, 법무팀 홍준혁
기존 v2.8 문제점:
  - API 키 유효기간 180일이 과도하게 긺
  - 유출 시 대응 절차 불명확
  - 운영/개발 키 구분 없음
v3.1 주요 변경:
  - 키 유효기간 단축 (개발 90일, 운영 365일, 긴급 24시간)
  - 보안팀 승인 프로세스 추가
  - 유출 시 10분 내 폐기 의무화
결정: v3.1 시행일 2024-11-01 확정
기존 키 일괄 감사: 10월 한 달간
이민준: 전사 공지 11월 1일 전
김도현: 개발팀 하드코딩 키 점검 (10월까지)"""
    },
    {
        "doc_id": "FAQ-DATAPULSE-001",
        "title": "DataPulse FAQ",
        "category": "FAQ",
        "date": "2024-09-10",
        "content": """DataPulse 자주 묻는 질문
Q: v1.0에서 v1.1로 업그레이드 시 데이터 손실이 있나요?
A: 설정 데이터는 자동 마이그레이션. 메트릭 히스토리는 유지.
   단, 커스텀 대시보드는 수동 재설정 필요할 수 있음.
   업그레이드 전 반드시 백업 권장.
Q: 최소 사양은?
A: v1.1 기준 - CPU 2코어, 메모리 1GB, 디스크 10GB
   (v1.0은 메모리 512MB였으나 v1.1부터 1GB 필수)
Q: Slack 알림 설정 방법은?
A: config.yaml에 Slack Webhook URL 추가:
   notifications.slack.webhook_url: "https://hooks.slack.com/..."
Q: 데이터 보관 기간은?
A: 기본 30일. config.yaml에서 최대 365일까지 설정 가능.
담당: 데이터인프라팀 최서연"""
    },
    {
        "doc_id": "FAQ-SECURITY-001",
        "title": "보안 정책 FAQ (v3.1 기준)",
        "category": "FAQ",
        "date": "2024-11-05",
        "content": """보안 정책 FAQ (v3.1 기준)
Q: 기존 API 키는 어떻게 처리하나요?
A: 10월 일괄 감사로 새 정책에 맞게 유효기간 재설정.
   운영 키: 발급일 기준 365일, 개발 키: 90일로 재설정.
Q: AWS Secrets Manager 대신 다른 도구를 써도 되나요?
A: HashiCorp Vault, GCP Secret Manager도 공식 지원.
   개인 노트나 팀 위키 저장은 엄격히 금지.
Q: 보안팀 승인 SLA 2 영업일이 급할 때는?
A: #security-urgent Slack 채널로 연락하면 당일 처리 시도.
Q: .env 파일이 실수로 git에 올라간 경우?
A: 1) 즉시 키 폐기(10분 내)  2) #security-alert 보고
   3) git 히스토리 제거  4) 7일 내 보고서 제출
담당: 보안팀 이민준"""
    },
    {
        "doc_id": "FAQ-HR-001",
        "title": "HR 정책 FAQ",
        "category": "FAQ",
        "date": "2024-09-05",
        "content": """HR 정책 FAQ
Q: 재택 장비 지원 신청 방법은?
A: helpdesk.techcore.kr에서 '장비 지원 신청' 카테고리로 신청.
   연 50만원 한도, 영수증 제출 후 정산.
Q: 해외 원격 근무 신청 절차는?
A: 최소 2주 전 HR팀 이메일 신청.
   기간/위치/목적 명시 + 팀 리드 승인 첨부.
   세금 이슈 국가는 법무팀 추가 검토 필요.
Q: 인터넷 요금 지원 시작 시점은?
A: 입사 1개월 후 시작. 매월 급여일에 3만원 지급.
담당: HR팀 강하늘"""
    },
    {
        "doc_id": "PROC-DEPLOY-001",
        "title": "운영 배포 체크리스트 v2",
        "category": "프로세스",
        "date": "2024-08-15",
        "content": """운영 환경 배포 체크리스트 v2
배포 전:
  - 모든 테스트 통과 (Unit + Integration + E2E)
  - 코드 리뷰 최소 2명 승인
  - 보안 스캔 통과 (Snyk/SAST)
  - 스테이징 QA 완료
  - 롤백 계획 문서화
  - 팀 리드 최종 승인
배포 권장 시간: 화/수/목 오전 10시~오후 2시
배포 시:
  - Slack #deployments 채널 공지
  - Grafana + DataPulse 대시보드 오픈
배포 후:
  - 핵심 지표 확인 (응답시간, 에러율, CPU)
롤백 기준: 에러율 5% 초과 또는 P0/P1 인시던트 발생
담당: DevOps팀 박철원"""
    },
    {
        "doc_id": "PROC-INCIDENT-001",
        "title": "인시던트 대응 절차 v1.3",
        "category": "프로세스",
        "date": "2024-07-01",
        "content": """인시던트 대응 절차 v1.3
심각도 분류:
  P0: 서비스 전체 다운 - 30분 내 대응, 즉시 CTO 보고
  P1: 핵심 기능 장애 - 1시간 내, 팀리드 보고
  P2: 성능 저하/부분 장애 - 4시간 내
  P3: 경미한 버그 - 다음 스프린트 내
대응 프로세스:
  1. 인식 → 5분 내 심각도 분류
  2. Slack #incidents 채널 생성 및 관련자 태그
  3. 영향 범위 파악 → 임시 방편 조치
  4. 에스컬레이션 (P0/P1: CTO까지)
  5. 해결 및 복구
  6. P0/P1: 48시간 내 포스트모템 작성
롤백: 에러율 5% 초과 시 즉시
온콜 로테이션: PagerDuty 참조"""
    },
    {
        "doc_id": "PROC-CODE-REVIEW-001",
        "title": "코드 리뷰 가이드라인",
        "category": "프로세스",
        "date": "2024-06-01",
        "content": """코드 리뷰 가이드라인
리뷰어 원칙:
  - 24시간 이내 첫 리뷰 (영업일)
  - 중요도 표시: Nit / Minor / Major / Blocking
리뷰 체크포인트:
  - 비즈니스 로직이 요구사항과 일치하는가?
  - 보안 취약점은 없는가? (OWASP Top 10)
  - 성능 이슈 없는가? (N+1 쿼리, 불필요한 루프)
  - 테스트 커버리지 80% 이상?
PR 작성자:
  - PR 설명에 변경 이유와 영향 범위 명시
  - 500줄 이하 PR 권장
  - Self-review 후 리뷰 요청
머지 조건: 최소 2명 Approve + CI 통과 + Blocking 없음"""
    },
]
# ========================================================================
# 01_llm_as_interface
# ========================================================================
MEETING_MEMO = """2024년 11월 20일 스프린트 회의

참석: 김도현(팀리드), 이수진(백엔드), 박민재(프론트), 최서연(QA)

논의 내용:
- CloudSync v2.3 배포가 다음 주 화요일로 예정됨. 이수진이 마이그레이션 스크립트
  최종 검토를 금요일까지 완료해야 함.
- 박민재는 로딩 스피너 버그 수정이 아직 안 됨. 오늘 중으로 처리 요청.
- QA 테스트 결과 3개 이슈 발견됨. 최서연이 Jira에 등록 예정.
- 김도현: 다음 스프린트 플래닝은 12월 2일로 확정.
- 보안팀에서 API 키 감사 결과 공유받아야 함. 이민준에게 연락 필요.
- 신규 ML 엔지니어 온보딩 시작. 멘토: 이수진.

결정 사항:
- v2.3 배포일: 2024-11-26 (화)
- 롤백 기준: 에러율 5% 초과
- 다음 회의: 2024-12-02
"""

SUPPORT_TICKET_TEXT = """안녕하세요, CloudSync를 v2.2에서 v2.3으로 업그레이드했는데요,
기존에 쓰던 Python 스크립트가 갑자기 안 되기 시작했어요.
에러 메시지는 'Authentication failed: JWT token not supported'이고요,
파이썬 버전은 3.9인데 혹시 이게 문제일까요? 급하게 처리가 필요합니다."""

USER_SEARCH_REQUEST = """지난 달에 배포된 DataPulse 최신 버전이 뭔지 알고 싶고,
거기서 Kafka 연동 설정하는 방법이랑 Slack 알림 설정도 같이 알려줘. 
가능하면 공식 문서 링크도."""

# ========================================================================
# 02_multimodal_demo
# ========================================================================
MOCK_RECEIPT_OCR = """[영수증 OCR 결과]
TECHCORE 구내식당
2024-11-20  12:34
김치찌개 세트: 8,500원
제육볶음 세트: 9,000원
아메리카노: 3,000원
물: 무료
소계: 20,500원
부가세(10%): 2,050원
합계: 22,550원
결제수단: 법인카드 ****-****-****-1234
승인번호: 20241120-8834521"""

MOCK_WHITEBOARD_OCR = """[화이트보드 OCR 결과]
Q4 주요 목표 (2024)
[제품] CloudSync v2.3 출시 ✓
[제품] DataPulse v1.1 출시 ✓
[보안] API 키 정책 v3.1 시행 ✓
[채용] 시니어 백엔드 3명 → 2명 완료
[채용] ML 엔지니어 2명 → 진행중
핵심 메트릭:
- MAU 목표: 50K → 현재 43K (갭 7K)
- API 응답속도: < 200ms ✓
- 서비스 가용성: 99.9% ✓
TODO:
→ ML엔지니어 채용 마무리 (강하늘)
→ MAU 갭 분석 필요 (장유진)"""

UI_DESCRIPTION = """CloudSync 웹 대시보드 스크린샷 설명:
- 페이지: 로그인 후 메인 대시보드
- 상단: 로고, 파일/공유/팀/설정 메뉴, 알림아이콘(빨간뱃지 3), 프로필
- 메인: '최근 파일' 5개, '공유된 파일' 3개
- 하단 배너: 'v2.3 마이그레이션 안내' (무시되고 있음, 3번째 방문)
- 마우스 커서: 설정 아이콘 근처에 있다가 알림으로 이동
- 세션 시간: 4분 20초, 클릭 3회"""

UX_ANALYSIS_PROMPT = f"""아래 UI 스크린샷 설명을 바탕으로 사용자 행동을 분석하세요.

반환 형식 JSON:
{{
  "user_intent": "사용자가 원하는 것 (1문장)",
  "friction_points": ["문제가 되는 UX 요소"],
  "ignored_features": ["무시되는 기능"],
  "recommendations": ["개선 제안"]
}}

스크린샷:
{UI_DESCRIPTION}"""

mock_ux = {
    "user_intent": "알림을 확인하려고 했으나 설정 페이지를 찾다가 알림으로 이동한 것으로 보임",
    "friction_points": [
        "설정과 알림 아이콘이 시각적으로 가까워 혼동 유발",
        "마이그레이션 배너가 3번 방문에도 무시됨 → 배너 피로도 높음"
    ],
    "ignored_features": [
        "v2.3 마이그레이션 안내 배너",
        "공유된 파일 섹션 (클릭 없음)"
    ],
    "recommendations": [
        "알림 아이콘과 설정 아이콘 간격 확대",
        "마이그레이션 배너 → 모달/인터스티셜로 전환 고려",
        "3회 이상 무시된 배너는 자동 숨김 처리"
    ]
}

# ========================================================================
# 03_embeddings_and_vector_search
# ========================================================================
SAMPLE_DOCS_MINI_03 = [
    {"doc_id": "SEC-POL-003", "category": "보안정책",
     "content": "API 키 관리 정책 v3.1 (현행). 개발용 키 90일, 운영용 키 365일, 긴급 키 24시간 유효. 코드 하드코딩 금지, AWS Secrets Manager 또는 환경변수 사용 필수. 유출 시 10분 내 폐기, Slack #security-alert 즉시 보고. 보안팀 승인 필요 (SLA 2 영업일)."},
    {"doc_id": "SEC-POL-002", "category": "보안정책",
     "content": "API 키 관리 정책 v2.8 (구버전, 비효력). 모든 키 180일 만료. 팀 리드 관리. 분실 시 IT헬프데스크 티켓. 현재는 SEC-POL-003 참조."},
    {"doc_id": "REL-CLOUDSYNC-023", "category": "릴리즈노트",
     "content": "CloudSync v2.3 릴리즈 (2024-10-20). 파일 동기화 속도 40% 향상. Breaking Changes: Python 3.10 필수, REST API v1 제거, 설정 파일 경로 변경, JWT에서 OAuth 2.0으로 인증 방식 변경. 대용량 파일 버그 수정."},
    {"doc_id": "REL-CLOUDSYNC-022", "category": "릴리즈노트",
     "content": "CloudSync v2.2 릴리즈 (2024-07-15). 선택적 동기화, 오프라인 모드 추가. 파일 버전 히스토리 30일 제공. API v1 deprecated 예고."},
    {"doc_id": "REL-DATAPULSE-011", "category": "릴리즈노트",
     "content": "DataPulse v1.1 릴리즈 (2024-09-05). Kafka 0.11+ 네이티브 커넥터 추가. Slack 웹훅 알림 연동. 설정 파일 JSON에서 YAML로 전환. 최소 메모리 1GB 필요."},
    {"doc_id": "WFH-POL-001", "category": "HR정책",
     "content": "원격 근무 정책 v2.0. 주 3일 사무실, 2일 재택. 인터넷 50Mbps 이상 필요. VPN 필수. 해외 원격 근무 연 30일 한도. 장비 지원: 노트북, 주변기기 연 50만원, 인터넷 월 3만원. 코어타임 오전 10시~오후 4시."},
    {"doc_id": "ONBOARD-ENG-001", "category": "프로세스",
     "content": "개발자 온보딩 체크리스트. 1주차: 노트북 수령, GitHub 초대, 보안 교육 (2시간 필수). 2주차: 코드베이스 세션, 첫 PR. 3~4주차: 독립 기능 구현, 코드 리뷰. 온보딩 버디는 시니어 엔지니어."},
    {"doc_id": "MTG-2024Q3-STRATEGY", "category": "회의록",
     "content": "Q3 전략 회의 (2024-07-02). CloudSync v2.3 출시 10월 확정, DataPulse v1.1 9월 확정, 보안 정책 v3.1 11월 시행. 채용: 시니어 백엔드 3명, ML 엔지니어 2명."},
    {"doc_id": "MTG-2024-SEC-REVIEW", "category": "회의록",
     "content": "보안 정책 개정 검토 회의 (2024-09-15). v2.8 문제점: 키 유효기간 180일 과다, 대응 절차 불명확. v3.1 개선: 키 단축, 보안팀 승인 추가, 유출 10분 내 폐기 의무화. 시행일 2024-11-01 확정."},
    {"doc_id": "FAQ-DATAPULSE-001", "category": "FAQ",
     "content": "DataPulse FAQ. v1.0→v1.1 업그레이드 시 데이터 손실 없음. 최소 사양 메모리 1GB. Slack 알림: config.yaml에 webhook_url 추가. 데이터 보관 기간 기본 30일, 최대 365일."},
    {"doc_id": "FAQ-SECURITY-001", "category": "FAQ",
     "content": "보안 정책 FAQ v3.1 기준. 기존 API 키는 10월 일괄 감사로 새 정책 적용. Vault, GCP Secret Manager도 지원. 긴급 시 #security-urgent 채널. .env 파일 git 유출 시: 키 폐기→보고→히스토리 제거→보고서."},
    {"doc_id": "FAQ-HR-001", "category": "FAQ",
     "content": "HR 정책 FAQ. 장비 지원 신청: helpdesk.techcore.kr. 해외 원격 근무: 2주 전 HR팀 신청. 인터넷 요금: 입사 1개월 후 월 3만원 지원."},
    {"doc_id": "PROC-DEPLOY-001", "category": "프로세스",
     "content": "운영 배포 체크리스트 v2. 배포 전: 테스트 통과, 코드 리뷰 2명, 보안 스캔, 스테이징 QA, 롤백 계획. 권장 시간: 화~목 오전 10시~오후 2시. 에러율 5% 초과 시 즉시 롤백."},
    {"doc_id": "PROC-INCIDENT-001", "category": "프로세스",
     "content": "인시던트 대응 절차 v1.3. P0 (전체 다운): 30분 내, CTO 즉시 보고. P1 (핵심 장애): 1시간 내. P2 (성능 저하): 4시간 내. P0/P1: 48시간 내 포스트모템. 롤백: 에러율 5% 초과."},
    {"doc_id": "PROC-CODE-REVIEW-001", "category": "프로세스",
     "content": "코드 리뷰 가이드라인. 리뷰어: 24시간 내 첫 리뷰. Blocking 코멘트 해소 필수. 머지 조건: 2명 Approve + CI 통과. PR 크기 500줄 이하 권장. 보안 취약점 OWASP Top 10 기준 확인."},
]
TEST_TEXTS_03 = [
    "API 키를 안전하게 관리하는 방법",      # 보안 관련
    "시크릿 키 저장 및 보안 정책",           # 보안 관련 (유사)
    "CloudSync 파일 동기화 속도 개선",       # 제품 관련
    "재택근무 장비 지원 신청 절차",          # HR 관련
    "점심 메뉴 추천해주세요",               # 완전 무관
]
# ========================================================================
# 04_basic_rag_demo
# ========================================================================
SAMPLE_DOCS_MINI_04 = [
    {"doc_id": "SEC-POL-003", "category": "보안정책",
     "content": "API 키 관리 정책 v3.1 (현행, 시행 2024-11-01). 개발용 키 90일, 운영용 키 365일, 긴급 키 24시간 유효. 코드 하드코딩 금지. AWS Secrets Manager 또는 환경변수 필수. .env 파일은 .gitignore 필수. 유출 시 10분 내 폐기, Slack #security-alert 즉시 보고. 보안팀 승인 SLA 2 영업일. 담당: 보안팀 이민준."},
    {"doc_id": "SEC-POL-002", "category": "보안정책",
     "content": "API 키 관리 정책 v2.8 (구버전, 비효력). 모든 키 180일 만료. 팀리드 관리. 현행은 SEC-POL-003 참조."},
    {"doc_id": "REL-CLOUDSYNC-023", "category": "릴리즈노트",
     "content": "CloudSync v2.3 (2024-10-20). 동기화 40% 향상. Breaking: Python 3.10 필수, REST API v1 제거, 설정파일 경로 변경, JWT→OAuth 2.0. 대용량 파일 버그 수정. 담당: 클라우드플랫폼팀 김도현."},
    {"doc_id": "REL-CLOUDSYNC-022", "category": "릴리즈노트",
     "content": "CloudSync v2.2 (2024-07-15). 선택적 동기화, 오프라인 모드. 버전 히스토리 30일. API v1 deprecated 예고."},
    {"doc_id": "REL-DATAPULSE-011", "category": "릴리즈노트",
     "content": "DataPulse v1.1 (2024-09-05). Kafka 커넥터, Slack 알림 추가. 설정 JSON→YAML. 최소 메모리 1GB. 담당: 데이터인프라팀 최서연."},
    {"doc_id": "WFH-POL-001", "category": "HR정책",
     "content": "원격 근무 정책 v2.0. 주 3일 사무실 2일 재택. VPN 필수. 해외 원격 연 30일 한도. 장비: 노트북, 주변기기 연 50만원, 인터넷 월 3만원. 코어타임 10~16시."},
    {"doc_id": "ONBOARD-ENG-001", "category": "프로세스",
     "content": "개발자 온보딩. 1주차: 노트북, GitHub, 보안교육 2시간. 2주차: 코드베이스 세션, 첫 PR. 3~4주차: 독립 기능 구현, 30일 체크인."},
    {"doc_id": "MTG-2024Q3-STRATEGY", "category": "회의록",
     "content": "Q3 전략 회의 (2024-07-02). CloudSync v2.3 10월, DataPulse v1.1 9월, 보안정책 v3.1 11월 확정. ML 엔지니어 2명 채용 결정."},
    {"doc_id": "MTG-2024-SEC-REVIEW", "category": "회의록",
     "content": "보안정책 개정 회의 (2024-09-15). v2.8 문제: 180일 과다, 대응 불명확. v3.1 개선: 키 단축, 승인 프로세스, 10분 내 폐기 의무. 시행 2024-11-01."},
    {"doc_id": "FAQ-DATAPULSE-001", "category": "FAQ",
     "content": "DataPulse FAQ. v1.0→v1.1 업그레이드 데이터 손실 없음. 최소 메모리 1GB. Slack 알림: config.yaml webhook_url 추가. 보관 기간 기본 30일, 최대 365일."},
    {"doc_id": "FAQ-SECURITY-001", "category": "FAQ",
     "content": "보안정책 FAQ v3.1. 기존 키는 10월 일괄 감사 후 새 정책 적용. Vault, GCP Secret Manager도 지원. .env git 유출 시: 10분 내 키 폐기, #security-alert 보고."},
    {"doc_id": "PROC-DEPLOY-001", "category": "프로세스",
     "content": "운영 배포 체크리스트. 배포 전: 테스트, 코드리뷰 2명, 보안스캔, QA, 롤백계획. 권장 시간 화~목. 에러율 5% 초과 즉시 롤백."},
    {"doc_id": "PROC-INCIDENT-001", "category": "프로세스",
     "content": "인시던트 대응. P0 전체 다운 30분 내 CTO 보고. P1 핵심 장애 1시간. P0/P1 48시간 내 포스트모템. 롤백 에러율 5% 초과."},
]
MOCK_LLM_ONLY = {
    "api_policy": """API 키 유효기간은 일반적으로 보안 정책에 따라 다르지만,
보통 6개월에서 1년 정도로 설정하는 것이 일반적입니다.
정확한 내용은 사내 보안 정책 문서를 확인하거나
보안팀에 문의하시기 바랍니다.""",
    "cloudsync_v23": """CloudSync v2.3의 업그레이드 방법은 공식 문서를 통해
확인하실 수 있습니다. 일반적으로 기존 설정을 백업하고
새 버전을 설치하면 됩니다.""",
    "wfh": """재택근무 정책은 회사마다 다르며, 일반적으로 팀장 승인이
필요합니다. 구체적인 내용은 HR팀에 문의하세요."""
}

MOCK_RAG_RESPONSE = {
    "api_policy": """현행 API 키 관리 정책 (SEC-POL-003 v3.1, 2024-11-01 시행) 기준:

• 개발용 키: 90일 자동 만료
• 운영용 키: 365일 자동 만료 (60일 전 갱신 알림)
• 긴급 키: 발급 후 24시간 내 폐기 의무

※ 주의: 구버전 v2.8에는 '모든 키 180일'로 되어 있으나 현재 비효력입니다.

[참고: SEC-POL-003]""",
    "cloudsync_v23": """CloudSync v2.2에서 v2.3으로 업그레이드 시 반드시 확인할 사항:

⚠️ Breaking Changes:
1. Python SDK 최소 버전: 3.8 → 3.10 (반드시 업그레이드)
2. REST API v1 완전 제거 → v2 마이그레이션 필요
3. 설정 파일 경로 변경: ~/.cloudsync/config → ~/.config/cloudsync/config.yaml
4. 인증 방식 변경: JWT → OAuth 2.0 Bearer Token

마이그레이션 스크립트: scripts/migrate_v23.sh
[참고: REL-CLOUDSYNC-023]""",
    "wfh": """원격 근무 정책 v2.0 (2024-09-01 시행) 기준:

• 기본 형태: 주 3일 사무실 / 2일 재택 (하이브리드)
• 코어타임: 오전 10시 ~ 오후 4시 온라인 필수
• 인터넷 최소 50Mbps, VPN 필수
• 장비 지원: 노트북 1대 + 주변기기 연 50만원 + 인터넷 월 3만원
• 해외 원격: 연 30일 한도, HR팀 사전 승인 필수

[참고: WFH-POL-001]"""
}

# ========================================================================
# 05_better_rag_hybrid_and_rerank
# ========================================================================
SAMPLE_DOCS_05 = [
    # 키워드 검색이 중요한 문서들 (정확한 버전/코드)
    {"doc_id": "REL-CLOUDSYNC-023", "category": "릴리즈노트",
     "content": "CloudSync v2.3 릴리즈. Breaking Changes: Python 3.10 필수. REST API v1 완전 제거. OAuth 2.0 Bearer Token으로 인증 방식 변경. 설정 파일 경로: ~/.config/cloudsync/config.yaml. 동기화 속도 40% 향상."},
    {"doc_id": "REL-CLOUDSYNC-022", "category": "릴리즈노트",
     "content": "CloudSync v2.2 릴리즈. 선택적 동기화 추가. API v1 deprecated 예고 (v2.3에서 제거). 버전 히스토리 30일 제공."},
    {"doc_id": "REL-DATAPULSE-011", "category": "릴리즈노트",
     "content": "DataPulse v1.1 릴리즈. Kafka 0.11+ 네이티브 커넥터. Slack webhook 알림. JSON→YAML 설정 전환. 메모리 최소 1GB 필요."},
    # 의미 검색이 중요한 문서들 (정책/개념)
    {"doc_id": "SEC-POL-003", "category": "보안정책",
     "content": "API 키 보안 관리 정책 v3.1. 시크릿은 코드에 절대 저장하지 마세요. 환경변수 또는 전용 비밀 관리 도구를 사용하세요. 키 노출 시 즉시 폐기하고 보안팀에 보고하세요."},
    {"doc_id": "SEC-POL-002", "category": "보안정책",
     "content": "API 키 관리 구버전(v2.8). 모든 키 180일 만료. 현재 비효력. 현행은 SEC-POL-003 참조."},
    {"doc_id": "WFH-POL-001", "category": "HR정책",
     "content": "재택 근무 정책. 주 3일 사무실, 2일 원격 근무. 인터넷 50Mbps 이상. VPN 필수. 해외 근무 연 30일 한도. 장비: 노트북, 주변기기 50만원, 인터넷 3만원/월."},
    {"doc_id": "ONBOARD-ENG-001", "category": "프로세스",
     "content": "신규 개발자 온보딩 가이드. 1주차: 계정 생성, 보안 교육. 2주차: 코드베이스 학습, 첫 PR 제출. 3-4주차: 독립 작업 시작."},
    {"doc_id": "MTG-2024Q3-STRATEGY", "category": "회의록",
     "content": "Q3 전략 회의록. CloudSync v2.3 10월 출시, DataPulse v1.1 9월 출시, 보안정책 v3.1 11월 시행. 시니어 백엔드 3명, ML 엔지니어 2명 채용."},
    {"doc_id": "FAQ-DATAPULSE-001", "category": "FAQ",
     "content": "DataPulse FAQ. v1.1 최소 메모리 1GB. Slack 알림 설정 방법: config.yaml에 webhook_url 추가. 데이터 보관 기본 30일 최대 365일."},
    {"doc_id": "FAQ-SECURITY-001", "category": "FAQ",
     "content": "보안 FAQ. API 키 유출 시 대응: 10분 내 폐기, Slack #security-alert 보고, 7일 내 보고서. Vault, GCP Secret Manager도 공식 도구."},
    {"doc_id": "PROC-DEPLOY-001", "category": "프로세스",
     "content": "배포 체크리스트. 테스트 통과, 코드리뷰 2명, 보안 스캔. 권장 시간 화~목. 에러율 5% 초과 즉시 롤백. DataPulse 대시보드로 모니터링."},
    {"doc_id": "PROC-INCIDENT-001", "category": "프로세스",
     "content": "서비스 장애 대응 절차. P0 전체 다운: 30분 내 대응, CTO 즉시 보고. P1 핵심 장애: 1시간 내. 장애 후 포스트모템 48시간 내 작성."},
]
TEST_CASES_05 = [
    (
        "CloudSync v2.3 Python 버전 요구사항",
        ["REL-CLOUDSYNC-023"]
    ),
    (
        "API 시크릿을 안전하게 보관하는 올바른 방법",
        ["SEC-POL-003", "FAQ-SECURITY-001"]
    ),
    (
        "DataPulse 최신 버전 Kafka 및 Slack 설정 가이드",
        ["REL-DATAPULSE-011", "FAQ-DATAPULSE-001"]
    ),
]
# ========================================================================
# 06_agentic_search_or_tool_use
# ========================================================================
RELEASE_NOTES = {
    "CloudSync": {
        "v2.3": "CloudSync v2.3 (2024-10-20): 동기화 40% 향상. Breaking: Python 3.10 필수, REST API v1 제거, JWT→OAuth 2.0 인증 변경. 마이그레이션 스크립트: migrate_v23.sh",
        "v2.2": "CloudSync v2.2 (2024-07-15): 선택적 동기화, 오프라인 모드. API v1 deprecated 예고.",
        "latest": "v2.3"
    },
    "DataPulse": {
        "v1.1": "DataPulse v1.1 (2024-09-05): Kafka 0.11+ 커넥터. Slack webhook 알림. JSON→YAML 설정. 메모리 최소 1GB.",
        "v1.0": "DataPulse v1.0 (2024-03-01): 초기 릴리즈. 기본 모니터링 기능.",
        "latest": "v1.1"
    }
}

# 정책 DB
POLICIES = {
    "API 키 관리": "[SEC-POL-003 v3.1 현행] 개발키 90일, 운영키 365일, 긴급키 24시간. 하드코딩 금지, Secrets Manager 사용. 유출 시 10분 내 폐기, #security-alert 보고.",
    "보안": "[SEC-POL-003] API 키: 개발 90일, 운영 365일. 유출 시 즉시 폐기. AWS Secrets Manager 또는 Vault 사용.",
    "원격근무": "[WFH-POL-001] 주 3일 사무실 2일 재택. VPN 필수. 장비: 노트북, 주변기기 50만원, 인터넷 3만원/월.",
    "배포": "[PROC-DEPLOY-001] 코드리뷰 2명, 보안스캔, QA 완료 후 배포. 에러율 5% 초과 즉시 롤백.",
    "인시던트": "[PROC-INCIDENT-001] P0 30분 내 CTO 보고, P1 1시간, P2 4시간. P0/P1 48시간 내 포스트모템.",
}

# 문서 벡터 DB (03, 04, 05 노트북의 확장)
SAMPLE_DOCS_06 = [
    {"doc_id": "SEC-POL-003", "category": "보안정책", "content": "API 키 관리 정책 v3.1. 개발키 90일, 운영키 365일, 긴급키 24시간. 하드코딩 금지. Secrets Manager 필수. 유출 10분 내 폐기."},
    {"doc_id": "REL-CLOUDSYNC-023", "category": "릴리즈노트", "content": "CloudSync v2.3. Breaking: Python 3.10, API v1 제거, OAuth 2.0 전환. 동기화 40% 향상."},
    {"doc_id": "REL-DATAPULSE-011", "category": "릴리즈노트", "content": "DataPulse v1.1. Kafka 커넥터, Slack 알림, YAML 설정, 메모리 1GB."},
    {"doc_id": "MTG-2024Q3-STRATEGY", "category": "회의록", "content": "Q3 전략 회의. CloudSync v2.3 10월, DataPulse v1.1 9월, 보안정책 v3.1 11월 확정."},
    {"doc_id": "MTG-2024-SEC-REVIEW", "category": "회의록", "content": "보안정책 개정 회의. v2.8→v3.1 개선. 키 유효기간 단축, 승인 프로세스 추가, 시행일 2024-11-01."},
    {"doc_id": "FAQ-DATAPULSE-001", "category": "FAQ", "content": "DataPulse FAQ. 업그레이드 데이터 손실 없음. 메모리 1GB. Slack: config.yaml webhook_url."},
    {"doc_id": "FAQ-SECURITY-001", "category": "FAQ", "content": "보안 FAQ. 유출 시: 10분 폐기, 보고, git 히스토리 제거, 7일 내 보고서."},
    {"doc_id": "PROC-DEPLOY-001", "category": "프로세스", "content": "배포 체크리스트. 테스트, 코드리뷰 2명, 보안스캔. 에러율 5% 초과 롤백."},
]

MOCK_AGENTIC_ANSWER_1 = """[보안 정책 v3.1 변경 사항과 CloudSync v2.3 배포 일정 통합 정리]

=== 보안 정책 v3.1 (2024-11-01 시행) ===
주요 변경:
• API 키 유효기간 단축: 전 버전(v2.8)의 '모든 키 180일'에서 개발 90일/운영 365일/긴급 24시간으로 세분화
• 유출 대응 강화: 10분 내 폐기 의무, Slack #security-alert 즉시 보고
• 보안팀 승인 프로세스 추가 (SLA 2 영업일)
[출처: SEC-POL-003, MTG-2024-SEC-REVIEW]

=== CloudSync v2.3 배포 정보 ===
• 출시일: 2024년 10월 20일 (Q3 전략 회의에서 10월로 확정)
• 주요 Breaking Changes:
  - Python 3.10 최소 버전 요구
  - REST API v1 완전 제거 → v2 마이그레이션 필요
  - JWT → OAuth 2.0 인증 방식 변경
[출처: REL-CLOUDSYNC-023, MTG-2024Q3-STRATEGY]

=== 주의 사항 ===
두 변경이 거의 동시에 적용됨 (CloudSync v2.3: 10월, 보안정책 v3.1: 11월).
기존 API 키를 사용하는 CloudSync 연동 스크립트는 두 가지 변경을 모두 반영해야 합니다."""

# ========================================================================
# 07_graphrag_concept_demo
# ========================================================================
ENTITIES = {
    # 사람
    "이민준": {"type": "person", "role": "보안팀", "desc": "보안팀 담당자, CISO 직속"},
    "김도현": {"type": "person", "role": "클라우드플랫폼팀 리드", "desc": "CloudSync 개발팀 리드"},
    "최서연": {"type": "person", "role": "데이터인프라팀 리드", "desc": "DataPulse 개발팀 리드"},
    "송재원": {"type": "person", "role": "CTO", "desc": "기술 최고 책임자"},
    "장유진": {"type": "person", "role": "PM", "desc": "제품팀 프로덕트 매니저"},
    "강하늘": {"type": "person", "role": "HR팀", "desc": "HR 담당자, 채용/온보딩 관리"},

    # 문서/정책
    "SEC-POL-003": {"type": "document", "category": "보안정책",
                    "desc": "API 키 관리 정책 v3.1 (현행)"},
    "SEC-POL-002": {"type": "document", "category": "보안정책",
                    "desc": "API 키 관리 정책 v2.8 (구버전)"},
    "REL-CLOUDSYNC-023": {"type": "document", "category": "릴리즈노트",
                           "desc": "CloudSync v2.3 릴리즈 노트"},
    "REL-DATAPULSE-011": {"type": "document", "category": "릴리즈노트",
                           "desc": "DataPulse v1.1 릴리즈 노트"},
    "MTG-2024Q3": {"type": "document", "category": "회의록",
                   "desc": "2024년 Q3 전략 회의록"},
    "MTG-SEC-REVIEW": {"type": "document", "category": "회의록",
                       "desc": "보안 정책 개정 검토 회의록"},

    # 제품
    "CloudSync": {"type": "product", "desc": "파일 동기화 서비스"},
    "DataPulse": {"type": "product", "desc": "데이터 파이프라인 모니터링 서비스"},

    # 이슈/변경사항
    "API-키-정책-강화": {"type": "issue", "desc": "API 키 유효기간 단축 및 관리 절차 강화"},
    "CloudSync-v2.3-출시": {"type": "issue", "desc": "CloudSync v2.3 릴리즈 및 마이그레이션"},
    "DataPulse-v1.1-출시": {"type": "issue", "desc": "DataPulse v1.1 릴리즈"},
    "ML-엔지니어-채용": {"type": "issue", "desc": "ML 엔지니어 2명 채용 진행"},
}

# ──────────────────────────────────────────────────
# 관계(엣지) 정의
# ──────────────────────────────────────────────────

RELATIONS = [
    # 사람 → 문서 담당
    ("이민준", "SEC-POL-003", "담당"),
    ("이민준", "SEC-POL-002", "구버전_담당"),
    ("이민준", "MTG-SEC-REVIEW", "주도"),
    ("김도현", "REL-CLOUDSYNC-023", "담당"),
    ("김도현", "MTG-2024Q3", "참석"),
    ("최서연", "REL-DATAPULSE-011", "담당"),
    ("최서연", "MTG-2024Q3", "참석"),
    ("송재원", "MTG-2024Q3", "주재"),
    ("송재원", "MTG-SEC-REVIEW", "참석"),
    ("장유진", "MTG-2024Q3", "참석"),
    ("강하늘", "ML-엔지니어-채용", "담당"),

    # 문서 → 이슈 연결
    ("SEC-POL-003", "API-키-정책-강화", "구현"),
    ("MTG-SEC-REVIEW", "API-키-정책-강화", "결정"),
    ("REL-CLOUDSYNC-023", "CloudSync-v2.3-출시", "기록"),
    ("MTG-2024Q3", "CloudSync-v2.3-출시", "결정"),
    ("REL-DATAPULSE-011", "DataPulse-v1.1-출시", "기록"),
    ("MTG-2024Q3", "DataPulse-v1.1-출시", "결정"),
    ("MTG-2024Q3", "ML-엔지니어-채용", "결정"),

    # 이슈 → 제품 영향
    ("API-키-정책-강화", "CloudSync", "영향"),
    ("API-키-정책-강화", "DataPulse", "영향"),
    ("CloudSync-v2.3-출시", "CloudSync", "업데이트"),
    ("DataPulse-v1.1-출시", "DataPulse", "업데이트"),

    # 문서 간 관계
    ("SEC-POL-002", "SEC-POL-003", "개정됨"),
    ("REL-CLOUDSYNC-023", "SEC-POL-003", "참조"),  # CloudSync v2.3이 OAuth 2.0 = 보안정책 반영
]

# ──────────────────────────────────────────────────
# networkx 그래프 구성
# ──────────────────────────────────────────────────

