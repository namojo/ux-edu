# AI 하네스로 UX를 바꾸다 — CX/UX 팀 교육

코딩 경험이 없는 CX/UX 실무자가 **AI 에이전트 팀(하네스)** 을 실무에 적용하도록 만드는 교육 프로그램입니다.
목적지는 도구 사용법이 아니라 **일하는 방식의 전환**입니다 — 반복 작업은 AI 팀에게, UX 전문가는 판단과 발견에.

**🌐 교육 사이트: https://namojo.github.io/ux-edu/**

---

## 교육 프로그램 (반나절 워크샵 × 3회, 6개 모듈)

각 모듈은 90분(도입·시연 ≤30분 / 실습 ≥45분 / 공유·정리 15분)이며, 학습자는 연습용 예제가 아니라
**자기 실무의 초안**을 만들어 갑니다. 상세 설계는 [교육 설계서](content/program/curriculum.md) 참조.

### 1회차 — L1 · AI와 첫 대화

| 모듈 | 학습 목표 | 제공 자료 |
|------|----------|----------|
| **01. AI에게 내 파일을 맡기는 첫 경험** | 터미널을 열고, 작업 폴더로 이동해 Claude Code를 켜고, 파일을 읽혀 첫 결과를 받는 전 과정을 혼자 해낸다. 로그인·폴더 신뢰·권한 창 등 첫 실행의 함정을 모두 다룬다 | [실습 가이드](content/program/modules/first-contact/guide.md) · [핸드아웃](content/program/modules/first-contact/handout.html) · [강사용 슬라이드 개요](content/program/modules/first-contact/slides-outline.md) · [샘플 데이터](content/program/modules/first-contact/sample-reviews.txt) |
| **02. 좋은 요청과 결과 검증 — 함정 피하기** | 후속 프롬프트로 결과를 다듬고, 환각(AI가 지어낸 인용)과 개인정보 노출을 스스로 검증한다. "사람이 먼저 마스킹"이 기본 원칙임을 체득한다 | [실습 가이드](content/program/modules/prompt-and-verify/guide.md) · [핸드아웃](content/program/modules/prompt-and-verify/handout.md) · [워크시트](content/program/modules/prompt-and-verify/worksheet.md) |

### 2회차 — L2 · 내 업무에 붙이기

| 모듈 | 학습 목표 | 제공 자료 |
|------|----------|----------|
| **03. 내 VoC 데이터로 개선 기회 뽑기** | 자기 서비스의 리뷰·CS 티켓에서 주제별 분류표와 개선 기회 초안을 만든다. 건수·비율의 한계, 소수 의견 매몰, 인용 검증까지 다룬다 | [실습 가이드](content/program/modules/voc-in-practice/guide.md) · [워크시트](content/program/modules/voc-in-practice/worksheet.md) |
| **04. 내 리서치에서 인사이트·페르소나 만들기** | 자기 인터뷰 데이터를 어피니티 종합 → 근거 참가자 번호가 달린 페르소나·저니맵 초안으로 잇는다. 두 사례를 연결하는 파이프라인 작업 | [실습 가이드](content/program/modules/research-to-persona/guide.md) · [워크시트](content/program/modules/research-to-persona/worksheet.md) |

### 3회차 — L2+L3 · 시제품과 나만의 하네스

| 모듈 | 학습 목표 | 제공 자료 |
|------|----------|----------|
| **05. 내 아이디어를 클릭되는 시제품으로** | 자기 서비스 아이디어를 사용성 테스트에 쓸 수 있는 HTML MVP로 만든다. [완성 예시](content/mvp-example/)를 체험한 뒤 자연어 수정 요청으로 자기 것을 만든다 | [실습 가이드](content/program/modules/mvp-in-practice/guide.md) · [핸드아웃](content/program/modules/mvp-in-practice/handout.md) |
| **06. 반복 업무 하나를 나만의 AI 팀으로** | 반복 업무 1개를 역할(수집·분류·검증·리포트)이 나뉜 에이전트 팀으로 분해 설계한다. 이 저장소를 만든 하네스 자체가 실물 교보재 | [실습 가이드](content/program/modules/my-harness/guide.md) · [워크시트: 역할 분해 캔버스](content/program/modules/my-harness/worksheet.md) · [강사용 슬라이드 개요](content/program/modules/my-harness/slides-outline.md) |

## 활용 사례집 (10편)

교육이 끝난 뒤에도 책상에 두고 쓰는 참조 자산. 모든 사례는 **복사해 쓰는 프롬프트 + 화면 기준 따라 하기
+ 기대 결과 예시 + "꼭 사람이 확인하세요" 검증 체크**를 포함합니다.

| 사례 | 이런 때 씁니다 |
|------|---------------|
| [사용자 리서치 종합](content/usecases/research-synthesis.md) | 인터뷰 녹취 5건 → 어피니티 그룹핑 + 핵심 인사이트 |
| [페르소나 & 저니맵](content/usecases/persona-journey.md) | 리서치 데이터 → 근거 있는 페르소나 2종 + 저니맵 |
| [사용성 테스트 분석](content/usecases/usability-analysis.md) | 세션 노트 → 이슈 목록 + Nielsen 심각도 우선순위 |
| [VoC/CX 피드백 분석](content/usecases/voc-mining.md) | 리뷰·CS 티켓 수백 건 → 주제 분류 + 개선 기회 |
| [UX 라이팅](content/usecases/ux-writing.md) | 마이크로카피 시안 N종 + 톤앤매너 규칙 대조 검수 |
| [IA·내비게이션 검토](content/usecases/ia-review.md) | 메뉴 구조 → 카드소팅 관점 대안 + 라벨 개선 |
| [경쟁사 UX 벤치마킹](content/usecases/competitor-bench.md) | 경쟁 3사 온보딩 → 비교표 한 장 |
| [MVP 프로토타입](content/usecases/mvp-prototype.md) | 아이디어 → 클릭 가능한 HTML 시제품 (코드 없이) |
| [접근성 점검](content/usecases/a11y-audit.md) | 화면 HTML → WCAG 관점 이슈 + 개선안 |
| [디자인 시스템 문서화](content/usecases/design-system-doc.md) | 컴포넌트 규칙 메모 → 일관된 사용 가이드 |

## 실제 산출물

- **[클릭되는 MVP 시제품](https://namojo.github.io/ux-edu/mvp-example/index.html)** — 프롬프트만으로 만든 카페 온보딩 4화면
- **[1회차 핸드아웃 실물](https://namojo.github.io/ux-edu/modules/first-contact/handout.html)** — 인쇄해서 책상에 두는 치트시트
- **[하네스 설계 캔버스](https://namojo.github.io/ux-edu/modules/my-harness/worksheet.html)** — 반복 업무 → 역할 분해 워크시트

## 제작 과정 (이 저장소 자체가 사례입니다)

이 교육 자료 전체가 [revfactory/harness](https://github.com/revfactory/harness) 방법론 기반의
**UX 인에이블먼트 하네스**로 생산되었습니다: 사례 작성 에이전트 → 전문 검수 에이전트(비개발자 눈높이·실행
가능성·정직성 렌즈) → 수정 반영의 생성-검증 파이프라인을 워크플로우로 돌려, 사례 10편과 모듈 6개 자료가
모두 검수를 통과했습니다. 3회차 my-harness 모듈에서 이 구조를 직접 열어봅니다.

## 저장소 구조 & 빌드

```
content/
  program/     교육 설계서 + 모듈 6개 자료 (실습 가이드·워크시트·핸드아웃·슬라이드 개요)
  usecases/    활용 사례집 10편
  mvp-example/ 완성 MVP 시제품
assets/        디자인 시스템 (CSS/JS/일러스트)
build.py       정적 사이트 빌더
docs/          빌드 결과 — GitHub Pages 서빙 (main /docs)
```

```bash
python3 build.py   # content/ + assets/ → docs/
```

콘텐츠를 수정하려면 `content/`의 마크다운을 고치고 다시 빌드하세요.
