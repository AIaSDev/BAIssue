#!/usr/bin/env bash
# Requires Bash (Git Bash/WSL on Windows). Canonical instructions stay unchanged.
# Usage: setup-skills.sh [copilot|codex|opencode|claude|cline|junie|both]
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
[[ -d skills && -f AGENTS.md ]] || { echo "Missing skills/ or AGENTS.md" >&2; exit 1; }

choice=${1:-}
if [[ -z "$choice" ]]; then
  printf '%s\n' '1) .agents (Copilot, Codex, OpenCode)' '2) .claude (Claude Code, Cline)' '3) both' '4) cancel'
  read -r -p 'Selection [1-4]: ' choice
fi
[[ $# -le 1 ]] || { echo "Expected one target." >&2; exit 1; }

link_skills() {
  local target="$1/skills"
  mkdir -p "$1"
  if [[ -L "$target" ]]; then
    [[ "$(readlink "$target")" == ../skills && -d "$target" ]] ||
      { echo "Conflicting link: $target; unchanged." >&2; return 1; }
  elif [[ -e "$target" ]]; then
    [[ -d "$target" ]] && diff -qr skills "$target" >/dev/null ||
      { echo "Conflicting or stale copy: $target; unchanged." >&2; return 1; }
  else
    ln -s ../skills "$target" 2>/dev/null || cp -R skills "$target"
  fi
  echo "Ready: $target"
}

claude_bridge() {
  if [[ -e CLAUDE.md || -L CLAUDE.md ]]; then
    echo "Existing CLAUDE.md preserved; ensure it imports @AGENTS.md."
  else
    printf '%s\n' '@AGENTS.md' > CLAUDE.md
    echo "Created CLAUDE.md adapter."
  fi
}

case "$choice" in
  1|.agents|copilot|codex|opencode) link_skills .agents ;;
  2|.claude|claude) link_skills .claude; claude_bridge ;;
  cline) link_skills .claude ;;
  3|both) link_skills .agents; link_skills .claude; claude_bridge ;;
  junie) echo "Junie uses AGENTS.md; follow the linked phase instructions." ;;
  4|cancel) exit 0 ;;
  -h|--help) echo "Usage: $0 [copilot|codex|opencode|claude|cline|junie|both]"; exit 0 ;;
  *) echo "Unknown target: $choice" >&2; exit 1 ;;
esac
echo "Canonical skills remain in skills/. Run setup in each fresh checkout; verify discovery in your agent."
