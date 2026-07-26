# CX/UX 팀 하네스 바이브코딩 교육 — 말로 팀을 만들어 내 업무를 시키는 사람 되기

코딩 경험이 없는 CX/UX 팀원을 **revfactory/harness로 자기 업무의 에이전트 팀을 구성·실행·진화시키는 사람**으로
만드는 **반나절 워크샵 × 3회 시리즈**입니다. 상세 설계는 [curriculum.md](curriculum.md)를 보세요.

> 생성: 2026-07-26 (v2 — revfactory/harness 바이브코딩 중심 개편), UX 인에이블먼트 하네스 (설계 → 제작 → 전문 검수 → 수정 반영 완료)

## 회차 구성

| 회차 | 레벨 | 모듈 (각 90분) | 학습자가 가져가는 것 |
|------|------|---------------|---------------------|
| 1회차 | L1 | [first-contact](modules/first-contact/) + [first-harness](modules/first-harness/) | **첫날 내 손으로 구성한 첫 하네스 팀** |
| 2회차 | L2 | [voc-team](modules/voc-team/) + [research-persona-team](modules/research-persona-team/) | 내 데이터로 돌린 VoC 팀 + 리서치→페르소나 파이프라인 |
| 3회차 | L2+L3 | [mvp-team](modules/mvp-team/) + [design-my-harness](modules/design-my-harness/) | 클릭되는 MVP + 실행되는 나만의 하네스 |

각 모듈 폴더의 자료: `guide.md`(실습 가이드 — 학습자 배포), `handout.md`(치트시트 — 인쇄 배포),
`worksheet.md`(실습 중 기입), `slides-outline.md`(강사용 슬라이드 개요).

## 운영 전 준비 체크리스트

- [ ] **설치 선결**: 참가자 전원 Claude Code 설치+로그인 완료 (revfactory/harness 플러그인 설치는 1회차 first-contact에서 다 함께 진행)
- [ ] **네트워크 사전 점검**: 교육망에서 `/plugin marketplace add revfactory/harness`가 동작하는지 강사가 리허설 (방화벽 환경이면 대안 준비)
- [ ] **데이터 지참 안내**: 2회차부터 자기 프로젝트의 실데이터(익명화된 리뷰·인터뷰) 지참 — 사전 공지 필수
- [ ] **인원·TA**: 회당 8~12명, 강사 1 + 실습 보조 1 (설치·터미널에서 막힌 사람 즉시 지원)
- [ ] **실습 교재 배포**: `usecases/` 사례집(각 사례의 2단계가 곧 팀 구성 프롬프트)과 `mvp/onboarding-smoke/` 예시 공유
- [ ] 1회차 공용 샘플: [modules/first-contact/sample-reviews.txt](modules/first-contact/sample-reviews.txt) 배포

## 효과 측정

- 평가는 시험이 아니라 **산출물 리뷰** — L2 이후는 "구성된 하네스 + 실행 결과"가 평가 대상 (성공 기준은 curriculum.md 모듈별 명세)
- 종료 설문 3문항: ① 이번 주 실무에 하네스를 쓸 것인가 ② 가장 유용한 사례는 ③ 막힌 지점은 — ③은 "하네스 회고" 요청으로 이 하네스 개선에 반영하세요

## 알려진 개선점 (검수 잔여 minor 권고)

- 하네스가 생성하는 팀 구성·실행 문구는 세션마다 조금씩 다릅니다 — 자료 전반에 안내되어 있으나, 강사는 사전 리허설로 자기 환경의 실제 출력을 확인해 두기를 권장
- 사내 프록시/방화벽 환경의 플러그인 설치 대안은 조직 환경 확정 후 first-contact 가이드에 보완 필요
