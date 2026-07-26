# 월요일 아침에 바로 쓰는 AI — CX/UX 팀 교육

코딩 경험이 없는 CX/UX 실무자를 위한 Claude Code 실무 활용 워크샵 시리즈.

**🌐 웹사이트: https://namojo.github.io/ux-edu/**

## 구성

- **교육 프로그램** — 반나절 워크샵 × 3회 (L1 첫 대화 → L2 내 업무에 붙이기 → L3 나만의 하네스), 6개 모듈
- **활용 사례집 10편** — 리서치 종합, 페르소나, 사용성 테스트 분석, VoC 분석, UX 라이팅, IA 검토, 경쟁 벤치마킹, MVP, 접근성, 디자인 시스템
- **완성 MVP 예시** — 클릭되는 카페 온보딩 시제품

## 저장소 구조

```
content/   교육 콘텐츠 원본 (마크다운)
  program/   커리큘럼 + 모듈별 자료 (실습 가이드·워크시트·핸드아웃·슬라이드 개요)
  usecases/  활용 사례집 10편
assets/    디자인 시스템 (CSS/JS/이미지)
build.py   정적 사이트 빌더 (content → docs)
docs/      빌드 결과 — GitHub Pages 서빙 (main /docs)
```

## 빌드

```bash
python3 build.py   # content/ + assets/ → docs/
```

콘텐츠를 수정하려면 `content/`의 마크다운을 고치고 다시 빌드하세요.

---

UX 인에이블먼트 하네스([revfactory/harness](https://github.com/revfactory/harness) 방법론 기반)로 제작되었습니다.
