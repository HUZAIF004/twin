"""Styling constants for the digital twin Gradio app."""

import gradio as gr
from gradio.themes.utils import colors, fonts, sizes

GOLD = "#ecad0a"
BLUE = "#209dd7"
PURPLE = "#753991"

# ── Custom dark theme ──
THEME = gr.themes.Base(
    primary_hue=gr.themes.Color(
        c50="#fef9e7", c100="#fdf0c4", c200="#fbe49d", c300="#f9d776",
        c400="#f5c53a", c500="#ecad0a", c600="#d49a08", c700="#b07e06",
        c800="#8c6405", c900="#6b4c04", c950="#4a3403",
    ),
    secondary_hue=gr.themes.Color(
        c50="#f0e6f6", c100="#d9c0e8", c200="#c299db", c300="#ab73cd",
        c400="#9553c0", c500="#753991", c600="#5e2e74", c700="#472358",
        c800="#30183b", c900="#190c1e", c950="#0d0610",
    ),
    neutral_hue=gr.themes.Color(
        c50="#ececef", c100="#d5d5da", c200="#ababb5", c300="#808090",
        c400="#60606e", c500="#45454f", c600="#30303a", c700="#22222c",
        c800="#16161e", c900="#0e0e14", c950="#08080c",
    ),
    font=(gr.themes.GoogleFont("Inter"), "ui-sans-serif", "system-ui", "sans-serif"),
    font_mono=(gr.themes.GoogleFont("JetBrains Mono"), "ui-monospace", "monospace"),
).set(
    # Global dark backgrounds
    body_background_fill="#08080c",
    body_background_fill_dark="#08080c",
    background_fill_primary="#0e0e14",
    background_fill_primary_dark="#0e0e14",
    background_fill_secondary="#16161e",
    background_fill_secondary_dark="#16161e",
    # Text
    body_text_color="#e8e8f0",
    body_text_color_dark="#e8e8f0",
    body_text_color_subdued="#808090",
    body_text_color_subdued_dark="#808090",
    # Borders
    border_color_primary="rgba(255,255,255,0.06)",
    border_color_primary_dark="rgba(255,255,255,0.06)",
    # Inputs
    input_background_fill="#12121a",
    input_background_fill_dark="#12121a",
    input_border_color="rgba(255,255,255,0.10)",
    input_border_color_dark="rgba(255,255,255,0.10)",
    # Blocks
    block_background_fill="#12121a",
    block_background_fill_dark="#12121a",
    block_border_color="rgba(255,255,255,0.06)",
    block_border_color_dark="rgba(255,255,255,0.06)",
    block_label_text_color="#808090",
    block_label_text_color_dark="#808090",
    block_title_text_color="#e8e8f0",
    block_title_text_color_dark="#e8e8f0",
    # Buttons
    button_primary_background_fill="linear-gradient(135deg, #ecad0a, #d49a08)",
    button_primary_background_fill_dark="linear-gradient(135deg, #ecad0a, #d49a08)",
    button_primary_text_color="#0d0d10",
    button_primary_text_color_dark="#0d0d10",
    button_primary_border_color="#ecad0a",
    button_primary_border_color_dark="#ecad0a",
    button_secondary_background_fill="transparent",
    button_secondary_background_fill_dark="transparent",
    button_secondary_text_color="#a0a0b0",
    button_secondary_text_color_dark="#a0a0b0",
    button_secondary_border_color="rgba(255,255,255,0.10)",
    button_secondary_border_color_dark="rgba(255,255,255,0.10)",
    # Shadows
    block_shadow="0 4px 24px rgba(0,0,0,0.30)",
    block_shadow_dark="0 4px 24px rgba(0,0,0,0.30)",
    # Radius
    block_radius="16px",
    container_radius="16px",
    input_radius="10px",
    button_large_radius="10px",
    button_medium_radius="10px",
    button_small_radius="6px",
)

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ═══════════════════════════════════════════
   DESIGN TOKENS
   ═══════════════════════════════════════════ */
:root {
  --twin-gold: #ecad0a;
  --twin-gold-soft: rgba(236, 173, 10, 0.12);
  --twin-gold-glow: rgba(236, 173, 10, 0.25);
  --twin-blue: #209dd7;
  --twin-blue-soft: rgba(32, 157, 215, 0.15);
  --twin-blue-glow: rgba(32, 157, 215, 0.30);
  --twin-purple: #753991;
  --twin-purple-soft: rgba(117, 57, 145, 0.15);
  --twin-purple-glow: rgba(117, 57, 145, 0.30);
  --twin-cyan: #00d4aa;
  --twin-bg: #08080c;
  --twin-bg-2: #0c0c12;
  --twin-surface: rgba(18, 18, 26, 0.85);
  --twin-surface-2: rgba(24, 24, 34, 0.80);
  --twin-surface-solid: #12121a;
  --twin-border: rgba(255, 255, 255, 0.06);
  --twin-border-strong: rgba(255, 255, 255, 0.10);
  --twin-border-glow: rgba(236, 173, 10, 0.20);
  --twin-text: #e8e8f0;
  --twin-text-dim: #a0a0b0;
  --twin-muted: #606070;
  --twin-glass: rgba(255, 255, 255, 0.03);
  --twin-radius: 16px;
  --twin-radius-sm: 10px;
  --twin-radius-xs: 6px;
  --twin-shadow: 0 8px 32px rgba(0, 0, 0, 0.40), 0 2px 8px rgba(0, 0, 0, 0.20);
  --twin-shadow-glow: 0 0 40px rgba(236, 173, 10, 0.06), 0 8px 32px rgba(0, 0, 0, 0.40);
}

/* ═══════════════════════════════════════════
   GLOBAL RESET & BACKGROUND
   ═══════════════════════════════════════════ */
footer, .built-with, .show-api, .api-docs { display: none !important; }

html, body, gradio-app {
  background: var(--twin-bg) !important;
  min-height: 100vh;
}

/* Animated subtle mesh gradient background */
body::before {
  content: '';
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background:
    radial-gradient(ellipse 80% 60% at 20% 10%, rgba(117, 57, 145, 0.08) 0%, transparent 60%),
    radial-gradient(ellipse 60% 50% at 80% 20%, rgba(32, 157, 215, 0.06) 0%, transparent 50%),
    radial-gradient(ellipse 70% 40% at 50% 90%, rgba(236, 173, 10, 0.05) 0%, transparent 50%),
    radial-gradient(ellipse 50% 50% at 10% 80%, rgba(0, 212, 170, 0.04) 0%, transparent 50%);
  z-index: 0;
  pointer-events: none;
  animation: meshShift 25s ease-in-out infinite alternate;
}

@keyframes meshShift {
  0%   { opacity: 0.7; transform: scale(1) translateY(0); }
  50%  { opacity: 1;   transform: scale(1.05) translateY(-10px); }
  100% { opacity: 0.8; transform: scale(1) translateY(5px); }
}

/* Fine noise overlay */
body::after {
  content: '';
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.015'/%3E%3C/svg%3E");
  z-index: 0;
  pointer-events: none;
  opacity: 0.5;
}

/* ═══════════════════════════════════════════
   CONTAINER
   ═══════════════════════════════════════════ */
.gradio-container {
  position: relative;
  z-index: 1;
  background: transparent !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  width: 100% !important;
  max-width: 900px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 28px 24px 48px !important;
}
.gradio-container .main, .gradio-container .contain, .gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}
.gradio-container * { min-width: 0; }

/* ═══════════════════════════════════════════
   TITLE & DESCRIPTION
   ═══════════════════════════════════════════ */
.gradio-container h1 {
  color: var(--twin-text) !important;
  font-size: 28px !important;
  font-weight: 800 !important;
  letter-spacing: -0.03em !important;
  margin: 0 0 4px !important;
  padding: 0 0 0 16px !important;
  text-align: left !important;
  border: none !important;
  position: relative;
}
.gradio-container h1::before {
  content: '';
  position: absolute;
  left: 0; top: 4px; bottom: 4px;
  width: 4px;
  border-radius: 2px;
  background: linear-gradient(180deg, var(--twin-gold), var(--twin-purple));
  box-shadow: 0 0 12px var(--twin-gold-glow);
}

/* Description text */
.gradio-container .prose,
.gradio-container .md,
.gradio-container p.description {
  color: var(--twin-text-dim) !important;
  font-size: 14px !important;
  font-weight: 400 !important;
  margin-bottom: 8px !important;
}

/* ═══════════════════════════════════════════
   BLOCK & FORM SURFACES
   ═══════════════════════════════════════════ */
.block, .form {
  background: transparent !important;
  box-shadow: none !important;
  border: none !important;
}

/* ═══════════════════════════════════════════
   CHATBOT LABEL – HIDE
   ═══════════════════════════════════════════ */
.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
  display: none !important;
}

/* ═══════════════════════════════════════════
   CHATBOT FRAME – GLASSMORPHISM
   ═══════════════════════════════════════════ */
.chatbot, .chatbot.block {
  background: var(--twin-surface) !important;
  backdrop-filter: blur(24px) saturate(1.4) !important;
  -webkit-backdrop-filter: blur(24px) saturate(1.4) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: var(--twin-radius) !important;
  min-height: 480px !important;
  box-shadow: var(--twin-shadow-glow) !important;
  position: relative;
  overflow: hidden;
}

/* Top edge glow accent */
.chatbot::before {
  content: '';
  position: absolute;
  top: 0; left: 10%; right: 10%;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--twin-gold-glow), var(--twin-purple-glow), transparent);
  z-index: 2;
}

.chatbot .placeholder, .chatbot .placeholder * {
  color: var(--twin-muted) !important;
  font-style: italic;
}

/* ═══════════════════════════════════════════
   MESSAGE ROWS – CLEAR BACKGROUNDS
   ═══════════════════════════════════════════ */
.message-row,
.message-row > div,
.message-row .role,
.message-wrap, .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

/* ═══════════════════════════════════════════
   BUBBLES – BASE RESET
   ═══════════════════════════════════════════ */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  border: 0 !important;
  box-shadow: none !important;
  padding: 10px 14px !important;
  border-radius: var(--twin-radius-sm) !important;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

/* ─── User bubbles ─── */
.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble {
  background: linear-gradient(135deg, var(--twin-blue), #1a7ab5) !important;
  color: #ffffff !important;
  border-radius: var(--twin-radius-sm) var(--twin-radius-sm) 4px var(--twin-radius-sm) !important;
  box-shadow: 0 4px 16px rgba(32, 157, 215, 0.20) !important;
}
.message-row.user-row:hover .message,
.message-row.user-row:hover .message-bubble,
.message-row.user-row:hover .bubble,
.message-row[data-role="user"]:hover .message,
.message-row[data-role="user"]:hover .message-bubble {
  transform: translateY(-1px);
  box-shadow: 0 6px 24px rgba(32, 157, 215, 0.30) !important;
}

/* ─── Assistant bubbles ─── */
.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble {
  background: var(--twin-surface-2) !important;
  backdrop-filter: blur(12px) !important;
  color: var(--twin-text) !important;
  border-left: 3px solid transparent !important;
  border-image: linear-gradient(180deg, var(--twin-purple), var(--twin-gold)) 1 !important;
  border-radius: var(--twin-radius-sm) var(--twin-radius-sm) var(--twin-radius-sm) 4px !important;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.15) !important;
}
.message-row.bot-row:hover .message,
.message-row.bot-row:hover .message-bubble,
.message-row.bot-row:hover .bubble,
.message-row[data-role="assistant"]:hover .message,
.message-row[data-role="assistant"]:hover .message-bubble {
  transform: translateY(-1px);
  box-shadow: 0 4px 20px rgba(117, 57, 145, 0.15) !important;
}

/* ─── Nested bubble stripe suppression ─── */
.message-row.bot-row .message .message,
.message-row.bot-row .message .bubble,
.message-row.bot-row .message .message-bubble,
.message-row.bot-row .bubble .message,
.message-row.bot-row .bubble .bubble,
.message-row.bot-row .bubble .message-bubble,
.message-row.bot-row .message-bubble .message,
.message-row.bot-row .message-bubble .bubble,
.message-row.bot-row .message-bubble .message-bubble,
.message-row[data-role="assistant"] .message .message,
.message-row[data-role="assistant"] .message .bubble,
.message-row[data-role="assistant"] .message .message-bubble,
.message-row[data-role="assistant"] .bubble .message,
.message-row[data-role="assistant"] .bubble .bubble,
.message-row[data-role="assistant"] .bubble .message-bubble,
.message-row[data-role="assistant"] .message-bubble .message,
.message-row[data-role="assistant"] .message-bubble .bubble,
.message-row[data-role="assistant"] .message-bubble .message-bubble {
  border-left: 0 !important;
  border-image: none !important;
}

/* ═══════════════════════════════════════════
   BUBBLE TYPOGRAPHY – UNIFORM
   ═══════════════════════════════════════════ */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  font-size: 14px !important;
  line-height: 1.6 !important;
}
.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
  font-size: 14px !important;
  line-height: 1.6 !important;
  margin: 0 0 8px !important;
  color: inherit !important;
}
.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child { margin-bottom: 0 !important; }

/* Strip stray inner styles */
.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * {
  background: transparent !important;
  border-color: transparent !important;
  box-shadow: none !important;
  color: inherit !important;
}

/* Links inside bubbles */
.message-row .message a,
.message-row .message-bubble a {
  color: var(--twin-gold) !important;
  text-decoration: none !important;
  border-bottom: 1px solid var(--twin-gold-soft);
  transition: border-color 0.2s ease;
}
.message-row .message a:hover,
.message-row .message-bubble a:hover {
  border-bottom-color: var(--twin-gold) !important;
}

/* Bold & strong text accent */
.message-row .message strong,
.message-row .message-bubble strong,
.message-row .message b,
.message-row .message-bubble b {
  color: var(--twin-text) !important;
  font-weight: 600 !important;
}

/* Code inside bubbles */
.message-row .message code,
.message-row .message-bubble code {
  font-family: 'JetBrains Mono', 'SF Mono', monospace !important;
  font-size: 12.5px !important;
  background: rgba(255, 255, 255, 0.06) !important;
  padding: 2px 6px !important;
  border-radius: 4px !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
}

/* ═══════════════════════════════════════════
   INPUT AREA – GLASSMORPHISM
   ═══════════════════════════════════════════ */
.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] { align-items: stretch !important; }

textarea, input[type="text"] {
  background: var(--twin-surface) !important;
  backdrop-filter: blur(16px) !important;
  border: 1px solid var(--twin-border-strong) !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 14px !important;
  padding: 14px 16px !important;
  line-height: 1.5 !important;
  min-height: 50px !important;
  border-radius: var(--twin-radius-sm) !important;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}
textarea:focus, input[type="text"]:focus {
  border-color: var(--twin-gold) !important;
  outline: none !important;
  box-shadow: 0 0 0 2px var(--twin-gold-soft), 0 0 20px rgba(236, 173, 10, 0.08) !important;
}
textarea::placeholder, input::placeholder {
  color: var(--twin-muted) !important;
  font-weight: 300;
}

/* ═══════════════════════════════════════════
   BUTTONS – MODERN GLASS
   ═══════════════════════════════════════════ */
button {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  letter-spacing: 0.03em !important;
  text-transform: none !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  border: 1px solid var(--twin-border-strong) !important;
  background: var(--twin-glass) !important;
  color: var(--twin-text-dim) !important;
  padding: 0 16px !important;
  min-height: 50px !important;
  align-self: stretch !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer;
  border-radius: var(--twin-radius-sm) !important;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
button:hover {
  border-color: var(--twin-gold) !important;
  color: var(--twin-gold) !important;
  background: var(--twin-gold-soft) !important;
  box-shadow: 0 0 16px rgba(236, 173, 10, 0.08) !important;
}

/* ─── Primary / Submit ─── */
button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  background: linear-gradient(135deg, var(--twin-gold), #d49a08) !important;
  border: 1px solid var(--twin-gold) !important;
  color: #0d0d10 !important;
  font-weight: 600 !important;
  min-height: 50px !important;
  align-self: stretch !important;
  padding: 0 18px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  border-radius: var(--twin-radius-sm) !important;
  box-shadow: 0 4px 16px rgba(236, 173, 10, 0.20) !important;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
button.primary:hover,
button.submit:hover,
.submit-button:hover,
button.lg.primary:hover {
  background: linear-gradient(135deg, #ffc320, var(--twin-gold)) !important;
  border-color: #ffc320 !important;
  color: #0d0d10 !important;
  box-shadow: 0 6px 24px rgba(236, 173, 10, 0.35) !important;
  transform: translateY(-1px);
}

/* ─── Submit icon ─── */
button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {
  width: 18px !important;
  height: 18px !important;
  margin: 0 auto !important;
  display: block !important;
  align-self: center !important;
  color: #0d0d10 !important;
  fill: currentColor !important;
  stroke: currentColor !important;
}

/* ═══════════════════════════════════════════
   EXAMPLES – PILL CARDS
   ═══════════════════════════════════════════ */
.examples, .examples-holder, [data-testid="examples"] {
  background: transparent !important;
  padding: 0 !important;
  margin-top: 16px !important;
}
.examples table, .examples-table { background: transparent !important; border: 0 !important; }

.examples button, .example, .examples td button, [data-testid="examples"] button {
  background: var(--twin-surface) !important;
  backdrop-filter: blur(12px) !important;
  border: 1px solid var(--twin-border) !important;
  color: var(--twin-text-dim) !important;
  text-transform: none !important;
  letter-spacing: 0 !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 13px !important;
  font-weight: 400 !important;
  padding: 10px 16px !important;
  text-align: left !important;
  min-height: 0 !important;
  align-self: auto !important;
  display: inline-block !important;
  border-radius: 999px !important;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
.examples button:hover, .example:hover, [data-testid="examples"] button:hover {
  border-color: var(--twin-blue) !important;
  color: var(--twin-blue) !important;
  background: var(--twin-blue-soft) !important;
  box-shadow: 0 0 12px rgba(32, 157, 215, 0.10) !important;
  transform: translateY(-1px);
}

/* ═══════════════════════════════════════════
   ICON BUTTONS (clear, retry, copy)
   ═══════════════════════════════════════════ */
.icon-button, .chatbot .icon-button {
  color: var(--twin-muted) !important;
  background: transparent !important;
  border: 0 !important;
  min-height: 0 !important;
  align-self: auto !important;
  padding: 6px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  border-radius: 8px !important;
  transition: all 0.2s ease;
}
.icon-button:hover, .chatbot .icon-button:hover {
  color: var(--twin-gold) !important;
  background: var(--twin-gold-soft) !important;
}

/* ═══════════════════════════════════════════
   SCROLLBAR – SLEEK
   ═══════════════════════════════════════════ */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  background: var(--twin-border-strong);
  border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover { background: var(--twin-purple); }

/* ═══════════════════════════════════════════
   SELECTION
   ═══════════════════════════════════════════ */
::selection {
  background: var(--twin-gold);
  color: #0d0d10;
}

/* ═══════════════════════════════════════════
   TYPING ANIMATION DOTS
   ═══════════════════════════════════════════ */
@keyframes pulse-dot {
  0%, 80%, 100% { opacity: 0.3; transform: scale(0.8); }
  40% { opacity: 1; transform: scale(1); }
}

/* ═══════════════════════════════════════════
   RESPONSIVE
   ═══════════════════════════════════════════ */
@media (max-width: 640px) {
  .gradio-container { padding: 18px 12px 32px !important; }
  .gradio-container h1 { font-size: 22px !important; }
  .chatbot, .chatbot.block { min-height: 380px !important; border-radius: 12px !important; }
  textarea, input[type="text"] { border-radius: 8px !important; }
  button { border-radius: 8px !important; }
}

/* ═══════════════════════════════════════════
   ENTRANCE ANIMATION
   ═══════════════════════════════════════════ */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
.gradio-container {
  animation: fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) both;
}
"""

JS = """
() => {
  document.title = 'Digital Twin';

  // Force dark mode
  document.body.classList.add('dark');

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  // Re-focus the message field whenever Gradio re-enables it
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
