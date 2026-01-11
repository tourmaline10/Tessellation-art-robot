<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <title>敷き詰めアート・ロボット</title>
  <style>
    body {
      font-family: system-ui, sans-serif;
      text-align: center;
      background: #f5f5f5;
    }
    svg {
      background: white;
      margin: 16px auto;
      display: block;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    button {
      padding: 10px 16px;
      margin: 6px;
      font-size: 16px;
      cursor: pointer;
    }
  </style>
</head>
<body>

<h1>🎨 敷き詰めアート・ロボット</h1>

<button onclick="generate()">🔁 再生成</button>
<button onclick="saveImage()">💾 画像として保存</button>

<svg id="art" width="400" height="400"></svg>

<script>
  const SIZE = 40;
  const ROWS = 10;
  const COLS = 10;

  function rand(max) {
    return Math.floor(Math.random() * max);
  }

  function randomColor() {
    return `rgb(${rand(256)}, ${rand(256)}, ${rand(256)})`;
  }

  function generate() {
    const svg = document.getElementById('art');
    svg.innerHTML = '';

    for (let y = 0; y < ROWS; y++) {
      for (let x = 0; x < COLS; x++) {
        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('x', x * SIZE);
        rect.setAttribute('y', y * SIZE);
        rect.setAttribute('width', SIZE);
        rect.setAttribute('height', SIZE);
        rect.setAttribute('fill', randomColor());
        svg.appendChild(rect);
      }
    }
  }

  function saveImage() {
    const svg = document.getElementById('art');
    const serializer = new XMLSerializer();
    const source = serializer.serializeToString(svg);

    const img = new Image();
    const canvas = document.createElement('canvas');
    canvas.width = 400;
    canvas.height = 400;
    const ctx = canvas.getContext('2d');

    img.onload = () => {
      ctx.drawImage(img, 0, 0);
      const a = document.createElement('a');
      a.href = canvas.toDataURL('image/png');
      a.download = 'tessellation-art.png';
      a.click();
    };

    img.src = 'data:image/svg+xml;base64,' + btoa(unescape(encodeURIComponent(source)));
  }

  generate();
</script>

</body>
</html>
