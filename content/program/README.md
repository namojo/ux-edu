# CX/UX 팀 AI 실무 활용 교육 — "월요일 아침에 바로 쓰는 AI"

코딩 경험이 없는 CX/UX 팀원을 대상으로, Claude Code를 실무에 쓰는 사람으로 만드는 **반나절 워크샵 × 3회 시리즈**입니다.
상세 설계는 [curriculum.md](curriculum.md)를 보세요.

> 생성: 2026-07-26, UX 인에이블먼트 하네스 (설계 → 모듈별 제작 → 전문 검수 → 수정 반영 완료)

## 회차 구성

| 회차 | 레벨 | 모듈 (각 90분) | 학습자가 가져가는 것 |
|------|------|---------------|---------------------|
| 1회차 | L1 | [first-contact](modules/first-contact/) + [prompt-and-verify](modules/prompt-and-verify/) | 첫 성공 경험 + 환각·개인정보 검증 습관 |
| 2회차 | L2 | [voc-in-practice](modules/voc-in-practice/) + [research-to-persona](modules/research-to-persona/) | 자기 서비스의 VoC 개선 기회 초안 + 페르소나·저니맵 초안 |
| 3회차 | L2+L3 | [mvp-in-practice](modules/mvp-in-practice/) + [my-harness](modules/my-harness/) | 자기 아이디어의 클릭되는 MVP + 반복 업무의 하네스 설계 캔버스 |

각 모듈 폴더의 자료: `guide.md`(실습 가이드 — 학습자 배포), `handout.*`(치트시트 — 인쇄 배포), `worksheet.md`(실습 중 기입), `slides-outline.md`(강사용 슬라이드 개요).

## 운영 전 준비 체크리스트

- [ ] **설치 선결**: 참가자 전원 Claude Code 설치+로그인 완료 (사내 공통 설치 가이드 링크를 각 자료의 "사내 위키 › AI 도구 › Claude Code 설치" 자리에 치환)
- [ ] **데이터 지참 안내**: 2회차부터 자기 프로젝트의 실데이터(익명화된 인터뷰·리뷰·VoC) 지참 — 사전 공지 필수
- [ ] **인원·TA**: 회당 8~12명, 강사 1 + 실습 보조 1 (비개발자 대상 — 막힌 사람 즉시 지원이 이탈 방지의 핵심)
- [ ] **실습 교재 배포**: `usecases/` 사례집과 `mvp/onboarding-smoke/` 예시를 참가자에게 미리 공유
- [ ] 1회차 공용 샘플: [modules/first-contact/sample-reviews.txt](modules/first-contact/sample-reviews.txt) 배포

## 효과 측정

- 평가는 시험이 아니라 **산출물 리뷰** — 각 모듈의 성공 기준은 curriculum.md 모듈별 명세 참조
- 종료 설문 3문항: ① 이번 주 실무에 쓸 것인가 ② 가장 유용한 사례는 ③ 막힌 지점은 — ③은 "하네스 회고" 요청으로 이 하네스 개선에 반영하세요

## 알려진 개선점 (검수 잔여 minor 권고)

- 자료 곳곳의 "사내 위키 › AI 도구 › Claude Code 설치"는 배포 전 실제 링크로 일괄 치환 필요
- first-contact handout의 "권한 창 ③"은 첫 프롬프트를 보낸 뒤에 뜬다는 시점 안내를 강사가 구두 보완 권장
- curriculum.md의 my-harness 모듈에 도입-실습-정리 시간 배분이 명시되어 있지 않음 (자료는 30/45/15로 제작됨) — 다음 개편 시 설계서에 반영
