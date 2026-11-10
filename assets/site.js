// Render the concept graph + fill the hall-of-fame list, from graph/concepts.json
(function () {
  var statusColor = { verified: "#34d399", supported: "#4f46e5", candidate: "#f59e0b", untested: "#64748b" };

  function renderList(nodes) {
    var order = { verified: 0, supported: 1, candidate: 2, untested: 3 };
    nodes = nodes.slice().sort(function (a, b) {
      return (order[a.status] || 9) - (order[b.status] || 9) || (b.scores.viability - a.scores.viability);
    });
    var ul = document.getElementById("concept-list");
    ul.innerHTML = "";
    nodes.forEach(function (n) {
      var li = document.createElement("li");
      var s = n.scores;
      li.innerHTML =
        '<span class="name">' + esc(n.name) + '</span>' +
        '<span class="status st-' + n.status + '">' + n.status + '</span>' +
        '<p>' + esc(n.def) + '</p>' +
        '<div class="scores">coherence ' + s.coherence + ' · relational ' + s.relational +
        ' · viability ' + s.viability + ' · living ' + s.living + ' · ' + esc(n.pairing) + '</div>';
      ul.appendChild(li);
    });
  }

  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function renderGraph(nodes, edges) {
    var box = document.getElementById("graph-container");
    var W = box.clientWidth || 900, H = 520;
    var cx = W / 2, cy = H / 2;

    // radial layout, ordered by status then viability
    var byId = {};
    nodes.forEach(function (n) { byId[n.id] = n; });
    var order = { verified: 0, supported: 1, candidate: 2, untested: 3 };
    nodes = nodes.slice().sort(function (a, b) {
      return (order[a.status] || 9) - (order[b.status] || 9) || (b.scores.viability - a.scores.viability);
    });
    var pos = {};
    var R = Math.min(W, H) * 0.38;
    nodes.forEach(function (n, i) {
      var a = (i / nodes.length) * Math.PI * 2 - Math.PI / 2;
      var r = R * (0.55 + 0.45 * ((n.scores.viability || 3) / 5));
      pos[n.id] = { x: cx + Math.cos(a) * r, y: cy + Math.sin(a) * r * 0.82 };
    });

    var svgNS = "http://www.w3.org/2000/svg";
    var svg = document.createElementNS(svgNS, "svg");
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);

    // edges
    edges.forEach(function (e) {
      if (!pos[e.from] || !pos[e.to]) return;
      var line = document.createElementNS(svgNS, "line");
      line.setAttribute("x1", pos[e.from].x); line.setAttribute("y1", pos[e.from].y);
      line.setAttribute("x2", pos[e.to].x); line.setAttribute("y2", pos[e.to].y);
      line.setAttribute("stroke", "rgba(139,151,179,.25)");
      line.setAttribute("stroke-width", "1");
      svg.appendChild(line);
    });

    // nodes
    nodes.forEach(function (n) {
      var p = pos[n.id];
      var g = document.createElementNS(svgNS, "g");
      g.setAttribute("transform", "translate(" + p.x + "," + p.y + ")");
      var r = 5 + (n.scores.viability || 3) * 1.6;
      var c = document.createElementNS(svgNS, "circle");
      c.setAttribute("r", r);
      c.setAttribute("fill", statusColor[n.status] || "#64748b");
      if (n.status === "verified") c.setAttribute("opacity", "0.95"); else c.setAttribute("opacity", "0.7");
      g.appendChild(c);

      var t = document.createElementNS(svgNS, "text");
      t.setAttribute("class", "node-label");
      t.setAttribute("x", r + 7); t.setAttribute("y", 4);
      t.setAttribute("text-anchor", "start");
      t.textContent = n.name.length > 28 ? n.name.slice(0, 28) + "…" : n.name;
      g.appendChild(t);

      // hover label
      g.addEventListener("mouseenter", function () {
        c.setAttribute("r", r + 3); c.setAttribute("opacity", "1");
        t.setAttribute("class", "node-hover-label");
      });
      g.addEventListener("mouseleave", function () {
        c.setAttribute("r", r); c.setAttribute("opacity", n.status === "verified" ? "0.95" : "0.7");
        t.setAttribute("class", "node-label");
      });

      svg.appendChild(g);
    });

    box.appendChild(svg);
  }

  fetch("graph/concepts.json")
    .then(function (r) { return r.json(); })
    .then(function (g) {
      renderGraph(g.nodes, g.edges);
      renderList(g.nodes);
    })
    .catch(function (err) {
      document.getElementById("graph-container").innerHTML =
        '<p style="padding:20px;color:#8b97b3">Could not load graph/concepts.json (' + esc(err && err.message) + ')</p>';
    });
})();
