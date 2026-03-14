#!/usr/bin/env bash

set -e

echo "AI-SDLC Skill Setup"
echo "-------------------"

if [ ! -d "skills" ]; then
  echo "Error: skills/ directory not found."
  exit 1
fi

echo ""
echo "Select the tools you want to support:"
echo ""
echo "1) .agents   (GitHub Copilot, OpenAI Codex, Cline, other agents)"
echo "2) .claude   (Claude Code)"
echo "3) both"
echo "4) cancel"
echo ""

read -p "Selection [1-4]: " choice

create_link () {
  target_dir=$1

  mkdir -p "$target_dir"

  if [ -e "$target_dir/skills" ]; then
    echo "✓ $target_dir/skills already exists"
    return
  fi

  if ln -s ../skills "$target_dir/skills" 2>/dev/null; then
    echo "✓ Symlink created: $target_dir/skills → ../skills"
  else
    echo "Symlink not supported, copying skills instead..."
    cp -r skills "$target_dir/skills"
    echo "✓ Skills copied to $target_dir/skills"
  fi
}

case $choice in
  1)
    create_link ".agents"
    ;;
  2)
    create_link ".claude"
    ;;
  3)
    create_link ".agents"
    create_link ".claude"
    ;;
  *)
    echo "Cancelled."
    exit 0
    ;;
esac

echo ""
echo "Setup complete."
echo ""
echo "Detected structure:"
echo ""

[ -d ".agents/skills" ] && echo "✓ .agents/skills"
[ -d ".claude/skills" ] && echo "✓ .claude/skills"

echo ""
echo "Your canonical skills remain in:"
echo "skills/"
echo ""