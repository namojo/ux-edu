# AI 하네스로 UX를 바꾸다 — CX/UX 팀 하네스 바이브코딩 교육

코딩 경험이 없는 CX/UX 실무자가 **[revfactory/harness](https://github.com/revfactory/harness)** 로
자기 업무의 에이전트 팀을 **말로 구성하고(바이브코딩), 실행하고, 진화시키는** 사람이 되도록 만드는 교육 프로그램입니다.

**🌐 교육 사이트: https://namojo.github.io/ux-edu/**

핵심 도구는 revfactory/harness입니다 — Claude Code 대화창에 `하네스 구성해줘: {원하는 팀 설명}`을 입력하면
전문 에이전트 팀(`.claude/agents/`)과 작업 방법(`.claude/skills/`)이 자동 생성되고, 오케스트레이터 트리거 한 문장으로
팀이 일합니다. **구축 1회, 실행 반복** — 이 구조를 UX 실무(리서치·VoC·페르소나·MVP)에 이식하는 것이 이 교육의 전부입니다.

---

## 교육 프로그램 (반나절 워크샵 × 3회, 6개 모듈)

각 모듈 90분(도입 ≤30분 / 실습 ≥45분 / 정리 15분). 상세 설계는 [교육 설계서](content/program/curriculum.md) 참조.

### 1회차 — L1 · 첫 대화, 첫 하네스

| 모듈 | 학습 목표 | 제공 자료 |
|------|----------|----------|
| **01. Claude Code 열고 하네스 설치까지** | Claude Code를 켜 파일을 다루고, `/plugin marketplace add revfactory/harness` → `/plugin install harness@harness-marketplace`로 하네스 플러그인을 설치한다 | [실습 가이드](content/program/modules/first-contact/guide.md) · [핸드아웃](content/program/modules/first-contact/handout.md) · [강사용 슬라이드](content/program/modules/first-contact/slides-outline.md) · [샘플 데이터](content/program/modules/first-contact/sample-reviews.txt) |
| **02. 하네스 구성해줘 — 내 손으로 만든 첫 팀** | 자연어 한 문단으로 첫 미니 VoC 팀을 구성·실행하고, 팀에 검증 담당이 있는 구조(Producer-Reviewer)를 이해한다. **첫날 안에 "내가 팀을 만들었다"에 도달** | [실습 가이드](content/program/modules/first-harness/guide.md) · [핸드아웃](content/program/modules/first-harness/handout.md) · [강사용 슬라이드](content/program/modules/first-harness/slides-outline.md) |

### 2회차 — L2 · 내 업무를 팀에게

| 모듈 | 학습 목표 | 제공 자료 |
|------|----------|----------|
| **03. VoC 분석 팀을 만들어 내 리뷰 돌리기** | 자기 서비스의 리뷰·CS 티켓·설문으로 VoC 분석 팀(수집→분류→검증→리포트 Pipeline)을 구성·실행하고, 검증 담당의 결과를 사람이 최종 확인한다 | [실습 가이드](content/program/modules/voc-team/guide.md) · [워크시트](content/program/modules/voc-team/worksheet.md) |
| **04. 리서치 종합 팀 → 페르소나 팀 잇기** | 두 하네스를 연결해 자기 인터뷰 데이터에서 근거(참가자 번호)가 달린 페르소나·저니맵 초안까지 만든다 | [실습 가이드](content/program/modules/research-persona-team/guide.md) · [워크시트](content/program/modules/research-persona-team/worksheet.md) |

### 3회차 — L2+L3 · 시제품, 그리고 팀 설계자

| 모듈 | 학습 목표 | 제공 자료 |
|------|----------|----------|
| **05. MVP 팀으로 클릭되는 시제품 만들기** | 구현자+검수자 팀을 구성해 자기 아이디어를 클릭 가능한 HTML MVP로 만든다 ([완성 예시](content/mvp-example/) 체험 포함) | [실습 가이드](content/program/modules/mvp-team/guide.md) · [핸드아웃](content/program/modules/mvp-team/handout.md) |
| **06. 내 반복 업무를 팀 구조로 직접 설계·진화** | "반복 업무 → 역할 분해 캔버스"로 자기 업무를 팀 구조(역할·검증 단계·트리거)로 설계해 구성하고, "하네스 회고" 피드백으로 진화시킨다. [harness-100](https://github.com/revfactory/harness-100)을 출발점 대안으로 소개 | [실습 가이드](content/program/modules/design-my-harness/guide.md) · [워크시트: 역할 분해 캔버스](content/program/modules/design-my-harness/worksheet.md) · [강사용 슬라이드](content/program/modules/design-my-harness/slides-outline.md) |

## 사례집 — 바로 구성할 수 있는 10개의 팀

모든 사례가 같은 뼈대를 따릅니다: **⓪ 하네스 설치 → ① 데이터 준비 → ② 팀 구성("하네스 구성해줘: …") →
③ 팀 실행 → ④ 팀 진화("하네스 회고: …")** + "꼭 사람이 확인하세요" + "하네스가 과한 경우"(1회성 판단 기준).

| 팀 | 패턴 | 이런 반복 업무에 |
|------|------|------------------|
| [리서치 종합 팀](content/usecases/research-synthesis.md) | Pipeline | 분기마다 인터뷰 녹취 더미를 인사이트로 종합 |
| [페르소나 팀](content/usecases/persona-journey.md) | Producer-Reviewer | 근거 검증 담당을 둔 페르소나·저니맵 생성 |
| [사용성 테스트 분석 팀](content/usecases/usability-analysis.md) | Pipeline | 라운드마다 세션 노트 → 이슈·심각도 리포트 |
| [VoC 분석 팀](content/usecases/voc-mining.md) | Pipeline | 분기마다 리뷰·CS 티켓에서 개선 기회 도출 |
| [카피 팀](content/usecases/ux-writing.md) | Producer-Reviewer | 시안 생성과 톤 검수 분리 |
| [IA 검토 팀](content/usecases/ia-review.md) | Pipeline + P-R | 개편마다 진단→대안→평가 반복 |
| [벤치마킹 팀](content/usecases/competitor-bench.md) | Fan-out/Fan-in | 경쟁 서비스 병렬 조사 → 비교표 |
| [MVP 프로토타입 팀](content/usecases/mvp-prototype.md) | Producer-Reviewer | 구현·검수 팀으로 시제품 반복 검증 |
| [접근성 팀](content/usecases/a11y-audit.md) | Pipeline | 릴리스마다 접근성 점검 |
| [문서화 팀](content/usecases/design-system-doc.md) | Fan-out/Fan-in | 수십 개 컴포넌트에 같은 문서 형식 적용 |

## 실제 산출물

- **[클릭되는 MVP 시제품](https://namojo.github.io/ux-edu/mvp-example/index.html)** — MVP 팀이 만드는 것과 같은 종류의 산출물
- **[1회차 핸드아웃](https://namojo.github.io/ux-edu/modules/first-contact/handout.html)** — 설치 명령·첫 실행 함정 치트시트
- **[역할 분해 캔버스](https://namojo.github.io/ux-edu/modules/design-my-harness/worksheet.html)** — 반복 업무 → 팀 구조 설계 워크시트

## 제작 과정 (이 저장소 자체가 하네스 산출물입니다)

이 교육 자료 전체가 revfactory/harness 방법론 기반의 **UX 인에이블먼트 하네스**로 생산되었습니다:
사례 작성 에이전트 → 전문 검수 에이전트(비개발자 눈높이·실행 가능성·정직성) → 수정 반영의 생성-검증
파이프라인이 워크플로우로 돌아 사례 10편과 6개 모듈 자료가 모두 검수를 통과했습니다.
"교육이 가르치는 방식 그대로 교육이 만들어졌다" — 3회차 design-my-harness 모듈에서 이 구조를 직접 다룹니다.

## 저장소 구조 & 빌드

```
content/
  program/     교육 설계서 + 모듈 6개 자료 (가이드·워크시트·핸드아웃·슬라이드 개요)
  usecases/    하네스 활용 사례집 10편
  mvp-example/ 완성 MVP 시제품
assets/        디자인 시스템 (CSS/JS/SVG 일러스트)
build.py       정적 사이트 빌더
docs/          빌드 결과 — GitHub Pages 서빙 (main /docs)
```

```bash
python3 build.py   # content/ + assets/ → docs/
```
