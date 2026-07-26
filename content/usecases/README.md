# CX/UX 팀 하네스 활용 사례집

코딩 경험이 없어도 따라 할 수 있는, **revfactory/harness로 에이전트 팀을 구성해 UX 업무를 처리하는** 사례 10편입니다.
모든 사례는 같은 뼈대를 따릅니다: **⓪ 하네스 설치 → ① 데이터 준비 → ② 팀 구성(바이브코딩) → ③ 팀 실행 → ④ 팀 진화** —
그리고 "꼭 사람이 확인하세요"와 "하네스가 과한 경우"(1회성이면 팀 없이 프롬프트로)의 정직한 판단 기준을 포함합니다.

> 생성: 2026-07-26 (v2 — revfactory/harness 바이브코딩 중심 개편), UX 인에이블먼트 하네스 (작성 → 전문 검수 → 수정 반영 완료)

## 추천 학습 순서

1. **[VoC 분석 팀](voc-mining.md)** — "구축 1회, 분기마다 실행"의 대표 사례. 첫 하네스로 가장 좋습니다
2. **[리서치 종합 팀](research-synthesis.md)** → **[페르소나 팀](persona-journey.md)** — 두 하네스를 이어 붙이는 파이프라인
3. **[MVP 프로토타입 팀](mvp-prototype.md)** — 구현·검수 팀을 부려 클릭되는 시제품 만들기

## 전체 사례 목록

| 사례 | 팀 패턴 | 난이도 | 이런 반복 업무에 |
|------|---------|--------|------------------|
| [리서치 종합 팀](research-synthesis.md) | Pipeline | 중급 | 분기마다 인터뷰 녹취 더미를 인사이트로 종합할 때 |
| [페르소나 팀](persona-journey.md) | Producer-Reviewer | 중급 | 근거 없는 페르소나를 걸러내며 페르소나·저니맵을 만들 때 |
| [사용성 테스트 분석 팀](usability-analysis.md) | Pipeline | 중급 | 라운드마다 세션 노트를 이슈·심각도 리포트로 만들 때 |
| [VoC 분석 팀](voc-mining.md) | Pipeline | 중급 | 분기마다 리뷰·CS 티켓에서 개선 기회를 뽑을 때 |
| [카피 팀](ux-writing.md) | Producer-Reviewer | 중급 | 마이크로카피 시안 생성과 톤 검수를 분리해 돌릴 때 |
| [IA 검토 팀](ia-review.md) | Pipeline + P-R | 중급 | 개편 프로젝트마다 진단→대안→평가를 반복할 때 |
| [벤치마킹 팀](competitor-bench.md) | Fan-out/Fan-in | 중급 | 경쟁 서비스 여럿을 병렬 조사해 비교표로 만들 때 |
| [MVP 프로토타입 팀](mvp-prototype.md) | Producer-Reviewer | 중급 | 아이디어를 클릭되는 시제품으로 반복 검증할 때 |
| [접근성 팀](a11y-audit.md) | Pipeline | 중급 | 릴리스마다 화면 접근성을 점검할 때 |
| [문서화 팀](design-system-doc.md) | Fan-out/Fan-in | 중급 | 수십 개 컴포넌트에 같은 문서 형식을 적용할 때 |

## 함께 보기

- **revfactory/harness**: https://github.com/revfactory/harness — 설치·트리거는 각 사례 0단계에 동일하게 안내
- **harness-100**: https://github.com/revfactory/harness-100 — 10개 도메인 100개 기성 팀 하네스 (출발점으로 활용)
- **완성 MVP 예시**: `../mvp/onboarding-smoke/` — MVP 팀이 만드는 것과 같은 종류의 산출물
- **교육 프로그램**: `../education/` — 이 사례집을 실습 교재로 쓰는 3레벨 워크샵 시리즈

## 알려진 개선점

- 사례 속 설치 안내는 revfactory/harness 공개 저장소 기준입니다 — 사내 프록시·권한 환경이 다르면 운영 가이드에서 보완하세요
- 하네스가 생성하는 팀 구성은 세션마다 조금씩 다를 수 있습니다(사례의 팀 미리보기는 대표 예시) — 이 점은 각 사례 2단계에 안내되어 있습니다
