/* 히어로 타이핑 데모 + 프롬프트 복사 + 목차 하이라이트 */
(function () {
  // 1) 히어로 타이핑 데모 — 교육의 약속을 3초로 보여준다
  var demo = document.getElementById("typing-demo");
  if (demo) {
    var promptText = "reviews.txt 읽고 자주 나오는 불만을 표로 정리해줘";
    var replyLines = [
      "reviews.txt (리뷰 120건)를 읽었습니다.",
      "",
      "| 순위 | 주제           | 건수 |",
      "|------|----------------|------|",
      "| 1    | 결제·쿠폰 오류 | 34건 |",
      "| 2    | 배송 지연      | 27건 |",
      "| 3    | 로그인 불편    | 19건 |",
    ];
    var inEl = demo.querySelector(".in");
    var outEl = demo.querySelector(".out");
    var caret = demo.querySelector(".caret");
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    if (reduce) {
      inEl.textContent = promptText;
      outEl.textContent = replyLines.join("\n");
    } else {
      var i = 0;
      var typeIn = function () {
        if (i <= promptText.length) {
          inEl.textContent = promptText.slice(0, i);
          i += 1;
          setTimeout(typeIn, 46);
        } else {
          setTimeout(showOut, 500);
        }
      };
      var j = 0;
      var showOut = function () {
        if (j < replyLines.length) {
          outEl.textContent += (j ? "\n" : "") + replyLines[j];
          j += 1;
          setTimeout(showOut, 170);
        } else {
          caret.style.display = "none";
          setTimeout(function () {
            inEl.textContent = "";
            outEl.textContent = "";
            caret.style.display = "";
            i = 0; j = 0;
            setTimeout(typeIn, 1400);
          }, 5200);
        }
      };
      setTimeout(typeIn, 700);
    }
  }

  // 2) 프롬프트 카드 복사 버튼
  document.querySelectorAll(".prompt-card").forEach(function (card) {
    var btn = card.querySelector(".copy-btn");
    var pre = card.querySelector("pre");
    if (!btn || !pre) return;
    btn.addEventListener("click", function () {
      navigator.clipboard.writeText(pre.textContent).then(function () {
        var old = btn.textContent;
        btn.textContent = "복사됨!";
        setTimeout(function () { btn.textContent = old; }, 1600);
      });
    });
  });

  // 3) 목차 현재 위치 하이라이트
  var tocLinks = document.querySelectorAll(".toc a[href^='#']");
  if (tocLinks.length) {
    var map = {};
    tocLinks.forEach(function (a) {
      var id = decodeURIComponent(a.getAttribute("href").slice(1));
      var h = document.getElementById(id);
      if (h) map[id] = a;
    });
    var obs = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting && map[e.target.id]) {
            tocLinks.forEach(function (a) { a.classList.remove("on"); });
            map[e.target.id].classList.add("on");
          }
        });
      },
      { rootMargin: "-10% 0px -75% 0px" }
    );
    Object.keys(map).forEach(function (id) {
      obs.observe(document.getElementById(id));
    });
  }
})();
