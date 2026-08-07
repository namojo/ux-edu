# CX/UX 팀 하네스 바이브코딩 교육 — 말로 팀을 만들어 내 업무를 시키는 사람 되기

코딩 경험이 없는 CX/UX 팀원이 **revfactory/harness로 자기 업무의 에이전트 팀을 구성·실행·진화시키는 사람**이
되도록 만드는 **자가 학습형 6모듈 프로그램**입니다. 모든 가이드는 혼자 화면만 보고 따라갈 수 있게 쓰여 있으며,
팀 단위 그룹 스터디로 운영해도 됩니다. 상세 설계는 [curriculum.md](curriculum.md)를 보세요.

> 생성: 2026-07-26 (v2 — revfactory/harness 바이브코딩 중심), UX 인에이블먼트 하네스 (설계 → 제작 → 전문 검수 → 수정 반영 완료)

## 학습 경로

| 단계 | 레벨 | 모듈 (각 약 90분) | 가져가는 것 |
|------|------|-------------------|-------------|
| 1 | L1 | [first-contact](modules/first-contact/) → [first-harness](modules/first-harness/) | **첫날 내 손으로 구성한 첫 하네스 팀** |
| 2 | L2 | [voc-team](modules/voc-team/) → [research-persona-team](modules/research-persona-team/) | 내 데이터로 돌린 VoC 팀 + 리서치→페르소나 파이프라인 |
| 3 | L2+L3 | [mvp-team](modules/mvp-team/) → [design-my-harness](modules/design-my-harness/) | 클릭되는 MVP + 실행되는 나만의 하네스 |

각 모듈 폴더의 자료: `guide.md`(실습 가이드 — 혼자 따라 하는 본문), `handout.md`(치트시트),
`worksheet.md`(실습 중 기입).

## 시작 전 준비

- [ ] Claude Code 설치 + 로그인 (사내 설치 가이드 참조)
- [ ] revfactory/harness 플러그인 설치 — [first-contact](modules/first-contact/guide.md)에서 안내 (전 과정에서 한 번만)
- [ ] 2단계(L2)부터는 자기 프로젝트의 실데이터(익명화된 리뷰·인터뷰) 준비 — 없으면 아래 대체 데이터로 진행
- [ ] 실습 교재: `usecases/` 사례집(각 사례의 2단계가 곧 팀 구성 프롬프트)과 완성 MVP 예시 [`../mvp-example/`](../mvp-example/index.html)
- [ ] 모듈별 실습 데이터 (전부 가상 데이터 · 사이트 자료실에서도 개별 다운로드 가능)
  - L1 공용 샘플: [modules/first-contact/sample-reviews.txt](modules/first-contact/sample-reviews.txt) (리뷰 20건)
  - `voc-team`: [sample-reviews-appstore.txt](modules/voc-team/sample-reviews-appstore.txt) (리뷰 60건·별점 있음) · [sample-tickets-cs.txt](modules/voc-team/sample-tickets-cs.txt) (CS 티켓 25건·별점 없음) · [sample-prev-quarter-report.md](modules/voc-team/sample-prev-quarter-report.md) (전 분기 리포트)
  - `research-persona-team`: [sample-interview-p1.txt](modules/research-persona-team/sample-interview-p1.txt) ~ [p6.txt](modules/research-persona-team/sample-interview-p6.txt) (인터뷰 6건)
  - `mvp-team`: [sample-idea.md](modules/mvp-team/sample-idea.md) (준비물 대체용) · [sample-idea-onboarding.md](modules/mvp-team/sample-idea-onboarding.md) (완성 예시의 입력 메모)
  - `design-my-harness`: [sample-usability-notes.txt](modules/design-my-harness/sample-usability-notes.txt) (세션 노트 6건)

## 완료 기준

- 평가는 시험이 아니라 **산출물** — 각 모듈의 성공 기준(구성한 하네스 + 실행 결과)은 curriculum.md 모듈별 명세 참조
- 전 과정을 마치면: 스스로 3문항을 점검하세요 — ① 이번 주 실무에 하네스를 쓸 것인가 ② 가장 유용했던 사례는 ③ 막힌 지점은 — ③은 "하네스 회고" 요청으로 이 하네스 개선에 반영할 수 있습니다

## 알려진 개선점

- 하네스가 생성하는 팀 구성·실행 문구는 세션마다 조금씩 다릅니다 — 자료 전반에 "이렇게 나오면 정상입니다"로 안내되어 있습니다
- 사내 프록시/방화벽 환경의 플러그인 설치 대안은 조직 환경 확정 후 first-contact 가이드에 보완이 필요합니다
