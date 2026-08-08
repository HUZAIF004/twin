"""Styling constants for the digital twin Gradio app."""

GOLD = "#ecad0a"
BLUE = "#209dd7"
PURPLE = "#753991"

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
/* Import premium Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Inter:wght@400;500;600&display=swap');

:root {
  --twin-gold: #ffb703;
  --twin-gold-glow: rgba(255, 183, 3, 0.5);
  --twin-blue: #00b4d8;
  --twin-purple: #7209b7;
  
  /* Glassmorphism Dark Theme base colors */
  --twin-bg: #000000;
  --twin-surface: rgba(20, 20, 35, 0.4);
  --twin-surface-2: rgba(30, 30, 50, 0.6);
  --twin-border: rgba(255, 255, 255, 0.1);
  --twin-border-strong: rgba(255, 255, 255, 0.25);
  --twin-text: #f8f9fa;
  --twin-muted: #e0e0e0;

  /* Force Gradio variables to transparent/dark */
  --background-fill-primary: transparent !important;
  --background-fill-secondary: transparent !important;
  --block-background-fill: transparent !important;
  --panel-background-fill: transparent !important;
  --border-color-primary: transparent !important;
  --border-color-accent: transparent !important;
  --body-text-color: var(--twin-text) !important;
  --body-text-color-subdued: var(--twin-muted) !important;
  --input-background-fill: transparent !important;
  --block-label-text-color: var(--twin-text) !important;
}

/* Base dark mode */
html, body, gradio-app {
  background-color: #000000 !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', sans-serif !important;
  margin: 0;
  padding: 0;
}

/* Hide Gradio footers and unnecessary UI */
footer, .built-with, .show-api, .api-docs { display: none !important; }

/* ---------- Stable layout ---------- */
.gradio-container {
  background: transparent !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', sans-serif !important;
  width: 100% !important;
  max-width: 900px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 32px 24px 48px !important;
}

/* ---------- Title ---------- */
.gradio-container h1 {
  color: var(--twin-text) !important;
  font-size: 32px !important;
  font-family: 'Outfit', sans-serif !important;
  font-weight: 700 !important;
  letter-spacing: -0.02em !important;
  margin: 4px 0 16px !important;
  text-align: left !important;
  background: linear-gradient(90deg, #ffb703, #fb8500);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.gradio-container p.description {
  font-size: 16px !important;
  color: var(--twin-muted) !important;
  margin-bottom: 24px !important;
}

/* ---------- Smooth rounded corners ---------- */
.chatbot, .chatbot *, .block, .form,
button, input, textarea,
.examples button {
  border-radius: 12px !important;
}

/* ---------- Chatbot glass frame ---------- */
.chatbot, .chatbot.block {
  background: var(--twin-surface) !important;
  backdrop-filter: blur(20px) !important;
  -webkit-backdrop-filter: blur(20px) !important;
  border: 1px solid var(--twin-border) !important;
  height: 450px !important;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
}

.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap { display: none !important; }

/* ---------- Message Rows ---------- */
.message-row, .message-wrap, .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

/* Reset inner borders */
.message-row .message, .message-row .message-bubble, .message-row .bubble {
  border: 0 !important;
  box-shadow: none !important;
  padding: 12px 18px !important;
  animation: slideUpFade 0.4s ease-out forwards;
}

/* Keyframes for micro-animation */
@keyframes slideUpFade {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}

/* User Message Bubble */
.message-row.user-row .message,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble {
  background: linear-gradient(135deg, #00b4d8 0%, #0077b6 100%) !important;
  color: #ffffff !important;
  box-shadow: 0 4px 15px rgba(0, 180, 216, 0.3) !important;
  border-bottom-right-radius: 4px !important;
}

/* Assistant Message Bubble */
.message-row.bot-row .message,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble {
  background: var(--twin-surface-2) !important;
  backdrop-filter: blur(10px) !important;
  color: var(--twin-text) !important;
  border: 1px solid var(--twin-border) !important;
  border-left: 3px solid var(--twin-gold) !important;
  border-bottom-left-radius: 4px !important;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
}

/* Text alignment and font sizes */
.message-row .message, .message-row .message-bubble, .message-row .bubble {
  font-size: 15px !important;
  line-height: 1.6 !important;
  letter-spacing: 0.01em !important;
}

.message-row .message p, .message-row .message-bubble p, .message-row .prose p {
  font-size: 15px !important;
  line-height: 1.6 !important;
  margin: 0 0 10px !important;
  color: inherit !important;
}

.message-row .message p:last-child { margin-bottom: 0 !important; }

.message-row .message a,
.message-row .message-bubble a {
  color: var(--twin-gold) !important;
  text-decoration: underline;
  text-decoration-color: var(--twin-gold-glow);
  text-underline-offset: 4px;
}
.message-row .message a:hover {
  text-decoration-color: var(--twin-gold);
}

/* Strip inner background/borders if Gradio nests bubbles */
.message-row .message .message,
.message-row .message-bubble .message-bubble {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
}

/* ---------- Input row ---------- */
/* Erase the ugly outer box from Gradio's wrappers */
fieldset, .form, form, .panel, .wrap {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
}

.input-row, form[class*="input"] { 
  align-items: stretch !important;
  margin-top: 16px !important;
  gap: 12px !important;
}

textarea, input[type="text"] {
  background: rgba(20, 20, 35, 0.5) !important;
  backdrop-filter: blur(15px) !important;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: 26px !important; /* Elegant pill shape */
  color: var(--twin-text) !important;
  font-family: 'Inter', sans-serif !important;
  font-size: 15px !important;
  padding: 14px 24px !important;
  line-height: 1.5 !important;
  min-height: 52px !important;
  transition: all 0.3s ease !important;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
}

textarea:focus, input[type="text"]:focus {
  border-color: var(--twin-gold) !important;
  outline: none !important;
  box-shadow: 0 0 20px var(--twin-gold-glow) !important;
  background: rgba(30, 30, 45, 0.7) !important;
}

textarea::placeholder, input::placeholder { color: var(--twin-muted) !important; }

/* ---------- Send Button ---------- */
button.primary, button.submit, button[variant="primary"], .submit-button {
  background: linear-gradient(135deg, #ffb703, #fb8500) !important;
  border: none !important;
  border-radius: 26px !important; /* Elegant pill shape */
  color: #030014 !important;
  font-family: 'Outfit', sans-serif !important;
  font-weight: 700 !important;
  font-size: 14px !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
  min-height: 52px !important;
  padding: 0 28px !important;
  transition: transform 0.2s ease, box-shadow 0.2s ease !important;
  cursor: pointer;
  box-shadow: 0 4px 15px var(--twin-gold-glow) !important;
  margin-left: 8px !important;
}

button.primary:hover, button.submit:hover, .submit-button:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 20px var(--twin-gold-glow) !important;
}

/* ---------- Examples ---------- */
.examples { margin-top: 24px !important; }

.examples button, .example, [data-testid="examples"] button {
  background: rgba(30, 30, 50, 0.4) !important;
  backdrop-filter: blur(8px) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', sans-serif !important;
  font-size: 13px !important;
  padding: 10px 16px !important;
  transition: all 0.2s ease !important;
  border-radius: 20px !important; /* Pill shape for examples */
  margin-right: 8px !important;
  margin-bottom: 8px !important;
}

.examples button:hover, .example:hover, [data-testid="examples"] button:hover {
  background: rgba(255, 183, 3, 0.1) !important;
  border-color: var(--twin-gold) !important;
  color: var(--twin-gold) !important;
  transform: translateY(-1px);
}

/* ---------- Custom Scrollbar ---------- */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.2); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: rgba(255, 255, 255, 0.4); }

::selection { background: var(--twin-gold); color: #030014; }
"""

JS = """
() => {
  document.title = 'Digital Twin';

  // --- Low Poly Animated Canvas Background ---
  const canvas = document.createElement('canvas');
  canvas.style.position = 'fixed';
  canvas.style.top = '0';
  canvas.style.left = '0';
  canvas.style.width = '100vw';
  canvas.style.height = '100vh';
  canvas.style.zIndex = '-2';
  document.body.appendChild(canvas);
  
  const ctx = canvas.getContext('2d');
  let width, height, grid = [], cols, rows;
  const spacing = 180;
  
  const init = () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
    cols = Math.ceil(width / spacing) + 2;
    rows = Math.ceil(height / spacing) + 2;
    grid = [];
    
    for (let i = 0; i < cols; i++) {
      let col = [];
      for (let j = 0; j < rows; j++) {
        col.push({
          x: (i - 1) * spacing + (Math.random() - 0.5) * spacing * 0.8,
          y: (j - 1) * spacing + (Math.random() - 0.5) * spacing * 0.8,
          ox: (i - 1) * spacing,
          oy: (j - 1) * spacing,
          vx: (Math.random() - 0.5) * 0.2,
          vy: (Math.random() - 0.5) * 0.2,
          c: Math.random() * 20
        });
      }
      grid.push(col);
    }
  };
  
  const draw = () => {
    ctx.fillStyle = '#000';
    ctx.fillRect(0, 0, width, height);
    
    for (let i = 0; i < cols; i++) {
      for (let j = 0; j < rows; j++) {
        let p = grid[i][j];
        p.x += p.vx;
        p.y += p.vy;
        if (Math.abs(p.x - p.ox) > spacing * 0.6) p.vx *= -1;
        if (Math.abs(p.y - p.oy) > spacing * 0.6) p.vy *= -1;
      }
    }
    
    for (let i = 0; i < cols - 1; i++) {
      for (let j = 0; j < rows - 1; j++) {
        const p1 = grid[i][j], p2 = grid[i+1][j], p3 = grid[i][j+1], p4 = grid[i+1][j+1];
        
        const drawTri = (pA, pB, pC) => {
           ctx.beginPath();
           ctx.moveTo(pA.x, pA.y);
           ctx.lineTo(pB.x, pB.y);
           ctx.lineTo(pC.x, pC.y);
           ctx.closePath();
           const shade = Math.floor(4 + pA.c + (pB.x - pA.x) * 0.04 + (pC.y - pA.y) * 0.04);
           const safeShade = Math.max(10, Math.min(45, shade)); // Deep greys matching the reference image
           ctx.fillStyle = `rgb(${safeShade}, ${safeShade}, ${safeShade})`;
           ctx.fill();
           ctx.strokeStyle = `rgb(${safeShade}, ${safeShade}, ${safeShade})`;
           ctx.lineWidth = 1;
           ctx.stroke();
        };
        
        if ((i + j) % 2 === 0) {
          drawTri(p1, p2, p4);
          drawTri(p1, p4, p3);
        } else {
          drawTri(p1, p2, p3);
          drawTri(p2, p4, p3);
        }
      }
    }
    requestAnimationFrame(draw);
  };
  
  window.addEventListener('resize', init);
  init();
  draw();
  // --- End Low Poly ---

  // Interactive mouse glow
  const glow = document.createElement('div');
  glow.id = 'mouse-glow';
  glow.style.width = '800px';
  glow.style.height = '800px';
  glow.style.background = 'radial-gradient(circle, rgba(255,183,3,0.06) 0%, transparent 60%)';
  glow.style.position = 'fixed';
  glow.style.top = '0';
  glow.style.left = '0';
  glow.style.pointerEvents = 'none';
  glow.style.zIndex = '-1';
  glow.style.opacity = '0';
  glow.style.transition = 'opacity 0.5s ease';
  document.body.appendChild(glow);

  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let currentX = mouseX;
  let currentY = mouseY;

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    glow.style.opacity = '1';
  });

  document.addEventListener('mouseleave', () => {
    glow.style.opacity = '0';
  });

  const animateGlow = () => {
    currentX += (mouseX - currentX) * 0.05; // Smooth interpolation
    currentY += (mouseY - currentY) * 0.05;
    glow.style.transform = `translate(${currentX - 400}px, ${currentY - 400}px)`;
    requestAnimationFrame(animateGlow);
  };
  animateGlow();

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  // Watch for Gradio disabling/enabling the textarea
  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""
