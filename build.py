#!/usr/bin/env python3
"""ux-edu 정적 사이트 빌더 — content/*.md → site/*.html"""
import os, re, shutil, html
import markdown
from markdown.extensions.toc import TocExtension, slugify_unicode

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, "content")
SITE = os.path.join(ROOT, "docs")  # GitHub Pages: main 브랜치 /docs 서빙

# ---------------- 메타데이터 ----------------
SESSIONS = [
    {"no": "1회차", "level": "L1", "badge": "l1", "img": "session-l1.svg",
     "title": "첫 대화, 첫 하네스", "modules": ["first-contact", "first-harness"],
     "desc": "Claude Code와 첫 대화를 나누고, 하네스를 설치해 그날 바로 첫 에이전트 팀을 구성해 본다.",
     "take": "가져가는 것 — 내 손으로 구성한 첫 하네스 팀"},
    {"no": "2회차", "level": "L2", "badge": "l2", "img": "session-l2.svg",
     "title": "내 업무를 팀에게", "modules": ["voc-team", "research-persona-team"],
     "desc": "자기 서비스의 진짜 데이터(VoC·인터뷰)로 분석 팀을 구성·실행하고, 검증 담당의 결과를 확인한다.",
     "take": "가져가는 것 — 내 데이터로 돌린 VoC 팀 + 페르소나 파이프라인"},
    {"no": "3회차", "level": "L2+L3", "badge": "l3", "img": "session-l3.svg",
     "title": "시제품, 그리고 팀 설계자", "modules": ["mvp-team", "design-my-harness"],
     "desc": "MVP 팀으로 시제품을 만들고, 자기 반복 업무를 역할 분해해 하네스로 직접 설계·진화시킨다.",
     "take": "가져가는 것 — 클릭되는 MVP + 실행되는 나만의 하네스"},
]

MODULES = {
    "first-contact":     {"title": "Claude Code 열고 하네스 설치까지", "level": "L1", "badge": "l1", "dur": "90분",
                          "desc": "Claude Code를 켜 파일을 다루고, revfactory/harness 플러그인을 설치한다."},
    "first-harness":     {"title": "하네스 구성해줘 — 내 손으로 만든 첫 팀", "level": "L1", "badge": "l1", "dur": "90분",
                          "desc": "자연어로 첫 하네스를 구성·실행하고, 팀에 검증 담당이 있는 구조를 이해한다."},
    "voc-team":          {"title": "VoC 분석 팀을 만들어 내 리뷰 돌리기", "level": "L2", "badge": "l2", "dur": "90분",
                          "desc": "자기 VoC 데이터로 분석 팀을 구성·실행하고 검증 결과를 사람이 확인한다."},
    "research-persona-team": {"title": "리서치 종합 팀 → 페르소나 팀 잇기", "level": "L2", "badge": "l2", "dur": "90분",
                          "desc": "두 하네스를 연결해 자기 인터뷰에서 페르소나·저니맵 초안까지 만든다."},
    "mvp-team":          {"title": "MVP 팀으로 클릭되는 시제품 만들기", "level": "L2", "badge": "l2", "dur": "90분",
                          "desc": "구현·검수 팀을 구성해 자기 아이디어를 클릭 가능한 HTML MVP로 만든다."},
    "design-my-harness": {"title": "내 반복 업무를 팀 구조로 직접 설계·진화", "level": "L3", "badge": "l3", "dur": "90분+과제",
                          "desc": "반복 업무를 역할 분해·검증 단계로 직접 설계해 구성하고, 실행 결과로 진화시킨다."},
}
MODULE_ORDER = list(MODULES.keys())

MATERIAL_LABEL = {"guide": "실습 가이드", "worksheet": "워크시트", "handout": "핸드아웃",
                  "slides-outline": "강사용 슬라이드 개요", "sample-reviews": "샘플 데이터"}

CASES = {
    "research-synthesis": ("리서치 종합 팀", "리서치", "분기마다 인터뷰 녹취 더미를 인사이트로 종합할 때"),
    "persona-journey":    ("페르소나 팀", "리서치", "근거 검증 담당을 둔 팀으로 페르소나·저니맵을 만들 때"),
    "usability-analysis": ("사용성 테스트 분석 팀", "평가", "라운드마다 세션 노트를 이슈·심각도 리포트로 만들 때"),
    "voc-mining":         ("VoC 분석 팀", "CX", "분기마다 리뷰·CS 티켓에서 개선 기회를 뽑을 때"),
    "ux-writing":         ("카피 팀", "라이팅", "시안 생성과 톤 검수를 분리한 팀으로 돌릴 때"),
    "ia-review":          ("IA 검토 팀", "설계", "개편마다 진단→대안→평가를 반복할 때"),
    "competitor-bench":   ("벤치마킹 팀", "리서치", "경쟁 서비스 여럿을 병렬 조사해 비교표로 만들 때"),
    "mvp-prototype":      ("MVP 프로토타입 팀", "프로토타이핑", "구현·검수 팀을 부려 시제품을 반복 검증할 때"),
    "a11y-audit":         ("접근성 팀", "평가", "릴리스마다 화면 접근성을 점검할 때"),
    "design-system-doc":  ("문서화 팀", "시스템", "수십 개 컴포넌트에 같은 문서 형식을 적용할 때"),
}
CASE_ORDER = list(CASES.keys())

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Hahmlet:wght@500;600;700&family=Gaegu:wght@400;700&family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">'
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">'
)
FAVICON = ('<link rel="icon" href="data:image/svg+xml,'
           '%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22%3E'
           '%3Crect x=%2210%22 y=%2210%22 width=%2280%22 height=%2280%22 rx=%2218%22 fill=%22%23FFE455%22/%3E'
           '%3Ctext x=%2250%22 y=%2268%22 font-size=%2252%22 text-anchor=%22middle%22 font-family=%22monospace%22 fill=%22%2322242A%22%3E%E2%80%BA%3C/text%3E%3C/svg%3E">')

SITE_URL = "https://namojo.github.io/ux-edu"

# ---------------- 마크다운 렌더 ----------------
def md_render(text):
    mdp = markdown.Markdown(extensions=[
        "tables", "fenced_code", "sane_lists",
        TocExtension(slugify=slugify_unicode, separator="-", toc_depth="2-3"),
    ])
    return mdp.convert(text), mdp.toc_tokens

def postprocess(body, root):
    # 코드블록 → 친근한 터미널 프롬프트 카드
    def to_card(m):
        code = m.group(1)
        return ('<div class="prompt-card"><div class="terminal">'
                '<div class="terminal-bar"><i></i><i></i><i></i>'
                '<span>복사해서 쓰세요</span><button class="copy-btn" type="button">복사</button></div>'
                f'<div class="terminal-body"><pre>{code}</pre></div></div></div>')
    body = re.sub(r'<pre><code[^>]*>(.*?)</code></pre>', to_card, body, flags=re.S)
    # 방어: 블록쿼트 등에서 펜스가 인라인 code로 붕괴된 경우(개행 포함 인라인 코드) → 줄바꿈 보존 블록 표시
    body = re.sub(r'<code>([^<]*\n[^<]*)</code>', r'<code class="block">\1</code>', body)
    # ⚠️ 블록쿼트 → warn
    body = re.sub(r'<blockquote>(\s*<p>[^<]{0,12}(?:⚠️|주의:|개인정보 주의))',
                  r'<blockquote class="warn">\1', body)
    # "꼭 사람이 확인하세요" 섹션 → 포스트잇 래핑 (h2 + 다음 리스트/문단 묶음)
    body = re.sub(
        r'(<h2 id="[^"]*">꼭 사람이 확인하세요</h2>)(.*?)(?=<h2 |<div class="pager"|$)',
        r'<div class="human-check">\1\2</div>', body, flags=re.S)
    # 내부 링크 매핑
    body = re.sub(r'href="(?:\.\./)*(?:usecases/)?setup\.md"', rf'href="{root}setup.html"', body)
    body = re.sub(r'href="(?:\.\./)*usecases/([a-z0-9-]+)\.md"', rf'href="{root}cases/\1.html"', body)
    body = re.sub(r'href="\.\./mvp/onboarding-smoke/?[^"]*"', rf'href="{root}mvp-example/index.html"', body)
    body = re.sub(r'href="mvp/onboarding-smoke/?[^"]*"', rf'href="{root}mvp-example/index.html"', body)
    body = re.sub(r'href="modules/([a-z0-9-]+)/?"', rf'href="{root}modules/\1/index.html"', body)
    body = re.sub(r'href="curriculum\.md"', rf'href="{root}curriculum.html"', body)
    body = re.sub(r'href="(worksheet|handout|guide|slides-outline)\.md"', r'href="\1.html"', body)
    body = body.replace('href="slides-outline.html"', 'href="slides.html"')
    body = re.sub(r'href="([a-z0-9-]+)\.md"',
                  lambda m: f'href="{m.group(1)}.html"' if m.group(1) in CASES else m.group(0), body)
    # 코드 스팬으로 적힌 사례 경로도 클릭 가능하게
    body = re.sub(r'<code>(?:usecases/)?([a-z0-9-]+)\.md</code>',
                  lambda m: (f'<a href="{root}cases/{m.group(1)}.html"><code>{m.group(1)}.md</code></a>'
                             if m.group(1) in CASES else m.group(0)), body)
    return body

# ---------------- 페이지 셸 ----------------
def nav(root, current):
    items = [("index", "홈", "index.html"), ("curriculum", "커리큘럼", "curriculum.html"),
             ("modules", "모듈", "index.html#modules"), ("cases", "사례집", "index.html#cases"),
             ("setup", "설치", "setup.html")]
    links = "".join(
        f'<a href="{root}{href}"{" aria-current=page" if key == current else ""}>{label}</a>'
        for key, label, href in items)
    return (f'<header class="topnav"><div class="wrap">'
            f'<a class="brand" href="{root}index.html"><span class="dot"></span>UX × AI 하네스</a>'
            f'<nav>{links}</nav></div></header>')

def shell(*, root, current, title, desc, body, og_img=None):
    og = og_img or f"{SITE_URL}/assets/img/hero.svg"
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{og}">
<meta property="og:type" content="website">
{FAVICON}
{FONTS}
<link rel="stylesheet" href="{root}assets/style.css">
</head>
<body>
{nav(root, current)}
{body}
<footer><div class="wrap">
  <div>사내 CX/UX 팀 교육 프로그램 · <span style="font-family:var(--font-hand);font-size:17px">코딩 없이, 한국어 문장으로.</span></div>
  <div><a href="https://github.com/namojo/ux-edu">GitHub</a> · UX 인에이블먼트 하네스로 제작</div>
</div></footer>
<script src="{root}assets/site.js"></script>
</body>
</html>"""

def toc_html(tokens):
    if not tokens:
        return ""
    links = "".join(f'<a href="#{t["id"]}">{html.escape(t["name"])}</a>' for t in tokens if t["level"] == 2)
    return f'<div class="side-box toc"><h4>목차</h4>{links}</div>' if links else ""

def strip_h1(md_text):
    lines = md_text.split("\n")
    title = None
    out = []
    for ln in lines:
        if title is None and ln.startswith("# "):
            title = ln[2:].strip()
            continue
        out.append(ln)
    return title, "\n".join(out)

# ---------------- 개별 페이지 빌드 ----------------
def write(path, htm):
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(htm)

def content_page(md_path, out_path, *, root, current, eyebrow, meta_html="", side_extra="", pager=""):
    raw = open(md_path, encoding="utf-8").read()
    title, rest = strip_h1(raw)
    body_html, toc = md_render(rest)
    body_html = postprocess(body_html, root)
    side = side_extra + toc_html(toc)
    layout_cls = "layout" if side else "layout single"
    aside = f'<aside class="side">{side}</aside>' if side else ""
    page = f"""
<div class="wrap page-head">
  <div class="eyebrow">{eyebrow}</div>
  <h1>{html.escape(title or "")}</h1>
  <div class="meta">{meta_html}</div>
</div>
<div class="wrap {layout_cls}">
  <article class="prose">{body_html}{pager}</article>
  {aside}
</div>"""
    write(out_path, shell(root=root, current=current, title=f"{title} — AI 하네스로 UX를 바꾸다",
                          desc=(eyebrow + " · " + (title or "")), body=page))

def build_modules():
    for idx, slug in enumerate(MODULE_ORDER):
        m = MODULES[slug]
        srcdir = os.path.join(CONTENT, "program", "modules", slug)
        files = set(os.listdir(srcdir))
        # 자료 사이드박스
        mats = []
        if "worksheet.md" in files: mats.append(('worksheet.html', '📝 워크시트'))
        if "handout.md" in files or "handout.html" in files: mats.append(('handout.html', '📄 핸드아웃'))
        if "sample-reviews.txt" in files: mats.append(('sample-reviews.txt', '💾 샘플 데이터'))
        matbox = ('<div class="side-box"><h4>이 모듈의 자료</h4>'
                  + f'<a href="index.html" class="on">📘 실습 가이드</a>'
                  + "".join(f'<a href="{h}">{t}</a>' for h, t in mats) + "</div>")
        # 이전/다음
        pager_items = []
        if idx > 0:
            p = MODULE_ORDER[idx-1]
            pager_items.append(f'<a href="../{p}/index.html"><span class="dir">← 이전 모듈</span><b>{MODULES[p]["title"]}</b></a>')
        if idx < len(MODULE_ORDER) - 1:
            n = MODULE_ORDER[idx+1]
            pager_items.append(f'<a class="next" href="../{n}/index.html"><span class="dir">다음 모듈 →</span><b>{MODULES[n]["title"]}</b></a>')
        pager = f'<div class="pager">{"".join(pager_items)}</div>'
        meta = (f'<span class="badge {m["badge"]}">{m["level"]}</span>'
                f'<span>⏱ {m["dur"]}</span><span>모듈 {idx+1} / {len(MODULE_ORDER)}</span>')
        content_page(os.path.join(srcdir, "guide.md"), f"modules/{slug}/index.html",
                     root="../../", current="modules", eyebrow=f"모듈 {idx+1} · 실습 가이드",
                     meta_html=meta, side_extra=matbox, pager=pager)
        # 부속 자료 페이지
        sub_side = matbox.replace('href="index.html" class="on"', 'href="index.html"')
        if "worksheet.md" in files:
            content_page(os.path.join(srcdir, "worksheet.md"), f"modules/{slug}/worksheet.html",
                         root="../../", current="modules", eyebrow=f"{m['title']} · 워크시트",
                         meta_html='<button class="copy-btn" onclick="window.print()" type="button">🖨 인쇄하기</button>',
                         side_extra=sub_side.replace('📝 워크시트</a>', '📝 워크시트 (현재)</a>'))
        if "handout.md" in files:
            content_page(os.path.join(srcdir, "handout.md"), f"modules/{slug}/handout.html",
                         root="../../", current="modules", eyebrow=f"{m['title']} · 핸드아웃",
                         meta_html='<button class="copy-btn" onclick="window.print()" type="button">🖨 인쇄하기</button>',
                         side_extra=sub_side)
        elif "handout.html" in files:
            shutil.copy(os.path.join(srcdir, "handout.html"), os.path.join(SITE, f"modules/{slug}/handout.html"))
        if "sample-reviews.txt" in files:
            shutil.copy(os.path.join(srcdir, "sample-reviews.txt"), os.path.join(SITE, f"modules/{slug}/sample-reviews.txt"))

def build_cases():
    for idx, slug in enumerate(CASE_ORDER):
        title, area, desc = CASES[slug]
        prev_nxt = []
        if idx > 0:
            p = CASE_ORDER[idx-1]
            prev_nxt.append(f'<a href="{p}.html"><span class="dir">← 이전 사례</span><b>{CASES[p][0]}</b></a>')
        if idx < len(CASE_ORDER) - 1:
            n = CASE_ORDER[idx+1]
            prev_nxt.append(f'<a class="next" href="{n}.html"><span class="dir">다음 사례 →</span><b>{CASES[n][0]}</b></a>')
        pager = f'<div class="pager">{"".join(prev_nxt)}</div>'
        content_page(os.path.join(CONTENT, "usecases", f"{slug}.md"), f"cases/{slug}.html",
                     root="../", current="cases", eyebrow=f"활용 사례 · {area}",
                     meta_html=f'<span class="badge l2">따라 하기</span><span>{desc}</span>', pager=pager)

def build_index():
    session_cards = ""
    for s in SESSIONS:
        mods = "".join(
            f'<a href="modules/{m}/index.html" style="font-size:14px;display:block;padding:3px 0">'
            f'· {MODULES[m]["title"]}</a>' for m in s["modules"])
        session_cards += f"""
<div class="session-card">
  <img src="assets/img/{s['img']}" alt="{s['title']} 일러스트">
  <div class="pad">
    <div><span class="badge {s['badge']}">{s['level']}</span>
      <span class="eyebrow" style="display:inline;margin-left:8px">{s['no']}</span></div>
    <h3>{s['title']}</h3>
    <p>{s['desc']}</p>
    <div>{mods}</div>
    <div class="take"><b>{s['take']}</b></div>
  </div>
</div>"""
    module_rows = ""
    for i, slug in enumerate(MODULE_ORDER):
        m = MODULES[slug]
        module_rows += f"""
<a class="module-row" href="modules/{slug}/index.html">
  <span class="no">{i+1:02d}</span>
  <span><span class="badge {m['badge']}">{m['level']}</span>
    <h3>{m['title']}</h3><p>{m['desc']}</p>
    <span class="mats">⏱ {m['dur']}</span></span>
</a>"""
    case_cards = ""
    for slug in CASE_ORDER:
        title, area, desc = CASES[slug]
        case_cards += f"""
<a class="case-card" href="cases/{slug}.html">
  <span class="area">{area}</span><h3>{title}</h3><p>{desc}</p>
</a>"""
    body = f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <div class="eyebrow">CX/UX 팀 교육 프로그램 · 워크샵 시리즈</div>
    <h1>AI 하네스로,<br><span class="hl">UX가 일하는 방식</span>을 바꿉니다.</h1>
    <p class="lead">인터뷰 녹취 정리부터 클릭되는 시제품까지 — 반복 작업은 역할이 나뉜
    AI 에이전트 팀(하네스)에게 맡기고, UX 전문가는 <strong>판단과 발견</strong>에 집중합니다.
    이 교육은 도구 사용법이 아니라 일하는 방식의 전환을 다룹니다. 코딩은 필요 없습니다.</p>
    <div>
      <a class="btn btn-primary" href="modules/first-contact/index.html">지금 시작하기</a>
      <a class="btn btn-ghost" href="curriculum.html">커리큘럼 보기</a>
    </div>
  </div>
  <div>
    <div class="terminal" id="typing-demo" aria-label="Claude Code 사용 예시 데모">
      <div class="terminal-bar"><i></i><i></i><i></i><span>claude</span></div>
      <div class="terminal-body"><div class="in"></div><span class="caret"></span>
      <div class="out" style="margin-top:10px"></div></div>
    </div>
    <div class="hand-note">↑ 진짜로 이게 전부예요</div>
  </div>
</div></section>

<section class="block alt" id="sessions"><div class="wrap">
  <h2 class="sec">전환 로드맵 — 도구에서, 팀으로</h2>
  <p class="sec-sub">AI에게 말을 거는 것(L1)에서 출발해, 자기 실무 데이터를 다루고(L2),
  마지막에는 반복 업무를 AI 팀으로 설계(L3)하는 데까지 갑니다. 목적지는 도구 사용이 아니라
  <strong>업무 구조의 재설계</strong>입니다.</p>
  <div class="sessions">{session_cards}</div>
</div></section>

<section class="block" id="modules"><div class="wrap">
  <h2 class="sec">6개 모듈</h2>
  <p class="sec-sub">각 90분, 핸즈온 50% 이상. 첫날 안에 첫 하네스를 구성하고, 마지막 모듈에서는
  자기 반복 업무의 팀을 직접 설계합니다. 막히기 쉬운 곳마다 "이렇게 나오면 정상입니다" 안내가 있습니다.</p>
  <div class="modules">{module_rows}</div>
</div></section>

<section class="block alt" id="cases"><div class="wrap">
  <h2 class="sec">사례집 — 바로 구성할 수 있는 10개의 팀</h2>
  <p class="sec-sub">모든 사례가 같은 뼈대를 따릅니다 — 하네스 설치 → <b>"하네스 구성해줘"</b>(팀 구성 프롬프트)
  → 팀 실행 → 피드백으로 팀 진화. 복사해 쓰는 구성 프롬프트와 "꼭 사람이 확인하세요" 체크 포함.
  처음이라면 <a href="setup.html"><b>하네스 설치 (처음 한 번만, 2분)</b></a>부터.</p>
  <div class="cases">{case_cards}</div>
</div></section>

<section class="block" id="deliverables"><div class="wrap">
  <h2 class="sec">실제 산출물 — 말이 아니라 결과로</h2>
  <p class="sec-sub">이 프로그램이 약속하는 것을 미리 확인하세요. 아래는 전부 이 하네스가
  실제로 만들어 낸 것들입니다 — 여러분이 교육에서 만들게 될 것과 같은 종류입니다.</p>
  <div class="cases">
    <a class="case-card" href="mvp-example/index.html">
      <span class="area">MVP 시제품</span><h3>📱 클릭되는 카페 온보딩 앱</h3>
      <p>코드 한 줄 없이 프롬프트로 만든 4화면 시제품. 지금 바로 클릭해 보세요.</p></a>
    <a class="case-card" href="modules/first-contact/handout.html">
      <span class="area">교육 자료</span><h3>📄 1회차 핸드아웃 실물</h3>
      <p>책상에 두고 보는 치트시트 — 터미널 여는 법부터 권한 창 대응까지 한 장.</p></a>
    <a class="case-card" href="modules/design-my-harness/worksheet.html">
      <span class="area">워크시트</span><h3>📝 하네스 설계 캔버스</h3>
      <p>3회차에서 자기 반복 업무를 AI 팀으로 분해할 때 쓰는 실제 양식.</p></a>
    <a class="case-card" href="modules/first-contact/sample-reviews.txt">
      <span class="area">실습 데이터</span><h3>💾 1회차 샘플 데이터</h3>
      <p>첫 실습에서 AI에게 읽히는 리뷰 20건 — 다운로드해 그대로 따라 할 수 있습니다.</p></a>
    <a class="case-card" href="cases/voc-mining.html">
      <span class="area">사례 실물</span><h3>🔍 VoC 분석 사례 전문</h3>
      <p>프롬프트 원문과 기대 결과, 검증 체크까지 — 사례집의 대표 사례.</p></a>
    <a class="case-card" href="https://github.com/namojo/ux-edu/tree/main/content">
      <span class="area">GitHub</span><h3>🗂 콘텐츠 원본 저장소</h3>
      <p>모든 교육 자료의 마크다운 원본과 빌드 과정을 공개합니다.</p></a>
  </div>
</div></section>

<section class="block alt"><div class="wrap" style="display:grid;grid-template-columns:1fr 1fr;gap:22px" id="extra">
  <a class="module-row" href="setup.html" style="align-items:center">
    <span style="font-size:28px">⚙️</span>
    <span><h3>하네스 설치 (처음 한 번만)</h3>
    <p>모든 사례·모듈의 공통 준비물 — 2분이면 끝납니다.</p></span>
  </a>
  <a class="module-row" href="curriculum.html" style="align-items:center">
    <span style="font-size:28px">🧭</span>
    <span><h3>교육 설계서 전문</h3>
    <p>레벨 체계, 모듈별 학습 목표·시간 배분·성공 기준.</p></span>
  </a>
</div></section>"""
    write("index.html", shell(root="", current="index",
        title="AI 하네스로 UX를 바꾸다 — CX/UX 팀 교육",
        desc="반복 작업은 AI 에이전트 팀(하네스)에게, UX 전문가는 판단과 발견에. CX/UX 실무자를 위한 워크샵 시리즈 — 사례집 10편, 6개 모듈, 실제 산출물 공개.",
        body=body))

def build_setup():
    content_page(os.path.join(CONTENT, "usecases", "setup.md"), "setup.html",
                 root="", current="setup", eyebrow="시작하기 · 처음 한 번만",
                 meta_html='<span class="badge l1">약 2분</span><span>설치는 전체 사례집·교육에서 딱 한 번입니다</span>')

def build_top_pages():
    content_page(os.path.join(CONTENT, "program", "curriculum.md"), "curriculum.html",
                 root="", current="curriculum", eyebrow="교육 설계서",
                 meta_html='<span class="badge l1">L1</span><span class="badge l2">L2</span><span class="badge l3">L3</span><span>반나절 × 3회 시리즈</span>')

def main():
    if os.path.exists(SITE):
        shutil.rmtree(SITE)
    os.makedirs(SITE)
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(SITE, "assets"))
    shutil.copytree(os.path.join(CONTENT, "mvp-example"), os.path.join(SITE, "mvp-example"))
    build_index()
    build_setup()
    build_top_pages()
    build_modules()
    build_cases()
    n = sum(len(fs) for _, _, fs in os.walk(SITE))
    print(f"OK — site/ 아래 {n}개 파일 생성")

if __name__ == "__main__":
    main()
