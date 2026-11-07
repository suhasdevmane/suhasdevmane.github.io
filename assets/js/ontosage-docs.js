/* OntoSage documentation: small enhancements on top of the GitBook theme.
 *
 *  - wide tables scroll inside a rounded frame
 *  - h2/h3/h4 get a "#" link on hover
 *  - code blocks are labelled with their language
 *  - ```mermaid blocks are drawn as diagrams in the site's colours, light or dark following the
 *    system, with a caption taken from a "%% caption: ..." line and an Expand button
 *
 * Pages load normally (GitBook does not swap pages by script here), so everything runs once.
 */
(function () {
    "use strict";

    var MERMAID_URL = "https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.esm.min.mjs";

    function ready(fn) {
        if (document.readyState === "loading") {
            document.addEventListener("DOMContentLoaded", fn);
        } else {
            fn();
        }
    }

    function section() {
        return document.querySelector(".markdown-section");
    }

    // ── tables ──────────────────────────────────────────────────────────────
    function wrapTables(root) {
        root.querySelectorAll("table").forEach(function (t) {
            if (t.parentElement && t.parentElement.classList.contains("os-table")) return;
            var w = document.createElement("div");
            w.className = "os-table";
            t.parentNode.insertBefore(w, t);
            w.appendChild(t);
        });
    }

    // ── long inline code ────────────────────────────────────────────────────
    // A path or setting name in a narrow table column would otherwise break between any two
    // letters. Break opportunities go after / _ . - instead, and nowhere else.
    function softBreakCode(root) {
        root.querySelectorAll("code").forEach(function (c) {
            if (c.closest("pre") || c.children.length) return;
            var text = c.textContent;
            if (text.length < 16 || !/[\/_.\-]/.test(text)) return;
            c.textContent = "";
            text.replace(/([\/_.\-])/g, "$1\u0001").split("\u0001").forEach(function (part, i) {
                if (!part) return;
                if (i) c.appendChild(document.createElement("wbr"));
                c.appendChild(document.createTextNode(part));
            });
            c.classList.add("os-soft");
        });
    }

    // ── heading anchors ─────────────────────────────────────────────────────
    function addAnchors(root) {
        root.querySelectorAll("h2[id], h3[id], h4[id]").forEach(function (h) {
            if (h.closest(".os-hero") || h.closest(".os-cards-head") || h.querySelector(".os-anchor")) return;
            var a = document.createElement("a");
            a.className = "os-anchor";
            a.href = "#" + h.id;
            a.setAttribute("aria-label", "Link to this section");
            a.textContent = "#";
            h.insertBefore(a, h.firstChild);
        });
    }

    // ── code language labels ────────────────────────────────────────────────
    var LANG_NAMES = {
        bash: "bash", sh: "shell", shell: "shell", console: "console", powershell: "powershell",
        yaml: "yaml", yml: "yaml", json: "json", python: "python", py: "python", sql: "sql",
        sparql: "sparql", turtle: "turtle", ttl: "turtle", html: "html", xml: "xml", ini: "ini",
        env: "env", dotenv: "env", text: "text", plaintext: "text", js: "javascript",
        javascript: "javascript", http: "http", toml: "toml", dockerfile: "dockerfile", csv: "csv"
    };
    function labelCode(root) {
        root.querySelectorAll("div.highlighter-rouge").forEach(function (d) {
            var m = (d.className || "").match(/language-([\w-]+)/);
            if (!m || m[1] === "mermaid") return;
            var name = LANG_NAMES[m[1].toLowerCase()];
            if (name) d.setAttribute("data-lang", name);
        });
    }

    // ── diagrams ────────────────────────────────────────────────────────────
    function isDark() {
        return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
    }

    function themeVariables(dark) {
        var font = "Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif";
        if (dark) {
            return Object.assign({
                darkMode: true, fontFamily: font, fontSize: "14px", background: "transparent",
                primaryColor: "#15264a", primaryBorderColor: "#5a8bff", primaryTextColor: "#e6eeff",
                secondaryColor: "#0c2a3f", secondaryBorderColor: "#38bdf8", secondaryTextColor: "#e0f2fe",
                tertiaryColor: "#111c31", tertiaryBorderColor: "#2c4066", tertiaryTextColor: "#d3ddef",
                mainBkg: "#15264a", nodeBorder: "#5a8bff", nodeTextColor: "#e6eeff", textColor: "#d3ddef",
                lineColor: "#7d8db0", clusterBkg: "rgba(17,28,49,.85)", clusterBorder: "#2c4066", titleColor: "#eaf0fb",
                edgeLabelBackground: "#0f1830",
                actorBkg: "#15264a", actorBorder: "#5a8bff", actorTextColor: "#e6eeff", actorLineColor: "#41557d",
                signalColor: "#a6b6d1", signalTextColor: "#d3ddef", labelBoxBkgColor: "#15264a",
                labelBoxBorderColor: "#5a8bff", labelTextColor: "#e6eeff", loopTextColor: "#d3ddef",
                noteBkgColor: "#33240b", noteBorderColor: "#fbbf24", noteTextColor: "#fef3c7",
                activationBkgColor: "#1e3366", activationBorderColor: "#5a8bff", sequenceNumberColor: "#0b1220",
                labelColor: "#d3ddef", altBackground: "#0f1830", compositeBackground: "#111c31",
                compositeTitleBackground: "#15264a", stateLabelColor: "#e6eeff", transitionColor: "#7d8db0",
                cScale0: "#15264a", cScale1: "#0c2a3f", cScale2: "#251a46", cScale3: "#0d2e26", cScale4: "#33240b"
            }, scales(DARK_SCALE));
        }
        return Object.assign({
            darkMode: false, fontFamily: font, fontSize: "14px", background: "transparent",
            primaryColor: "#eef4ff", primaryBorderColor: "#2563eb", primaryTextColor: "#0f1b2d",
            secondaryColor: "#e0f2fe", secondaryBorderColor: "#0284c7", secondaryTextColor: "#0c4a6e",
            tertiaryColor: "#f8fafd", tertiaryBorderColor: "#d1dae8", tertiaryTextColor: "#26354d",
            mainBkg: "#eef4ff", nodeBorder: "#2563eb", nodeTextColor: "#0f1b2d", textColor: "#26354d",
            lineColor: "#64748b", clusterBkg: "rgba(246,248,252,.9)", clusterBorder: "#d1dae8", titleColor: "#0f1b2d",
            edgeLabelBackground: "#ffffff",
            actorBkg: "#eef4ff", actorBorder: "#2563eb", actorTextColor: "#0f1b2d", actorLineColor: "#94a3b8",
            signalColor: "#475569", signalTextColor: "#26354d", labelBoxBkgColor: "#eef4ff",
            labelBoxBorderColor: "#2563eb", labelTextColor: "#0f1b2d", loopTextColor: "#26354d",
            noteBkgColor: "#fffbeb", noteBorderColor: "#d97706", noteTextColor: "#78350f",
            activationBkgColor: "#dbe7ff", activationBorderColor: "#2563eb", sequenceNumberColor: "#ffffff",
            labelColor: "#26354d", altBackground: "#f6f8fc", compositeBackground: "#ffffff",
            compositeTitleBackground: "#eef4ff", stateLabelColor: "#0f1b2d", transitionColor: "#64748b",
            cScale0: "#eef4ff", cScale1: "#e0f2fe", cScale2: "#f5f3ff", cScale3: "#ecfdf5", cScale4: "#fffbeb"
        }, scales(LIGHT_SCALE));
    }

    // Twelve section colours for mindmaps and other diagrams that colour by section: [fill, line].
    // Mermaid falls back to saturated defaults past the ones a theme defines.
    var LIGHT_SCALE = [
        ["#eef4ff", "#2563eb"], ["#e0f2fe", "#0284c7"], ["#f5f3ff", "#7c3aed"], ["#ecfdf5", "#059669"],
        ["#fffbeb", "#d97706"], ["#fef2f2", "#dc2626"], ["#f1f5f9", "#475569"], ["#fdf4ff", "#c026d3"],
        ["#f0fdfa", "#0d9488"], ["#fff7ed", "#ea580c"], ["#eef2ff", "#4f46e5"], ["#f7fee7", "#65a30d"]
    ];
    var DARK_SCALE = [
        ["#15264a", "#5a8bff"], ["#0c2a3f", "#38bdf8"], ["#251a46", "#a78bfa"], ["#0d2e26", "#34d399"],
        ["#33240b", "#fbbf24"], ["#3a1515", "#f87171"], ["#1c2638", "#94a3b8"], ["#2e1736", "#e879f9"],
        ["#0b2d2b", "#2dd4bf"], ["#36210d", "#fb923c"], ["#1d1f4d", "#818cf8"], ["#1f2e0e", "#a3e635"]
    ];
    function scales(pairs) {
        var dark = pairs === DARK_SCALE;
        var out = {};
        pairs.forEach(function (p, i) {
            out["cScale" + i] = p[0];
            out["cScalePeer" + i] = p[1];
            out["cScaleInv" + i] = p[1];
            out["cScaleLabel" + i] = dark ? "#e6eeff" : "#0f1b2d";
        });
        return out;
    }

    // Node kinds a diagram marks with classDef. Mermaid writes a classDef's colours inline with
    // !important, so a stylesheet cannot recolour them for dark mode: instead each known classDef
    // line is rewritten to the active palette before the diagram is drawn. [fill, stroke, text]
    var KINDS_LIGHT = {
        store: ["#ecfdf5", "#059669", "#064e3b"], llm: ["#f5f3ff", "#7c3aed", "#3b0764"],
        check: ["#fffbeb", "#d97706", "#78350f"], stop: ["#fef2f2", "#dc2626", "#7f1d1d"],
        user: ["#f1f5f9", "#475569", "#0f172a"], ext: ["#ffffff", "#94a3b8", "#334155"],
        answer: ["#e0f2fe", "#0284c7", "#0c4a6e"]
    };
    var KINDS_DARK = {
        store: ["#0d2e26", "#34d399", "#d1fae5"], llm: ["#251a46", "#a78bfa", "#ede9fe"],
        check: ["#33240b", "#fbbf24", "#fef3c7"], stop: ["#3a1515", "#f87171", "#fee2e2"],
        user: ["#1c2638", "#94a3b8", "#e2e8f0"], ext: ["#111c31", "#64748b", "#cbd5e1"],
        answer: ["#0c2a3f", "#38bdf8", "#e0f2fe"]
    };
    function themedSource(source, dark) {
        var kinds = dark ? KINDS_DARK : KINDS_LIGHT;
        return source.replace(/^(\s*)classDef\s+(\w+)\s+[^\n]*$/gm, function (line, indent, name) {
            var k = kinds[name];
            if (!k) return line;
            var style = "fill:" + k[0] + ",stroke:" + k[1] + ",color:" + k[2];
            if (name === "ext") style += ",stroke-dasharray:5 4";
            return indent + "classDef " + name + " " + style;
        });
    }

    var diagrams = [];   // {figure, canvas, source}
    var mermaidLib = null;
    var counter = 0;

    function collectDiagrams(root) {
        var blocks = root.querySelectorAll("div.language-mermaid, pre > code.language-mermaid");
        var n = 0;
        blocks.forEach(function (block) {
            var host = block.tagName === "CODE" ? block.closest("pre") : block;
            if (!host || host.closest("figure.os-diagram")) return;
            var code = host.querySelector("code") || host;
            var source = code.textContent.replace(/\s+$/, "") + "\n";
            var cap = source.match(/^\s*%%\s*caption:\s*(.+)$/m);
            n += 1;

            var figure = document.createElement("figure");
            figure.className = "os-diagram is-loading";
            figure.setAttribute("data-index", String(n));
            var canvas = document.createElement("div");
            canvas.className = "os-diagram-canvas";
            figure.appendChild(canvas);
            if (cap) {
                var fc = document.createElement("figcaption");
                var b = document.createElement("b");
                b.textContent = "Figure " + n + ". ";
                fc.appendChild(b);
                fc.appendChild(document.createTextNode(cap[1].trim()));
                figure.appendChild(fc);
                figure.setAttribute("aria-label", "Figure " + n + ": " + cap[1].trim());
            }
            var btn = document.createElement("button");
            btn.type = "button";
            btn.className = "os-diagram-expand";
            btn.innerHTML = '<i class="fa fa-expand" aria-hidden="true"></i> Expand';
            btn.addEventListener("click", function () { openLightbox(figure); });
            figure.appendChild(btn);

            // a legend line written right after the block (a <p class="os-legend">) moves inside
            var next = host.nextElementSibling;
            host.parentNode.replaceChild(figure, host);
            if (next && next.classList && next.classList.contains("os-legend")) figure.appendChild(next);
            diagrams.push({ figure: figure, canvas: canvas, source: source });
        });
    }

    function renderAll() {
        var dark = isDark();
        mermaidLib.initialize({
            startOnLoad: false,
            theme: "base",
            themeVariables: themeVariables(dark),
            securityLevel: "strict",
            flowchart: { curve: "basis", htmlLabels: true, padding: 12, nodeSpacing: 36, rankSpacing: 42, diagramPadding: 6, useMaxWidth: true },
            sequence: { useMaxWidth: true, mirrorActors: false, width: 128, actorMargin: 34, boxMargin: 8, noteMargin: 10, messageMargin: 34, wrap: false },
            state: { useMaxWidth: true },
            er: { useMaxWidth: true },
            mindmap: { useMaxWidth: true, padding: 14 }
        });
        var chain = Promise.resolve();
        diagrams.forEach(function (d) {
            chain = chain.then(function () {
                counter += 1;
                var id = "os-mermaid-" + counter;
                return mermaidLib.render(id, themedSource(d.source, dark)).then(function (out) {
                    d.canvas.innerHTML = out.svg;
                    if (out.bindFunctions) out.bindFunctions(d.canvas);
                    keepReadable(d.canvas);
                    d.figure.classList.remove("is-loading");
                    d.figure.setAttribute("data-rendered", "true");
                }).catch(function (err) {
                    console.error("Diagram " + d.figure.getAttribute("data-index") + " could not be drawn:", err);
                    var stray = document.getElementById("d" + id);
                    if (stray) stray.remove();
                    d.canvas.innerHTML = "";
                    var box = document.createElement("div");
                    box.className = "os-diagram-error";
                    var p = document.createElement("p");
                    p.textContent = "This diagram could not be drawn; its source is shown instead.";
                    var pre = document.createElement("pre");
                    pre.textContent = d.source;
                    box.appendChild(p);
                    box.appendChild(pre);
                    d.canvas.appendChild(box);
                    d.figure.classList.remove("is-loading");
                    d.figure.setAttribute("data-rendered", "error");
                });
            });
        });
        return chain;
    }

    // Mermaid scales a wide diagram down to the column. Past 75% its 14px text is too small
    // to read, so below that the diagram keeps 75% of its size and the frame scrolls sideways.
    var MIN_SCALE = 0.75;
    function keepReadable(canvas) {
        var svg = canvas.querySelector("svg");
        if (!svg) return;
        var vb = svg.viewBox && svg.viewBox.baseVal;
        var natural = vb && vb.width ? vb.width : parseFloat(svg.style.maxWidth) || 0;
        if (!natural) return;
        var room = canvas.clientWidth;
        if (room && natural * MIN_SCALE > room) {
            svg.style.width = Math.round(natural * MIN_SCALE) + "px";
            svg.style.maxWidth = "none";
            canvas.classList.add("is-wide");
        }
    }

    function loadDiagrams(root) {
        collectDiagrams(root);
        if (!diagrams.length) return;
        import(MERMAID_URL).then(function (mod) {
            mermaidLib = mod.default;
            return renderAll();
        }).then(function () {
            document.documentElement.setAttribute("data-diagrams", "done");
            if (window.matchMedia) {
                var mq = window.matchMedia("(prefers-color-scheme: dark)");
                var rerender = function () { renderAll(); };
                if (mq.addEventListener) mq.addEventListener("change", rerender);
                else if (mq.addListener) mq.addListener(rerender);
            }
        }).catch(function (err) {
            console.error("Mermaid could not be loaded:", err);
            diagrams.forEach(function (d) {
                d.figure.classList.remove("is-loading");
                d.canvas.innerHTML = "";
                var pre = document.createElement("pre");
                pre.textContent = d.source;
                d.canvas.appendChild(pre);
            });
            document.documentElement.setAttribute("data-diagrams", "failed");
        });
    }

    // ── lightbox ────────────────────────────────────────────────────────────
    function openLightbox(figure) {
        var svg = figure.querySelector(".os-diagram-canvas svg");
        if (!svg) return;
        var overlay = document.createElement("div");
        overlay.className = "os-lightbox";
        overlay.setAttribute("role", "dialog");
        overlay.setAttribute("aria-modal", "true");
        var inner = document.createElement("div");
        inner.className = "os-lightbox-inner os-diagram";
        var close = document.createElement("button");
        close.type = "button";
        close.className = "os-lightbox-close";
        close.setAttribute("aria-label", "Close");
        close.innerHTML = "&times;";
        inner.appendChild(close);
        // Larger than inline: the whole diagram when it fits the window, otherwise at least 1.3x
        // its natural size within the window's width, scrolling vertically. Never above 1.8x.
        var big = svg.cloneNode(true);
        var vb = svg.viewBox && svg.viewBox.baseVal;
        if (vb && vb.width && vb.height) {
            var fitWidth = window.innerWidth * 0.88 / vb.width;
            var fitBoth = Math.min(fitWidth, window.innerHeight * 0.78 / vb.height);
            var k = Math.min(Math.max(fitBoth, Math.min(1.3, fitWidth)), 1.8);
            big.style.width = Math.round(vb.width * k) + "px";
            big.style.height = Math.round(vb.height * k) + "px";
            big.style.maxWidth = "none";
        }
        inner.appendChild(big);
        var cap = figure.querySelector("figcaption");
        if (cap) {
            var c = document.createElement("div");
            c.className = "os-lightbox-caption";
            c.textContent = cap.textContent;
            inner.appendChild(c);
        }
        overlay.appendChild(inner);
        function shut() {
            overlay.remove();
            document.removeEventListener("keydown", onKey);
        }
        function onKey(e) { if (e.key === "Escape") shut(); }
        overlay.addEventListener("click", function (e) { if (e.target === overlay) shut(); });
        close.addEventListener("click", shut);
        document.addEventListener("keydown", onKey);
        document.body.appendChild(overlay);
        close.focus();
    }

    // ── sidebar: keep the open page in view ─────────────────────────────────
    function revealActive() {
        var active = document.querySelector(".book-summary li.chapter.active");
        var box = document.querySelector(".book-summary");
        if (active && box && active.offsetTop > box.clientHeight * 0.6) {
            box.scrollTop = active.offsetTop - 120;
        }
    }

    ready(function () {
        var root = section();
        if (!root) return;
        wrapTables(root);
        softBreakCode(root);
        addAnchors(root);
        labelCode(root);
        loadDiagrams(root);
        revealActive();
    });
})();
